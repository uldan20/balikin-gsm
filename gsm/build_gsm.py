# -*- coding: utf-8 -*-
"""Buku GSM Balikin — 24 halaman A5 lanskap. Tata letak dikunci, isi placeholder."""
import os, json
from kit_gsm import *
DIR = os.path.dirname(os.path.abspath(__file__))

HAL = []                                  # (berkas, judul kanvas)

def simpan(nomor, nama, isi, latar=CREAM):
    berkas = ('Main' if nomor == 1 else 'H%02d' % nomor) + '.dc.html'
    tulis(berkas, halaman(isi, latar), latar)
    HAL.append((berkas, '%02d · %s' % (nomor, nama)))

def pembatas(nomor, angka, judul, ringkas, daftar, warna, warna2):
    isi = (dv(P(x=0, y=0, w=W, h=H, z=1, lain='overflow:hidden;'), sarang(CREAM, '.09', 3))
           + dv(P(x=M, y=120, z=5, lain=font(AR, 150, 700, 'rgba(251,248,243,.22)', -6, 1)), angka)
           + dv(P(x=M + 8, y=196, z=6, lain=font(PJ, 10, 700, EMAS_M, 4)), 'BAB ' + angka)
           + dv(P(x=M + 8, y=216, w=460, z=6, lain=font(AR, 44, 700, CREAM, -1.5, 1.1)), judul)
           + dv(P(x=M + 8, y=316, w=420, z=6, lain=font(PJ, 13, 400, 'rgba(207,230,224,.85)', None, 1.6)), ringkas)
           + dv(P(r=M, y=150, w=250, z=6), ''.join(
               dv('display:flex;gap:12px;padding:9px 0;border-bottom:1px solid rgba(251,248,243,.16);',
                  tk(font(AR, 12, 700, EMAS_M, 1) + 'width:26px;flex:none;', h)
                  + tk(font(PJ, 12, 500, CREAM), t)) for h, t in daftar))
           + dv(P(r=M, b=40, z=6), lambang(34, CREAM, EMAS_M)))
    return isi, 'linear-gradient(145deg,' + warna + ' 0%,' + warna2 + ' 100%)'

# ---------------------------------------------------------------- 01 sampul
s = (dv(P(x=0, y=0, w=W, h=H, z=1, lain='overflow:hidden;'), sarang(CREAM, '.1', 3))
     + dv(P(x=M, y=56, z=6), lambang(46, CREAM, EMAS_M))
     + dv(P(r=M, y=62, z=6, lain=font(PJ, 10, 700, 'rgba(207,230,224,.8)', 4, 1, 'right')),
          'GRAPHIC STANDARD MANUAL<br><span style="opacity:.6">EDISI PERTAMA &middot; 2026</span>')
     + dv(P(x=M, y=214, z=6, lain=font(AR, 124, 700, CREAM, -6, 1)), 'BALIKIN')
     + dv(P(x=M + 6, y=348, z=6, lain=font(AR, 26, 700, EMAS_M, -.5)), 'Yang hilang, balik pulang.')
     + dv(P(x=M + 6, y=392, w=430, z=6, lain=font(PJ, 12, 400, 'rgba(207,230,224,.8)', None, 1.6)),
          'Panduan identitas visual aplikasi lost and found berbasis sistem reputasi komunitas.')
     + dv(P(x=M, b=44, z=6, lain=font(PJ, 11, 500, 'rgba(207,230,224,.7)', None, 1.6)),
          'Uldan Pamungkas &middot; 20210060127<br>Desain Komunikasi Visual &middot; Universitas Nusa Putra Sukabumi')
     + dv(P(r=M, b=40, w=196, h=226, z=5, lain='background:rgba(251,248,243,.08);' + HEKS_T))
     + dv(P(r=64, b=88, z=7, lain='width:132px;height:150px;background:' + EMAS_M + ';' + HEKS
            + 'display:grid;place-items:center;'), lambang(62, TEAL_X, TEAL)))
simpan(1, 'Sampul', s, 'linear-gradient(150deg,' + TEAL + ' 0%,' + TEAL_X + ' 100%)')

# ---------------------------------------------------------------- 02 daftar isi
BAB = [('I', 'Tentang Balikin', '03 – 05', TEAL),
       ('II', 'Identitas Utama', '06 – 13', TEAL_G),
       ('III', 'Elemen Visual', '14 – 21', EMAS),
       ('IV', 'Penerapan', '22 – 24', TERRA)]
baris = ''
for a, t, h, c in BAB:
    baris += dv('display:flex;align-items:center;gap:16px;padding:18px 0;border-bottom:1px solid ' + GARIS + ';',
                dv('width:30px;height:34px;background:' + c + ';' + HEKS + 'display:grid;'
                   'place-items:center;flex:none;', tk(font(AR, 13, 700, PUTIH), a))
                + tk(font(AR, 20, 700, INK, -.4) + 'flex:1;', t)
                + tk(font(PJ, 12, 700, REDUP, 1), h))
