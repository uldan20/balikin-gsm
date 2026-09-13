# Kartu Barang (case card) — 90 × 120 mm

Kartu kasus yang menemani tiap barang di **Meja Barang Temuan**. Pengunjung
ambil barangnya, baca kartunya, pindai QR-nya, lalu menjalankan alur aplikasi.

Art carton 260 gsm, laminasi doff, cetak dua sisi, 24 keping. Skala berkas
4 satuan = 1 mm (360 × 480), `width`/`height` sudah dalam mm.

| Berkas | Arah |
| --- | --- |
| `svg/kartu-barang-a-arsip.svg` | **A · Arsip** — bingkai tipis, kode besar, seperti label museum. Paling netral dan paling murah tinta |
| `svg/kartu-barang-b-aplikasi.svg` | **B · Kartu Aplikasi** — meniru kartu barang di dalam aplikasi: bidang gambar, keping kategori, pita teal ber-QR |
| `svg/kartu-barang-c-koleksi.svg` | **C · Koleksi** — teal pekat, dua sudut dipangkas 60°, heksagon emas. Terasa seperti kartu koleksi |
| `svg/kartu-barang-c-belakang.svg` | **Belakang C** — tiga langkah membalikin, kotak kode serah terima empat huruf, ajakan tukar lencana |
| `svg/kartu-barang-d-tag.svg` | **D · Tag Gantung** — berlubang gantung dan bergaris sobek; bisa digantung langsung di barangnya |

## Isi satu kasus

Kode `BLK-P042` · kategori · nama barang · dua ciri · lokasi dan waktu
ditemukan · status · QR · poin untuk penemu. Semua teks ada di bagian atas
`build_kartu.py` — ganti isinya lalu bangun ulang untuk kasus berikutnya.

## Sebelum cetak

1. **Ganti pola QR dengan QR asli** — sekarang masih pola contoh.
2. QR paling kecil di sini 20 mm (modul ±0,74 mm). Kalau tautannya panjang,
   perbesar atau pakai tautan pendek.
3. Lapisan `POTONG` magenta adalah garis potong — hapus sebelum cetak.
4. Outline teks atau sematkan huruf; tambah bleed 3 mm.
5. Belakang baru dibuat untuk **C · Koleksi** (`kartu-barang-c-belakang.svg`).
   Sudut pangkasnya **dicerminkan** — kanan atas dan kiri bawah — supaya pas
   waktu dicetak bolak-balik lalu dipotong sekali. Jangan diputar, cukup
   dipasang apa adanya sebagai sisi belakang.

## Bangun ulang

```bash
cd kartu && python3 build_kartu.py
```

Sisa desimal di berkas hanya nilai `opacity`, `version="1.0"` pada deklarasi
XML, dan teks jam **16.20** — bukan koordinat.
