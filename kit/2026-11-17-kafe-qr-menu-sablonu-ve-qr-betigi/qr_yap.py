"""Menü adresini QR koda çevirir.

Kullanım:
    python qr_yap.py            -> qr.png ve qr.svg (MASA için)
    python qr_yap.py --hepsi    -> qr_masa1.png/.svg ... qr_masa10.png/.svg

Gereksinim: pip install segno
"""
import sys
from urllib.parse import urlencode

import segno

ADRES = "http://localhost:8017/"
MASA = 5


def masa_adresi(masa):
    ayrac = "&" if "?" in ADRES else "?"
    return ADRES + ayrac + urlencode({"masa": masa})


def qr_yaz(adres, dosya_adi):
    qr = segno.make(adres, error="m")
    qr.save(dosya_adi + ".png", scale=10, border=4)
    qr.save(dosya_adi + ".svg", scale=10, border=4)
    print(f"{dosya_adi}.png / .svg  ->  {adres}")


if __name__ == "__main__":
    if "--hepsi" in sys.argv[1:]:
        for masa in range(1, 11):
            qr_yaz(masa_adresi(masa), f"qr_masa{masa}")
    else:
        qr_yaz(masa_adresi(MASA), "qr")
