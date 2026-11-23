'use strict';

/*
 * Mesai Sayacı — tüm veriler chrome.storage.local içinde tutulur.
 *
 * Saklanan anahtarlar:
 *   clients          [{ id, name, rate }]
 *   entries          [{ id, clientId, clientName, start, end, rate }]  (start/end: ms zaman damgası)
 *   running          { clientId, start } | null
 *   selectedClientId string
 *
 * Sayaç, başlangıç zamanı saklandığı için popup kapalıyken de "çalışır";
 * popup açıldığında geçen süre şimdiki zamandan hesaplanır.
 */

const DEFAULT_CLIENTS = [
  { id: 'pudra-bulut', name: 'Pudra Bulut Pastanesi', rate: 750 },
  { id: 'kirk-sumbul', name: 'Kırk Sümbül Çiçekçilik', rate: 600 },
  { id: 'telve-tarcin', name: 'Telve & Tarçın', rate: 900 },
];

const MAX_RATE = 1000000;

const moneyFmt = new Intl.NumberFormat('tr-TR', {
  minimumFractionDigits: 2,
  maximumFractionDigits: 2,
});

const $ = (id) => document.getElementById(id);
const els = {
  clientSelect: $('client-select'),
  lockNote: $('lock-note'),
  rateInput: $('rate-input'),
  rateSave: $('rate-save'),
  timerStatus: $('timer-status'),
  timer: $('timer'),
  timerAmount: $('timer-amount'),
  toggle: $('toggle'),
  todayTime: $('today-time'),
  todayAmount: $('today-amount'),
  totalTime: $('total-time'),
  totalAmount: $('total-amount'),
  addDetails: $('add-details'),
  addForm: $('add-form'),
  newName: $('new-name'),
  newRate: $('new-rate'),
  exportBtn: $('export'),
  message: $('message'),
};

let state = { clients: [], entries: [], running: null, selectedClientId: null };
let busy = false;
let messageTimer = null;
let lastTickKey = '';

/* ---------- Biçimlendirme ---------- */

const pad = (n) => String(n).padStart(2, '0');

function formatMoney(n) {
  return moneyFmt.format(n) + ' TL';
}

function formatDuration(totalSec) {
  const s = Math.max(0, Math.floor(totalSec));
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  return `${pad(h)}:${pad(m)}:${pad(s % 60)}`;
}

function formatDate(ts) {
  const d = new Date(ts);
  return `${pad(d.getDate())}.${pad(d.getMonth() + 1)}.${d.getFullYear()}`;
}

function formatTime(ts) {
  const d = new Date(ts);
  return `${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`;
}

function dayKey(ts) {
  const d = new Date(ts);
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
}

/**
 * "750", "750,5", "1.250,50", "1250.50", "1.250" gibi girişleri sayıya çevirir.
 * Geçersizse NaN döner.
 */
function parseAmount(input) {
  let s = String(input).trim().replace(/\s+/g, '').replace(/(TL|₺)$/i, '');
  if (!s) return NaN;
  if (s.includes(',')) {
    // Türkçe biçim: nokta binlik ayırıcı, virgül ondalık.
    s = s.replace(/\./g, '').replace(',', '.');
  } else if (/^\d{1,3}(\.\d{3})+$/.test(s)) {
    // "1.250" → binlik ayırıcı kabul edilir.
    s = s.replace(/\./g, '');
  }
  if (!/^\d+(\.\d{1,2})?$/.test(s)) return NaN;
  const n = Number(s);
  return n >= 0 && n <= MAX_RATE ? n : NaN;
}

/* ---------- Hesaplama ---------- */

function amountFor(seconds, rate) {
  // seconds * rate / 3600, kuruşa yuvarlanmış
  return Math.round((seconds * rate) / 36) / 100;
}

function entryDuration(e) {
  return Math.max(0, Math.floor((e.end - e.start) / 1000));
}

function entryAmount(e) {
  return amountFor(entryDuration(e), e.rate);
}

function findClient(id) {
  return state.clients.find((c) => c.id === id) || null;
}