s = (kepala('Daftar isi', 2)
     + dv(P(x=M, y=90, z=6, lain=font(AR, 44, 700, INK, -1.5, 1)), 'Daftar Isi')
     + dv(P(x=M, y=152, w=340, z=6, lain=font(PJ, 12, 400, REDUP, None, 1.55)),
          'Manual ini mengunci cara memakai identitas Balikin — logo, warna, huruf, ikon, '
          'maskot, dan penerapannya di aplikasi maupun cetak.')
     + dv(P(r=M, y=96, w=400, z=6), baris)
     + dv(P(x=M, b=48, z=6), lambang(30, TEAL, EMAS))
     + dv(P(x=M + 44, b=52, z=6, lain=font(PJ, 10, 700, REDUP, 3)), '24 HALAMAN &middot; A5 LANSKAP'))
simpan(2, 'Daftar Isi', s)

# ---------------------------------------------------------------- 03 pembatas I
s, bg = pembatas(3, 'I', 'Tentang<br>Balikin', 'Apa itu Balikin, untuk siapa, dan bagaimana ia '
                 'ingin terdengar.', [('04', 'Produk dan pengguna'), ('05', 'Tagline & kepribadian')],
                 TEAL_T, TEAL_G)
simpan(3, 'Pembatas Bab I', s, bg)

# ---------------------------------------------------------------- 04 tentang
s = (kepala('Bab I · Tentang Balikin', 4)
     + judul_bagian('1', 'Produk dan pengguna', 'Aplikasi lost and found untuk warga Sukabumi. '
                    'Penemu melapor, pemilik mencari, keduanya bertemu di titik aman.')
     + dv(P(x=M, y=210, w=330, z=6), ''.join(
         dv('display:flex;gap:12px;margin-top:14px;',
            dv('width:26px;height:30px;background:' + MINT_M + ';' + HEKS + 'display:grid;'
               'place-items:center;flex:none;', ik(i, 14, TEAL))
            + dv('flex:1;', dv(font(AR, 13, 700, INK), a)
                 + dv(font(PJ, 11, 400, REDUP, None, 1.4) + 'margin-top:3px;', b)))
         for i, a, b in (('cari', 'Melapor kehilangan', 'Empat langkah, dua menit.'),
                         ('bag', 'Melapor temuan', 'Foto, kategori, lokasi.'),
                         ('bintang', 'Reputasi komunitas', 'Poin dan lencana, bukan uang.'))))
     + kotak(452, 96, 340, 400, sarang(TEAL, '.1', 2), FILL, 18)
     + ponsel(500, 140, 118, 7, rot=-4)
     + ponsel(636, 178, 118, 6, rot=5)
     + label(452, 516, 'Placeholder — ganti dengan tangkapan layar asli'))
simpan(4, 'Produk dan pengguna', s)

# ---------------------------------------------------------------- 05 tagline
sifat = ''
for t, k in (('Hangat', 'bukan formal'), ('Jelas', 'bukan pintar'),
             ('Rendah hati', 'bukan pamer'), ('Tenang', 'bukan heboh')):
    sifat += kotak(0, 0, 0, 0)  # penjaga urutan
sifat = ''.join(
    dv('flex:1;background:' + PUTIH + ';border-radius:14px;padding:14px 16px;box-sizing:border-box;',
       dv(font(AR, 17, 700, TEAL, -.3), t) + dv(font(PJ, 10, 500, REDUP) + 'margin-top:4px;', k))
    for t, k in (('Hangat', 'bukan formal'), ('Jelas', 'bukan pintar'),
                 ('Rendah hati', 'bukan pamer'), ('Tenang', 'bukan heboh')))
s = (kepala('Bab I · Tentang Balikin', 5)
     + judul_bagian('2', 'Tagline & kepribadian')
     + dv(P(x=M, y=170, w=W - M * 2, z=6, lain=font(AR, 54, 700, INK, -2, 1.1, 'center')),
          'Yang hilang, balik pulang.')
     + dv(P(x=0, y=250, w=W, z=6, lain=font(PJ, 12, 400, REDUP, None, 1.5, 'center')),
          'Kalimat penutup di tiap materi. Selalu diakhiri titik. Jangan diterjemahkan.')
     + dv(P(x=M, y=316, w=W - M * 2, z=6, lain='display:flex;gap:12px;'), sifat)
     + dv(P(x=M, b=50, w=W - M * 2, z=6,
            lain='display:flex;align-items:baseline;justify-content:space-between;gap:20px;'),
          tk('font-family:' + CV + ';font-size:30px;font-weight:600;color:' + TEAL
             + ';white-space:nowrap;', 'Small things make a big difference')
          + tk(font(PJ, 10, 700, REDUP, 3) + 'white-space:nowrap;',
               'ELEMEN TULISAN TANGAN &middot; HAL. 21')))
simpan(5, 'Tagline & kepribadian', s)

# ---------------------------------------------------------------- 06 pembatas II
s, bg = pembatas(6, 'II', 'Identitas<br>Utama', 'Logogram, konstruksi, ruang aman, ukuran, '
                 'konfigurasi, warna, dan larangan.',
                 [('07', 'Logogram'), ('08', 'Konstruksi'), ('09', 'Ruang aman'),
                  ('10', 'Ukuran minimum'), ('11', 'Konfigurasi'), ('12', 'Warna logo'),
                  ('13', 'Larangan')], TEAL, TEAL_X)
simpan(6, 'Pembatas Bab II', s, bg)

