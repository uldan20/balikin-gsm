# Poster & Infografis Balikin

Empat rancangan **A3 potret** untuk pameran: dua poster penelitian, dua
infografis. Poster menjelaskan **penelitiannya**, infografis menjelaskan
**produknya** — pembagian yang sama dipakai booth CERTAKU dan Juz Amma Journey.

| Berkas | Versi | Gagasan |
| --- | --- | --- |
| `Main.dc.html` | **P1 · Kolom** | Dua kolom, tiap bagian bertanda heksagon. Susunan akademik yang lazim, paling enak dibaca penguji sambil berdiri |
| `LimaTahap.dc.html` | **P2 · Lima Tahap** | Lima tahap Design Thinking jadi **sumbu** poster, membelah bidang jadi sebelum dan sesudah. Metodenya bukan satu kotak di antara kotak lain — metodenya kerangkanya |
| `Perjalanan.dc.html` | **I1 · Perjalanan Sebuah Dompet** | Tujuh perhentian dari tertinggal di angkot sampai pulang, berselang-seling di sisi garis putus-putus |
| `Reputasi.dc.html` | **I2 · Sarang Kepercayaan** | Tangga lima tingkat sebagai batang yang meninggi, sembilan lencana, dan tabel poin naik–turun |

## Ukuran

A3 potret **297 × 420 mm**. Artboard **1122 × 1587 px** — A3 pada 96 ppi, jadi
ekspor PDF dari kanvas keluar tepat A3. Untuk cetak akhir, berkas SVG pada
ukuran milimeter sebenarnya dibuat menyusul, mengikuti aturan di `CLAUDE.md`.

Teks isi 16 px = **12 pt**, sesuai batas bawah teks cetak yang dibaca dari jarak
tangan.

## Isi

Seluruh teks diambil dari `REVISI_24_JUNI.docx` lewat `isi.py` — satu berkas,
jadi kalau naskahmu berubah, cukup ubah di sana lalu bangun ulang:

```bash
python3 build_poster.py
```

## Kesimpulan sengaja ditandai "menunggu data"

Abstrak naskahmu sendiri menulis *"[Ringkasan hasil pengujian usability diisi
setelah data terkumpul.]"* — jadi angka SEQ dan hasil pengujian belum ada.
Bagian Kesimpulan di kedua poster memakai penanda **MENUNGGU DATA** dan bukan
angka karangan. Begitu datamu masuk, ganti `KESIMPULAN_PENDING` di `isi.py`.

## Yang masih placeholder

- **QR** di keempatnya masih pola tiruan. Ganti dengan QR pendek dinamis ke
  prototipe sebelum naik cetak.
- **Gambar layar aplikasi** belum dipasang. Kalau mau, sisakan satu blok di P1
  atau P2 untuk tangkapan layar — sekarang keempatnya murni teks dan diagram.
