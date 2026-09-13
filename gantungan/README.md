# Gantungan kunci — lima Tingkat Komunitas

Siluet potongnya **mengikuti bentuk lencana reputasi di aplikasi**, bukan
bentuk baru: bulat → kotak membulat → heksagon → perisai berletusan → letusan.
Wadahnya ikut naik seiring tingkat, persis aturan di `Tiers.tsx`.

Akrilik **3 mm**, cetak UV dua sisi, potong mengikuti bentuk, lubang cincin
**4 mm**. Lencana ±48 mm. Lembar 174 × 126 mm, lima keping (3 + 2).
Skala 4 satuan = 1 mm.

| Tingkat | Bentuk | Warna |
| --- | --- | --- |
| 1 · Warga Baru | bulat | krem, cincin titik abu |
| 2 · Tetangga Baik | kotak membulat | mint, hati bersudut enam |
| 3 · Penolong | heksagon | teal, heksagon dalam |
| 4 · Penjaga Kota | perisai berletusan 8 | terakota |
| 5 · Legenda Balikin | letusan 12 | emas, bintang enam |

**Depan:** lencana + pita nama tingkat.
**Belakang:** nomor tingkat, nama, dan wordmark di atas dasar krem.

## Catatan produksi

1. Lapisan `POTONG` magenta = jalur pisau dan lubang cincin. Hapus sebelum cetak.
2. Berkas depan dan belakang **urutannya sama**. Vendor yang mencerminkan sisi
   belakang saat memasang — sebutkan ini waktu memesan supaya tidak dicerminkan
   dua kali.
3. Akrilik bening perlu dasar putih (*white ink*) supaya warnanya tidak tembus.
4. Ujung letusan tingkat 4 dan 5 sengaja dibuat tumpul; jangan diruncingkan
   lagi, 3 mm akrilik gampang patah di ujung tipis.
5. Untuk pameran: 5 desain × 2 = 10 keping (lihat `rencana-1juta.md`).

## Bangun ulang

```bash
cd gantungan && python3 build_gantungan.py
```

Sisa desimal hanya `version="1.0"` pada deklarasi XML.
