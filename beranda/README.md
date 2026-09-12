# Beranda sebagai hub

Tiga kotak kosong di `beranda balikin` diisi jadi tiga pintu masuk. Ukuran
mengikuti berkas yang dikirim: layar **384 × 844**, kolom isi `x = 22`,
lebar **340**.

| Kotak | y | tinggi | Isi |
| --- | --- | --- | --- |
| 1 | 128 | 214 | **Barang di sekitarmu** — judul tengah + tumpukan folder, pola dari acuan HiFi dan Portfolio |
| 2 | 362 | 122 | **Mau lapor apa hari ini?** — dua tombol ke alur pilih jenis laporan |
| 3 | 508 | 214 | dua versi: **A Reputasimu**, **B Jelajahi peta** |

Bagian kosong di tengah tiga tombol header diisi **pil lokasi**
(`pil_lokasi()` di `kit_app.py`): titik hijau + `CISAAT, SUKABUMI` + panah.

## Dua versi kartu ketiga

- **A · Reputasimu** — panel teal tua, lencana heksagon, tingkat 3 dari 5,
  720 poin, sisa 180 poin ke Penjaga Kota, empat lencana terakhir. Angkanya
  sama dengan layar Profil di prototipe.
- **B · Jelajahi peta** — peta ringkas (digambar, bukan peta asli), keping
  lokasi, 12 titik aktif, tumpukan avatar warga, tombol *Buka peta*. Dengan
  versi ini beranda punya tiga pintu lengkap: barang sekitar → pelaporan →
  jelajahi.

Isi kartu 1 dan kartu 3B sengaja tidak memakai angka yang sama supaya tidak
terbaca dobel: kartu 1 bicara **barang** (42 barang), kartu 3B bicara
**wilayah** (12 titik aktif, 18 warga).

## Berkas

```bash
python3 build_beranda.py                   # dua layar + empat kartu mandiri
node lihat.mjs $PWD/Main.dc.html           # potret PNG
for f in Main BerandaB Kartu1 Kartu2 Kartu3A Kartu3B; do
  node ../showcase/ekstrak.mjs $PWD/$f.dc.html /tmp/claude-0/br-$f.json
done
python3 ke_svg_app.py                      # tulis svg/*.svg
```

- `kit_app.py` — palet aplikasi, bar status, header, navigasi bawah, heksagon
- `build_beranda.py` — isi tiap kartu
- `ke_svg_app.py` — ekspor SVG dengan satuan piksel

## Catatan

- Warna diambil dari tangkapan layar prototipe, bukan dari `tokens` di
  `base.tsx` — dua sumber itu memang masih perlu disamakan (lihat README utama).
- Heksagon di sini **bersisi datar** (titik di kiri-kanan), mengikuti tombol
  utama dan lencana di prototipe.
- Peta di kartu 3B digambar sendiri. Kalau nanti dipakai peta asli, ganti
  lapisan `peta_svg()` dengan tangkapan peta.
- Sisa desimal di SVG hanya nilai `opacity`.
