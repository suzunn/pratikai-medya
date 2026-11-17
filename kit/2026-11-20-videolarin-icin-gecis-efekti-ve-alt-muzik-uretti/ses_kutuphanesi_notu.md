# Ses kütüphanesi: nasıl hazırladım, nasıl kullanıyorum

Ses dosyalarını paylaşmıyorum (ticari kullanım şartı üretildiği hizmetin planına bağlı). Burada yalnız yöntem var.

## Kırpma ve seviye (efektler)

- Model her istekte 2 sürüm verdi; ikisini de dinleyip birini seçtim.
- Her efektte sesin en güçlü anını buldum, 0,3 ile 1,2 saniye arasında kırptım. Başa 4 ms, sona kısa bir fade koydum (tık sesi olmasın).
- 35 Hz altını ve 8,5 kHz üstünü kestim (gümbürtü ve tiz cızırtı gitsin), tepeyi -2 dBFS'e çektim.
- Çok bas ağırlıklı olanlara (hava süpürmesi, tok kesme, bas düşüşü) biraz doygunluk ekledim; telefon hoparlörü derin bası çok az veriyor, harmonikler sayesinde telefonda da duyuluyor.

ffmpeg örneği (efekt, 0,20-1,10 sn arası):

```
ffmpeg -i ham.mp3 -af "atrim=0.20:1.10,asetpts=PTS-STARTPTS,highpass=f=35,lowpass=f=8500,afade=t=in:d=0.004,afade=t=out:st=0.78:d=0.12" efekt.wav
```

## Seviye (müzikler)

- 60 saniyeye kırptım, 30 Hz altını kestim, 2,2 kHz'de -3 dB'lik geniş bir oyuk açtım (konuşmanın en anlaşılır bölgesi, müzik oraya basmasın).
- -20 LUFS'e normalize ettim, başa 0,3 sn, sona 1,5 sn fade.
- Videoda müziği konuşmanın 20-24 dB altında tutuyorum.

```
ffmpeg -i ham.mp3 -af "atrim=0:60,asetpts=PTS-STARTPTS,highpass=f=30,equalizer=f=2200:width_type=o:width=1.6:g=-3,loudnorm=I=-20:TP=-2:LRA=7,afade=t=in:d=0.3,afade=t=out:st=58.5:d=1.5" muzik.wav
```

## Nerede hangisi

| Ses | Kullandığım yer |
|---|---|
| hava süpürme | genel sahne geçişi |
| tok kesme | sert kesme, madde başı |
| kart çevirme | liste maddesi, ekran değişimi |
| dijital tık | ekran kaydına geçiş |
| bant geri sarma | önce/sonra, geri dönüş anı |
| bas düşüşü | vurgu anı; tek başına telefonda zayıf, tok kesmeyle üst üste |
| tok pop | küçük bir öğe ya da yazı belirince |
| ters tok | yakınlaşma geçişi |

## Kurallarım

- Girişteki büyük whoosh videoda yalnız bir kez, kanca cümlesi biterken. Diğer geçişlerde başka efektler.
- Hazır kütüphaneden gelen iki parlak swoosh'u dinleyip eledim; geçişlerde artık kendi setim var.
- Her video için yeni ses üretmiyorum: kütüphane bir kez kuruldu, tekrar tekrar kullanılıyor. Yeni bir ihtiyaç çıkarsa tek efekt ekliyorum.
- Seslendirme sesini seçerken aynı cümleyi 5 sesle okuttum ve yan yana dinledim; tek cümleyle karar vermek yetti.
