# Poster Showcase Balikin

Enam arah poster **showcase produk** A3 potret — memamerkan layar dan konsep
aplikasinya, bukan penelitiannya. Poster penelitian yang akademik ada di folder
`../poster/`.

| Berkas | Versi | Acuan | Gagasan |
| --- | --- | --- | --- |
| `Main.dc.html` | **S1 · Kartu Melayang** | Pangea | Gradien teal, ponsel terpotong di atas, kartu pil laporan melayang lengkap dengan penanda peta |
| `Editorial.dc.html` | **S2 · Editorial** | Nebula | Gradien teal ke emas, wordmark hantu raksasa, label sudut ala studi kasus portofolio |
| `Saku.dc.html` | **S3 · Saku** | Ladaar | Ponsel muncul dari balik saku miring berjahit emas — terjemahan saku jeans ke bahasa Balikin |
| `Stiker.dc.html` | **S4 · Stiker** | Whatnow | Blok warna, dua ponsel miring, stiker die-cut, bagian "Sekilas" dwibahasa |
| `Irisan.dc.html` | **S5 · Irisan** | Klever | Irisan miring berisi pola dan slot foto, tombol pil melayang, ponsel menembus sudut |
| `CapLogo.dc.html` | **S6 · Cap Logo** | Tunnest | Logo heksagon Balikin dibesarkan jadi latar penuh, dua ponsel di atasnya, wordmark besar di bawah |

## Ukuran

A3 potret **297 × 420 mm**. Artboard **1122 × 1587 px** — A3 pada 96 ppi, jadi
ekspor PDF dari kanvas keluar tepat A3.

## Isi layar masih placeholder

Tiap ponsel memuat rangka layar samar bertanda **LAYAR APLIKASI**. Ganti dengan
tangkapan layar asli lewat fungsi `ponsel(lebar, putaran, layar)` di `kit.py` —
argumen `layar` menerima potongan HTML apa pun, termasuk `<img src="...">`.

## Yang tidak bisa dibuat di sini: foto

Tidak ada foto sama sekali di berkas-berkas ini — semuanya vektor dan CSS.
Di mana acuannya bergantung pada fotografi, penggantinya:

- **S3** memakai bidang saku bergambar jahitan, bukan foto jeans.
- **S5** menyediakan **dua slot foto** bertanda garis putus-putus; tinggal
  diisi foto sendiri.

## Membangun ulang

```bash
python3 build_showcase.py
```

`kit.py` memuat perkakas bersama: bingkai ponsel, rangka layar, stiker, penanda
peta, kartu pil, pola sarang, dan baris kredit.

## Catatan sistem

Gradien **belum ada** di sistem visual Balikin — dipakai di S1, S2, dan S5
mengikuti gaya acuan. Kalau arah bergradien yang dipilih, tambahkan aturannya ke
GSM Bab III supaya tidak jadi keputusan sekali pakai.
