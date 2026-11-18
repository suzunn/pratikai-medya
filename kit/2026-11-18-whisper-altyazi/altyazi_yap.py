# -*- coding: utf-8 -*-
"""altyazi_yap.py - videoya bilgisayarinda, internetsiz altyazi ekler (Whisper + ffmpeg).

Kullanim:
  python altyazi_yap.py video.mp4
  python altyazi_yap.py video.mp4 --model small --dil tr

Cikti (videonun yaninda):
  video.srt            duzenlenebilir altyazi dosyasi
  video_altyazili.mp4  altyazisi gomulu video

Gerekenler: Python 3.9+, ffmpeg (PATH'te), faster-whisper (pip install faster-whisper).
Model ilk calistirmada bir kez indirilir; sonra internet gerekmez.
"""
import argparse
import os
import subprocess
import sys
import time

SARI, YESIL, GRI, SIFIR = "\033[38;2;255;210;63m", "\033[38;2;80;220;120m", "\033[38;2;150;150;150m", "\033[0m"
VIDEO_UZANTI = (".mp4", ".mov", ".mkv", ".m4v", ".avi", ".webm")


def zaman_srt(sn):
    ms = int(round(sn * 1000))
    s, ms = divmod(ms, 1000)
    d, s = divmod(s, 60)
    sa, d = divmod(d, 60)
    return f"{sa:02d}:{d:02d}:{s:02d},{ms:03d}"


def kisa_zaman(sn):
    d, s = divmod(sn, 60)
    return f"{int(d):02d}:{s:04.1f}".replace(".", ",")


def sure_yaz(sn):
    return f"{sn:.1f}".replace(".", ",") + " sn"


def kelimeleri_grupla(kelimeler, azami_harf=30, azami_sure=2.6):
    """kelime zamanlarindan kisa altyazi satirlari kurar (dikey video icin 1-2 satir)"""
    gruplar, simdiki = [], []
    for w in kelimeler:
        metin = w.word.strip()
        if not metin:
            continue
        if simdiki:
            yeni_metin = " ".join(x[0] for x in simdiki) + " " + metin
            if len(yeni_metin) > azami_harf or w.end - simdiki[0][1] > azami_sure:
                gruplar.append(simdiki)
                simdiki = []
        simdiki.append((metin, w.start, w.end))
        if metin[-1] in ".?!,;:":
            gruplar.append(simdiki)
            simdiki = []
    if simdiki:
        gruplar.append(simdiki)
    satirlar = []
    for g in gruplar:
        metin = " ".join(x[0] for x in g)
        metin = metin.replace(" '", "'")   # Whisper ekleri ayri kelime verebilir: AI 'yi -> AI'yi
        satirlar.append((g[0][1], g[-1][2], metin))
    return satirlar


def video_bul(klasor):
    for ad in sorted(os.listdir(klasor)):
        if ad.lower().endswith(VIDEO_UZANTI) and "_altyazili" not in ad.lower():
            return os.path.join(klasor, ad)
    return None


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    os.system("")   # Windows konsolunda renk kodlarini acar
    ap = argparse.ArgumentParser(description="Videoya internetsiz altyazi ekler (Whisper + ffmpeg)")
    ap.add_argument("video", nargs="?", help="video dosyasi (bos birakilirsa bu klasordeki ilk video)")
    ap.add_argument("--model", default="large-v3-turbo", help="Whisper modeli: large-v3-turbo (varsayilan), medium, small")
    ap.add_argument("--dil", default="tr", help="konusma dili (tr, en, ...)")
    ap.add_argument("--cihaz", default="cpu", help="cpu ya da cuda (NVIDIA ekran karti kuruluysa)")
    ap.add_argument("--yazi-boyu", type=int, default=0, help="altyazi boyu (varsayilan 20; dikey videoda 26 iyi okunur)")
    a = ap.parse_args()

    video = a.video or video_bul(os.path.dirname(os.path.abspath(__file__)))
    if not video or not os.path.exists(video):
        print("Video bulunamadı. Kullanım: python altyazi_yap.py video.mp4")
        return 1
    video = os.path.abspath(video)
    klasor, ad = os.path.split(video)
    kok = os.path.splitext(ad)[0]
    srt_ad, cikti_ad = kok + ".srt", kok + "_altyazili.mp4"

    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("faster-whisper kurulu değil: pip install faster-whisper")
        return 1

    t_bas = time.time()
    print(f"{SARI}[1/3]{SIFIR} Whisper {a.model} yükleniyor ({a.cihaz.upper()})", flush=True)
    model = WhisperModel(a.model, device=a.cihaz, compute_type="int8" if a.cihaz == "cpu" else "float16",
                         cpu_threads=os.cpu_count() or 4)
    t_model = time.time() - t_bas
    print(f"      hazır: {sure_yaz(t_model)}", flush=True)

    print(f"{SARI}[2/3]{SIFIR} Konuşma yazıya dökülüyor...", flush=True)
    t2 = time.time()
    parcalar, bilgi = model.transcribe(video, language=a.dil, word_timestamps=True, vad_filter=True)
    satirlar = []
    for p in parcalar:
        for bas, bit, metin in kelimeleri_grupla(p.words or []):
            satirlar.append((bas, bit, metin))
            print(f"  {GRI}{kisa_zaman(bas)}{SIFIR}  {metin}", flush=True)
    t_yazi = time.time() - t2
    if not satirlar:
        print("Konuşma bulunamadı.")
        return 1
    with open(os.path.join(klasor, srt_ad), "w", encoding="utf-8") as f:
        for i, (bas, bit, metin) in enumerate(satirlar, 1):
            f.write(f"{i}\n{zaman_srt(bas)} --> {zaman_srt(max(bit, bas + 0.4))}\n{metin}\n\n")
    print(f"      {sure_yaz(bilgi.duration)} video, {len(satirlar)} satır: {sure_yaz(t_yazi)}", flush=True)

    print(f"{SARI}[3/3]{SIFIR} Altyazı videoya gömülüyor (ffmpeg)", flush=True)
    t3 = time.time()
    boy = a.yazi_boyu or 20
    stil = (f"FontName=Arial,FontSize={boy},Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
            f"BorderStyle=1,Outline=2,Shadow=0,Alignment=2,MarginV=26")
    komut = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", ad,
             "-vf", f"subtitles={srt_ad}:charenc=UTF-8:force_style='{stil}'",
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "copy", cikti_ad]
    try:
        r = subprocess.run(komut, cwd=klasor)   # klasorde calisir: Windows yollarindaki ':' filtre sozdizimini bozmasin
    except FileNotFoundError:
        print("ffmpeg bulunamadı: ffmpeg'i kurup PATH'e ekle (README).")
        return 1
    if r.returncode != 0:
        print("ffmpeg hata verdi; SRT dosyası yine de hazır.")
        return 1
    t_gom = time.time() - t3
    print(f"      bitti: {sure_yaz(t_gom)}", flush=True)

    toplam = time.time() - t_bas
    print(f"\n{YESIL}BİTTİ{SIFIR}  toplam {sure_yaz(toplam)}", flush=True)
    print(f"  {srt_ad}\n  {cikti_ad}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
