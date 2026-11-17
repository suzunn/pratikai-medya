# 8 denemenin hikâyesi: her turda ne dedim, ne değişti

Hepsi aynı gün oldu: ilk taslaklar 12:49'da geldi, sekizinci deneme 15:57'de onaylandı.

| Tur | Saat | Deneme | Ne dedim | Ne değişti |
|---|---|---|---|---|
| 0 | öğle | Eski kart şablonu | "Kayıt çok küçük, arka plan çok büyük." | Claude iki yeni yön çıkardı |
| 1 | 12:49 | A (tam ekran) · B (büyük pencere) | A'yı seçtim: "Ekranı niye kaplıyorsun, gözükmüyor. Ortadaki şeridi kaldır. Kedi arada bir sağdan soldan çıksın." | Kedi sürekli yerine kenardan kısa bakış, şerit kalktı |
| 2 | 13:49 | A1 · A2 · A3 | "Üstteki sabit yazıyı kaldır. Ekranda 3-4 yazı oluyor, sade olmalı. Ekran kararmış, olmamalı." | Claude 13 popüler Short'u inceledi, 10 kural çıkardı (format_kurallari.md) |
| 3 | 15:02 | A4 · A5 | "Kenarlar ucundan kaçıyor, kötü duruyor. İlk başlık altyazıyla aynı olunca karışıyor." | Kenar payı 30 px, kanca yazısı ya farklı stil ya hiç |
| 4 | 15:40 | A6 · A7 | - | Kenarlar düzeldi ama yatay kayıt dikeyde küçük kaldı; sıradaki denemede parçalar baştan dikey kuruldu |
| 5 | 15:57 | A8 | "Bu daha iyi olmuş." | ONAY: dikey parçalar, tek altyazı, kanca yazısı yok, seyrek kedi |

## Çıkardığım ders

Claude'a "güzel bir format yap" demek yetmedi. Her turda neyin kalabalık durduğunu ben söyledim. En çok işe yarayan adım,
zevkimi tarif etmek yerine tutan videoları inceletip kuralları yazdırmak oldu. Kendi formatını ararken sen de aynısını dene
(prompt.txt).
