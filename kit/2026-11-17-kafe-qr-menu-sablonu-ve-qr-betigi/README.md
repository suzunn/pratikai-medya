# Kafe QR menü şablonu ve QR betiği

Kâğıt menünün görüntüsünü Claude Code'a verip telefonda açılan bir QR menü sitesi ve masa masa QR kodu ürettirdiğim denemenin
dosyaları. 17 Kasım 2026 videosunda gösterildi. Kafe ("Telve & Tarçın") ve menü kurgusal.

## İçinde ne var

- `prompt.txt`: Claude Code'a verdiğim prompt, birebir.
- `ornek_kagit_menu.png`: denemede kullandığım örnek kâğıt menü (17 ürün; Latte'nin fiyatı üstü çizilip elle 125 yazılmış).
- `menu.html`: Claude'un yazdığı QR menü sitesi (Claude'un çıktısında adı `index.html`; kit sayfasında bu ad ayrılmış olduğu için `menu.html` diye koydum). Tek dosya, internet gerektirmez; kategoriler üstte yapışkan düğme, adresin sonunda `?masa=5` varsa üstte "Masa 5" yazar.
- `qr_yap.py`: menünün adresini QR koda çeviren betik (Claude yazdı). `qr.png` + `qr.svg` üretir; `--hepsi` ile 1-10. masalar için ayrı QR.

## Nasıl kullanırsın

1. İndirince `menu.html`'in adını `index.html` yap. Kendi menün için onu bir metin düzenleyicide aç, `const MENU = [` ile başlayan listede ürün adlarını ve fiyatları değiştir. Kafenin adı sayfanın en üstündeki başlık satırında ("Telve & Tarçın" yazan yer).
   İstersen bunu da Claude'a yaptır: kendi menünün fotoğrafını klasöre koy, `prompt.txt`'deki `menu.png` adını kendi dosyanın adıyla değiştirip Claude Code'a ver.
2. Bilgisayarında dene: klasörde `python -m http.server 8017` çalıştır, tarayıcıda `http://localhost:8017/?masa=5` adresini aç.
3. QR için önce `pip install segno`, sonra `qr_yap.py`'nin başındaki `ADRES` satırına sitenin gerçek adresini yaz (siteyi nereye koyduysan) ve `python qr_yap.py --hepsi` çalıştır. Çıkan `qr_masa1.png` ... `qr_masa10.png` dosyalarını bastırıp masalara koy.

## Bilmen gerekenler

- İşletme adı ve menü kurgusal; kendi bilgilerini yaz. Varsayılan adres `http://localhost:8017/` yalnız kendi bilgisayarında çalışır: telefonla okutmadan önce adresi değiştir.
- Bu sürümde yönetim paneli yok: fiyat değişince `index.html`'i düzenleyip yeniden yüklemen gerekir.
- Videodaki süre (43 saniye) ve maliyet (0,17 $, API liste fiyatı karşılığı; Max abonelikte ayrıca ödemedim) benim denememe ait; senin denemende farklı çıkabilir.
- Claude Code bu oturumda komut çalıştıramıyordu; betiği ben çalıştırdım, 10 QR'ın hepsini bilgisayarda okutup kontrol ettim.
- Armut'taki 2.000-7.000 TL bir talep/teklif bandıdır (Kasım 2026), kazanç sözü değildir.

Pratik AI · her gün yeni kit: https://suzunn.github.io/pratikai-medya/kit/
