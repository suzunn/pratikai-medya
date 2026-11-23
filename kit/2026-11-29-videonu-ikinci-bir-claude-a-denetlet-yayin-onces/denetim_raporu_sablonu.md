# Denetim raporu şablonu

Denetçi Claude'dan raporu bu biçimde iste. Altta benim videolarımdan gerçek bulgularla doldurulmuş bir örnek var.

## Boş şablon

Video: [video adı] · Süre: [saniye] · Denetim tarihi: [gün ay yıl]

| # | Saniye | Ne gördüm | Hangi kural | Kanıt (kare) | Öneri | Büyük / küçük |
|---|---|---|---|---|---|---|
| 1 | [bas - bit] | [kısa tarif] | [kuralın kendisi] | [kare numarası] | [nasıl düzelir] | [büyük / küçük] |

Kural çelişkisi ya da emin olmadığım şeyler: [varsa yaz, yoksa "yok"]

Karar: [YAYINA HAZIR / YAYINA HAZIR DEĞİL: en önemli neden]

## Dolu örnek (dört videomdan seçme gerçek bulgular, 19 Kasım 2026 gecesi denetimi)

| # | Saniye | Ne gördüm | Hangi kural | Kanıt (kare) | Öneri | Büyük / küçük |
|---|---|---|---|---|---|---|
| 1 | 23 Kasım videosu, 0,0 - 3,5 | Kancada 12 satırlık liste var, telefonda okunmuyor | İlk 3 saniyede yalnız tek başlık + tek görsel | 1,5. saniye | Listeyi tek satıra indir, o satıra halka çiz | büyük |
| 2 | 22 Kasım videosu, 17,40 - 17,85 | Ekran tamamen boş, altyazı da yok, sesten kelime duyuluyor | Boş kare olmaz | 17,6. saniye | Sahnenin ilk karesine içerik koy | büyük |
| 3 | 20 Kasım videosu, 44,0 civarı | Kırmızı artı işareti altyazının altına giriyor | Altyazı bandına hiçbir şey girmez | 44,0. saniye | Artıyı kartın köşesine taşı | küçük |
| 4 | 21 Kasım videosu, 7,4 - 8,6 | Ekranın üstünde küçük bir kart var, alt yarısı boş | İçerik ekranı doldurur | 8,0. saniye | Alttaki öğeleri sahnenin başına al | küçük |

Kural çelişkisi: Kural listesinde "sonraki geçişler sessiz" yazıyor, ama asıl istek geçişlerin sesli olması. Uygulamadım, karar sende.

Karar: YAYINA HAZIR DEĞİL: 1 ve 2 düzelmeden yayına çıkmasın.

Not: Çelişki notunu 23 Kasım videosunun denetçisi gerçekten yazdı. 20 ve 21 Kasım videolarının denetçileri ise aynı satıra sormadan uydu ve
geçiş seslerini kapattı. Bu yüzden promptta "çelişki görürsen uygulamadan önce sor" maddesi var.
