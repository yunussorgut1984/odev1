# odev1 – Dosya Düzenleme Aracı

Bir klasördeki dosyaları türlerine göre alt klasörlere taşıyan küçük bir Python programı.

## Özellikler

- Dosyaları uzantılarına göre kategorilere ayırır:

  | Klasör   | Uzantılar                    |
  |----------|------------------------------|
  | Resimler | .jpg .jpeg .png .gif         |
  | Belgeler | .pdf .docx .txt .xlsx        |
  | Muzik    | .mp3 .wav                    |
  | Videolar | .mp4 .avi .mkv               |
  | Diger    | Diğer tüm dosyalar           |

- Büyük/küçük harf fark etmez (`.PNG` ve `.png` aynı kategoriye gider).
- **Hiçbir dosyayı silmez.** Hedefte aynı isimde bir dosya varsa
  yeni dosyanın adına numara ekler: `foto (1).jpg`
- Klasörlere dokunmaz, sadece dosyaları taşır.

## Gereksinimler

- Python 3 (ek kütüphane gerekmez)

## Kullanım

```
python duzenle.py <klasor_adi>
```

Örnek:

```
python duzenle.py indirilenler
```

Örnek çıktı:

```
foto.jpg -> Resimler/foto.jpg
odev.pdf -> Belgeler/odev.pdf
sarki.mp3 -> Muzik/sarki.mp3
program.exe -> Diger/program.exe
```

> ⚠️ Programı `duzenle.py` dosyasının bulunduğu klasörde (`python duzenle.py .`)
> çalıştırmayın; aksi halde programın kendi dosyalarını da taşır.
