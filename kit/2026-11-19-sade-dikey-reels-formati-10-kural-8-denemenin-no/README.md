# Sade dikey Reels formatı: 10 kural, 8 denemenin notları ve parça planı

Günlük Reels formatımı Claude'la 8 denemede bulduk. Bu kitte o günün kuralları, her turda ne dediğim ve dikey parça planının
örneği var. Videoda 19 Kasım 2026'da gösterildi.

## İçinde ne var

- `format_kurallari.md`: 13 popüler Short'tan çıkan 10 kural + benim eklediğim 4 not (kenar payı, kanca yazısı, maskot, telefon boyu).
- `revize_turlari.md`: kart şablonundan A8'e kadar her tur: saat, ne dedim, ne değişti.
- `arastirma_ozeti.md`: 13 videonun ölçümleri (süre, yazı sayısı, kesim aralığı) kanal adı olmadan, özet tablo.
- `prompt.txt`: kendi formatını bulmak için Claude Code'a verebileceğin prompt.
- `dikey_parca_plan_ornegi.json`: bu videonun parça planı (1080x1920 dikey sahneler: görsel, büyüteç, halka, ok, konsol). Yollar örnek.

## Nasıl kullanılır

1. `format_kurallari.md`'yi oku, son videonun ilk 20 saniyesini bu kurallara göre kontrol et (aynı anda kaç yazı var, kenarda kesik var mı).
2. `prompt.txt`'yi aç, köşeli parantezli yerlere kendi konunu ve örnek Short linklerini yaz, Claude Code'a ver.
3. Çıkan iki taslaktan birini seç, beğenmediğin yeri tek cümleyle söyle. `revize_turlari.md` tur tur nasıl ilerlediğimi gösteriyor.

## Bilmen gerekenler

- Kurallar benim kanalım için çıktı (ekran kaydı + maskot). Yüzle çekim yapıyorsan 6. kuralı kendine göre değiştir.
- Plan dosyası bizim iç aracımızın biçiminde; aracı değil fikri alırsın: her sahne baştan dikey, kenar payı 30 px.
- Format değişikliğinin izlenmeye etkisini henüz ölçmedim, bu bir deneme notudur.

Pratik AI · her gün yeni kit: https://suzunn.github.io/pratikai-medya/kit/
