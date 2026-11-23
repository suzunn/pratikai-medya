# Videonu ikinci bir Claude'a denetlet: yayın öncesi kontrol listesi, denetçi promptu ve rapor şablonu

Videolarımı bir Claude yapıyor, yayından önce de ikinci bir Claude kontrol ediyor. 19 Kasım gecesi dört videoda 10 hata buldu, hepsi
yayından önce düzeldi. Denetçinin kendisi de bir hata yaptı. 29 Kasım 2026 videosunda bu süreci anlattım. Bu kitte aynı kontrolü kendi
videoların için kurman için gereken üç dosya var.

## İçinde ne var

- `denetim_listesi.md`: yayın öncesi altı madde (kanca, boş kare, altyazı çakışması, kenar payı, yasak ses, süre), her birinde neye ve nasıl bakacağın.
- `denetci_promptu.txt`: videoyu yapan sohbetten ayrı, yeni bir Claude sohbetine vereceğin denetçi promptu. Kare kare kontrol ettirir, her bulguyu saniyesiyle yazdırır.
- `denetim_raporu_sablonu.md`: denetçiden isteyeceğin rapor biçimi ve benim videolarımdan gerçek bulgularla doldurulmuş bir örnek.

## Nasıl kullanırsın

1. Videoyu saniyede 4 kareye böl (komut `denetim_listesi.md`'nin başında) ya da videoyu doğrudan ver.
2. Yeni bir Claude sohbeti aç. `denetci_promptu.txt`'deki köşeli parantezli yerlere kendi kurallarını yaz, kareleri ve promptu ver.
3. Raporu `denetim_raporu_sablonu.md`'deki tabloyla al. Büyük bulgular düzelmeden videoyu yayına koyma.
4. Düzelttikten sonra aynı denetimi bir kez daha yaptır. Benim videomdaki boş kareyi ikinci tur yakaladı.

## Bilmen gerekenler

- Denetçi, verdiğin kurala harfiyen uyar. Kural yanlışsa o da yanlış yapar. Kurallarını da arada bir gözden geçir.
- Videodaki süre (2 saat 40 dakika) ve hata sayısı benim dört videoma ait; seninkinde farklı çıkabilir.
- Komutlar ücretsiz ffmpeg aracıyla çalışır. Kurmadıysan kareleri telefonda ekran görüntüsüyle de alabilirsin.

Pratik AI · her gün yeni kit: https://suzunn.github.io/pratikai-medya/kit/
