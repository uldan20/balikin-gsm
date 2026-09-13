# Buku GSM — 24 halaman A5 lanskap

210 × 148 mm, art paper 150 gsm, jilid spiral. Artboard 840 × 592 px
(4 satuan = 1 mm). Gaya mengikuti poster showcase: bidang besar, tipografi
tegas, banyak ruang kosong — **tata letaknya yang dikunci, isinya masih
placeholder.**

| Hal. | Isi | Berkas |
| ---: | --- | --- |
| 01 | Sampul | `Main.dc.html` |
| 02 | Daftar isi | `H02` |
| 03 | Pembatas Bab I | `H03` |
| 04–05 | Produk dan pengguna · Tagline & kepribadian | `H04`–`H05` |
| 06 | Pembatas Bab II | `H06` |
| 07–13 | Logogram · Konstruksi · Ruang aman · Ukuran minimum · Konfigurasi · Warna logo · Larangan | `H07`–`H13` |
| 14 | Pembatas Bab III | `H14` |
| 15–21 | Palet · Tipografi · Sudut Enam · Pustaka ikon · Pola sarang · Maskot · Tulisan tangan | `H15`–`H21` |
| 22 | Pembatas Bab IV | `H22` |
| 23–24 | Layar dan cetak · Merchandise & booth | `H23`–`H24` |

## Latar dan supergrafis

Halaman isi tidak polos — tiap halaman memakai empat lapis yang sama, warnanya
mengikuti bab:

1. **Bidang miring 30°** — sudut yang sama dengan sisi heksagon, memotong
   halaman dari tepi atas ke sudut bawah. Arahnya berganti kiri–kanan tiap
   halaman, jadi kalau bukunya dibuka, dua halaman saling mencerminkan.
2. **Pola sarang** hanya di dalam bidang miring itu, bukan di seluruh halaman —
   supaya polanya punya tepi dan terbaca sebagai grafis, bukan tekstur.
3. **Angka hantu** nomor bagian setinggi 300 px, opasitas 6%, menyembul di tepi.
4. **Indeks tepi** — pita warna bab di sisi kanan, posisinya turun satu tingkat
   tiap bab, jadi keempat bab terlihat bertingkat waktu buku ditutup.

Kepala halaman diberi heksagon kecil dan garis rambut sewarna bab. Kotak
spesimen mengambang dengan bayangan tipis di atas bidang itu.

Pembatas bab memakai lapis yang sama dengan arah tetap ke kanan.

## Yang masih placeholder

- **Tangkapan layar aplikasi** di halaman 04 dan 23 — sekarang ponsel kosong.
- **Foto cetakan asli** di halaman 23 dan 24 — sekarang blok warna.
- **Lembar ikon lengkap** di halaman 18 — sekarang 18 dari 98 bentuk.
- **Nilai CMYK dan Pantone** di halaman 15 — menunggu uji cetak pertama.
- **Pose maskot tambahan** di halaman 20.

Teks aturannya sudah diisi dengan isi yang benar (satuan X, ruang aman 1X,
ukuran minimum, larangan, aturan pola dan tulisan tangan) — tinggal disunting
kalau ada yang mau diperketat.

## Bangun ulang

```bash
cd gsm
python3 build_gsm.py                 # 24 halaman + canvas.json
node lihat.mjs $PWD/Main.dc.html     # potret PNG
```

`kit_gsm.py` memuat kepala halaman, judul bagian, kotak spesimen, lambang,
pola sarang, dan mockup ponsel. Satu pembatas bab dipakai ulang empat kali.

## Kalau nanti diekspor ke cetak

Halaman dibangun sebagai HTML supaya gampang disunting di kanvas. Untuk berkas
cetak, jalankan pengonversi yang sama dengan poster:

```bash
node ../showcase/ekstrak.mjs $PWD/H07.dc.html /tmp/claude-0/gsm-H07.json
```

lalu tulis SVG dengan `bangun(..., ukuran=('210mm', '148mm'))`.
