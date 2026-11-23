# Süre ve ücret sayacı: Chrome eklentisi ve prompt

Müşteri başına çalıştığın süreyi tutan ve saatlik ücretinden tutarı hesaplayan küçük bir Chrome eklentisi (Manifest V3, araç çubuğundaki simgeye basınca açılan pencere). 28 Kasım 2026 videosunda gösterildi; eklentiyi Claude Code yazdı, adını da o koydu: Mesai Sayacı.

## İçinde ne var

- `mesai-sayaci-eklenti.zip`: eklentinin kendisi (4 dosya: `manifest.json`, `popup.html`, `popup.css`, `popup.js`). Kurulum için bunu indir.
- `eklenti/`: aynı 4 dosya tek tek, indirmeden göz atmak için.
- `prompt.txt`: Claude'a verdiğim prompt, birebir.

## Kurulum (geliştirici modu, 2 dakika)

1. `mesai-sayaci-eklenti.zip`'i indir ve bir klasöre çıkar. İçinden `mesai-sayaci` klasörü çıkar.
2. Chrome'un adres çubuğuna `chrome://extensions` yaz.
3. Sağ üstteki "Geliştirici modu"nu aç.
4. "Paketlenmemiş öğe yükle"ye bas, `mesai-sayaci` klasörünü seç.
5. Araç çubuğundaki yapboz simgesinden "Mesai Sayacı"nı sabitle. Simge dosyası olmadığı için Chrome harfli varsayılan simgeyi gösterir.

Klasörü silme ya da taşıma: Chrome eklentiyi o klasörden çalıştırıyor.

## Kullanım

- Müşteriyi seç, saatlik ücreti yazıp "Kaydet"e bas, sonra "Başlat".
- Pencereyi kapatabilirsin. Eklenti başlangıç saatini sakladığı için sayaç kapalıyken de sayar, açınca kaldığı yerden görürsün.
- "Durdur"a basınca kayıt düşer: o müşterinin bugünkü ve toplam süresiyle tutarı görünür.
- Yeni müşteri için "Yeni müşteri ekle".
- "Kayıtları CSV olarak indir": tarih, müşteri, başlangıç, bitiş, süre, saatlik ücret ve tutar sütunları. Türkçe Excel'de doğrudan açılsın diye ayırıcı noktalı virgül, Türkçe harfler bozulmasın diye UTF-8.

## Veri nerede kalıyor?

- Yalnız bu bilgisayarda, Chrome'un eklenti deposunda (`chrome.storage.local`). İzin olarak yalnız `storage` istiyor, hiçbir sunucuya istek atmıyor, dış kaynak (CDN, yazı tipi, uzak görsel) yüklemiyor. Benim denememde dış istek sıfır çıktı.
- Eklentiyi kaldırırsan kayıtları da gider. Kaldırmadan önce CSV'yi indir.

## Bilmen gerekenler

- Müşteri adları ve ücretler örnek, kurgusal (Pudra Bulut Pastanesi, Kırk Sümbül Çiçekçilik, Telve & Tarçın). Kendi müşterilerini ve ücretini yaz.
- Claude eklentiyi yazarken denemediğini kendisi söyledi. Ben temiz bir Chromium'a yükleyip denedim: konsol hatası ve dış istek yoktu, 20 saniye x saatlik 900 TL = 5,00 TL doğru çıktı, pencere kapalıyken de saydı.
- Bildiğim küçük kusurlar: sayaç göstergesi bir saniyeye kadar geriden gelebiliyor (kaydedilen süre başlangıç ve bitiş saatinden doğru hesaplanıyor); CSV'de başlangıç ve bitiş saatleri ayrı ayrı yuvarlandığı için ikisinin farkı süreden 1 saniye fazla görünebiliyor; 1 saniyeden kısa oturumlar kaydedilmiyor; müşteri silme ve kayıt düzenleme yok. İstersen Claude'a "müşteri silme ve kayıt düzenleme ekle" diye yazabilirsin.
- Mağazaya yüklemedim. Geliştirici modunda kendi bilgisayarında kullanmak için.
- Videodaki süre (3 dk 4 sn) ve maliyet (liste fiyatı karşılığı 0,61 $) benim denememe ait; senin denemende farklı çıkabilir.
- Toggl fiyatı resmi fiyat sayfasından (23 Kasım 2026): saatlik ücret ("Billable rates") ücretsiz planda yok, Starter planda; yıllık ödemede kullanıcı başına ayda 9 $, aylık ödemede 12 $. Fiyatlar değişebilir. Toggl telefon uygulaması ve cihazlar arası eşitleme de veriyor, ücretli planı ekip raporları ekliyor; bu eklenti tek kişi ve tek bilgisayar için.

Pratik AI · her gün yeni kit: https://suzunn.github.io/pratikai-medya/kit/
