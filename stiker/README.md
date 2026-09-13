# Sticker pack — satu lembar vinyl A3 kiss-cut

**28 keping** dalam satu lembar 297 × 420 mm. Vinyl, laminasi doff, kiss-cut
(potong hanya sampai lapisan stiker, kertas alasnya tetap utuh).
Skala 4 satuan = 1 mm. Tepi putih 3 mm di tiap keping.

## Isinya

| Kelompok | Keping |
| --- | --- |
| Identitas | wordmark BALIKIN, logogram heksagon, maskot lebah kecil |
| Lima Tingkat Komunitas | Warga Baru, Tetangga Baik, Penolong, Penjaga Kota, Legenda Balikin — bentuk sama dengan gantungan kunci, jadi bisa dikoleksi berpasangan |
| Suara aplikasi | pita "Yang hilang, balik pulang.", letusan "+150 POIN", pin titik aman |
| Enam kategori barang | Dompet, Kunci, HP, Dokumen, Tas, Botol |
| Gelembung percakapan | "Ketemu!", "Balikin, yuk", "Punyaku!", "Makasih ya" |
| Penanda booth | lebah besar, sel sarang "42", label kode `BLK-P042`, heksagon "Pindai Aku" |
| Kaki | tulisan tangan *Small things make a big difference*, "TITIK AMAN", "balikin.id" |

Kepingnya sengaja beragam ukuran: yang besar untuk laptop dan botol, yang
kecil untuk kartu dan buku catatan. Tidak ada yang di bawah 20 mm supaya masih
gampang dikelupas.

## Catatan produksi

1. Lapisan `POTONG` magenta = jalur kiss-cut. Hapus sebelum cetak; sebagian
   vendor lebih suka membuat *cut contour* sendiri dari tepi putihnya.
2. Tepi putih 3 mm sudah ada di gambar — jangan ditambah lagi.
3. Persegi latar krem ikut tercetak. Kalau mau hemat tinta, hapus persegi
   paling bawah supaya latarnya putih polos.
4. Empat lembar (sesuai `rencana-1juta.md`) = 112 keping, cukup untuk
   giveaway sepanjang pameran.

## Bangun ulang

```bash
cd stiker && python3 build_stiker.py
```

Sisa desimal hanya `version="1.0"` pada deklarasi XML.
