# Fable 5.2 mi Opus 5.5 mi? Aynı berber sitesi

Videodaki denemenin dosyaları: iki Claude modeline aynı anda verdiğim prompt ve iki modelin yazdığı siteler.
Siteler kurgusal: dükkân adı, adres ve fiyatlar uydurma.

## İçinde ne var

- `prompt.txt`: ikisine de verdiğim prompt, kelimesi kelimesine.
- `fable_site.html`: Claude Fable 5.2'nin yazdığı site.
- `opus_site.html`: Claude Opus 5.5'in yazdığı site.

## Nasıl kullanırsın

1. `fable_site.html` ya da `opus_site.html` dosyasını indir ve çift tıkla. Tarayıcıda açılır, internet gerekmez.
2. Telefonda nasıl durduğunu görmek için tarayıcıda telefon görünümünü aç (Chrome'da F12, sonra telefon simgesi).
3. Kendi işin için `prompt.txt`'yi Claude'a yapıştır. "Kurgusal bir berber dükkânı" yerine kendi işini, uydurma bilgiler yerine gerçek bilgilerini yaz.
4. Çıkan `index.html`'i önce kendin aç ve randevu formunu dene. Form hiçbir yere göndermiyor, gerçek randevu almak için bir form servisi bağlaman gerekir.

## Karşılaştırma (14 Kasım 2026, aynı prompt, aynı ayar)

| | Fable 5.2 | Opus 5.5 |
|---|---|---|
| Süre | 4 dk 47 sn | 1 dk 44 sn |
| Maliyet (API liste fiyatıyla) | 1,75 $ | 0,35 $ |
| Yazmaya başladığı an | 2 dk 27 sn (143 sn düşündü) | 8. saniye |
| Üretilen token | 30.706 | 12.144 |
| Dosya | 37 KB, 798 satır | 24 KB, 551 satır |
| Fiyat listesindeki hizmet | 8 | 7 |
| Randevu formu | açılıyor, çalışıyor | açılıyor, çalışıyor |
| 1M token liste fiyatı | 8 $ giriş, 40 $ çıkış | 4 $ giriş, 20 $ çıkış |

Claude Max aboneliğiyle çalıştırdım, ayrıca ödeme yapmadım. Maliyetler Claude Code'un API liste fiyatıyla hesapladığı karşılık.
Benchmark (Anthropic, 9 Kasım 2026): gerçek uzaktan freelance projelerinden kurulmuş Remote Labor Index testinde Fable 5.2 %41,3, Opus 5.5 %21,3.
