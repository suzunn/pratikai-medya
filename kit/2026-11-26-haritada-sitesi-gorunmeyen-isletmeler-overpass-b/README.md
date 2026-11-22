# Haritada sitesi görünmeyen işletmeler: Overpass betiği ve harita şablonu

Bir ilçedeki kafe, restoran, pastane, berber/kuaför ve çiçekçilerden OpenStreetMap'te web sitesi bilgisi girilmemiş olanları sayan
betik ve sonucu noktalarla gösteren harita şablonu. 26 Kasım 2026 videosunda gösterildi: Claude betiği yazdı, ben çalıştırdım,
Kadıköy'de 1.595 işletmenin 1.231'inde site bilgisi çıkmadı.

## İçinde ne var

- `prompt.txt`: Claude'a verdiğim istek, birebir.
- `ara.py`: Claude'un yazdığı betik (yalnız Python'un standart kütüphanesi). Overpass API'ye tek istek atar; `ozet.json`, `liste.csv` ve
  `harita.html` yazar.
- `harita_sablon.html`: `ara.py`'nin doldurduğu harita şablonu. Dış kaynak kullanmaz (CDN, font, harita karosu yok); işletme adı
  haritaya da sayfanın kaynağına da yazılmaz, yalnız nokta.

Videodaki gerçek işletme listesi ve CSV kitte yok. Kendi listeni betiği çalıştırarak kendin üretirsin.

## Nasıl çalışır

1. Python 3 kurulu olsun. `ara.py` ile `harita_sablon.html`'i aynı klasöre koy.
2. `ara.py`'nin başındaki ayarları değiştir: `IL_ADI`, `ILCE_ADI` (ör. "Kadıköy" yerine kendi ilçen) ve `KATEGORILER` listesi.
   Kategoriler OpenStreetMap etiketleridir: kafe `amenity=cafe`, restoran `amenity=restaurant`, pastane `shop=bakery` ya da
   `shop=pastry`, berber/kuaför `shop=hairdresser`, çiçekçi `shop=florist`.
3. Terminalde `python ara.py` yaz. Betik tek sorgu atar, en fazla 60 saniye bekler, tekrar denemez. Bende Kadıköy için 26 saniye sürdü.
4. Çıkan `harita.html`'i tarayıcıda aç. Kırmızı noktalar site bilgisi girilmemiş işletmeler, küçük gri noktalar site bilgisi olanlar.

"Site bilgisi" şu demek: işletmenin OpenStreetMap kaydında `website`, `contact:website` ya da `url` etiketinden biri var mı. Adı girilmemiş
kayıtlar sayılmaz.

## Önce şunu bil: haritada görünmemesi sitesi yok demek değil

OpenStreetMap'i gönüllüler dolduruyor. Bir işletmenin kaydında site bilgisi olmaması, sitesi olmadığını göstermez. Benim listemde bilinen
zincir kahvecilerin şubeleri bile vardı. Bu liste bir başlangıç noktası, müşteri listesi değil.

## Etik ve KVKK notu

- Betik telefon, e-posta, adres ya da kişi bilgisi toplamaz. Ekleme: `liste.csv`'de yalnız ad, kategori ve konum durur.
- Bu listeyle kimseye toplu ya da otomatik mesaj atma. Teklif vermeden önce işletmeyi internette bir kez arat; sitesi varsa teklifini ona göre kur.
- İletişime geçeceksen tek tek, kendin ve kibarca geç. Ticari ileti kurallarına (Türkiye'de 6563 sayılı Kanun) ve kişisel verilere dair
  kurallara (6698 sayılı KVKK) uymak senin sorumluluğunda.
- Overpass API ücretsiz ve hesapsız ama paylaşılan bir sunucu: günde 10.000 sorgudan, 1 GB veriden az kal, betiği döngüye sokma, aynı
  anda birden çok sorgu atma (overpass-api.de kullanım kuralı). Betik kendini tanıtan bir User-Agent gönderir, kişisel bilgi içermez.

## Atıf ve lisans (ODbL)

Veri: © OpenStreetMap katkıda bulunanlar, Open Database License (ODbL), https://www.openstreetmap.org/copyright

- Haritayı ya da ekran görüntüsünü paylaşırsan atıf haritanın köşesinde kalsın (şablon bunu kendisi yazar).
- Veriyi (CSV, JSON) paylaşırsan ODbL geçerli: atıf ver ve türettiğin veriyi aynı lisansla paylaş.

## Bilmen gerekenler

- Sayılar benim denememe ait: 23 Kasım 2026 OpenStreetMap verisi, Kadıköy. Senin ilçende ve senin gününde farklı çıkar.
- Claude'un betiği yazması 3 dakika 19 saniye sürdü ve liste fiyatı karşılığı 0,62 dolar tuttu (Max abonelikte ayrıca ödemedim);
  senin denemende farklı çıkabilir.
- Armut'ta web sitesi yapımının ortalama fiyat bandı 3.600 TL - 111.110 TL (23 Kasım 2026). Bu bir talep bandıdır, kazanç sözü değildir.

Pratik AI · her gün yeni kit: https://suzunn.github.io/pratikai-medya/kit/