# ---------------------------------------------------------------- 07 logogram
s = (kepala('Bab II · Identitas Utama', 7)
     + judul_bagian('1', 'Logogram')
     + kotak(M, 150, 372, 346, dv(P(x=0, y=0, w=372, h=346, lain='display:grid;place-items:center;'),
                                  lambang(150, TEAL, EMAS)), PUTIH, 18)
     + label(M, 516, 'Logogram utama — heksagon bergaris dengan sel emas di dalamnya')
     + dv(P(x=460, y=160, w=332, z=6), ''.join(
         catatan(0, i * 92, 332, a, b) for i, (a, b) in enumerate((
             ('Heksagon', 'Sel sarang — satu warga, satu sel. Enam sisi, sudut 60°, sambungan mitre.'),
             ('Sel emas di tengah', 'Barang yang kembali. Selalu emas, tidak pernah warna lain.'),
             ('Garis terbuka', 'Heksagonnya bergaris, bukan padat — komunitas yang bisa dimasuki.')))))
     + dv(P(x=460, y=440, w=332, z=6, lain='background:' + MINT_M + ';border-radius:12px;padding:12px 14px;'),
          dv(font(PJ, 11, 400, INK, None, 1.45), 'Logogram tidak pernah dipakai tanpa ruang aman. '
             'Lihat halaman 09.')))
simpan(7, 'Logogram', s)

# ---------------------------------------------------------------- 08 konstruksi
kisi = ''.join('<path d="M' + str(60 + i * 30) + ' 0V320" stroke="' + TEAL + '" stroke-width="1" '
               'opacity=".18"/>' for i in range(11))
kisi += ''.join('<path d="M0 ' + str(20 + i * 30) + 'H360" stroke="' + TEAL + '" stroke-width="1" '
                'opacity=".18"/>' for i in range(10))
s = (kepala('Bab II · Identitas Utama', 8)
     + judul_bagian('2', 'Konstruksi', 'Seluruh bentuk diturunkan dari satu satuan X — setengah '
                    'lebar heksagon. Tidak ada ukuran yang dikarang.')
     + kotak(M, 196, 372, 300,
             '<svg width="372" height="300" viewBox="0 0 372 300" style="display:block">'
             '<g transform="translate(6 -10)">' + kisi + '</g>'
             '<path d="M186 40L280 95V205L186 260L92 205V95Z" fill="none" stroke="' + TEAL
             + '" stroke-width="9" stroke-linejoin="miter"/>'
             '<path d="M212 128L199 150H173L160 128L173 106H199Z" fill="' + EMAS + '"/>'
             '<path d="M92 278H280" stroke="' + TERRA + '" stroke-width="2"/>'
             '<path d="M92 272V284M280 272V284" stroke="' + TERRA + '" stroke-width="2"/>'
             '<text x="186" y="294" font-family="' + PJ + '" font-size="11" font-weight="700" '
             'fill="' + TERRA + '" text-anchor="middle">2X</text></svg>', PUTIH, 18)
     + dv(P(x=460, y=200, w=332, z=6), ''.join(
         catatan(0, i * 86, 332, a, b) for i, (a, b) in enumerate((
             ('Satuan X', 'Setengah lebar heksagon. Semua jarak kelipatan X.'),
             ('Sudut 60°', 'Kisi isometrik. Tidak ada sudut lain di logo.'),
             ('Tebal garis', 'X ÷ 6. Ikut mengecil kalau logonya mengecil.')))))
     + label(M, 516, 'Jangan menggambar ulang logo. Pakai berkas vektor yang disediakan.', TERRA))
simpan(8, 'Konstruksi', s)

# ---------------------------------------------------------------- 09 ruang aman
s = (kepala('Bab II · Identitas Utama', 9)
     + judul_bagian('3', 'Ruang aman', 'Tidak ada apa pun di dalam kotak putus-putus: teks, '
                    'gambar, tepi kertas, atau logo lain.')
     + kotak(M, 196, 372, 300,
             dv(P(x=76, y=56, w=220, h=188, lain='border:2px dashed ' + TERRA + ';'))
             + dv(P(x=136, y=100, lain='display:grid;place-items:center;'), lambang(100, TEAL, EMAS))
             + ''.join(dv(P(x=x, y=y, lain=font(PJ, 10, 700, TERRA, 1)), 'X')
                       for x, y in ((100, 68), (100, 212), (288, 68), (288, 212)))
             + dv(P(x=76, y=250, w=220, lain=font(PJ, 10, 700, TERRA, 1, None, 'center')),
                  'RUANG AMAN = 1X DI SEMUA SISI'), PUTIH, 18)
     + dv(P(x=460, y=200, w=332, z=6),
          catatan(0, 0, 332, 'Satu X di semua sisi', 'X sama dengan setengah lebar heksagon. '
                  'Kalau logonya membesar, ruang amannya ikut membesar.')
          + catatan(0, 96, 332, 'Di atas foto', 'Pakai bidang warna solid di belakang logo, '
                    'jangan menaruh logo langsung di atas foto ramai.'))
     + dv(P(x=460, y=372, w=332, h=124, z=6,
            lain='background:' + FILL + ';border-radius:14px;display:grid;place-items:center;'),
          dv(font(PJ, 11, 400, REDUP, None, 1.4, 'center') + 'padding:0 18px;',
             'Placeholder — contoh penerapan ruang aman di sampul buku dan header aplikasi.')))
simpan(9, 'Ruang aman', s)

