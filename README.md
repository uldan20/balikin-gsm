# Balikin — GSM & Perlengkapan Pameran

Materi *Graphic Standard Manual* aplikasi **Balikin** (Lost & Found) beserta
rencana produksi booth dan merchandise untuk pameran Tugas Akhir menjelang
sidang.

## Modal yang sudah ada

Dari repo [`uldan20/balikin`](https://github.com/uldan20/balikin):

| Aset | Status | Masuk GSM di |
| --- | --- | --- |
| **Logo** — logogram heksagon + wordmark, sudah dipakai di splash, header, dan ikon aplikasi | Selesai, aturannya belum ditulis | Bab II |
| **Judul skripsi, nama, NIM, pembimbing** — dari naskah REVISI 24 Juni | Ada | Bab 0 & I |
| **Maskot** — Lebah Sarang (`maskot/lebah.svg`) | Dipilih | Bab III |
| **Tagline** — "Yang hilang, balik pulang." | Ditetapkan | Bab I & II |
| **Elemen grafis tulisan tangan** — "Small Things Make a Big Difference" | Ditetapkan, aturannya belum ditulis | Bab III |
| **Gaya ilustrasi** — karakter warga, datar, hangat; teal · terakota · emas | Selesai, aturannya belum ditulis | Bab III |
| **Rancangan aplikasi** — onboarding, peta, feed, pencarian, detail, profil, notifikasi | Selesai (WIP) | Bab IV |
| Bahasa visual **Sudut Enam (Hexcut)** — kisi 60°, sudut dipangkas, sambungan mitre | Selesai | Bab III |
| 98 ikon × 2 varian (garis & padat) = 196 komponen | Selesai | Bab III |
| 76 file SVG mandiri + versi *tintable* | Selesai | Lampiran |
| Palet kerja (`tokens` di `base.tsx`) | Perlu dibakukan (CMYK/Pantone) | Bab III |
| Filosofi bentuk (6 prinsip) | Selesai | Bab II & III |
| 5 Tingkat Komunitas, 9 Lencana Pencapaian, 13 Kategori Barang | Selesai | Bab III & IV |

Tidak ada jalur kritis yang menghambat produksi. Logo, tagline, gaya
ilustrasi, dan seluruh rancangan aplikasi sudah jadi — yang tersisa adalah
**menuliskan aturannya**, bukan merancang ulang.

## Yang belum ada

1. **Aturan pemakaian logo** — clear space, ukuran minimum, konfigurasi, larangan
2. **Tipografi resmi** — typeface utama & sekunder, hierarki, lisensi
3. **Aturan kapan heksagon, kapan sudut membulat** — lihat catatan di `struktur-gsm.md`
4. **Lembar karakter ilustrasi** — konstruksi, pose baku, ekspresi, larangan
5. **Pola heksagon** (honeycomb pattern) untuk latar dan kemasan
6. **Baku warna cetak** — konversi CMYK/Pantone dan uji kontras
7. **Penerapan luar aplikasi** — stationery, signage, merchandise

## Tiga hal yang perlu diselaraskan lebih dulu

Ditemukan waktu membandingkan pustaka ikon dengan WIP rancangan aplikasi.
Selesaikan sebelum GSM naik cetak, supaya manualnya tidak bertentangan dengan
aplikasinya sendiri:

1. **Bentuk lencana tingkat.** Namanya sudah cocok — layar Tingkat & Poin
   memakai persis lima nama di `Tiers.tsx`. Yang belum cocok adalah **wadahnya**.
   README pustaka ikon menjanjikan heksagon terputus → kotak → heksagon utuh →
   perisai → letusan 12 sudut; aplikasi memakai cincin → persegi membulat
   berhati → heksagon berlian → perisai-bintang → letusan emas. Gantungan kunci
   akan dicetak dari salah satunya, jadi kunci dulu yang mana.
2. **Nama kategori barang.** Pustaka ikon punya 13 kategori; onboarding
   aplikasi menampilkan 8 (Tas & Dompet, Kunci, HP & Elektronik, Dokumen,
   Kartu identitas, Hewan, Aksesoris, Lainnya) dan filter pencarian
   menampilkan 10 (termasuk "Botol & bekal", "Perhiasan"). Samakan.
3. **Nilai warna.** Palet aplikasi terlihat sedikit lebih hangat dan lebih tua
   daripada `tokens` di `base.tsx`. Ambil nilai dari berkas rancangan, lalu
   perbarui `tokens` — atau sebaliknya — tapi jangan biarkan dua sumber.

## Peta dokumen

| File | Isi |
| --- | --- |
| [`struktur-gsm.md`](struktur-gsm.md) | Kerangka GSM bab per bab, halaman per halaman |
| [`merchandise.md`](merchandise.md) | Konsep, daftar item, spesifikasi, prioritas, estimasi biaya |
| [`booth-pameran.md`](booth-pameran.md) | Tata letak booth, display, interaksi pengunjung |
| [`timeline-produksi.md`](timeline-produksi.md) | Hitung mundur, lead time vendor, checklist |

## Catatan harga

Seluruh angka rupiah di dokumen ini **estimasi kasar** untuk menyusun anggaran,
bukan penawaran. Harga cetak bergerak mengikuti kota, kuantitas, dan bahan —
selalu minta *quote* tertulis ke vendor sebelum mengunci anggaran.

## Data resmi dari naskah skripsi

Diambil dari `REVISI_24_JUNI.docx`. Pakai ini di semua materi cetak, jangan
mengetik ulang dari ingatan:

- **Judul** — Perancangan UI/UX Aplikasi Lost and Found "Balikin" Berbasis
  Sistem Reputasi Komunitas dengan Pendekatan Design Thinking (Studi Kasus di
  Sukabumi)
- **Penulis** — Uldan Pamungkas · 20210060127
- **Program studi** — Desain Komunikasi Visual, Fakultas Teknik, Komputer dan
  Desain, Universitas Nusa Putra Sukabumi
- **Pembimbing I** — Firman Mutaqin, S.Ds., M.Ds
- **Pembimbing II** — Rifky Nugraha, S.Pd., M.Ds
- **Metode** — penelitian perancangan, metode campuran berdominasi kualitatif,
  kerangka Design Thinking (Empathize–Define–Ideate–Prototype–Test). Usability
  diukur dengan Single Ease Question (SEQ)
- **Landasan** — Self-Determination Theory (Ryan & Deci, 2000) untuk kebutuhan
  kompetensi dan keterhubungan; bystander effect (Latané & Darley, 1970) sebagai
  latar konteks sosial
- **Temuan yang paling kuat untuk materi cetak** — penemu barang kerap ragu
  bertindak: takut dituduh mencuri, atau tidak tahu cara mengembalikannya dengan
  aman

### Satu hal yang perlu diselaraskan dengan naskah

Tujuan penelitian menulis sistem reputasi sebagai **"bentuk pengakuan, bukan
imbalan uang"**, sementara rancangan aplikasi sekarang punya fitur **tip lewat
QRIS**. Dua-duanya bisa benar — poin reputasi memang bukan uang, dan tip itu
ucapan terima kasih sukarela dari pemilik yang terpisah dari sistem poin — tapi
naskahnya belum mengatakan itu. Penguji hampir pasti menanyakannya. Tambahkan
satu paragraf di Batasan Masalah atau di bab perancangan yang memisahkan
keduanya secara eksplisit.
