# Buku GSM — 24 halaman A5 lanskap

210 × 148 mm, art paper 150 gsm, jilid spiral. Artboard 840 × 592 px
(4 satuan = 1 mm).

Gaya presentasi **brand identity** — acuannya papan identitas merek di Behance:
tipografi besar bercampur, ruang kosong murah hati, blok warna penuh halaman,
kartu bersudut membulat besar, dan supergrafis heksagon yang keluar tepi
halaman. **Tata letaknya dikunci; tangkapan layar dan foto cetakan masih
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

## Aturan tata letak

Satu sistem dipakai di seluruh buku, jadi halaman mana pun terbaca sebagai satu
keluarga:

- **Tepi halaman 56 px**, lebar isi 728 px. Dua kolom 340 + 48 + 340;
  tiga kolom 224 + 28 + 224 + 28 + 224.
- **Kepala halaman**: label bab di kiri, nomor halaman di kanan, garis rambut
  di y = 72. Kaki halaman dibiarkan kosong kecuali ada yang perlu dikatakan.
- **Judul bagian** dicampur dua gaya — Archivo tebal + Archivo miring, selalu
  dipecah di **batas kata**, tidak pernah di tengah kata. Satu kalimat
  ringkasan rata kanan di seberangnya.
- **Supergrafis**: satu heksagon besar, bidang tint 5%, keluar tepi bawah
  halaman. Warnanya mengikuti bab (teal · teal tua · emas · terakota). Arahnya
  berganti kiri–kanan tiap halaman.
- **Pembatas bab** memakai warna penuh halaman: angka romawi hantu di kiri
  bawah, judul besar di kiri atas, daftar isi bab di kanan.
- Kartu putih **radius 16–26 px**. Tidak ada bayangan kecuali pada mockup.

## Huruf

Archivo (judul, wordmark, angka), Plus Jakarta Sans (teks, label), Caveat (satu
kalimat tulisan tangan). Halaman memuat sendiri ketiganya dari Google Fonts,
lengkap dengan **varian miring Archivo** yang dipakai di judul campur.

## Yang masih placeholder

- **Tangkapan layar aplikasi** di halaman 04 dan 23 — sekarang ponsel kosong.
- **Foto cetakan asli** di halaman 23 dan 24 — sekarang blok warna.
- **Lembar ikon lengkap** di halaman 18 — sekarang 16 dari 98 bentuk.
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

`kit_gsm.py` memuat seluruh perkakasnya: `tajuk()` judul campur, `mata()`
kata-mata, `blok()` kartu, `gambar()` mockup, `heks()` supergrafis, `sarang()`
pola, `lambang()` logo, `ponsel()` purwarupa, dan `bingkai()` kepala halaman.
Satu pembatas bab dipakai ulang empat kali.

> Potret PNG memakai huruf cadangan kalau Google Fonts tidak terjangkau dari
> mesin perender. Pasang Archivo, Plus Jakarta Sans, dan Caveat ke sistem kalau
> mau potretnya sesuai berkas aslinya.

## Kalau nanti diekspor ke cetak

Halaman dibangun sebagai HTML supaya gampang disunting di kanvas. Untuk berkas
cetak, jalankan pengonversi yang sama dengan poster:

```bash
node ../showcase/ekstrak.mjs $PWD/H07.dc.html /tmp/claude-0/gsm-H07.json
```

lalu tulis SVG dengan `bangun(..., ukuran=('210mm', '148mm'))`.
