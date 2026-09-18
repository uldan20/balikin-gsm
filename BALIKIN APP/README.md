# BALIKIN APP — ekspor dari Figma

Tangkapan layar rancangan aplikasi, diekspor dari berkas Figma
**BALIKIN-APP-EDU**. Dipakai sebagai acuan waktu menyusun GSM Bab IV, poster
showcase, dan mockup di booth pameran.

Folder ini adalah **titik serah** antara Figma dan repo. Berkas Figma tidak bisa
dibaca langsung dari sesi kerja — `figma.com` dan `api.figma.com` ditutup
kebijakan jaringan — jadi apa pun yang perlu dipakai dari Figma harus mendarat
di sini dulu sebagai berkas.

## Isi sekarang

| Berkas | Layar |
| --- | --- |
| `ONBOARDING.png` · `ONBOARDING PART 2.png` | Alur perkenalan |
| `Beranda Baru.png` · `New Home:Beranda.png` | Beranda, hub tiga pintu |
| `Jelajahi.png` | Pintu Jelajahi |
| `Barang di Sekitarmu.png` | Peta barang terdekat |
| `Pelaporan.png` | Alur lapor barang |
| `Chat.png` | Percakapan penemu–pemilik |
| `Momen Tip.png` · `QRIS.png` | Tip sukarela lewat QRIS |
| `Profile.png` | Profil, tingkat, dan poin |
| `LOGO.svg` | Logogram heksagon + wordmark |

Halaman **🪟 Final Screen (Low-fi & High-Fi) 2** belum ada di sini.

## Cara ekspor supaya langsung bisa dipakai

Di Figma, pilih frame yang dimaksud, lalu panel **Export** di kanan bawah:

- **PNG 2x** untuk acuan visual dan mockup — cukup untuk dilihat dan diukur.
- **SVG** kalau isinya mau dipakai ulang sebagai vektor di materi cetak. Centang
  *Include "id" attribute*, matikan *Outline text* kalau hurufnya masih mau
  diedit.

Ekspor SVG dari Figma hampir selalu keluar dengan koordinat berdesimal dan
`transform="scale(...)"`. Jangan pakai mentah-mentah untuk materi cetak —
lewatkan dulu ke `bakar_path()` dan `bidang()` di `xbanner/rapi.py`, sesuai
aturan di [`CLAUDE.md`](../CLAUDE.md).

## Aturan nama berkas

Pakai nama layar apa adanya dari Figma, biar gampang dilacak balik.

Satu hal yang perlu dihindari: **tanda titik dua (`:`)**. Berkas
`New Home:Beranda.png` tidak bisa di-checkout di Windows dan bikin repot
sebagian alat. Untuk berkas baru pakai tanda hubung — `New Home - Beranda.png`.

## Catatan

Ekspor PNG dari Figma sudah membawa hurufnya sendiri, jadi aman dilihat di mana
saja. Ini beda dengan ekspor dari kanvas HTML di repo ini, yang butuh Archivo,
Plus Jakarta Sans, dan Caveat terpasang — lihat [`CLAUDE.md`](../CLAUDE.md).
