#!/usr/bin/env python3
"""
OpenStreetMap'te web sitesi bilgisi girilmemiş işletmeleri sayar.

Overpass API'ye tek bir istek atar (tekrar deneme yok), sonuçları
ozet.json, liste.csv ve harita.html dosyalarına yazar.
Yalnız Python standart kütüphanesi kullanılır.

Çalıştırma:  python ara.py
"""

import csv
import json
import math
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# --------------------------------------------------------------------------
# AYARLAR — kolayca değiştirilebilir
# --------------------------------------------------------------------------
IL_ADI = "İstanbul"
IL_ADMIN_LEVEL = "4"
ILCE_ADI = "Kadıköy"
ILCE_ADMIN_LEVEL = "6"

# (kısa anahtar, görünen ad, [(OSM etiketi, değer), ...])
# Sıra önemlidir: iki kategoriye birden giren kayıt, listede ÖNCE gelen
# kategoriye yazılır ve yalnız bir kez sayılır.
KATEGORILER = [
    ("kafe", "Kafe", [("amenity", "cafe")]),
    ("restoran", "Restoran", [("amenity", "restaurant")]),
    ("pastane", "Pastane", [("shop", "bakery"), ("shop", "pastry")]),
    ("berber_kuafor", "Berber/Kuaför", [("shop", "hairdresser")]),
    ("cicekci", "Çiçekçi", [("shop", "florist")]),
]

# Bunlardan biri dolu ise "site bilgisi var" sayılır.
SITE_ETIKETLERI = ("website", "contact:website", "url")

OVERPASS_URL = "https://overpass-api.de/api/interpreter"
ZAMAN_ASIMI = 60  # saniye (hem sorgu içinde hem HTTP isteğinde)
USER_AGENT = "osm-site-bilgisi-sayimi/1.0 (Python urllib; tek Overpass sorgusu)"

KLASOR = Path(__file__).resolve().parent
SABLON = KLASOR / "harita_sablon.html"
OZET_DOSYASI = KLASOR / "ozet.json"
LISTE_DOSYASI = KLASOR / "liste.csv"
HARITA_DOSYASI = KLASOR / "harita.html"
YER_TUTUCU = "/*__VERI__*/null"

HARITA_GENISLIK = 1000  # SVG viewBox genişliği
HARITA_KENAR = 24       # SVG kenar boşluğu


# --------------------------------------------------------------------------
def hata(mesaj):
    print(f"HATA: {mesaj}", file=sys.stderr)
    sys.exit(1)


def oq(metin):
    """Overpass QL dize kaçışı."""
    return metin.replace("\\", "\\\\").replace('"', '\\"')


def sorgu_olustur():
    s = [
        f"[out:json][timeout:{ZAMAN_ASIMI}];",
        f'area["boundary"="administrative"]["admin_level"="{oq(IL_ADMIN_LEVEL)}"]'
        f'["name"="{oq(IL_ADI)}"]->.il;',
        f'rel["boundary"="administrative"]["admin_level"="{oq(ILCE_ADMIN_LEVEL)}"]'
        f'["name"="{oq(ILCE_ADI)}"](area.il)->.ilce;',
        ".ilce out geom;",
        ".ilce map_to_area->.alan;",
        "(",
    ]
    for _, _, etiketler in KATEGORILER:
        for k, v in etiketler:
            s.append(f'  nwr["{oq(k)}"="{oq(v)}"](area.alan);')
    s += [");", "out center;"]
    return "\n".join(s)


