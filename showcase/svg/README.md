# Poster showcase — berkas SVG

Enam poster sebagai vektor pada ukuran cetak **A3 potret, 297 × 420 mm**.
Terbuka di Illustrator dan Figma langsung pada ukuran sebenarnya.

| Berkas | Versi |
| --- | --- |
| `poster-s1-kartu-melayang.svg` | S1 · Kartu Melayang |
| `poster-s2-editorial.svg` | S2 · Editorial |
| `poster-s3-saku.svg` | S3 · Saku |
| `poster-s4-stiker.svg` | S4 · Stiker |
| `poster-s5-irisan.svg` | S5 · Irisan |
| `poster-s6-cap-logo.svg` | S6 · Cap Logo |

## Cara berkas ini dibuat

Bukan digambar ulang tangan. Dua langkah, keduanya bisa dijalankan lagi kapan
saja kalau posternya berubah:

```bash
node ekstrak.mjs <artboard>.dc.html /tmp/<nama>.json   # ukur geometri di peramban
python3 ke_svg.py                                      # terjemahkan ke SVG
```

`ekstrak.mjs` melucuti seluruh transform lebih dulu supaya yang terukur adalah
kotak tata letak asli, lalu mencatat rantai putaran dan pemotongan milik tiap
leluhur secara terpisah. `ke_svg.py` memasangnya kembali sebagai grup bersarang,
jadi putaran dan clip tetap menurun persis seperti di CSS.

Yang ikut diterjemahkan: gradien, sudut membulat, bayangan berlapis, cincin
*spread*, tepi putus-putus, segitiga CSS (ekor penanda peta), dan ikon
ber-`currentColor`.

## Huruf

Pasang dulu **Archivo**, **Plus Jakarta Sans**, dan **Caveat** — ketiganya
gratis di Google Fonts. Teksnya masih hidup supaya bisa diubah; tanpa hurufnya
terpasang, tata letak akan bergeser.

## Koordinat

Seluruh koordinat bilangan bulat. Yang tersisa berdesimal hanya nilai `opacity`
dan satu sudut putaran pada S3 — dua-duanya bukan koordinat.

## Sebelum naik cetak

1. Ganti rangka **LAYAR APLIKASI** di tiap ponsel dengan tangkapan layar asli.
2. S5 punya **dua slot foto** bertanda garis putus-putus.
3. Ubah teks jadi kurva, atau kirim PDF dengan huruf tertanam.
4. Beri *bleed* 3 mm.

## Perbaikan 12 September

Ikon garis sempat terisi hitam di berkas SVG: atribut `fill="none"` milik
`<svg>` pembungkus hilang waktu tag dilucuti, sehingga tiap `<path>` yang hanya
punya `stroke` diisi warna bawaan. `ke_svg.py` sekarang memasang ulang atribut
penampilan itu sebagai atribut grup. Keenam berkas sudah dibangun ulang.
