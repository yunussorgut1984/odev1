import sys
import shutil
from pathlib import Path

KATEGORILER = {
    "Resimler": [".jpg", ".jpeg", ".png", ".gif"],
    "Belgeler": [".pdf", ".docx", ".txt", ".xlsx"],
    "Muzik": [".mp3", ".wav"],
    "Videolar": [".mp4", ".avi", ".mkv"],
}


def kategori_bul(uzanti):
    for kategori, uzantilar in KATEGORILER.items():
        if uzanti in uzantilar:
            return kategori
    return "Diger"


def bos_isim_bul(hedef):
    if not hedef.exists():
        return hedef
    sayi = 1
    while True:
        yeni = hedef.with_name(f"{hedef.stem} ({sayi}){hedef.suffix}")
        if not yeni.exists():
            return yeni
        sayi += 1


def duzenle(klasor):
    for dosya in list(klasor.iterdir()):
        if not dosya.is_file():
            continue
        kategori = kategori_bul(dosya.suffix.lower())
        hedef_klasor = klasor / kategori
        hedef_klasor.mkdir(exist_ok=True)
        hedef = bos_isim_bul(hedef_klasor / dosya.name)
        shutil.move(dosya, hedef)
        print(f"{dosya.name} -> {kategori}/{hedef.name}")


if len(sys.argv) != 2:
    print("Kullanim: python duzenle.py <klasor_adi>")
    sys.exit(1)

klasor = Path(sys.argv[1])
if not klasor.is_dir():
    print(f"Klasor bulunamadi: {klasor}")
    sys.exit(1)

duzenle(klasor)
