# Kendi DOSYA hunini kur: yorum yazana otomatik mesaj ve ücretsiz kit sayfası

Videonun sonunda "yorumlara DOSYA yaz" deyip yorum yazana otomatik mesaj attığım düzenin kurulum notları. 21 Kasım 2026
videosunda gösterildi. İçinde mesaj metni örnekleri ve tek dosyalık bir "ücretsiz kitler" sayfası şablonu var.

## İçinde ne var

- `README.md`: bu dosya; huninin adımları ve ücretsiz planın sınırları.
- `dm_metni.txt`: otomatik mesaj için metin örnekleri (benim kullandığım dahil) ve videonun son cümlesi için birkaç kalıp.
- `kit_sayfasi.html`: tek dosyalık "ücretsiz kitler" sayfası şablonu. Telefonda düzgün görünür, internet gerektirmez; en yeni kit en üstte durur.

## Huni nasıl çalışıyor

1. Videonun son cümlesinde tek bir kelime istiyorum: DOSYA. Her videoda aynı kelime, takipçinin aklında kalsın diye.
2. Biri yoruma DOSYA yazınca otomatik mesaj aracı (ben ReplyRush'ın ücretsiz planını kullanıyorum) ona tek bir mesaj atıyor.
3. Mesajda kısa bir cümle ve bir düğme var. Düğme ücretsiz kitler sayfasını açıyor.
4. Sayfada her günün kiti en üstte duruyor. Kitte o günkü videoda yaptığım işin dosyaları var.

17 Kasım 2026'ya kadar bu düzenle 59 mesaj gitti, 27'si açıldı, 23 kişi düğmeye bastı (aracın kendi sayaçları).

## Kurulum adımları

1. Instagram hesabın profesyonel hesap (içerik üreticisi ya da işletme) olsun. Otomatik mesaj araçları kişisel hesapla çalışmaz.
2. Bir otomatik mesaj aracına Instagram hesabınla bağlan. Ben ReplyRush kullanıyorum; ManyChat gibi başkaları da aynı işi yapıyor.
   Bağlanırken aracın Meta onaylı olduğuna bak.
3. Gönderiye özel değil, **bütün gönderilerde geçerli** (genel) bir tetikleyici kur. Böylece eski videolara gelen yorumlar da mesaj alır,
   her yeni videoda ayar yapmazsın.
4. Tetikleyici kelimeyi yaz: DOSYA. Sık yapılan yazım hatalarını da ekle (ben dosyaa, dsoya, dosay ekledim). Büyük/küçük harfi
   araç zaten aynı sayıyor; aynı kelimeyi iki kez eklersen hata verebilir.
5. "Yalnız tam eşleşme" gibi bir anahtar varsa kapalı bırak: "DOSYA lütfen" yazan da mesaj alsın.
6. "Kişi başı bir kez" seçeneğini aç. Aynı kişi beş videoya DOSYA yazsa da tek mesaj alır, ama sayfada bütün kitler zaten duruyor.
7. Mesajı yaz: kısa bir cümle, kare bir görsel ve tek düğme. Metin örnekleri `dm_metni.txt`'de.
8. Düğmenin linkini kit sayfana ver. Linki değiştirirsen mesajın önizleme başlığı ve görseli değişebilir; kaydettikten sonra kontrol et.
9. Kendine dene: ikinci bir hesapla bir videona DOSYA yaz, mesaj geliyor mu bak. O hesap seni takip etmiyorsa mesajı "istekler"de ara.

## Kit sayfası şablonu (`kit_sayfasi.html`)

1. Dosyayı bir metin düzenleyicide aç. Köşeli parantezli yerleri (kanal adın, açıklama, sosyal medya linklerin) kendininkiyle değiştir.
2. Her kit bir kart: tarih, başlık, iki satır açıklama ve link. Yeni kiti listenin en üstüne ekle. Şablonda kartın nasıl yazıldığını
   gösteren üç örnek kart var.
3. Sayfayı ücretsiz bir yere koy (ben GitHub Pages kullanıyorum). İstersen bunu da Claude'a yaptır: "Bu dosyayı GitHub Pages'te
   yayına al, adımları bana tek tek söyle" demen yeter.
4. Kitin kendisi (dosyalar) için ayrı bir sayfa ya da indirilebilir bir zip koyabilirsin; karttaki link oraya gider.

## Ücretsiz planın sınırları (ReplyRush, Kasım 2026)

- Ayda 1.500 mesaj. Bir üst plan (Lite) ayda 10 dolar ve 7.500 mesaj.
- Ücretsiz planda 5 genel tetikleyici var; yorumun altına otomatik "mesaj attım" cevabı ücretli planlarda.
- Fiyatlar ve sınırlar değişebilir: kurmadan önce aracın kendi fiyat sayfasına bak (replyrush.com/pricing).

## Instagram'ın kuralları (Meta geliştirici belgesi)

- Yorum yazan kişiye otomatik olarak yalnız **bir** özel mesaj gidebilir ve bu mesaj yorumdan sonraki **7 gün** içinde gitmeli.
  Kişi mesaja cevap verirse konuşma devam edebilir.
- Seni takip eden kişide mesaj gelen kutusuna düşer. **Takip etmeyen kişide "mesaj istekleri"ne düşer.** Videoda bunu söyle:
  "Mesaj gelmediyse isteklere bak." Bizde 59 mesajın 32'si hiç açılmadı; büyük ihtimalle bir kısmı isteklerde kaldı.

## Bilmen gerekenler

- Rakamlar benim hesabımın 17 Kasım 2026 sayaçları; senin hesabında farklı çıkar. Bu bir kazanç sözü değildir.
- Kimseye toplu ya da istenmemiş mesaj atma: yalnız yorumda kelimeyi yazan kişiye, bir kez.
- Örnek kartlardaki kitler örnektir; kendi kitlerinle değiştir.

Pratik AI · her gün yeni kit: https://suzunn.github.io/pratikai-medya/kit/