function selectedClient() {
  return findClient(state.selectedClientId) || state.clients[0];
}

function runningSeconds(now) {
  return state.running ? Math.max(0, Math.floor((now - state.running.start) / 1000)) : 0;
}

/* ---------- Depolama ---------- */

function isValidClient(c) {
  return c && typeof c.id === 'string' && typeof c.name === 'string' && Number.isFinite(c.rate);
}

function isValidEntry(e) {
  return e && typeof e.clientId === 'string' && Number.isFinite(e.start) &&
    Number.isFinite(e.end) && Number.isFinite(e.rate);
}

function isValidRunning(r) {
  return r && typeof r.clientId === 'string' && Number.isFinite(r.start);
}

async function loadState() {
  const data = await chrome.storage.local.get(['clients', 'entries', 'running', 'selectedClientId']);
  const toSave = {};

  let clients = Array.isArray(data.clients) ? data.clients.filter(isValidClient) : [];
  if (clients.length === 0) {
    clients = DEFAULT_CLIENTS.map((c) => ({ ...c }));
    toSave.clients = clients;
  }

  const entries = Array.isArray(data.entries) ? data.entries.filter(isValidEntry) : [];
  const running = isValidRunning(data.running) ? data.running : null;

  let selectedClientId = running ? running.clientId : data.selectedClientId;
  if (!clients.some((c) => c.id === selectedClientId)) {
    selectedClientId = clients[0].id;
    toSave.selectedClientId = selectedClientId;
  }

  state = { clients, entries, running, selectedClientId };

  if (Object.keys(toSave).length > 0) {
    await chrome.storage.local.set(toSave);
  }
}

/* ---------- Arayüz ---------- */

function showMessage(text, isError = false) {
  clearTimeout(messageTimer);
  els.message.textContent = text;
  els.message.classList.toggle('error', isError);
  messageTimer = setTimeout(() => {
    els.message.textContent = '';
  }, 5000);
}

function renderClients() {
  const options = state.clients.map((c) => {
    const opt = document.createElement('option');
    opt.value = c.id;
    opt.textContent = c.name;
    return opt;
  });
  els.clientSelect.replaceChildren(...options);
  els.clientSelect.value = selectedClient().id;
  els.clientSelect.disabled = Boolean(state.running);
  els.lockNote.hidden = !state.running;
}

function renderRate(force) {
  if (force || document.activeElement !== els.rateInput) {
    els.rateInput.value = moneyFmt.format(selectedClient().rate);
  }
}

function renderToggle() {
  const running = Boolean(state.running);
  els.toggle.textContent = running ? 'Durdur' : 'Başlat';
  els.toggle.classList.toggle('running', running);
  els.timerStatus.textContent = running
    ? `Çalışıyor · başlangıç ${formatTime(state.running.start)}`
    : 'Durdu';
}

function updateBadge() {
  const running = Boolean(state.running);
  try {
    chrome.action.setBadgeText({ text: running ? '●' : '' });
    if (running) chrome.action.setBadgeBackgroundColor({ color: '#2f7d5b' });
  } catch (_) {
    // Rozet yalnız görsel bir ipucu; hata olursa yok sayılır.
  }
}

function tick(force = false) {
  const now = Date.now();
  const runSec = runningSeconds(now);
  const today = dayKey(now);
  const client = selectedClient();

  // Saniye değişmediyse yeniden hesaplamaya gerek yok.
  const key = `${Math.floor(now / 1000)}|${client.id}`;
  if (!force && key === lastTickKey) return;
  lastTickKey = key;

  const runClient = state.running ? findClient(state.running.clientId) : null;
  const runAmount = amountFor(runSec, runClient ? runClient.rate : 0);

  els.timer.textContent = formatDuration(runSec);
  els.timerAmount.textContent = formatMoney(runAmount);

  let todaySec = 0;
  let todayAmt = 0;
  let totalSec = 0;
  let totalAmt = 0;

  for (const e of state.entries) {
    if (e.clientId !== client.id) continue;
    const sec = entryDuration(e);
    const amt = entryAmount(e);
    totalSec += sec;
    totalAmt += amt;
    // Oturum, başladığı güne sayılır (CSV'deki "Tarih" sütunuyla aynı).
    if (dayKey(e.start) === today) {
      todaySec += sec;
      todayAmt += amt;
    }
  }

  if (state.running && state.running.clientId === client.id) {
    totalSec += runSec;
    totalAmt += runAmount;
    if (dayKey(state.running.start) === today) {
      todaySec += runSec;
      todayAmt += runAmount;
    }
  }

  els.todayTime.textContent = formatDuration(todaySec);
  els.todayAmount.textContent = formatMoney(Math.round(todayAmt * 100) / 100);
  els.totalTime.textContent = formatDuration(totalSec);
  els.totalAmount.textContent = formatMoney(Math.round(totalAmt * 100) / 100);
}

