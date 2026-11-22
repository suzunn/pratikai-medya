# Korsan Atölye (T1): renk paleti ve fontlar

Kanalımın günlük videolarında kullandığım tema. Eski kâğıt ve harita dokusu, bantlı fotoğraf kartları, el çizimi kırmızı
mürekkep halka ve oklar, matbaa harfiyle rakamlar ve sarı fosfor kalem.

## Renkler

| Görev | Renk | Hex |
|---|---|---|
| Kâğıt zemin | açık kâğıt | `#EEE2C6` |
| Kart / etiket | krem kâğıt | `#F7EFDC` |
| İkinci zemin | kraft | `#D9C29A` |
| Yazı, çizgi | mürekkep | `#2A1B12` |
| Soluk yazı | soluk kahve | `#7A6450` |
| Vurgu, halka, çarpı | kırmızı mürekkep | `#C8352B` |
| Konuşulan kelime, rakam vurgusu | sarı | `#F2B417` |
| Fosfor kalem (yazının altına, yarı saydam) | fosfor | `rgba(255, 205, 40, 0.78)` |
| Fotoğraf kartının beyaz payı | kart beyazı | `#FFFDF6` |
| Altyazı dolgusu (mürekkep kontur + sert gölge ile) | krem | `#FFF8E8` |

## Fontlar (hepsi ücretsiz, SIL Open Font License)

| Görev | Font | Link |
|---|---|---|
| Başlık, rakam, altyazı (matbaa harfi) | Alfa Slab One | https://fonts.google.com/specimen/Alfa+Slab+One |
| Gövde yazısı | Manrope | https://fonts.google.com/specimen/Manrope |
| El notu (seyrek) | Caveat | https://fonts.google.com/specimen/Caveat |
| Daktilo / prompt yazısı | Courier Prime | https://fonts.google.com/specimen/Courier+Prime |

Font dosyalarını kite koymadım; linkten indir ya da sayfana Google Fonts bağlantısıyla ekle. Türkçe için "latin-ext" alt kümesi
gerekiyor (Google Fonts kendisi ekliyor).

## İmza öğeleri

- **Bantlı fotoğraf kartı:** ekran görüntüsü beyaz paylı kartın içinde, hafif eğik (−1,6° / +1,3°), üstünde iki yarı saydam bant.
- **Kırmızı mürekkep halka:** elle çizilmiş gibi biraz eğri, çizgi 11 px, 0,4 saniyede çizilir.
- **Matbaa rakam + fosfor:** rakam Alfa Slab One, altında sarı fosfor kalem çizgisi.
- **Soluk pusula gülü:** köşede, yüzde 16 opaklıkla.

Örnek: `ornek_kart.html` (tarayıcıda aç).
