# Infografis pameran — tiga lembar A3

Gaya mengikuti infografis editorial (satu benda besar yang "memuat" datanya,
judul dua baris, keping legenda, kartu catatan miring), tetapi seluruh bentuk,
warna, dan ikonnya memakai bahasa visual Balikin sendiri.

Ukuran artboard 1122 × 1587 px = A3 potret 297 × 420 mm pada 96 ppi.

| Lembar | Benda utama | Isi |
| --- | --- | --- |
| **I1 · Pustaka Ikon Sudut Enam** (`Main.dc.html`) | kotak komponen | 98 ikon garis dibagi sepuluh keluarga, luas petak sebanding jumlahnya; petak putus-putus = 8 dari 13 kategori yang tampil di onboarding |
| **I2 · Perjalanan Sebuah Dompet** (`Perjalanan.dc.html`) | jalan menuju cakrawala | tujuh langkah dari hilang sampai pulang; siluet lima lokasi observasi di cakrawala |
| **I3 · Naik Tingkat** (`Tingkat.dc.html`) | kolom ukur poin | lima tingkat, tinggi pita sebanding rentang poinnya; daftar poin naik/turun; sembilan lencana |

## Asal tiap angka

| Angka | Sumber |
| --- | --- |
| 98 ikon, 196 komponen, 76 berkas SVG | `src/icons/hexcut` di repo [`uldan20/balikin`](https://github.com/uldan20/balikin) — jumlah `export const` per berkas |
| 10 keluarga ikon dan isinya | berkas per keluarga: Actions 18, Items 13, System 12, Badges 11, Form 11, Achievements 9, Nav 8, Status 6, Pay 5, Tiers 5 |
| 13 kategori barang, 8 di onboarding | `Items.tsx` dan layar onboarding |
| Nama lima tingkat, sembilan lencana | `Tiers.tsx`, `Achievements.tsx` |
| Rentang poin tiap tingkat, nilai poin naik/turun | layar **Tingkat & Poin** di prototipe — **lihat catatan di bawah** |
| Tujuh langkah perjalanan | alur layar prototipe |
| Lima lokasi observasi, temuan lapangan | naskah `REVISI_24_JUNI.docx` |

## Yang harus dicek ulang sebelum cetak

1. **Ambang poin tiap tingkat.** Infografis memakai angka dari layar prototipe
   (0–150 · 150–400 · 400–900 · 900–2.000 · 2.000+). `communityTiers` di
   `Tiers.tsx` menulis angka lain: 0 · 100 · 400 · 1.000 · 2.500 PN. Hanya
   angka 400 yang sama. Kunci dulu yang mana yang benar, lalu perbarui
   `TINGKAT_I` di `build_info.py` (dan `TINGKAT` di `poster/isi.py`).
2. **Rincian pada langkah perjalanan** — radius lima kilometer, tiga pertanyaan
   ciri rahasia, kode empat huruf. Semua dari layar prototipe; cocokkan sekali
   lagi dengan berkas Figma sebelum naik cetak.
3. **Bentuk lencana tingkat** masih berbeda antara README pustaka ikon dan
   aplikasi. Di I3 dipakai siluet versi `Tiers.tsx`.

## Cara membangun ulang

```bash
cd infografis
python3 build_info.py                      # tiga .dc.html + canvas.json
node lihat.mjs $PWD/Main.dc.html           # potret PNG untuk diperiksa
```

SVG cetak:

```bash
for f in Main Perjalanan Tingkat; do
  node ../showcase/ekstrak.mjs $PWD/$f.dc.html /tmp/claude-0/inf-$f.json
done
python3 ke_svg_info.py                     # tulis svg/*.svg
```

Berkas: `ikon.py` (tambahan fragmen ikon), `kit_info.py` (perkakas bersama),
`build_info.py` (isi tiap lembar), `ke_svg_info.py` (ekspor).

## Catatan

- Seluruh koordinat bilangan bulat. Yang tersisa berdesimal di SVG hanya nilai
  `opacity` — dan pada I3 ada satu kecocokan palsu: teks **2.000** (pemisah
  ribuan), bukan koordinat.
- Huruf belum di-outline. Pasang Archivo, Plus Jakarta Sans, dan Caveat sebelum
  membuka berkasnya.
- Warna `#EDCFC2` (terakota muda) adalah turunan baru untuk blok data; kalau
  arah ini dipakai, masukkan ke GSM Bab III sebagai warna pendukung.
