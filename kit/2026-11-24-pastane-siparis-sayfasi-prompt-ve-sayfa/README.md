# Pastane sipariş sayfası: prompt ve sayfa

Müşterinin pastasını kendisi tasarladığı tek dosyalık mobil sipariş sayfası: kişi sayısı, kat, krema rengi ve üst yazı seçiliyor, pasta çizimi ve fiyat anında değişiyor, sipariş WhatsApp mesajı olarak hazırlanıyor. 24 Kasım 2026 videosunda gösterildi; pastane kurgusal (Pudra Bulut Pastanesi).

## İçinde ne var

- `prompt.txt`: Claude'a verdiğim prompt, birebir.
- `siparis.html`: Claude'un yazdığı sipariş sayfası (tek dosya, dış kaynak yok). Çift tıklayıp tarayıcıda açman yeter. Yayına alırken adını `index.html` yap.

## Fiyat listesini değiştirmek

Dosyayı bir metin düzenleyiciyle aç. Kodun script bölümünün en başında örnek fiyat listesi duruyor:

```js
const FIYAT_LISTESI = {
  kisi: { 6: 650, 10: 950, 16: 1400 },
  kat: { 1: 0, 2: 400, 3: 850 },
  renk: { vanilya: 0, pembe: 60, cikolata: 90, fistik: 140 },
  yazi: 50
};
```

- `kisi`: kişi sayısına göre taban fiyat (TL). Yeni boy eklemek için ör. `20: 1800` yaz; düğmeler listeden kendiliğinden oluşuyor.
- `kat`: kat başına ek ücret, `renk`: krema rengi ek ücreti, `yazi`: pasta üstü yazı ücreti (0 yaparsan ücretsiz olur).
- Rakamların hepsi örnek. Pastanenin gerçek fiyatlarını onunla birlikte gir.

## Renkleri ve adı değiştirmek

- Krema renkleri `RENKLER` içinde: her rengin adı (`ad`) ve çizimdeki tonları (`ana`, `acik`, `koyu`, `yazi`). Yeni renk eklersen aynı anahtarla `FIYAT_LISTESI.renk` içine ücretini de yaz.
- Sayfanın genel renkleri style bölümünün başındaki `:root` değişkenlerinde (`--pudra`, `--vurgu`, `--zemin`...).
- İşletme adı sayfada ve mesaj metninde "Pudra Bulut Pastanesi" olarak geçiyor. Dosyada arat, kendi adınla değiştir; en alttaki "kurgusal bir pastanedir" satırını da sil.

## WhatsApp numarası

- `WHATSAPP_NUMARASI` şu an yer tutucu (`+90 5XX XXX XX XX`). Pastanenin numarasını yaz.
- Sayfa bugün yalnız mesajın önizlemesini gösteriyor, hiçbir yere bir şey göndermiyor. Müşterinin WhatsApp'ı mesaj hazır şekilde açılsın istiyorsan Claude'a şunu yaz: "Önizlemenin altına 'WhatsApp'ta aç' düğmesi ekle, wa.me bağlantısıyla mesaj hazır gelsin." Sonra kendi numaranla dene.

## Ücretsiz yayına almak

Hesabı sen açarsın, sayfa tek dosya olduğu için hepsi birkaç dakika sürer:

- **Netlify Drop:** `siparis.html`'in adını `index.html` yapıp bir klasöre koy, klasörü Netlify'ın "Drop" sayfasına sürükle. Kalıcı olması için ücretsiz hesap gerekiyor.
- **GitHub Pages:** ücretsiz GitHub hesabıyla yeni depo aç, `index.html`'i yükle, depo ayarlarından Pages'i aç.
- **Cloudflare Pages:** ücretsiz planda klasörü doğrudan yükleyerek yayına alabilirsin.

## Pastaneye sunarken 3 madde

1. Gitmeden önce adı, fiyatları ve ürünleri o pastaneye göre değiştir; kurgusal örnekle değil, onların pastasıyla göster.
2. Telefonunu pastacının eline ver: bir seçim yapsın, pasta ve fiyat değişsin, mesajı görsün. Anlatmaktan daha çok işe yarıyor.
3. Numarayı ve fiyatları birlikte girin, ilk siparişi birlikte deneyin. Teslim günü, kapasite ve kapora gibi kuralları sayfaya ondan sonra ekleyin.

## Bilmen gerekenler

- İşletme adı, fiyatlar ve numara kurgusal; kendi bilgilerini yaz.
- Videodaki süre (3 dk 13 sn) ve maliyet (liste fiyatı karşılığı 0,59 $) benim denememe ait; senin denemende farklı çıkabilir.
- Claude sayfayı yazarken tarayıcıda açmadı, bunu kendisi söyledi. Ben telefon görünümünde denedim: konsol hatası ve dış istek yoktu. Sen de yayından önce kendi telefonunda dene.
- Piyasa fiyatı bir ilan bandıdır (Armut, web sitesi yapımı, 23 Kasım 2026: 3.600 TL - 111.110 TL), kazanç sözü değildir.

Pratik AI · her gün yeni kit: https://suzunn.github.io/pratikai-medya/kit/
