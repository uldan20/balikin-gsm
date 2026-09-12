# Beranda sebagai hub

Tiga kotak kosong di `beranda balikin` diisi jadi tiga pintu masuk. Ukuran
mengikuti berkas yang dikirim: layar **384 × 844**, kolom isi `x = 22`,
lebar **340**. Jarak antar kartu **16px**, jarak kartu terakhir ke panel
navigasi juga **16px** (tombol tambah mulai di `y = 756`).

| Kotak | y | tinggi | Isi |
| --- | --- | --- | --- |
| 1 | 128 | 232 | **Barang di sekitarmu** — judul tengah + tumpukan folder |
| 2 | 376 | 140 | **Mau lapor apa hari ini?** — satu pintu ke halaman pilih laporan |
| 3 | 532 | 208 | tiga versi: **3A Reputasi**, **3C Pintu Jelajahi**, **3B Peta** |

## Kartu 2 — satu pintu, bukan dua tombol

Pilihan "barang hilang" dan "saya menemukan" tetap tinggal di halaman
tujuan; di beranda kartunya hanya mengantar ke sana. Dua versi:

- **2A · terang** — senada kartu 1. Label `LAPORAN BARU`, judul, satu tombol
  *Buat laporan*, keping `±3 menit`, dan dua folder (terakota + teal)
  menyembul di tepi kanan sebagai isyarat dua folder tujuan.
- **2B · teal** — satu blok warna utama, heksagon tambah, pola sarang samar,
  satu tombol putih *Pilih folder*. Lebih tegas sebagai aksi utama beranda.

## Kartu 3 — tiga versi

- **3A · Reputasimu** — panel teal tua, lencana heksagon, tingkat 3 dari 5,
  720 poin, sisa 180 poin ke Penjaga Kota, empat lencana terakhir.
- **3C · Pintu Jelajahi** — pintu ke halaman Jelajahi secara utuh, bukan peta:
  judul, jumlah titik dan warga, deretan saringan (Semua · Dompet · Kunci ·
  Kartu), lalu ubin barang yang menyembul terpotong tepi kartu.
- **3B · Peta** — versi peta *Jelajahi peta sekitarmu*. Tidak dihapus,
  disimpan sebagai pilihan.

## Tiga layar contoh

| Berkas | Isi |
| --- | --- |
| `Main.dc.html` | kartu 2A + kartu 3A |
| `BerandaB.dc.html` | kartu 2B + kartu 3C |
| `BerandaC.dc.html` | kartu 2A + kartu 3B (versi peta) |

Kartunya bisa ditukar bebas — tiap kartu juga ada sebagai artboard mandiri.

## Berkas

```bash
python3 build_beranda.py                   # tiga layar + enam kartu mandiri
node lihat.mjs $PWD/Main.dc.html           # potret PNG
for f in Main BerandaB BerandaC Kartu1 Kartu2A Kartu2B Kartu3A Kartu3B Kartu3C; do
  node ../showcase/ekstrak.mjs $PWD/$f.dc.html /tmp/claude-0/br-$f.json
done
python3 ke_svg_app.py                      # tulis svg/*.svg
```

- `kit_app.py` — palet aplikasi, bar status, header, navigasi bawah, heksagon
- `build_beranda.py` — isi tiap kartu
- `ke_svg_app.py` — ekspor SVG dengan satuan piksel

## Catatan

- Bagian kosong di tengah tiga tombol header diisi **pil lokasi**
  (`pil_lokasi()`): titik hijau + `CISAAT, SUKABUMI` + panah.
- Warna diambil dari tangkapan layar prototipe, bukan dari `tokens` di
  `base.tsx` — dua sumber itu memang masih perlu disamakan.
- Heksagon di sini **bersisi datar** (titik di kiri-kanan), mengikuti tombol
  utama dan lencana di prototipe.
- Peta di kartu 3B digambar sendiri, bukan peta asli.
- Sisa desimal di SVG hanya nilai `opacity`.
