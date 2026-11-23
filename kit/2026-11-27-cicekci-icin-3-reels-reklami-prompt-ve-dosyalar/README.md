# Çiçekçi için 3 Reels reklamı: prompt ve dosyalar

Kurgusal bir çiçekçi (Kırk Sümbül Çiçekçilik) için Claude Code'un yazdığı 15'er saniyelik üç dikey reklam: yılbaşı buketi, aynı gün teslim ve ilk siparişe indirim. Video programı ya da video modeli yok; reklamların hepsi HTML, CSS ve SVG animasyonu. 27 Kasım 2026 videosunda gösterildi.

## İçinde ne var

- `prompt.txt`: Claude'a verdiğim prompt, birebir.
- `reklam_1.html`: yılbaşı buketi (hediye paketi açılır, buket parça parça kurulur, fiyat etiketi sallanarak iner).
- `reklam_2.html`: aynı gün teslim (çalar saat 14.00'e döner, araba kapıya gelir).
- `reklam_3.html`: ilk siparişe indirim (rozet %0'dan %20'ye sayar, çiçekler açar).

Her dosya tek parça, dış kaynak yok (internet, font ya da görsel indirmez). Çift tıklayıp tarayıcıda açman yeter. Reklam 15. saniyede son karede durur; baştan oynatmak için sayfayı yenile (F5).

Dosyalar Claude'un yazdığı hâliyle duruyor; yalnız yayın öncesi gizlilik taramam bazı sayıları yanlışlıkla şifre, telefon ya da kart numarası sandığı için yazımlarını değiştirdim, değerleri aynı: çam dalı ve iki çiçek yaprağı çiziminin SVG koordinatlarına boşluk/virgül ekledim, rastgele sayı üretecindeki 2 üzeri 32 sayısını aynı değerin `0x100000000` yazımıyla değiştirdim. Görüntü aynı.

## Metni, fiyatı ve rengi değiştirmek

Dosyayı bir metin düzenleyiciyle aç (Not Defteri de olur) ve Bul ile arat:

- **İşletme adı:** "Kırk Sümbül" her dosyada üst rozette ve kapanışta geçiyor. Hepsini kendi adınla değiştir.
- **Fiyat (reklam_1):** `1.250` iki yerde geçiyor: etiket (`class="price"`) ve kapanıştaki hatırlatma satırı (`class="remind"`).
- **Saat (reklam_2):** `14.00` yazısı iki yerde. Akrebin dönüşü ayrı bir animasyon; saati değiştirirsen Claude'a "akrep 16.00'yı göstersin" demen yeterli.
- **İndirim (reklam_3):** sayaç `@keyframes count{from{--n:0}to{--n:20}}` satırında. 20'yi kendi oranınla değiştir, kapanıştaki "İlk siparişe %20 indirim" yazısını da düzelt.
- **"örnek" etiketleri:** gerçek fiyat ve kampanyayı yazınca `class="ornek"` olan küçük etiketleri silebilirsin.
- **Renkler:** renkler doğrudan kod olarak yazılı (ör. mor zemin `#2b1238`, kırmızı fiyat `#c81d34`). En kolayı Claude'a dosyayı verip "morları yeşil tonlara çevir, gerisi aynı kalsın" demek.

Değişiklikten sonra dosyayı tarayıcıda baştan sona izle: yazıların taşıp taşmadığına ve son karede neyin göründüğüne bak.

## Reklamı ücretsiz ve hesapsız mp4 yapmak

Reklam bir web sayfası; videoya çevirmenin en kolay yolu ekran kaydı:

1. **Telefondan:** HTML dosyasını telefonuna at, tarayıcıda aç, telefonun kendi ekran kaydını başlat, sayfayı yenile ve 15 saniye kaydet. Sonra galeride baştaki ve sondaki fazlalığı kırp, üstteki durum çubuğu görünüyorsa kadrajı daralt.
2. **Windows'tan:** Chrome ya da Edge'de dosyayı aç, F12 ile geliştirici araçlarını aç, Ctrl+Shift+M ile telefon görünümüne geç (ör. 360x640). Windows 11'deki Ekran Alıntısı Aracı'nın video kaydıyla ya da ücretsiz OBS Studio ile yalnız bu alanı kaydet, F5'e bas, 15 saniye sonra durdur.

İkisinde de hesap açman ya da bir şey satın alman gerekmez. Kaydı 9:16 (dikey) tut.

## Müzik ve lisans

Videoda reklamların altında çalan müzik bizim kütüphanemizden; kitte müzik yok ve o müzik dağıtılmıyor. Kendi reklamında ya lisansını bildiğin bir müzik kullan ya da Instagram'da paylaşırken uygulamanın kendi müzik kütüphanesinden seç (işletme hesaplarında seçenekler kısıtlı olabilir).

## Bilmen gerekenler

- İşletme adı, fiyat, saat ve kampanya kurgusal ve "örnek"; kendi bilgilerini yaz. Gerçek telefon, adres ya da hesap yok.
- Videodaki süre (20 dk 38 sn; bunun 15 dakikası yazmadan önce düşünme) ve maliyet (liste fiyatı karşılığı 3,70 $, Max abonelikte ayrıca ödenmedi) benim denememe ait; senin denemende farklı çıkabilir. Aynı promptla bir önceki denemeyi zaman sınırım yetmeyeceği için 12. dakikada ben durdurmuştum (dosya yazılmamıştı); videodaki rakamlar ikinci denemenin.
- Claude reklamları yazarken hiçbirini oynatamadı, bunu kendisi söyledi. Ben telefon görünümünde (360x640) kaydettim: üçü de tam 15 saniye sürdü, konsol hatası ve dış istek yoktu. Sen de müşteriye göstermeden önce baştan sona izle.
- Bu reklamlar ürün fotoğrafı ya da çekiminin yerini tutmaz; duyuru ve kampanya için iyi bir başlangıç.
- Piyasa fiyatı bir ilan bandıdır (Armut, video editörü, Instagram videosu, 23 Kasım 2026: 1.000 TL - 3.500 TL), kazanç sözü değildir.

Pratik AI · her gün yeni kit: https://suzunn.github.io/pratikai-medya/kit/
