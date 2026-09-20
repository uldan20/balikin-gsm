# SVG beranda hub

Satuan piksel logis, siap ditempel ke berkas rancangan.

| Berkas | Ukuran | Isi |
| --- | --- | --- |
| `beranda-a-reputasi.svg` | 384 × 844 | layar penuh: kartu 2A + kartu 3A |
| `beranda-b-jelajahi.svg` | 384 × 844 | layar penuh: kartu 2B + kartu 3C |
| `beranda-c-peta.svg` | 384 × 844 | layar penuh: kartu 2A + kartu 3B |
| `kartu-1-barang-di-sekitarmu.svg` | 390 × 272 | kartu 340 × 232 di x=20 y=20 |
| `kartu-2a-lapor-terang.svg` | 390 × 180 | kartu 340 × 140 |
| `kartu-2b-lapor-teal.svg` | 390 × 180 | kartu 340 × 140 |
| `kartu-3a-reputasi.svg` | 390 × 248 | kartu 340 × 208 |
| `kartu-3c-pintu-jelajahi.svg` | 390 × 248 | kartu 340 × 208 |
| `kartu-3b-jelajahi-peta.svg` | 390 × 248 | kartu 340 × 208 |
| `kartu-ajak-warga.svg` | 380 × 296 | kartu 340 × 256 di x=20 y=20 |

`kartu-ajak-warga.svg` tidak lewat jalur ekstraksi HTML seperti yang lain —
dibangun langsung oleh [`../build_ajak_warga.py`](../build_ajak_warga.py)
memakai `I()`, `hex6()`, dan `bidang()` dari `xbanner/rapi.py`. Jalankan
ulang skrip itu kalau isinya perlu diubah, jangan sunting SVG-nya.

Berkas kartu punya latar gradasi tipis supaya bayangannya kelihatan — hapus
persegi latar paling bawah kalau mau ditempel ke berkas sendiri.

Pasang Archivo dan Plus Jakarta Sans sebelum membuka.
