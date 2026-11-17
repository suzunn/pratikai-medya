# 13 popüler Short'un ölçümü (özet)

Yöntem: YouTube aramasından (Shorts filtresi, bu yıl) ekran kaydı ağırlıklı Short'lar indirildi. Her biri saniyede 1 kare,
ilk 2,5 saniye yarım saniyede 1 kare incelendi. Kesim sayısı ffmpeg sahne tespitiyle (eşik 0,3), sessizlik -40 dB ile ölçüldü.
Giriş yapılmadı, yalnız okundu. Kanal adları bu özette yok.

| # | İzlenme | Süre | Ekranda aynı anda yazı | Altyazı | Yüz/maskot | Kesim aralığı | İlk 2 sn |
|---|---|---|---|---|---|---|---|
| 1 | 352K | 50 sn | 1 (ilk 2,5 sn'de 2) | 2-3 kelime, beyaz, kalın, orta | alt %40'ta sabit yüz | ~1,2 sn | yazılı kanca + söz, kutu 2,5 sn'de kalkıyor |
| 2 | 742K | 44 sn | 1-2 | 1-2 kelime, orta | tam ekran yüz ile demo arasında | ~1 sn | büyük serif başlık + söz |
| 3 | 403K | 39 sn | 1-2 | 1-3 kelime | yalnız baş ve son (~8 sn) | ~0,8 sn | dev başlık + söz |
| 4 | 324K | 51 sn | 1-2 | 1-3 kelime, BÜYÜK HARF | alt yarıda sürekli yüz | ~0,3 sn | dört satırlık liste; en kalabalık örnek |
| 5 | 359K | 25 sn | 0 | yok | köşede küçük yüz | ~2,5 sn | doğrudan bitmiş iş, yazı yok |
| 6 | 297K | 29 sn | 1 | 1-3 kelime, gri kutulu | baş 3 sn + sonda | ~0,6 sn | sonuç üstte, yüz altta |
| 7 | 256K | 37 sn | 1 | 1 kelime + vurgu el yazısı | alt yarıda, sonra 20 sn yüzsüz | ~0,4 sn | fiyat yazılı sonuç + söz |
| 8 | 353K | 21 sn | 2 (sabit üst başlık + altyazı) | 2-3 kelime | baş ve son | ~1,5 sn | yüz + abartılı ifade |
| 9 | 481K | 22 sn | 1 | 3-5 kelime cümle | gerçek çekim | ~0,8 sn | soru sözle |
| 10 | 254K | 45 sn | 1 | 3-6 kelime, sarı | yüz ile kayıt arasında | ~1 sn | yüz + iddialı söz |
| 11 | 229K | 83 sn | 1 (ilk 4 sn dev başlık) | 2-4 kelime, sarı | yüz, araya kayıt | ~0,6 sn | yüz + dev başlık |
| 12 | 91K | 56 sn | 2 (bölüm etiketi + altyazı) | 2 kelime | baş ve son | ~3 sn | yüz + iki logo |
| 13 | 7K | 50 sn | 2-3 (altyazı + "link yorumlarda" + alt şerit) | 2-3 kelime | üst yarıda sürekli yüz | ~1,7 sn | kalabalık, düşük izlenme |

Ses: hiçbirinde 0,25 saniyeden uzun sessizlik yok. Sesin altında sürekli hafif müzik ya da oda sesi var.

Çıkan kurallar: `format_kurallari.md`.