# ---------------------------------------------------------------- 10 ukuran minimum
uk = ''
for i, (px_, lab, ket) in enumerate(((96, '18 mm', 'Cetak'), (58, '32 px', 'Layar'), (34, '16 px', 'Favicon'))):
    uk += dv(P(x=i * 124, y=0, w=112, z=6, lain='text-align:center;'),
             dv('height:120px;display:grid;place-items:center;', lambang(px_, TEAL, EMAS))
             + dv(font(AR, 15, 700, INK) + 'margin-top:6px;', lab)
             + dv(font(PJ, 10, 700, REDUP, 2) + 'margin-top:2px;', ket.upper()))
s = (kepala('Bab II · Identitas Utama', 10)
     + judul_bagian('4', 'Ukuran minimum', 'Di bawah ukuran ini sel emasnya menutup dan '
                    'heksagonnya jadi gumpalan. Jangan dipaksakan.')
     + kotak(M, 210, 400, 250, dv(P(x=28, y=44, w=380, z=6), uk), PUTIH, 18)
     + dv(P(x=488, y=214, w=304, z=6),
          catatan(0, 0, 304, 'Cetak 18 mm', 'Diukur dari lebar heksagon, bukan tinggi kunci.')
          + catatan(0, 84, 304, 'Layar 32 px', 'Di bawah ini pakai logogram tanpa wordmark.')
          + catatan(0, 168, 304, 'Favicon 16 px', 'Versi padat khusus — bukan logo utama diperkecil.'))
     + label(M, 480, 'Ukuran di halaman ini ditampilkan sesuai skala cetak sebenarnya'))
simpan(10, 'Ukuran minimum', s)

# ---------------------------------------------------------------- 11 konfigurasi
def sel_konfig(x, y, w, h, isi, lab):
    return (kotak(x, y, w, h, dv(P(x=0, y=0, w=w, h=h - 30, lain='display:grid;place-items:center;'), isi)
                  + dv(P(x=0, b=10, w=w, lain=font(PJ, 9, 700, REDUP, 2, None, 'center')), lab.upper()),
                  PUTIH, 14))
