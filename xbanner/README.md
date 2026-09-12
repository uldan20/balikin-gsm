# X-Banner Balikin

Tiga versi rancangan X-banner **60 × 160 cm** untuk booth pameran, plus satu
lembar elemen grafis.

| Berkas | Versi | Isi |
| --- | --- | --- |
| `Main.dc.html` | **A · Maskot** | Bidang teal penuh, maskot Heksa, alur empat langkah di pita krem bawah |
| `Tipografi.dc.html` | **B · Tipografi** | Tagline empat baris besar, tiga fitur inti, pita teal di bawah |
| `KartuBarang.dc.html` | **C · Kartu Barang** | Dua kartu laporan dari aplikasi sebagai bintang utama |
| `Grafik.dc.html` | Elemen grafis | Tulisan tangan "Small Things Make a Big Difference" beserta aturannya |

## Skala

Artboard **600 × 1600 px** — **1 px = 1 mm**, jadi ukuran di berkas bisa dibaca
langsung sebagai milimeter cetak. Tagline 68 px berarti tinggi huruf 68 mm.

Untuk cetak, keluarkan PDF dari kanvas lalu perbesar 100 % ke 60 × 160 cm, atau
gambar ulang di Illustrator memakai angka yang sama dalam milimeter.

## Zona tinggi

X-banner berdiri di lantai, jadi puncaknya kira-kira setinggi mata:

| Baris di artboard | Tinggi sebenarnya | Isi |
| --- | --- | --- |
| 0 – 500 | 160 – 110 cm | Logo dan tagline — zona mata |
| 500 – 1000 | 110 – 65 cm | Visual utama |
| 1000 – 1300 | 65 – 35 cm | Alur langkah dan QR |
| 1300 – 1600 | 35 – 0 cm | Baris kredit, zona lantai |

## Membangun ulang

Seluruh artboard dihasilkan oleh satu skrip, bukan diedit tangan:

```bash
python3 build.py
```

Ubah warna, salinan teks, atau tata letak di `build.py`, jalankan ulang, lalu
susun ulang kanvasnya. `x-banner-balikin.html` adalah hasil susunan — jangan
diedit langsung.

## Yang masih placeholder

- **QR** di ketiga versi masih pola tiruan. Ganti dengan QR pendek dinamis yang
  mengarah ke prototipe sebelum naik cetak, dan uji pindai dari 30 cm di bawah
  lampu booth yang sebenarnya.
- **Baris kredit** `[Nama Lengkap · NIM] · [Program Studi] · [Universitas]`.
- **Isi kartu** pada versi C memakai ikon Sudut Enam. Kalau ada foto barang yang
  bagus, tukar — kartunya jadi jauh lebih meyakinkan.
- **Huruf tulisan tangan** memakai Caveat. Pertimbangkan mengganti dengan
  tulisan tangan sendiri yang di-scan.

## Catatan huruf

Archivo untuk judul, Plus Jakarta Sans untuk teks, Caveat untuk elemen tulisan
tangan. Ekspor PNG/PDF dari kanvas belum bisa menyertakan huruf Google Fonts —
hasil ekspor memakai huruf cadangan. Untuk cetak akhir, gambar ulang di
Illustrator dengan huruf yang sudah dipasang, atau ekspor dari berkas rancangan.
