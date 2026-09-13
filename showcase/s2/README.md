# S2 Editorial — tiga arah baru

Latar, supergrafis, dan tata letak dirombak; **isi teksnya sama persis** dengan
versi lama. Semua supergrafis dibangun dari kisi 60°, bukan gradasi polos.

| Berkas | Arah | Latar | Supergrafis |
| --- | --- | --- | --- |
| `Main.dc.html` | **A · Irisan 60°** | teal, dipotong miring 30° jadi bidang krem di kaki | deret heksagon emas mengecil menyusuri garis irisan, heksagon raksasa terpotong di kanan atas |
| `S2b.dc.html` | **B · Sel Sarang** | kisi sel sarang penuh halaman, gelap ke terang | tujuh sel diisi warna sebagai aksen, ponsel duduk di jendela heksagon |
| `S2c.dc.html` | **C · Jejak** | radial teal pekat | tiga cincin heksagon di belakang ponsel, jejak putus-putus melintas dari kiri atas ke kanan bawah dengan penanda heksagon |

Tata letaknya juga dibedakan: A memakai kolom kanan untuk daftar proses,
B menyusun judul bertangga mengikuti offset sel, C memiringkan pita judul −4°
dan mengubah daftar proses jadi deret bernomor mendatar.

Layar ponsel masih placeholder — tinggal ditempel tangkapan layar Jelajahi.

## Bangun ulang

```bash
cd showcase && python3 build_s2.py     # tulis ke showcase/s2/
cd s2 && node lihat.mjs $PWD/Main.dc.html
```

Versi lama tetap ada di `showcase/Editorial.dc.html` dan
`showcase/svg/poster-s2-editorial.svg`.
