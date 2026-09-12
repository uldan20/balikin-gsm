# Standee QR meja — berkas potong

Akrilik **3 mm**, cetak UV satu sisi, potong mengikuti bentuk (*die-cut*).
Ukuran badan **150 × 215 mm**. Skala berkas: 4 satuan = 1 mm, `width`/`height`
sudah dalam mm jadi terbuka pada ukuran sebenarnya.

| Berkas | Konsep |
| --- | --- |
| `svg/standee-a-kotak-temuan.svg` | **A · Kotak Temuan** — bentuk map arsip berlidah, lebah menyembul di atas, keping "Pindai Aku" miring, pita krem di kaki |
| `svg/standee-b-sel-sarang.svg` | **B · Sel Sarang** — heksagon besar, QR duduk di dalam sel sarang, lebah menyembul di sisi atas |
| `svg/standee-dudukan.svg` | dudukan 100 × 24 mm, slot 3,25 mm — dipotong terpisah |

## Cara baca berkasnya

- Lapisan **`POTONG`** (garis magenta) = jalur pisau. **Hapus sebelum cetak** —
  itu panduan tukang, bukan bagian desain.
- Tepi putih di luar gambar adalah *border* die-cut, biarkan.
- Satu jalur potong utuh, tanpa garis sambungan di dalam.
- Slot pada dudukan juga dipotong.

## Sebelum kirim ke vendor

1. **Ganti pola QR dengan QR asli.** Yang ada sekarang pola contoh — layanan
   pembuat QR diblokir dari lingkungan kerja ini. Buat QR ke tautan prototipe
   Figma, ukuran modul jangan lebih kecil dari 0,8 mm.
2. Outline teks atau sematkan huruf (Archivo, Plus Jakarta Sans).
3. Tambah bleed 3 mm mengikuti jalur potong.
4. Pastikan vendor menandai sisi cetak — akrilik bening perlu dasar putih
   (*white ink*) supaya warnanya tidak tembus.

## Bangun ulang

```bash
cd standee && python3 build_standee.py
```

Ditulis langsung sebagai SVG (bukan lewat pengonversi HTML) supaya jalur
potongnya utuh. Sisa desimal hanya nilai `opacity` dan `version="1.0"` di
deklarasi XML.
