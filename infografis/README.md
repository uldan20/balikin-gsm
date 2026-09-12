# Infografis pameran — papan penelitian A3

Papan utama untuk booth: **lima bagian wajib** — latar belakang, temuan
permasalahan, tujuan penelitian, metode penelitian & perancangan, dan
kesimpulan — dalam bahasa visual Balikin.

Artboard 1122 × 1587 px = A3 potret 297 × 420 mm pada 96 ppi.

| Lembar | Berkas | Catatan |
| --- | --- | --- |
| **A · Papan Penelitian (terang)** | `Main.dc.html` | latar wash, kartu krem. Lebih aman untuk cetak dan fotokopi |
| **B · Papan Penelitian (gelap)** | `Gelap.dc.html` | latar teal bersarang, kartu kaca. Lebih menonjol di booth |
| Cadangan · Pustaka Ikon | `Ikon.dc.html` | 98 ikon dibagi sepuluh keluarga |
| Cadangan · Perjalanan | `Perjalanan.dc.html` | tujuh langkah hilang → pulang |
| Cadangan · Naik Tingkat | `Tingkat.dc.html` | lima tingkat, poin naik/turun, sembilan lencana |

Tiga lembar cadangan dari putaran sebelumnya **tidak dihapus** — isinya sistem
aplikasi, bukan isi penelitian, jadi cocok sebagai papan pendukung di samping
papan utama, bukan sebagai papan utama.

## Asal tiap angka di papan utama

Semua dikutip dari `REVISI_24_JUNI.docx` lewat `isi_riset.py`:

| Angka / pernyataan | Letak di naskah |
| --- | --- |
| Latar belakang, BPS 2023 | BAB I · 1.1 Latar Belakang |
| Tiga tujuan penelitian | BAB I · 1.4 Tujuan Penelitian |
| Pendekatan kualitatif | BAB III · 3.1 Metode Penelitian |
| Observasi 1–5 Mei 2025, lima lokasi, non-partisipatif | BAB III · 3.2 Metode Pengumpulan Data |
| Wawancara semi-terstruktur purposif | BAB III · 3.2 |
| Kuesioner 2–9 Juni 2025 · 60 responden · 15 butir · Google Form | BAB III · 3.2 |
| SWOT · User Journey Mapping · Kuesioner deskriptif · 5W + 1H | BAB III · 3.3 |
| Lima tahap Design Thinking | BAB III · 3.5.1 |
| SEQ rata-rata 6,1 dari 7 pada 50 responden | BAB IV · Hasil Pengujian |
| 82% · 74% · 88% | BAB IV · Hasil Pengujian |
| Empat alasan desain bekerja | BAB IV · Kesimpulan Sementara Efektivitas Media |
| Masukan iterasi (hubungi pemilik, status warna, CTA) | BAB IV · Hasil Pengujian |
| Batasan lingkup | BAB I · 1.3 Batasan Masalah |

Temuan permasalahan diringkas dari data observasi dan wawancara (BAB III) serta
kesimpulan deskriptif penelitian terdahulu (BAB II).

## Cara membangun ulang

```bash
cd infografis
python3 build_riset.py                     # papan utama A & B + canvas.json
python3 build_info.py                      # tiga lembar cadangan
node lihat.mjs $PWD/Main.dc.html           # potret PNG untuk diperiksa
```

SVG cetak:

```bash
for f in Main Gelap Ikon Perjalanan Tingkat; do
  node ../showcase/ekstrak.mjs $PWD/$f.dc.html /tmp/claude-0/inf-$f.json
done
python3 ke_svg_info.py                     # tulis svg/*.svg
```

Berkas: `isi_riset.py` (isi naskah), `ikon.py` (fragmen ikon tambahan),
`kit_info.py` (perkakas bersama), `build_riset.py` dan `build_info.py`
(tata letak), `ke_svg_info.py` (ekspor).

## Yang masih perlu dicek

1. **Ambang poin tiap tingkat** (hanya di lembar cadangan *Naik Tingkat*).
   `Tiers.tsx` menulis 0 · 100 · 400 · 1.000 · 2.500 PN; layar prototipe memakai
   0–150 · 150–400 · 400–900 · 900–2.000 · 2.000+. Kunci dulu yang benar.
2. **Rincian langkah perjalanan** (lembar cadangan) — radius lima kilometer,
   tiga pertanyaan ciri rahasia, kode empat huruf. Semua dari layar prototipe.
3. **Kesimpulan** di papan utama memakai hasil pengujian yang sudah tertulis di
   naskah. Kalau angkanya berubah setelah revisi, ubah `isi_riset.py` saja —
   tata letaknya ikut menyesuaikan.

## Catatan cetak

- Koordinat bilangan bulat. Sisa desimal di SVG hanya nilai `opacity`; pada
  lembar *Naik Tingkat* ada satu kecocokan palsu, teks **2.000** (pemisah ribuan).
- Pasang Archivo, Plus Jakarta Sans, dan Caveat sebelum membuka berkasnya.
- Warna `#EDCFC2` (terakota muda) turunan baru untuk blok data di lembar
  cadangan Pustaka Ikon; kalau dipakai, masukkan ke GSM Bab III.
