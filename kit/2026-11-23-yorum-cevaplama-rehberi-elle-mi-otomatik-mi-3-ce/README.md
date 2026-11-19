# Yorum cevaplama rehberi: elle mi otomatik mi, 3 cevap şablonu ve Meta kuralları

DOSYA yazan herkese yorumdan cevap vermenin iki yolu ve benim kullandığım 3 cevap cümlesi. 23 Kasım 2026 videosunda
gösterildi: otomatik cevap ücretli plandaydı, Claude tarayıcıda 39 yoruma tek tek cevap yazdı.

## İçinde ne var

- `README.md`: bu dosya; elle ve otomatik cevabın farkı, Meta'nın özel yanıt kuralları, spam gibi görünmemek için notlar.
- `cevap_sablonlari.txt`: yorumlara yazdığım 3 cevap cümlesi (birebir) ve kendi cümleni yazarken işine yarayacak birkaç kalıp.
- `prompt.txt`: Claude'a tarayıcıdan yorum cevaplatırken verdiğim talimatın düzenli hâli.

## Elle mi, otomatik mi?

| | Elle (sen ya da Claude tarayıcıda) | Otomatik cevap aracı |
|---|---|---|
| Ücret | Araç ücreti yok | Kullandığım araçta (ReplyRush) yoruma otomatik cevap ücretsiz planda kapalı, Lite planda açık: ayda 10 $ (fiyat sayfası, 18 Kasım 2026) |
| Hız | Yorum başına birkaç tıklama | Yorum gelir gelmez |
| Ne zaman mantıklı | Onlarca yorum, ara sıra | Her gün yüzlerce yorum |
| Dikkat | Doğru hesapla açık olduğundan emin ol | Aracın Meta onaylı olduğuna bak |

Benim fikrim: haftada birkaç düzine yorum için ücretli plana gerek yok. Yorumlar yüzlerle gelmeye başlarsa otomatik cevap daha mantıklı.

## Meta'nın özel yanıt kuralları (Instagram)

Kaynak: Meta for Developers, Instagram Platform "Private Replies" sayfası (17 Kasım 2026'da okundu). Otomatik DM araçları bu kurala göre çalışır.

1. Bir yoruma en fazla 1 özel mesaj gönderilebilir. Kişi mesaja cevap verirse konuşma 24 saat içinde sürebilir.
2. Özel mesaj, yorumun yazılmasından sonraki 7 gün içinde gönderilmeli. Daha eski yorumlara otomatik mesaj gitmez.
3. Kişi hesabını takip ediyorsa mesaj gelen kutusuna düşer. Takip etmiyorsa mesaj isteklerine düşer. Bu yüzden cevap cümlelerimde
   "gelmediyse mesaj isteklerine bak" diyorum.

## Spam gibi görünmemek için (benim uyguladıklarım)

- Aynı cümleyi art arda yapıştırma. 3 farklı cümleyi sırayla kullandım (`cevap_sablonlari.txt`).
- Cevaba link koyma. Linki DM'de ver; yorumda yalnız kısa bir cümle olsun.
- Çok hızlı gitme. Her cevap arasında birkaç saniye bırak, yüzlerce yorumu tek oturumda bitirmeye çalışma.
- Yanlış hesaptan yazma. Tarayıcıda hangi hesabın açık olduğuna yazmadan önce bak. Claude ilk denemede başka bir hesap açık
  olduğunu görünce hiç yazmadı, doğru hesaba geçmemi bekledi.
- Cevap verdiğin yorumu not et. Aynı kişiye iki kez cevap yazma.

## Claude'a nasıl yaptırdım

1. Tarayıcıda Instagram'ı kendi hesabımla açtım (Claude'un tarayıcı eklentisiyle).
2. `prompt.txt`'deki talimatı verdim: hangi videonun yorumları, hangi kelime, hangi 3 cümle, hangi hesap.
3. Claude yorumları tek tek bulup altına cevap yazdı. Bir tıklama hata verince ekrandaki yerinden tıklayıp devam etti.
4. Sonunda 37 + 1 + 1 = 39 cevap yazdı; videonun yorum sayısı 61'den 95 civarına çıktı (cevaplar dahil).

## Bilmen gerekenler

- Rakamlar benim hesabıma ait (18 Kasım 2026); senin hesabında farklı olur.
- Fiyatlar aracın Kasım 2026 fiyat sayfasından; değişebilir, kullanmadan önce kendin bak.
- Bu rehber bir kazanç sözü değildir. Instagram kurallarına uymak hesabın sahibinin sorumluluğundadır.

Pratik AI · her gün yeni kit: https://suzunn.github.io/pratikai-medya/kit/
