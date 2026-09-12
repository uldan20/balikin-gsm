# Balikin — catatan kerja

## Koordinat harus bilangan bulat

Berkas desain dibuka dan diperiksa di Figma. **Angka berdesimal di panel
Position/Dimensions tidak diterima.** Empat penyebab yang selalu muncul kalau
tidak dijaga, beserta penangkalnya:

| Penyebab | Penangkal |
| --- | --- |
| `transform="scale(...)"` — Figma meratakannya, koordinat 100 satuan jadi pecahan | Bakar transform ke dalam data path. Jangan sisakan `scale()` di keluaran |
| Geometri heksagon — setengah-lebar `= r × √3` tidak pernah bulat | Tetapkan setengah-lebar sebagai bilangan bulat, turunkan sisanya dari situ |
| Posisi hasil ukur dari peramban — `line-height` 0.93 × 58 = 53.94 | Bulatkan seluruh garis dasar dan kotak sebelum ditulis |
| Ukuran huruf dan tebal garis pecahan — 17.5px, 12.5px, 1.6 | Pakai bilangan bulat saja |

Alatnya sudah ada di `xbanner/rapi.py`: `bakar_path()`, `bakar_fragmen()`,
`hex6()`, `bidang()`, `I()`. Pakai itu, jangan menulis ulang.

**Tiap grup gambar diberi `bidang()`** — kotak tak terlihat seukuran bingkai
yang diinginkan, supaya Figma melaporkan W/H grup sebagai bilangan bulat.

**Satu pengecualian yang wajar:** lebar lapisan *teks* ditentukan metrik huruf,
jadi selalu berdesimal — itu berlaku untuk teks apa pun di Figma, termasuk yang
diketik tangan. Yang bisa dijamin bulat adalah bingkai grup yang membungkusnya.

Sebelum mengirim berkas, hitung sisanya:

```bash
grep -oE '\-?[0-9]+\.[0-9]+' berkas.svg | sort -u
```

Yang boleh tersisa hanya nilai `opacity` dan **sudut putaran** di dalam
`rotate(...)` — keduanya bukan koordinat. Sisanya perbaiki.

## Ukuran cetak

Gambar pada skala **1 satuan = 1 mm**, lalu tulis `width`/`height` dalam `mm`
supaya berkas terbuka di Illustrator dan Figma pada ukuran sebenarnya.
X-banner 600 × 1600. Poster A1 594 × 841.

## Data resmi

Judul skripsi, nama, NIM, pembimbing, metode, dan temuan ada di `README.md`.
Ambil dari sana, jangan mengetik ulang dari ingatan.

## Huruf

Archivo (judul), Plus Jakarta Sans (teks), Caveat (tulisan tangan). Ketiganya
dari Google Fonts. Ekspor PNG/PDF dari kanvas tidak menyertakan huruf ini —
hasilnya memakai huruf cadangan.

## Bahasa

Seluruh isi materi, nama lapisan, dan komentar dalam bahasa Indonesia.
