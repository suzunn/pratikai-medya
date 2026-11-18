# Whisper altyazı betiği: videoya bilgisayarında, ücretsiz altyazı

"CapCut'a para verme: altyazıyı bilgisayarımdaki Whisper yazdı" videosunda kullandığım betiğin aynısı. Videoyu verirsin;
konuşmayı Whisper ile yazıya döker, düzenlenebilir bir `.srt` dosyası yazar ve altyazıyı videoya gömer.

## İçinde ne var

- `altyazi_yap.py`: asıl betik (Whisper ile yazıya dökme + ffmpeg ile altyazıyı gömme)
- `altyazi_yap.bat`: Windows için tek tık. Videoyu bu dosyanın üstüne sürükle bırak ya da videoyu aynı klasöre koyup çift tıkla

## Kurulum (bir kez)

1. **Python 3.9 ya da üstü:** https://www.python.org/downloads/ (Windows'ta kurarken "Add python.exe to PATH" kutusunu işaretle).
2. **ffmpeg:** Windows'ta komut isteminde `winget install Gyan.FFmpeg`, Mac'te `brew install ffmpeg`, Linux'ta `sudo apt install ffmpeg`.
3. **faster-whisper:** komut isteminde `pip install faster-whisper` (Mac/Linux'ta `pip3`).
4. İlk çalıştırmada Whisper modeli (large-v3-turbo, yaklaşık 1,6 GB) bir kez iner. Sonra internet gerekmez.

## Nasıl kullanılır

1. Videonu (`.mp4`, `.mov`, `.mkv`) bu klasöre koy.
2. Windows: `altyazi_yap.bat`'a çift tıkla ya da videoyu üstüne sürükle. Mac/Linux: `python3 altyazi_yap.py video.mp4`.
3. Videonun yanında iki dosya çıkar: `video.srt` ve `video_altyazili.mp4`.
4. Bir kelime yanlışsa (çoğunlukla marka adları) `video.srt`'yi Not Defteri'nde düzelt. Düzeltilmiş SRT'yi CapCut, Premiere ya da YouTube'a doğrudan yükleyebilirsin.

## Ayarlar

- `--model small`: daha küçük ve hızlı model (Türkçede biraz daha fazla hata yapar). Varsayılan `large-v3-turbo`.
- `--dil en`: İngilizce konuşma için. Varsayılan `tr`.
- `--yazi-boyu 26`: altyazıyı büyütür (dikey videoda işe yarar). Varsayılan 20.
- `--cihaz cuda`: NVIDIA ekran kartın ve CUDA kurulumun varsa daha hızlı çalışır. Varsayılan işlemci (`cpu`).

## Bilmen gerekenler

- Videodaki süre benim denememe ait: 19,1 saniyelik konuşma, ekran kartı olmadan, toplam 19,3 saniye. Senin bilgisayarında farklı çıkabilir.
- Whisper Türkçe cümleleri iyi yazıyor ama marka adlarında takılabiliyor (benim denememde Suno'yu "Sunoe" yazdı). Yayından önce SRT'ye bir göz at.
- CapCut fiyatı Kasım 2026'da capcut.com Türkiye fiyat sayfasındaki rakamdır (Pro aylık 499,99 TL); fiyatlar değişebilir.
- Whisper, OpenAI'ın açık kaynak (MIT lisanslı) modelidir; faster-whisper onu işlemcide hızlı çalıştıran açık kaynak sürümdür.

Pratik AI · her gün yeni kit: https://suzunn.github.io/pratikai-medya/kit/
