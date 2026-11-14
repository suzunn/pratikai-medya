# Canva Pro yerine: tek HTML şablondan 30 Instagram görseli

"Canva Pro'ya ayda 240 TL vermeden Claude'a 30 Instagram görseli bastırdım" videosundaki (16 Kasım 2026) dosyaların aynısı.
Claude Code kurgusal bir kafe için tek bir şablon ve onu PNG'ye çeviren küçük bir betik yazdı; betik 30 gönderiyi 1080x1350 olarak bastı.

## İçinde ne var

- `sablon.html`: 30 gönderinin hepsi bu tek dosyada. Adresin sonundaki `#1` ... `#30` hangi gönderinin açılacağını seçer (tarayıcıda `sablon.html#7` gibi açıp bakabilirsin)
- `bas.py`: bilgisayardaki Microsoft Edge ya da Google Chrome'u görünmez (headless) çalıştırıp 30 gönderiyi `gorseller/gonderi_01.png` ... `gonderi_30.png` olarak basar. Yalnız Python'un kendi kütüphanesini kullanır, ek kurulum istemez
- `bas.bat`: Windows için tek tık (çift tıkla, `bas.py`'yi çalıştırır)
- `prompt.txt`: Claude Code'a verdiğim ilk prompt, birebir
- `prompt_duzeltme.txt`: ilk baskıda 4 gönderinin yerleşimi bozuk çıktı; düzeltmek için verdiğim kısa istek (4 cümle), birebir
- `prompt_kendi_isletmen.txt`: şablonu kendi işletmene uyarlatmak için doldurulacak prompt (köşeli parantezli yerler)
- `ornek/`: basılan 30 gönderiden 4 örnek

## Nasıl kullanılır

1. **Python 3** kurulu olsun: https://www.python.org/downloads/ (Windows'ta kurarken "Add python.exe to PATH" kutusunu işaretle). Edge Windows'ta zaten var; Mac'te Edge ya da Chrome kurulu olmalı.
2. Bu klasörü olduğu gibi bir yere çıkar. Windows'ta `bas.bat`'a çift tıkla; Mac/Linux'ta terminalde bu klasöre gelip `python3 bas.py` yaz.
3. 30 PNG `gorseller/` klasörüne düşer (benim bilgisayarımda 18-30 saniye sürdü). Instagram'a 4:5 dikey gönderi olarak doğrudan yüklenir.
4. Kendi işletmen için: `prompt_kendi_isletmen.txt`'yi doldur, bu klasörde Claude Code'a (ya da şablonu yapıştırarak Claude sohbetine) ver, sonra `bas.py`'yi yeniden çalıştır.
5. Bir gönderi bozuk görünürse Claude'a kısaca söyle ("6. gönderide başlık küçük kalmış, büyüt" gibi; benim verdiğim istek `prompt_duzeltme.txt`'te). Benim denememde düzeltme 51 saniye sürdü.

## Bilmen gerekenler

- "Mavi Fincanlık" ve içindeki ürünler, fiyatlar, yorumlar kurgusaldır; kendi bilgilerini yaz.
- Videodaki süre ve maliyet benim denememe ait: şablon + betik 9 dk 31 sn ve 1,79 $, düzeltme 51 sn ve 0,37 $ (Claude Opus 5.5, API liste fiyatı karşılığı; Max abonelikte ayrıca ödenmedi). Senin denemende farklı çıkabilir.
- Canva Pro fiyatı, 14 Kasım 2026'da canva.com/tr_tr/pricing sayfasındaki rakamdır: bir kişi için aylık 240 TL (yıllık 1.920 TL). Fiyatlar değişebilir.
- Canva'nın sürükle-bırak editörü ve hazır şablonları bu yöntemde yok; bu kit aynı düzeni her ay yeniden basmak isteyenler için.
- Şablon internete bağlanmaz (dış font, görsel, CDN yok); yazı tipleri bilgisayarındaki sistem yazı tiplerinden gelir, o yüzden görünüm bilgisayardan bilgisayara biraz değişebilir.

Pratik AI · her gün yeni kit: https://suzunn.github.io/pratikai-medya/kit/
