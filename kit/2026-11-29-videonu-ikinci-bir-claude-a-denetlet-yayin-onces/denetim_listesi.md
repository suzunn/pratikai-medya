# Yayın öncesi denetim listesi (dikey video: Reels, Shorts, TikTok)

Videoyu yayına koymadan önce bu altı maddeye tek tek bak. Her maddede "ne arıyorsun" ve "nasıl bakarsın" var.
Benim videolarımda ikinci bir Claude bu listeye göre baktı ve dört videoda 10 hata buldu.

## Hazırlık: videoyu karelere böl

Göz kayar, kare kaymaz. Videoyu saniyede 4 kareye böl ve karelere sırayla bak:

    ffmpeg -i video.mp4 -vf fps=4 kareler/kare_%04d.png

Kare numarasını 4'e bölersen saniyeyi bulursun (kare 70 = 17,5. saniye). Claude'a denetletiyorsan bu kareleri ona ver.

## 1. Kanca (ilk 3 saniye)

- Ekranda tek büyük başlık ve tek görsel kanıt var mı? Liste, tablo, kaynak satırı, küçük etiket kancaya girmez.
- İlk karede (0. saniye) bir şey görünüyor mu? Siyah ya da boş açılış olmaz.
- Ses ilk 0,3 saniyede başlıyor mu?
- Benim hatam: bir kancaya 12 satırlık liste koymuştuk, telefonda hiçbiri okunmuyordu. Tek satıra indirince okunur oldu.

## 2. Boş kare

- Ekranda hiçbir şeyin olmadığı (yalnız zemin) bir an var mı? Yarım saniye bile fark ediliyor.
- Sahne geçişlerinin hemen arkasına bak: yeni sahnenin içeriği gecikince ilk kareler boş kalıyor.
- Altyazı o anda da var mı? Ses konuşurken ekran boşsa izleyici kaydırır.
- Benim hatam: bir videoda 17,40 ile 17,85. saniye arasında ekran tamamen boştu, altyazı da yoktu.

## 3. Altyazı çakışması

- Altyazı bandının (ekranın ortası ve biraz altı) içine başka bir şey giriyor mu? İkon, artı işareti, logo, karakter?
- Altyazı bir kartın ya da karakterin yüzünün üstüne biniyor mu?
- Aynı kelime ekranda iki kez görünüyor mu (hem altyazıda hem sahnedeki yazıda)?
- Benim hatam: küçük kırmızı bir artı işareti altyazının altına girmişti. Kartın köşesine taşıyınca düzeldi.

## 4. Kenar payı ve güvenli alan

- Hiçbir yazı ya da kart ekranın kenarında kesilmiyor mu? En az 30 piksel boşluk bırak.
- Yazılar Reels ve Shorts düğmelerinin altında kalmıyor mu? Üstten ~250, alttan ~470, sağdan ~180 piksel uygulamanın kendi düğmelerine gider.
- İçerik ekranı dolduruyor mu? "Üstte küçük bir kart, altı boş" görüntüsü telefonda bomboş durur.

## 5. Yasak ya da istenmeyen ses

- Kendine koyduğun ses kuralları var mı (ör. "şu geçiş sesi kullanılmaz")? Videodaki her efektin adını ve saniyesini listele, kurala uymayanı çıkar.
- Müzik konuşmanın altında mı kalıyor? Konuşma rahat anlaşılmalı.
- Sesli bir efekt yarıda kesiliyor mu?
- Sessizlik kontrolü (videonun ilk saniyesinde sessiz açılış var mı):

    ffmpeg -t 1 -i video.mp4 -af silencedetect=n=-40dB:d=0.3 -f null -

## 6. Süre

- Video hedef süre aralığında mı (ör. 40-60 saniye)?
- Videoda söylediğin süreler ve sayılar kayıtla aynı mı? "Tek cümle", "3 dakika" gibi sözleri kayda bakarak kontrol et.

## Son olarak: kuralları da kontrol et

Denetçi, ona verdiğin kurala harfiyen uyar. Kural yanlışsa denetçi de yanlış yapar. Benim videolarımda kurallara yanlış bir satır girmişti
ve denetçi buna uyup iki videonun geçiş seslerini kapattı. İki kural çelişiyorsa denetçiye "uygulamadan önce bana sor" de.