function renderAll(forceRate = false) {
  renderClients();
  renderRate(forceRate);
  renderToggle();
  tick(true);
  updateBadge();
}

/* ---------- İşlemler ---------- */

async function startTimer() {
  const client = selectedClient();
  const running = { clientId: client.id, start: Date.now() };
  await chrome.storage.local.set({ running, selectedClientId: client.id });
  state.running = running;
  state.selectedClientId = client.id;
  renderAll();
}

async function stopTimer(fresh) {
  const run = fresh.running;
  const end = Date.now();
  const entries = Array.isArray(fresh.entries) ? fresh.entries.filter(isValidEntry) : [];
  const sec = Math.max(0, Math.floor((end - run.start) / 1000));
  const client = findClient(run.clientId);
  const rate = client ? client.rate : 0;

  if (sec >= 1) {
    entries.push({
      id: crypto.randomUUID(),
      clientId: run.clientId,
      clientName: client ? client.name : 'Bilinmeyen müşteri',
      start: run.start,
      end,
      rate,
    });
  }

  await chrome.storage.local.set({ entries, running: null });
  state.entries = entries;
  state.running = null;
  renderAll();

  if (sec >= 1) {
    showMessage(`Kaydedildi: ${formatDuration(sec)} · ${formatMoney(amountFor(sec, rate))}`);
  } else {
    showMessage('1 saniyeden kısa oturum kaydedilmedi.');
  }
}

async function toggleTimer() {
  if (busy) return;
  busy = true;
  els.toggle.disabled = true;
  try {
    // Başka bir pencerede açık popup durumu değiştirmiş olabilir; güncel veriyi oku.
    const fresh = await chrome.storage.local.get(['running', 'entries']);
    if (isValidRunning(fresh.running)) {
      await stopTimer(fresh);
    } else {
      await startTimer();
    }
  } catch (err) {
    showMessage('İşlem kaydedilemedi: ' + err.message, true);
  } finally {
    busy = false;
    els.toggle.disabled = false;
  }
}

async function selectClient() {
  if (state.running) {
    els.clientSelect.value = state.running.clientId;
    return;
  }
  state.selectedClientId = els.clientSelect.value;
  renderRate(true);
  tick(true);
  try {
    await chrome.storage.local.set({ selectedClientId: state.selectedClientId });
  } catch (err) {
    showMessage('Seçim kaydedilemedi: ' + err.message, true);
  }
}

async function saveRate() {
  const rate = parseAmount(els.rateInput.value);
  if (!Number.isFinite(rate)) {
    showMessage('Geçerli bir ücret girin (ör. 750 ya da 1.250,50).', true);
    return;
  }
  const client = selectedClient();
  const clients = state.clients.map((c) => (c.id === client.id ? { ...c, rate } : c));
  try {
    await chrome.storage.local.set({ clients });
    state.clients = clients;
    renderRate(true);
    tick(true);
    let text = `${client.name}: saatlik ücret ${formatMoney(rate)}.`;
    if (state.running && state.running.clientId === client.id) {
      text += ' Çalışan oturum bu ücretle kaydedilecek.';
    }
    showMessage(text);
  } catch (err) {
    showMessage('Ücret kaydedilemedi: ' + err.message, true);
  }
}