def overpass_iste(sorgu):
    govde = urllib.parse.urlencode({"data": sorgu}).encode("utf-8")
    istek = urllib.request.Request(
        OVERPASS_URL,
        data=govde,
        headers={
            "User-Agent": USER_AGENT,
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "Accept": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(istek, timeout=ZAMAN_ASIMI) as yanit:
            ham = yanit.read()
    except urllib.error.HTTPError as e:
        aciklama = {
            400: "Sorgu hatalı (400). Ayarları kontrol edin.",
            429: "Overpass çok fazla istek bildirdi (429). Birkaç dakika bekleyip tekrar çalıştırın.",
            504: "Overpass sunucusu meşgul ya da zaman aşımına uğradı (504). Daha sonra tekrar deneyin.",
        }.get(e.code, f"Overpass HTTP {e.code} hatası döndürdü.")
        hata(aciklama)
    except (TimeoutError, socket.timeout):
        hata(f"Overpass {ZAMAN_ASIMI} saniye içinde yanıt vermedi. Daha sonra tekrar deneyin.")
    except urllib.error.URLError as e:
        if isinstance(e.reason, (TimeoutError, socket.timeout)):
            hata(f"Overpass {ZAMAN_ASIMI} saniye içinde yanıt vermedi. Daha sonra tekrar deneyin.")
        hata(f"Overpass'a bağlanılamadı: {e.reason}. İnternet bağlantınızı kontrol edin.")
    except OSError as e:
        hata(f"Ağ hatası: {e}")

    try:
        veri = json.loads(ham.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        hata("Overpass'tan gelen yanıt JSON değil (sunucu yoğun olabilir). Daha sonra tekrar deneyin.")

    uyari = veri.get("remark", "")
    if uyari and ("error" in uyari.lower() or "timed out" in uyari.lower()):
        hata(f"Overpass sorgusu tamamlanamadı: {uyari.strip()}")
    return veri


def kategori_bul(etiketler):
    for i, (_, _, kosullar) in enumerate(KATEGORILER):
        for k, v in kosullar:
            if etiketler.get(k) == v:
                return i
    return None


def site_var_mi(etiketler):
    return any(str(etiketler.get(e, "")).strip() for e in SITE_ETIKETLERI)


def yuzde(pay, payda):
    return round(100.0 * pay / payda, 1) if payda else 0.0


def ilce_mi(el):
    t = el.get("tags", {})
    return (
        el.get("type") == "relation"
        and t.get("boundary") == "administrative"
        and t.get("admin_level") == ILCE_ADMIN_LEVEL
        and t.get("name") == ILCE_ADI
    )


def harita_verisi(sinir_cizgileri, kayitlar):
    """Enlem/boylamı basit eşdikdörtgen izdüşümle SVG koordinatına çevirir."""
    tum = [p for c in sinir_cizgileri for p in c] + [(k["enlem"], k["boylam"]) for k in kayitlar]
    if not tum:
        return {"genislik": HARITA_GENISLIK, "yukseklik": HARITA_GENISLIK, "sinir": [], "noktalar": []}

    enlemler = [p[0] for p in tum]
    boylamlar = [p[1] for p in tum]
    orta_enlem = (min(enlemler) + max(enlemler)) / 2
    kx = math.cos(math.radians(orta_enlem))

    x_min, x_max = min(boylamlar) * kx, max(boylamlar) * kx
    y_min, y_max = min(enlemler), max(enlemler)
    genislik_ham = max(x_max - x_min, 1e-9)
    yukseklik_ham = max(y_max - y_min, 1e-9)
    olcek = (HARITA_GENISLIK - 2 * HARITA_KENAR) / genislik_ham
    yukseklik = math.ceil(yukseklik_ham * olcek + 2 * HARITA_KENAR)

    def xy(enlem, boylam):
        return [
            round((boylam * kx - x_min) * olcek + HARITA_KENAR, 1),
            round((y_max - enlem) * olcek + HARITA_KENAR, 1),
        ]

    return {
        "genislik": HARITA_GENISLIK,
        "yukseklik": yukseklik,
        "sinir": [[xy(*p) for p in c] for c in sinir_cizgileri],
        # [x, y, kategori sırası, site bilgisi var mı (0/1)] — ad yok
        "noktalar": [xy(k["enlem"], k["boylam"]) + [k["kat"], 1 if k["site"] else 0] for k in kayitlar],
    }


def main():
    try:
        sys.stdout.reconfigure(errors="replace")
    except AttributeError:
        pass

    if not SABLON.exists():
        hata(f"Şablon bulunamadı: {SABLON.name} (ara.py ile aynı klasörde olmalı).")
    sablon = SABLON.read_text(encoding="utf-8")
    if YER_TUTUCU not in sablon:
        hata(f"Şablonda {YER_TUTUCU} yer tutucusu yok.")

    print(f"Overpass'a sorgu gönderiliyor ({ILCE_ADI}, {IL_ADI})... en fazla {ZAMAN_ASIMI} sn")
    sorgu_zamani = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    veri = overpass_iste(sorgu_olustur())
    osm_tarihi = veri.get("osm3s", {}).get("timestamp_osm_base")
    elemanlar = veri.get("elements", [])

    ilce = next((e for e in elemanlar if ilce_mi(e)), None)
    if ilce is None:
        hata(f"'{IL_ADI}' içinde admin_level={ILCE_ADMIN_LEVEL} olan '{ILCE_ADI}' sınırı bulunamadı. "
             "ILCE_ADI / IL_ADI ayarlarını kontrol edin.")

    sinir = []
    for uye in ilce.get("members", []):
        if uye.get("type") == "way" and uye.get("geometry"):
            cizgi = [(p["lat"], p["lon"]) for p in uye["geometry"] if p]
            if len(cizgi) >= 2:
                sinir.append(cizgi)

    gorulen = set()
    kayitlar = []
    adsiz = 0
    for el in elemanlar:
        if el is ilce:
            continue
        anahtar = (el.get("type"), el.get("id"))
        if anahtar in gorulen:
            continue
        gorulen.add(anahtar)

        etiketler = el.get("tags", {})
        kat = kategori_bul(etiketler)
        if kat is None:
            continue
        ad = str(etiketler.get("name", "")).strip()
        if not ad:
            adsiz += 1
            continue
        if "lat" in el and "lon" in el:
            enlem, boylam = el["lat"], el["lon"]
        elif "center" in el:
            enlem, boylam = el["center"]["lat"], el["center"]["lon"]
        else:
            continue
        kayitlar.append({"ad": ad, "kat": kat, "enlem": enlem, "boylam": boylam,
                         "site": site_var_mi(etiketler)})

    # --- özet ---
    kat_ozet = []
    for i, (anahtar, gorunen, _) in enumerate(KATEGORILER):
        toplam = sum(1 for k in kayitlar if k["kat"] == i)
        yok = sum(1 for k in kayitlar if k["kat"] == i and not k["site"])
        kat_ozet.append({"anahtar": anahtar, "kategori": gorunen, "toplam": toplam,
                         "site_bilgisi_yok": yok, "site_bilgisi_yok_yuzde": yuzde(yok, toplam)})
    genel_toplam = len(kayitlar)
    genel_yok = sum(1 for k in kayitlar if not k["site"])

    ozet = {
        "il": IL_ADI,
        "ilce": ILCE_ADI,
        "sorgu_zamani": sorgu_zamani,
        "osm_veri_tarihi": osm_tarihi,
        "kategoriler": kat_ozet,
        "genel": {"toplam": genel_toplam, "site_bilgisi_yok": genel_yok,
                  "site_bilgisi_yok_yuzde": yuzde(genel_yok, genel_toplam)},
        "adi_olmadigi_icin_sayilmayan": adsiz,
        "site_etiketleri": list(SITE_ETIKETLERI),
        "kaynak": "© OpenStreetMap katkıda bulunanlar, ODbL — https://www.openstreetmap.org/copyright",
    }
    OZET_DOSYASI.write_text(json.dumps(ozet, ensure_ascii=False, indent=2), encoding="utf-8")

    # --- liste (yalnız site bilgisi olmayanlar; yalnız ad, kategori, konum) ---
    eksikler = sorted((k for k in kayitlar if not k["site"]), key=lambda k: (k["kat"], k["ad"].casefold()))
    with LISTE_DOSYASI.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ad", "kategori", "enlem", "boylam"])
        for k in eksikler:
            w.writerow([k["ad"], KATEGORILER[k["kat"]][1], round(k["enlem"], 7), round(k["boylam"], 7)])

    # --- harita (adlar yok, yalnız noktalar) ---
    hv = harita_verisi(sinir, kayitlar)
    hv.update({
        "ilce": ILCE_ADI,
        "osm_tarihi": osm_tarihi,
        "kategoriler": [{"ad": k["kategori"], "toplam": k["toplam"], "yok": k["site_bilgisi_yok"]}
                        for k in kat_ozet],
        "toplam": genel_toplam,
        "yok": genel_yok,
    })
    json_metin = json.dumps(hv, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    HARITA_DOSYASI.write_text(sablon.replace(YER_TUTUCU, json_metin), encoding="utf-8")

    # --- ekran ---
    print()
    print(f"{ILCE_ADI}: web sitesi bilgisi olmayan / toplam (adı olanlar)")
    genislik = max(len(k["kategori"]) for k in kat_ozet + [{"kategori": "TOPLAM"}])
    for k in kat_ozet:
        print(f"  {k['kategori']:<{genislik}}  {k['site_bilgisi_yok']:>5} / {k['toplam']:<5}"
              f" (%{k['site_bilgisi_yok_yuzde']})")
    print(f"  {'-' * (genislik + 22)}")
    print(f"  {'TOPLAM':<{genislik}}  {genel_yok:>5} / {genel_toplam:<5} (%{yuzde(genel_yok, genel_toplam)})")
    print()
    print(f"Adı olmadığı için sayılmayan: {adsiz}")
    print(f"OSM veri tarihi: {osm_tarihi or 'bilinmiyor'}")
    print(f"Yazılan dosyalar: {OZET_DOSYASI.name}, {LISTE_DOSYASI.name}, {HARITA_DOSYASI.name}")


if __name__ == "__main__":
    main()
