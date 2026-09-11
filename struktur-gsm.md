# Struktur GSM Balikin

Kerangka *Graphic Standard Manual* yang disusun mengikuti kebiasaan GSM
Tugas Akhir DKV, tapi dipotong mengikuti apa yang Balikin benar-benar punya.
Perkiraan tebal: **60–80 halaman** ukuran A4 lanskap atau B5 potret.

Kolom **Status** memakai tiga tanda: `ADA` (tinggal ditata ulang ke halaman
GSM), `OLAH` (bahannya ada, aturannya belum ditulis), `BARU` (belum ada
sama sekali).

---

## Bab 0 — Pembuka (4–6 hal.)

| Halaman | Isi | Status |
| --- | --- | --- |
| Sampul | Logo + judul "Graphic Standard Manual" | BARU |
| Kata pengantar | Untuk siapa manual ini dan kenapa perlu dipatuhi | BARU |
| Daftar isi | | BARU |
| Cara membaca manual | Arti tanda ✓/✗, satuan ukuran, konvensi warna | BARU |

## Bab I — Tentang Balikin (8–10 hal.)

| Halaman | Isi | Status |
| --- | --- | --- |
| Latar belakang | Masalah barang hilang & rendahnya tingkat pengembalian | OLAH |
| Visi & misi | | BARU |
| Nilai merek | Usulan: **Jujur, Gotong royong, Aman, Tanpa drama** | BARU |
| Positioning | Bukan marketplace, bukan forum — *layanan pengembalian* | BARU |
| Target audiens | Primer, sekunder, persona singkat | OLAH |
| Kepribadian merek | Skala sifat (hangat↔formal, polos↔canggih) | BARU |
| *Brand essence* | Satu kalimat. Usulan: **"Barangmu pulang."** | BARU |
| Nada bicara | Contoh kalimat benar/salah untuk notifikasi & chat | BARU |