async function addClient(event) {
  event.preventDefault();
  const name = els.newName.value.trim().replace(/\s+/g, ' ');
  if (!name) {
    showMessage('Müşteri adı boş olamaz.', true);
    els.newName.focus();
    return;
  }
  const lower = name.toLocaleLowerCase('tr-TR');
  if (state.clients.some((c) => c.name.toLocaleLowerCase('tr-TR') === lower)) {
    showMessage('Bu adla bir müşteri zaten var.', true);
    els.newName.focus();
    return;
  }
  const rate = parseAmount(els.newRate.value);
  if (!Number.isFinite(rate)) {
    showMessage('Geçerli bir saatlik ücret girin (ör. 750 ya da 1.250,50).', true);
    els.newRate.focus();
    return;
  }

  const client = { id: crypto.randomUUID(), name, rate };
  const clients = [...state.clients, client];
  const toSave = { clients };
  if (!state.running) toSave.selectedClientId = client.id;

  try {
    await chrome.storage.local.set(toSave);
    state.clients = clients;
    if (!state.running) state.selectedClientId = client.id;
    els.addForm.reset();
    els.addDetails.open = false;
    renderAll(true);
    showMessage(`${name} eklendi.`);
  } catch (err) {
    showMessage('Müşteri eklenemedi: ' + err.message, true);
  }
}

/* ---------- CSV ---------- */

function csvCell(value) {
  let s = String(value);
  // Excel'de formül olarak yorumlanmasın.
  if (/^[=+\-@\t\r]/.test(s)) s = "'" + s;
  if (/[";\r\n]/.test(s)) s = '"' + s.replace(/"/g, '""') + '"';
  return s;
}

function csvNumber(n) {
  return n.toFixed(2).replace('.', ',');
}

function exportCsv() {
  if (state.entries.length === 0) {
    showMessage('Henüz kaydedilmiş çalışma yok.', true);
    return;
  }

  const header = ['Tarih', 'Müşteri', 'Başlangıç', 'Bitiş', 'Süre', 'Saatlik ücret (TL)', 'Tutar (TL)'];
  const rows = [...state.entries]
    .sort((a, b) => a.start - b.start)
    .map((e) => {
      const client = findClient(e.clientId);
      const end = dayKey(e.start) === dayKey(e.end)
        ? formatTime(e.end)
        : `${formatDate(e.end)} ${formatTime(e.end)}`;
      return [
        formatDate(e.start),
        client ? client.name : e.clientName || 'Bilinmeyen müşteri',
        formatTime(e.start),
        end,
        formatDuration(entryDuration(e)),
        csvNumber(e.rate),
        csvNumber(entryAmount(e)),
      ];
    });

  // Türkçe Excel için ";" ayırıcı ve UTF-8 BOM.
  const csv = '﻿' + [header, ...rows].map((r) => r.map(csvCell).join(';')).join('\r\n') + '\r\n';
  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `mesai-kayitlari-${dayKey(Date.now())}.csv`;
  document.body.append(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 10000);

  let text = `${rows.length} kayıt indirildi.`;
  if (state.running) text += ' Çalışan oturum, durdurulunca kayda geçer.';
  showMessage(text);
}

/* ---------- Başlatma ---------- */

els.toggle.addEventListener('click', toggleTimer);
els.clientSelect.addEventListener('change', selectClient);
els.rateSave.addEventListener('click', saveRate);
els.rateInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    e.preventDefault();
    saveRate();
  }
});
els.addForm.addEventListener('submit', addClient);
els.exportBtn.addEventListener('click', exportCsv);

// Aynı anda başka bir pencerede popup açıksa değişiklikler buraya da yansısın.
chrome.storage.onChanged.addListener((_changes, area) => {
  if (area !== 'local' || busy) return;
  loadState().then(() => renderAll(false)).catch(() => {});
});

(async function init() {
  try {
    await loadState();
    renderAll(true);
    setInterval(tick, 250);
  } catch (err) {
    showMessage('Veriler yüklenemedi: ' + err.message, true);
  }
})();
