# Videoların için geçiş efekti ve alt müzik ürettirme: promptlar

Claude'a kendi videolarım için 8 geçiş efekti ve 4 vokalsiz alt müzik ürettirdiğim denemenin promptları ve kullanım notları.
20 Kasım 2026 videosunda gösterildi. Ses dosyalarının kendisi bu kitte yok: aynı promptlarla kendi hesabında üretirsin.

## İçinde ne var

- `efekt_promptlari.txt`: 8 geçiş efektinin promptları, birebir (İngilizce; ses modelleri İngilizce tarifi daha iyi anlıyor).
- `muzik_promptlari.txt`: 3 alt müzik isteğinin stil promptları ve "olmasın" listesi, birebir.
- `claude_istegi.txt`: bu işi Claude'a (Claude Code) yaptırmak için kullanabileceğin kısa istek metni.
- `ses_kutuphanesi_notu.md`: ürettiğin sesleri nasıl kırpıp seviyelendirdiğim, hangisini nerede kullandığım, telefonda neye dikkat ettiğim.

## Nasıl kullanırsın

1. KIE (kie.ai) ya da Suno'yu doğrudan sunan bir hizmette hesabın olsun. Ben KIE üzerinden `ai-music-api/sounds` (efekt) ve `ai-music-api/generate` (müzik, instrumental) modellerini kullandım, ikisi de V6.
2. `efekt_promptlari.txt`'deki satırları tek tek ses efekti modeline ver. Her istek 2 sürüm döndürdü; dinleyip iyisini seç.
3. `muzik_promptlari.txt`'deki stil metnini müzik modeline ver: instrumental (vokalsiz) açık, süre 60 sn, "olmasın" listesini negatif etiket alanına yapıştır.
4. Bunu elle yapmak istemezsen `claude_istegi.txt`'yi Claude Code'a ver: promptları yazar, istekleri gönderir, sesleri indirir.
5. İnen sesleri `ses_kutuphanesi_notu.md`'deki gibi kırp, seviyelendir, adlandırıp bir klasörde tut. Her videoda yeniden üretme, aynı kütüphaneyi kullan.

## Bilmen gerekenler

- Benim denememde 8 efekt + 3 müzik isteği (6 parça çıktı, 4'ünü tuttum) 56 KIE kredisi tuttu, yaklaşık 0,28 $ (efekt başına 2,5, müzik isteği başına 12 kredi; 14 Kas 2026). Fiyatlar değişebilir: üretmeden önce hizmetin güncel fiyatına bak.
- Seslendirme için 5 erkek sesini (Gemini 3.1 Flash TTS: Fenrir, Orus, Iapetus, Alnilam, Algieba) aynı cümleyle denedim, toplam 4,09 kredi tuttu; Orus'u seçtim.
- Lisans: ürettiğin seslerin ticari kullanım şartları kullandığın hizmetin planına bağlı. Kanalda kullanmadan önce kendi planının şartlarını oku. Bu yüzden ses dosyalarını paylaşmıyorum, yalnız promptları veriyorum.
- Çıkan sesler her üretimde farklıdır; benim duyduğumla aynı olmaz.

Pratik AI · her gün yeni kit: https://suzunn.github.io/pratikai-medya/kit/