wm = lambda uk, c=INK: dv('display:flex;align-items:center;gap:' + str(uk // 3) + 'px;',
                          lambang(uk, TEAL, EMAS) + tk(font(AR, int(uk * .78), 700, c, 1), 'BALIKIN'))
s = (kepala('Bab II · Identitas Utama', 11)
     + judul_bagian('5', 'Konfigurasi')
     + sel_konfig(M, 172, 352, 158, wm(44), 'Mendatar — utama')
     + sel_konfig(440, 172, 352, 158,
                  dv('text-align:center;', lambang(44, TEAL, EMAS) + dv('height:8px;')
                     + tk(font(AR, 30, 700, INK, 1), 'BALIKIN')), 'Bertumpuk')
     + sel_konfig(M, 346, 352, 158, lambang(56, TEAL, EMAS), 'Logogram saja')
     + sel_konfig(440, 346, 352, 158,
                  dv('text-align:center;', tk(font(AR, 26, 700, INK, 1), 'BALIKIN')
                     + dv(font(CV, 20, 600, TEAL) + 'margin-top:2px;', 'Yang hilang, balik pulang.')),
                  'Dengan tagline'))
simpan(11, 'Konfigurasi', s)

# ---------------------------------------------------------------- 12 warna logo
def sel_warna(x, y, bg, isi, lab, tepi=False):
    return kotak(x, y, 172, 172,
                 dv(P(x=0, y=0, w=172, h=138, lain='display:grid;place-items:center;'), isi)
                 + dv(P(x=0, b=12, w=172, lain=font(PJ, 9, 700, REDUP, 2, None, 'center')), lab.upper()),
                 PUTIH, 14, lain=('border:1px solid ' + GARIS + ';') if tepi else '')
s = (kepala('Bab II · Identitas Utama', 12)
     + judul_bagian('6', 'Warna logo', 'Empat versi resmi. Di luar ini tidak ada.')
     + dv(P(x=M, y=210, w=172, h=138, z=4, lain='background:' + CREAM + ';border-radius:14px;'))
     + sel_warna(M, 210, CREAM, lambang(62, TEAL, EMAS), 'Utama di krem', True)
     + sel_warna(M + 188, 210, TEAL_X, dv('width:172px;height:138px;background:' + TEAL_X
                                          + ';display:grid;place-items:center;border-radius:14px 14px 0 0;',
                                          lambang(62, CREAM, EMAS_M)), 'Di latar gelap')
     + sel_warna(M + 376, 210, CREAM, lambang(62, INK, INK), 'Mono tinta', True)
     + sel_warna(M + 564, 210, INK, dv('width:172px;height:138px;background:' + INK
                                       + ';display:grid;place-items:center;border-radius:14px 14px 0 0;',
                                       lambang(62, CREAM, CREAM)), 'Mono krem')
     + dv(P(x=M, y=428, w=W - M * 2, z=6, lain='background:' + MINT_M + ';border-radius:14px;'
            'padding:16px 20px;box-sizing:border-box;'),
          dv(font(PJ, 11, 400, INK, None, 1.5),
             'Sel emas hanya hilang di versi mono. Di versi berwarna, sel emas wajib ada — '
             'itu yang membedakan logo Balikin dari heksagon biasa.')))
simpan(12, 'Warna logo', s)

# ---------------------------------------------------------------- 13 larangan
LARANG = ['Diregangkan', 'Diputar', 'Diganti warna', 'Diberi bayangan', 'Ditumpuk teks', 'Ditambah efek']
kis = ''
for i, t in enumerate(LARANG):
    x, y = M + (i % 3) * 248, 200 + (i // 3) * 158
    kis += kotak(x, y, 228, 138,
                 dv(P(x=0, y=0, w=228, h=100, lain='display:grid;place-items:center;'),
                    dv('opacity:.45;', lambang(44, TEAL, EMAS)))
                 + dv(P(x=0, b=12, w=228, lain=font(PJ, 10, 600, TERRA, None, None, 'center')), t)
                 + dv(P(x=14, y=12, w=22, h=22, z=8, lain='background:' + TERRA + ';border-radius:12px;'
                        'display:grid;place-items:center;' + font(PJ, 13, 700, PUTIH)), '&times;'), PUTIH, 14)
s = (kepala('Bab II · Identitas Utama', 13)
     + judul_bagian('7', 'Larangan', 'Enam hal yang membuat logo berhenti jadi logo Balikin.')
     + kis)
simpan(13, 'Larangan', s)

# ---------------------------------------------------------------- 14 pembatas III
s, bg = pembatas(14, 'III', 'Elemen<br>Visual', 'Warna, huruf, bahasa bentuk Sudut Enam, ikon, '
                 'pola sarang, maskot, dan tulisan tangan.',
                 [('15', 'Palet warna'), ('16', 'Tipografi'), ('17', 'Sudut Enam'),
                  ('18', 'Pustaka ikon'), ('19', 'Pola sarang'), ('20', 'Maskot'),
                  ('21', 'Tulisan tangan')], EMAS, '#A87722')
simpan(14, 'Pembatas Bab III', s, bg)

# ---------------------------------------------------------------- 15 palet
PALET = [('Teal', TEAL, '#1B7A63', 'Warna utama'), ('Teal tua', TEAL_X, '#0B4638', 'Latar gelap'),
         ('Mint', MINT, '#8FD4C4', 'Aksen lembut'), ('Emas', EMAS, '#C8952E', 'Penghargaan'),
         ('Terakota', TERRA, '#C05C33', 'Peringatan'), ('Krem', CREAM, '#FBF8F3', 'Latar terang'),
         ('Tinta', INK, '#12332C', 'Teks')]
sw = ''
for i, (nama, warna, kode, guna) in enumerate(PALET):
    x = M + i * 104
    terang = warna in (CREAM, MINT)
    sw += kotak(x, 196, 92, 200,
                dv(P(x=0, y=0, w=92, h=132, lain='background:' + warna + ';'))
                + dv(P(x=10, y=144, lain=font(AR, 13, 700, INK, -.2)), nama)
                + dv(P(x=10, y=162, lain=font(PJ, 9, 600, REDUP, .5)), kode)
                + dv(P(x=10, y=176, lain=font(PJ, 9, 400, REDUP)), guna),
                PUTIH, 12, lain='border:1px solid ' + GARIS + ';')
s = (kepala('Bab III · Elemen Visual', 15)
     + judul_bagian('1', 'Palet warna', 'Tujuh warna. Teal untuk aksi, emas untuk penghargaan, '
                    'terakota untuk peringatan — jangan ditukar perannya.')
     + sw
     + dv(P(x=M, y=424, w=W - M * 2, z=6, lain='display:flex;gap:12px;'),
          ''.join(dv('flex:1;background:' + PUTIH + ';border-radius:12px;padding:12px 14px;'
                     'box-sizing:border-box;border:1px solid ' + GARIS + ';',
                     dv(font(PJ, 9, 700, REDUP, 2), a) + dv(font(PJ, 11, 400, INK, None, 1.4)
                                                            + 'margin-top:5px;', b))
                  for a, b in (('CMYK & PANTONE', 'Nilai cetak dikunci setelah uji cetak pertama.'),
                               ('KONTRAS', 'Teks di atas teal wajib krem, bukan mint.'),
                               ('PERBANDINGAN', 'Teal 60% · krem 30% · emas dan terakota 10%.')))))
simpan(15, 'Palet warna', s)

# ---------------------------------------------------------------- 16 tipografi
s = (kepala('Bab III · Elemen Visual', 16)
     + judul_bagian('2', 'Tipografi')
     + kotak(M, 168, 340, 330,
             dv(P(x=24, y=16, lain=font(AR, 124, 700, TEAL, -4, 1)), 'Aa')
             + dv(P(x=24, y=180, lain=font(AR, 22, 700, INK, -.4)), 'Archivo')
             + dv(P(x=24, y=208, lain=font(PJ, 11, 400, REDUP, None, 1.45) + 'width:280px;'),
                  'Judul, angka besar, wordmark. Tebal 700. Spasi huruf rapat pada ukuran besar.')
             + dv(P(x=24, y=270, lain=font(AR, 15, 400, INK)), 'AaBbCc 0123456789'), PUTIH, 18)
     + kotak(412, 168, 380, 158,
             dv(P(x=22, y=18, lain=font(PJ, 44, 600, INK, -1)), 'Aa')
             + dv(P(x=110, y=30, lain=font(AR, 18, 700, INK, -.3)), 'Plus Jakarta Sans')
             + dv(P(x=110, y=54, w=250, lain=font(PJ, 11, 400, REDUP, None, 1.45)),
                  'Teks isi, label, antarmuka. Tebal 400–700.'), PUTIH, 18)
     + kotak(412, 340, 380, 158,
             dv(P(x=22, y=24, lain='font-family:' + CV + ';font-size:44px;font-weight:600;color:'
                  + EMAS + ';'), 'Aa')
             + dv(P(x=110, y=30, lain=font(AR, 18, 700, INK, -.3)), 'Caveat')
             + dv(P(x=110, y=54, w=250, lain=font(PJ, 11, 400, REDUP, None, 1.45)),
                  'Hanya untuk satu kalimat tulisan tangan. Tidak untuk teks isi.'), PUTIH, 18))
simpan(16, 'Tipografi', s)

# ---------------------------------------------------------------- 17 sudut enam
s = (kepala('Bab III · Elemen Visual', 17)
     + judul_bagian('3', 'Sudut Enam', 'Bahasa bentuk Balikin: kisi 60°, sudut dipangkas bukan '
                    'dibulatkan, sambungan mitre.')
     + kotak(M, 196, 364, 300,
             '<svg width="364" height="300" viewBox="0 0 364 300" style="display:block">'
             + ''.join('<path d="M' + str(20 + i * 36) + ' 20L' + str(56 + i * 36) + ' 280" '
                       'stroke="' + TEAL + '" stroke-width="1" opacity=".2"/>' for i in range(9))
             + ''.join('<path d="M' + str(344 - i * 36) + ' 20L' + str(308 - i * 36) + ' 280" '
                       'stroke="' + TEAL + '" stroke-width="1" opacity=".2"/>' for i in range(9))
             + '<path d="M74 96H182L218 158L182 220H74L38 158Z" fill="' + MINT_M + '" stroke="'
             + TEAL + '" stroke-width="5" stroke-linejoin="miter"/>'
             '<path d="M250 96H326V220H250Z" fill="none" stroke="' + TERRA + '" stroke-width="4" '
             'stroke-dasharray="8 7"/>'
             '<path d="M262 96H326V208L314 220H250V108Z" fill="' + CREAM + '" stroke="' + TERRA
             + '" stroke-width="5" stroke-linejoin="miter"/>'
             '<text x="288" y="254" font-family="' + PJ + '" font-size="11" font-weight="700" '
             'fill="' + TERRA + '" text-anchor="middle">SUDUT DIPANGKAS</text>'
             '<text x="128" y="254" font-family="' + PJ + '" font-size="11" font-weight="700" '
             'fill="' + TEAL + '" text-anchor="middle">KISI 60°</text></svg>', PUTIH, 18)
     + dv(P(x=452, y=200, w=340, z=6),
          catatan(0, 0, 340, 'Pangkas, jangan bulatkan', 'Radius membulat tidak dipakai di grafis '
                  'identitas. Antarmuka aplikasi boleh membulat — dua bahasa yang berbeda tugas.')
          + catatan(0, 108, 340, 'Sambungan mitre', 'Semua sudut garis bertemu tajam. '
                    'stroke-linejoin: miter, bukan round.')
          + catatan(0, 200, 340, 'Besar pangkasan', 'Seperenam sisi terpendek, dibulatkan ke '
                    'bilangan bulat.')))
simpan(17, 'Sudut Enam', s)

# ---------------------------------------------------------------- 18 pustaka ikon
IK6 = ['cari', 'wallet', 'kunci', 'ponsel', 'dokumen', 'kartu', 'peta', 'lonceng', 'gembok',
       'obrolan', 'warga', 'bintang', 'perisai', 'jam', 'check', 'tambah', 'panah', 'grid']
kis = ''
for i, n in enumerate(IK6):
    x, y = M + (i % 9) * 82, 206 + (i // 9) * 86
    kis += kotak(x, y, 70, 70, dv(P(x=0, y=0, w=70, h=70, lain='display:grid;place-items:center;'),
                                  ik(n, 34, TEAL)), PUTIH, 12, lain='border:1px solid ' + GARIS + ';')
s = (kepala('Bab III · Elemen Visual', 18)
     + judul_bagian('4', 'Pustaka ikon')
     + dv(P(r=M, y=86, z=6, lain='display:flex;gap:10px;'),
          ''.join(dv('background:' + PUTIH + ';border:1px solid ' + GARIS + ';border-radius:12px;'
                     'padding:8px 14px;text-align:center;',
                     dv(font(AR, 22, 700, TEAL, -1), a) + dv(font(PJ, 9, 700, REDUP, 1.5)
                                                             + 'margin-top:2px;', b))
                  for a, b in (('98', 'BENTUK'), ('2', 'VARIAN'), ('196', 'KOMPONEN'))))
     + kis
     + dv(P(x=M, y=396, w=W - M * 2, z=6, lain='display:flex;gap:14px;'),
          ''.join(dv('flex:1;background:' + PUTIH + ';border-radius:12px;padding:12px 14px;'
                     'box-sizing:border-box;border:1px solid ' + GARIS + ';',
                     dv(font(PJ, 9, 700, REDUP, 2), a) + dv(font(PJ, 11, 400, INK, None, 1.4)
                                                            + 'margin-top:5px;', b))
                  for a, b in (('KOTAK', 'Semua ikon digambar di kotak 100 × 100.'),
                               ('TEBAL GARIS', '6–7 satuan. Tidak menipis waktu diperkecil.'),
                               ('VARIAN', 'Garis untuk keadaan biasa, padat untuk aktif.'))))
     + label(M, 500, 'Placeholder — 18 dari 98 bentuk. Lembar lengkap ada di lampiran.'))
simpan(18, 'Pustaka ikon', s)

# ---------------------------------------------------------------- 19 pola sarang
s = (kepala('Bab III · Elemen Visual', 19)
     + judul_bagian('5', 'Pola sarang', 'Pola latar resmi. Selalu transparan di atas bidang warna, '
                    'tidak pernah jadi warna sendiri.')
     + kotak(M, 200, 230, 290, sarang(TEAL, '.18', 1)
             + dv(P(x=0, b=12, w=230, lain=font(PJ, 9, 700, REDUP, 2, None, 'center')), 'RAPAT · 26 MM'),
             PUTIH, 16, lain='border:1px solid ' + GARIS + ';')
     + kotak(M + 246, 200, 230, 290, sarang(TEAL, '.14', 2)
             + dv(P(x=0, b=12, w=230, lain=font(PJ, 9, 700, REDUP, 2, None, 'center')), 'SEDANG · 52 MM'),
             PUTIH, 16, lain='border:1px solid ' + GARIS + ';')
     + kotak(M + 492, 200, 252, 290,
             dv(P(x=0, y=0, w=252, h=290, lain='background:' + TEAL_X + ';'), sarang(CREAM, '.16', 3))
             + dv(P(x=0, b=12, w=252, lain=font(PJ, 9, 700, 'rgba(251,248,243,.7)', 2, None, 'center')),
                  'LONGGAR DI LATAR GELAP'), PUTIH, 16)
     + label(M, 512, 'Opasitas 8–16% di latar gelap, 4–8% di latar terang. Jangan lebih pekat.'))
simpan(19, 'Pola sarang', s)

# ---------------------------------------------------------------- 20 maskot
from build import LEBAH
def bee(px, rot=0):
    return ('<svg width="' + str(px) + '" height="' + str(px) + '" viewBox="0 0 200 200" '
            'style="display:block;transform:rotate(' + str(rot) + 'deg)">' + LEBAH + '</svg>')
s = (kepala('Bab III · Elemen Visual', 20)
     + judul_bagian('6', 'Maskot — Lebah Sarang')
     + kotak(M, 168, 330, 330, dv(P(x=0, y=0, w=330, h=330, lain='display:grid;place-items:center;'),
                                  bee(230)), PUTIH, 18)
     + dv(P(x=412, y=176, w=380, z=6),
          catatan(0, 0, 380, 'Kapan dipakai', 'Materi yang ramah: stiker, standee, x-banner, '
                  'kartu ucapan. Tidak dipakai di dalam antarmuka aplikasi.')
          + catatan(0, 96, 380, 'Ukuran minimum', '20 mm cetak. Di bawah itu sayapnya hilang.')
          + catatan(0, 172, 380, 'Larangan', 'Jangan diubah warnanya, jangan diberi mulut lain, '
                    'jangan dipakai sebagai logo.'))
     + dv(P(x=412, y=372, w=380, z=6, lain='display:flex;gap:12px;'),
          ''.join(dv('flex:1;background:' + PUTIH + ';border-radius:14px;height:126px;'
                     'display:grid;place-items:center;border:1px solid ' + GARIS + ';', bee(76, r))
                  for r in (-12, 0, 12)))
     + label(412, 512, 'Tiga pose baku — placeholder, pose tambahan menyusul'))
simpan(20, 'Maskot', s)

# ---------------------------------------------------------------- 21 tulisan tangan
s = (kepala('Bab III · Elemen Visual', 21)
     + judul_bagian('7', 'Elemen tulisan tangan')
     + kotak(M, 172, W - M * 2, 208,
             dv(P(x=0, y=40, w=W - M * 2, lain='font-family:' + CV + ';font-size:56px;font-weight:600;'
                  'color:' + TEAL_X + ';text-align:center;line-height:1.1;'),
                'Small things make a big difference')
             + '<svg width="' + str(W - M * 2) + '" height="46" viewBox="0 0 744 46" '
             'style="position:absolute;left:0;top:142px"><path d="M180 24Q372 46 564 20" stroke="'
             + EMAS + '" stroke-width="6" fill="none" stroke-linecap="round"/></svg>', PUTIH, 18)
     + dv(P(x=M, y=406, w=W - M * 2, z=6, lain='display:flex;gap:14px;'),
          ''.join(dv('flex:1;background:' + PUTIH + ';border-radius:12px;padding:14px 16px;'
                     'box-sizing:border-box;border:1px solid ' + GARIS + ';',
                     dv(font(PJ, 9, 700, REDUP, 2), a) + dv(font(PJ, 11, 400, INK, None, 1.45)
                                                            + 'margin-top:6px;', b))
                  for a, b in (('SATU PER MATERI', 'Cukup sekali di tiap lembar. Dua kali jadi ramai.'),
                               ('SELALU MIRING', 'Putaran −6° sampai −3°. Tidak pernah lurus.'),
                               ('WARNA', 'Teal tua, emas, atau krem. Tidak pernah terakota.')))))
simpan(21, 'Tulisan tangan', s)

# ---------------------------------------------------------------- 22 pembatas IV
s, bg = pembatas(22, 'IV', 'Penerapan', 'Bagaimana semuanya bertemu di layar, di cetakan, '
                 'dan di meja pameran.',
                 [('23', 'Layar dan cetak'), ('24', 'Merchandise & booth')], '#D2713F', '#A2421D')
simpan(22, 'Pembatas Bab IV', s, bg)

# ---------------------------------------------------------------- 23 layar & cetak
s = (kepala('Bab IV · Penerapan', 23)
     + judul_bagian('1', 'Layar dan cetak')
     + kotak(M, 160, 330, 336, dv(P(x=0, y=0, w=330, h=336, lain='background:linear-gradient(160deg,'
                                    + MINT_M + ' 0%,' + CREAM + ' 100%);'))
             + ponsel(54, 46, 104, 8, rot=-5) + ponsel(178, 82, 104, 7, rot=6)
             + dv(P(x=0, b=12, w=330, z=9, lain=font(PJ, 9, 700, REDUP, 2, None, 'center')),
                  'APLIKASI — PLACEHOLDER'), PUTIH, 18)
     + kotak(412, 160, 180, 336,
             dv(P(x=24, y=30, w=132, h=246, lain='background:' + TEAL + ';border-radius:6px;'))
             + dv(P(x=24, y=30, w=132, h=246, lain='overflow:hidden;border-radius:6px;'), sarang(CREAM, '.14', 1))
             + dv(P(x=0, b=12, w=180, lain=font(PJ, 9, 700, REDUP, 2, None, 'center')), 'X-BANNER'),
             PUTIH, 18)
     + kotak(612, 160, 180, 336,
             dv(P(x=30, y=40, w=120, h=170, lain='background:' + CREAM + ';border:1px solid ' + GARIS
                  + ';border-radius:4px;'))
             + dv(P(x=44, y=60, w=92, h=54, lain='background:' + TERRA + ';border-radius:3px;'))
             + dv(P(x=44, y=124, w=92, h=8, lain='background:' + GARIS + ';'))
             + dv(P(x=44, y=140, w=64, h=8, lain='background:' + GARIS + ';'))
             + dv(P(x=30, y=226, w=120, h=60, lain='background:' + TEAL_X + ';border-radius:4px;'))
             + dv(P(x=0, b=12, w=180, lain=font(PJ, 9, 700, REDUP, 2, None, 'center')), 'POSTER & KARTU'),
             PUTIH, 18)
     + label(M, 516, 'Semua mockup di halaman ini placeholder — diganti foto cetakan asli'))
simpan(23, 'Layar dan cetak', s)

# ---------------------------------------------------------------- 24 merchandise & booth
s = (kepala('Bab IV · Penerapan', 24)
     + judul_bagian('2', 'Merchandise & booth')
     + kotak(M, 160, 372, 336,
             ''.join(dv(P(x=30 + (i % 3) * 108, y=40 + (i // 3) * 130, w=88, h=100,
                          lain='background:' + c + ';' + (HEKS if i % 2 == 0 else '')
                               + ('border-radius:14px;' if i % 2 else '')))
                     for i, c in enumerate([MINT, EMAS_M, TERRA, TEAL, CREAM, EMAS]))
             + dv(P(x=0, b=12, w=372, lain=font(PJ, 9, 700, REDUP, 2, None, 'center')),
                  'GANTUNGAN KUNCI · STIKER · KARTU'), PUTIH, 18)
     + kotak(452, 160, 340, 336,
             dv(P(x=28, y=40, w=284, h=180, lain='background:' + FILL + ';border-radius:10px;'))
             + dv(P(x=44, y=56, w=90, h=120, lain='background:' + TEAL + ';border-radius:6px;'))
             + dv(P(x=148, y=56, w=146, h=54, lain='background:' + CREAM + ';border:1px solid '
                    + GARIS + ';border-radius:6px;'))
             + dv(P(x=148, y=122, w=68, h=54, lain='background:' + EMAS_M + ';border-radius:6px;'))
             + dv(P(x=228, y=122, w=66, h=54, lain='background:' + TERRA + ';border-radius:6px;'))
             + dv(P(x=28, y=240, w=284, lain=font(PJ, 11, 400, REDUP, None, 1.45)),
                  'Denah meja: x-banner di belakang, kotak barang temuan di tengah, standee QR '
                  'dan kartu di depan.')
             + dv(P(x=0, b=12, w=340, lain=font(PJ, 9, 700, REDUP, 2, None, 'center')), 'DENAH BOOTH'),
             PUTIH, 18))
simpan(24, 'Merchandise & booth', s)

# ---------------------------------------------------------------- kanvas
papan, anot = [], []
for i, (berkas, judul) in enumerate(HAL):
    papan.append({"file": berkas, "x": (i % 6) * 900, "y": (i // 6) * 700,
                  "w": W, "h": H, "title": judul})
kanvas = {"artboards": papan,
  "annotations": [{"id": "catatan", "x": 0, "y": -160, "w": 1000,
    "text": "Buku GSM Balikin — 24 halaman A5 lanskap 210 × 148 mm (840 × 592 px, 4 satuan = 1 mm).\n"
            "Tata letak dan hierarki sudah dikunci; isi teks, tangkapan layar, dan foto cetakan "
            "masih placeholder.\nUrut membaca dari kiri ke kanan, enam halaman per baris."}],
  "launch": {"view": "canvas"}}
open(os.path.join(DIR, 'canvas.json'), 'w', encoding='utf-8').write(
    json.dumps(kanvas, indent=2, ensure_ascii=False))
print('%d halaman + canvas.json' % len(HAL))
