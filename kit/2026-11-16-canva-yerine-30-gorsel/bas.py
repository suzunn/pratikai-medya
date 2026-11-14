#!/usr/bin/env python3
"""Mavi Fincanlık gönderilerini PNG olarak basar.

sablon.html#1 ... #30 sayfalarını, bilgisayarda bulunan Microsoft Edge ya da
Google Chrome'u headless çalıştırarak 1080x1350 boyutunda
gorseller/gonderi_01.png ... gonderi_30.png olarak kaydeder.

Yalnız Python standart kütüphanesini kullanır. Tarayıcı için geçici bir profil
klasörü açılır ve iş bitince (hata ya da Ctrl+C olsa bile) silinir.

Kullanım:  python bas.py
"""

import os
import shutil
import struct
import subprocess
import sys
import tempfile
import time
from pathlib import Path

GENISLIK, YUKSEKLIK = 1080, 1350
ADET = 30
ZAMAN_ASIMI = 90  # saniye, tek bir ekran görüntüsü için

KOK = Path(__file__).resolve().parent
SABLON = KOK / "sablon.html"
CIKTI = KOK / "gorseller"


def tarayici_bul():
    """Önce Edge'i, yoksa Chrome'u arar; bulduğu çalıştırılabilir dosyanın yolunu döndürür."""
    edge, chrome = [], []
    if os.name == "nt":
        for degisken in ("PROGRAMFILES(X86)", "PROGRAMFILES", "LOCALAPPDATA"):
            kok = os.environ.get(degisken)
            if kok:
                edge.append(Path(kok) / "Microsoft" / "Edge" / "Application" / "msedge.exe")
                chrome.append(Path(kok) / "Google" / "Chrome" / "Application" / "chrome.exe")
    elif sys.platform == "darwin":
        edge.append(Path("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"))
        chrome.append(Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"))

    for aday in edge + chrome:
        if aday.is_file():
            return aday

    for ad in ("msedge", "microsoft-edge", "microsoft-edge-stable",
               "chrome", "google-chrome", "google-chrome-stable"):
        yol = shutil.which(ad)
        if yol:
            return Path(yol)
    return None


def png_boyutu(yol):
    """PNG başlığından (genişlik, yükseklik) okur; geçersizse None döner."""
    try:
        with open(yol, "rb") as f:
            bas = f.read(24)
    except OSError:
        return None
    if len(bas) < 24 or bas[:8] != b"\x89PNG\r\n\x1a\n" or bas[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", bas[16:24])


def ekran_goruntusu(tarayici, profil, url, hedef, pencere):
    """Tarayıcıyı headless çalıştırıp url'nin görüntüsünü hedef dosyaya yazar."""
    if hedef.exists():
        hedef.unlink()
    komut = [
        str(tarayici),
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--mute-audio",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-extensions",
        "--disable-sync",
        "--disable-background-networking",
        "--disable-component-update",
        "--disable-default-apps",
        "--force-device-scale-factor=1",
        "--run-all-compositor-stages-before-draw",
        f"--user-data-dir={profil}",
        f"--window-size={pencere[0]},{pencere[1]}",
        f"--screenshot={hedef}",
        url,
    ]
    return subprocess.run(komut, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          timeout=ZAMAN_ASIMI)


def hata_nedeni(sonuc):
    if sonuc is None:
        return "bilinmeyen hata"
    satirlar = [s for s in sonuc.stderr.decode("utf-8", "replace").splitlines() if s.strip()]
    if sonuc.returncode != 0:
        return f"tarayıcı {sonuc.returncode} koduyla çıktı" + (f": {satirlar[-1][:120]}" if satirlar else "")
    return "PNG oluşmadı ya da boyutu yanlış"


def profil_sil(profil):
    """Tarayıcının alt süreçleri dosyaları kısa süre kilitli tutabilir; birkaç kez dener."""
    for _ in range(20):
        if not profil.exists():
            return
        try:
            shutil.rmtree(profil)
            return
        except OSError:
            time.sleep(0.5)
    shutil.rmtree(profil, ignore_errors=True)
    if profil.exists():
        print(f"Uyarı: geçici profil silinemedi: {profil}")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")

    baslangic = time.perf_counter()

    if not SABLON.is_file():
        print(f"Şablon bulunamadı: {SABLON}")
        return 1

    tarayici = tarayici_bul()
    if tarayici is None:
        print("Microsoft Edge ya da Google Chrome bulunamadı.")
        return 1
    print(f"Tarayıcı: {tarayici}")

    CIKTI.mkdir(exist_ok=True)
    taban_url = SABLON.as_uri()
    pencere = (GENISLIK, YUKSEKLIK)
    basarili = 0

    profil = Path(tempfile.mkdtemp(prefix="mavi_fincanlik_profil_"))
    try:
        for i in range(1, ADET + 1):
            t0 = time.perf_counter()
            hedef = CIKTI / f"gonderi_{i:02d}.png"
            url = f"{taban_url}#{i}"
            sonuc, boyut, neden = None, None, None
            try:
                sonuc = ekran_goruntusu(tarayici, profil, url, hedef, pencere)
                boyut = png_boyutu(hedef)
                if boyut and boyut != (GENISLIK, YUKSEKLIK):
                    # Bazı sürümlerde görüntü alanı pencereden biraz farklı olur:
                    # farkı pencereye ekleyip bir kez daha dene, sonrakiler de bunu kullansın.
                    pencere = (pencere[0] + GENISLIK - boyut[0], pencere[1] + YUKSEKLIK - boyut[1])
                    sonuc = ekran_goruntusu(tarayici, profil, url, hedef, pencere)
                    boyut = png_boyutu(hedef)
            except subprocess.TimeoutExpired:
                neden = f"{ZAMAN_ASIMI} sn içinde bitmedi"
            except OSError as hata:
                neden = f"tarayıcı çalıştırılamadı: {hata}"

            sure = time.perf_counter() - t0
            if boyut == (GENISLIK, YUKSEKLIK):
                basarili += 1
                print(f"[{i:02d}/{ADET}] {hedef.name}  {boyut[0]}x{boyut[1]}  {sure:.1f} sn")
            else:
                print(f"[{i:02d}/{ADET}] {hedef.name}  HATA: {neden or hata_nedeni(sonuc)}  {sure:.1f} sn")
    except KeyboardInterrupt:
        print("\nKullanıcı tarafından durduruldu.")
    finally:
        profil_sil(profil)

    toplam = time.perf_counter() - baslangic
    print(f"\nToplam süre: {toplam:.1f} sn  ({basarili}/{ADET} gönderi basıldı, klasör: {CIKTI})")
    return 0 if basarili == ADET else 1


if __name__ == "__main__":
    sys.exit(main())