> **Kenapa nada bicara penting di sini.** Balikin menangani orang yang sedang
> panik kehilangan barang dan orang asing yang sedang berbaik hati. Dua-duanya
> tidak butuh bahasa korporat. Sediakan 6–8 contoh mikrocopy asli dari app
> (notifikasi "Ada yang menemukan tasmu", tombol "Balikin", status "Sudah
> kembali") — bagian ini biasanya dinilai tinggi karena jarang ada di GSM
> mahasiswa lain.

## Bab II — Identitas Utama / Logo (14–18 hal.)

**Ini jalur kritis.** Semua bab sesudahnya menunggu logo final.

| Halaman | Isi | Status |
| --- | --- | --- |
| Konsep & filosofi logo | Heksagon, panah balik, sarang lebah | BARU |
| Proses perancangan | Sketsa → digitalisasi → penyederhanaan (sertakan yang gagal) | BARU |
| Konstruksi & grid | Logo dibangun di kisi 60° yang sama dengan ikon | BARU |
| Anatomi | Nama tiap bagian: logogram, wordmark, *lockup* | BARU |
| Clear space | Satuan `x` = tinggi heksagon logogram | BARU |
| Ukuran minimum | Cetak (mm) & digital (px), diuji betulan | BARU |
| Konfigurasi | Horizontal, vertikal, logogram saja, wordmark saja | BARU |
| Ikon aplikasi | Semua ukuran, *safe area*, versi adaptif Android | BARU |
| Varian warna | Positif, negatif, monokrom, emas, satu warna | BARU |
| Penempatan di latar | Terang, gelap, warna merek, foto ramai | BARU |
| Larangan | Min. 12 contoh ✗ (diregang, diputar, dibayangi, diganti warna, dioutline, ditempel gradasi, dipakai sebagai pola, diganti font, ditambah efek, dipepet elemen lain, dipakai di latar kontras rendah, disusun ulang) | BARU |
| Lockup dengan tagline | Jarak & perbandingan ukuran | BARU |
| Co-branding | Lockup dengan logo kampus/mitra, garis pemisah | BARU |

> **Arah logo yang paling nyambung dengan aset yang sudah ada.** Repo ikon
> sudah menetapkan heksagon sebagai wadah (tile kategori, avatar, tombol
> lapor) dan menjelaskan sarang lebah sebagai metafora komunitas. Logo yang
> lahir dari kisi itu akan terasa satu keluarga sejak halaman pertama.
> Tiga arah yang layak dieksplorasi:
>
> 1. **Heksagon + panah balik** — panah yang melengkung kembali ke dalam sel.
>    Paling lugas membaca "balikin".
> 2. **Dua sel bersandar** — dua heksagon yang berbagi satu sisi: yang
>    kehilangan dan yang menemukan. Paling dekat dengan filosofi di README.
> 3. **Sel + titik emas** — heksagon berlubang dengan satu titik emas kembali
>    ke tengah: barang yang pulang ke tempatnya. Paling hemat bentuk, paling
>    aman di ukuran 16 px.
>
> Apa pun yang dipilih, uji di 16 px sebelum dikunci — ikon aplikasi adalah
> tempat logo ini paling sering dilihat.

## Bab III — Elemen Visual Pendukung (18–22 hal.)

| Halaman | Isi | Status |
| --- | --- | --- |
| Palet primer | Teal `#1B7A6E`, Emas `#C8952E` + HEX/RGB/CMYK/Pantone | OLAH |
| Palet sekunder | `#34A28F` `#15655B` `#12564D` `#F3D77C` | OLAH |
| Palet netral | `#FBF8F3` `#F1ECE3` `#A99F90` `#211C16` | OLAH |
| Warna semantik | Hilang `#BC5A3C` · Ditemukan · Sudah kembali · Ditolak | OLAH |
| Perbandingan warna | Aturan 60-30-10, contoh komposisi benar/salah | BARU |
| Kontras & aksesibilitas | Uji WCAG AA teks di atas tiap warna | BARU |
| Tipografi utama | Typeface, berat, contoh kalimat, lisensi | BARU |
| Tipografi sekunder | Untuk angka, label, dan UI | BARU |
| Hierarki tipografi | H1–H4, body, caption, dengan ukuran & *tracking* | BARU |
| **Sistem ikon Sudut Enam** | 6 prinsip bentuk, kisi 60°, chamfer, mitre | ADA |
| Spesifikasi ikon | Kanvas 100×100, area aman 8–92, stroke 7/6.5/5.5 | ADA |
| Varian garis & padat | Kapan pakai yang mana, aturan `fill-rule="evenodd"` | ADA |
| Aturan aksen emas | Maksimal satu titik emas per ikon | ADA |
| Dua pengecualian bentuk | `BadgeStar` lima sudut, `AchNightWatch` lengkung | ADA |
| Larangan ikon | Jangan dibulatkan, jangan digradasi, jangan dicampur pustaka lain | OLAH |
| Pola heksagon | Kerapatan, opasitas, kapan boleh dipakai sebagai latar | BARU |
| Elemen grafis | Wadah heksagon, bidang chamfer, garis pemisah, bingkai | OLAH |
| Maskot | Konstruksi, proporsi, pose baku, ekspresi, larangan | BARU |
| Gaya ilustrasi | Garis, warna, tingkat detail | BARU |
| Fotografi | Tone, subjek, perlakuan, contoh ✓/✗ | BARU |
| Grid & layout | Margin, kolom, modul heksagon | BARU |

> **Warna sudah hampir jadi.** `src/icons/hexcut/base.tsx` mengekspor objek
> `tokens` berisi 12 warna yang sudah dipakai konsisten di seluruh pustaka.
> Yang kurang tinggal konversi CMYK/Pantone untuk cetak dan uji kontras.
> Jangan ubah nilai HEX-nya — 196 komponen dan 196 file SVG sudah terlanjur
> memakainya.

> **Maskot — keputusan yang masih terbuka.** Tiga arah, pilih satu sebelum
> produksi merchandise dimulai:
>
> | Arah | Isi | Cocok untuk | Risiko |
> | --- | --- | --- | --- |
> | **A. Lebah** | Satu lebah pengantar; menyambung metafora sarang lebah di README | Plushie, standee, logo sekunder | Lebah sudah dipakai banyak merek |
> | **B. Warga heksagon** | Karakter manusia mengikuti 5 Tingkat Komunitas | Standee, papan peringkat, sistem tingkat | Butuh 5 desain sekaligus |
> | **C. Keluarga Barang Hilang** | Kunci, payung, tumbler, dompet, kacamata yang hidup — "barang juga pengin pulang" | Plushie, stiker, komik pendek, gantungan | Gaya wajah harus dijembatani ke ikon yang bersudut |
>
> **Rekomendasi: C, dengan A sebagai elemen sistem.** Arah C langsung lahir
> dari 13 Kategori Barang yang sudah ada, menghasilkan satu *cast* untuk
> merchandise tanpa mengarang konsep baru, dan memberi pameran sisi emosional
> yang tidak dimiliki ikon geometris. Heksagon/sarang tetap jadi wadah dan
> pola sistemnya. Konsekuensinya, GSM perlu satu halaman khusus yang
> menjelaskan **bagaimana gaya maskot yang bulat dan ramah bisa hidup
> berdampingan dengan ikon yang bersudut tajam** — jawabannya: maskot memakai
> siluet bersudut yang sama tapi diberi wajah, dan tidak pernah tampil di
> dalam komponen UI.

## Bab IV — Penerapan Identitas (16–20 hal.)

| Kelompok | Item |
| --- | --- |
| **Digital** | Ikon aplikasi, splash screen, cuplikan UI kit, template notifikasi, profil & feed Instagram, template story, tanda tangan email, *banner* Play Store |
| **Stationery** | Kartu nama, kop surat, amplop, map, stempel, ID card tim, lanyard |
| **Merchandise** | Lihat [`merchandise.md`](merchandise.md) |
| **Signage & pameran** | Backdrop, X-banner, standee, *table cloth*, hangtag, papan peringkat |
| **Kemasan** | Hangtag merchandise, stiker segel, paper bag, kotak kecil |
| **Operasional** | Rompi/kaus relawan, seragam titik serah terima, papan "Titik Balikin" |
| **Iklan** | Poster A2, spanduk, materi digital |

> **Bab ini yang dilihat penguji paling lama.** Halaman penerapan adalah
> bukti bahwa sistemnya jalan, bukan cuma cantik di halaman logo. Foto
> *mockup* yang rapi di sini bernilai lebih besar daripada tambahan halaman
> aturan.

## Bab V — Lampiran (4–6 hal.)

| Halaman | Isi |
| --- | --- |
| Struktur file aset | Penamaan file, format, di mana disimpan |
| Daftar aset | 196 komponen React, 196 SVG, versi *tintable* & putih |
| Checklist pra-cetak | Warna CMYK, *bleed*, resolusi, *outline* font |
| Pengelolaan & kontak | Siapa yang boleh mengubah GSM, versi keberapa |

---

## Urutan kerja yang disarankan

Kerjakan menurun — tiap langkah memakai hasil langkah sebelumnya.

1. **Logo** (Bab II) — semua menunggu ini. Kunci dulu sebelum apa pun dicetak.
2. **Tipografi + baku warna cetak** (Bab III) — cepat, sekali duduk.
3. **Maskot & gaya ilustrasi** (Bab III) — penentu seluruh merchandise.
4. **Pola & elemen grafis** (Bab III) — bahan latar untuk semua penerapan.
5. **Penerapan** (Bab IV) — kerjakan yang dipakai di pameran lebih dulu:
   backdrop → X-banner → hangtag → merchandise → stationery.
6. **Bab I & Bab 0** — tulis terakhir, waktu isinya sudah kelihatan semua.
7. **Lampiran** — sekali *sweep* di akhir.

## Bentuk akhir GSM

Siapkan tiga keluaran dari satu berkas yang sama:

| Keluaran | Untuk | Catatan |
| --- | --- | --- |
| **Buku cetak** A4 lanskap, jilid spiral/lem | Meja pameran & meja penguji | Satu eksemplar cukup; kertas isi HVS 100gr, sampul artcarton 260gr laminasi doff |
| **PDF** | Lampiran laporan & pengumpulan | Sertakan *hyperlink* daftar isi |
| **Papan ringkas** A1 | Dipajang di booth | Ringkasan logo, palet, ikon, penerapan dalam satu bidang |
