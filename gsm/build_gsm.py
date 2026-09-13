# -*- coding: utf-8 -*-
"""Buku GSM Balikin — 24 halaman A5 lanskap.

Register editorial: tipografi besar bercampur, ruang kosong murah hati, blok
warna penuh halaman, kartu bersudut membulat. Isi teks sudah benar; tangkapan
layar dan foto cetakan masih placeholder.
"""
import os, json
from kit_gsm import *

HAL = []                                   # (berkas, judul kanvas)
BAB_W = [TEAL, TEAL_G, EMAS, TERRA]        # warna aksen tiap bab

def simpan(nomor, nama, isi, latar=KRIM):
    berkas = ('Main' if nomor == 1 else 'H%02d' % nomor) + '.dc.html'
    tulis(berkas, halaman(isi, latar), latar)
    HAL.append((berkas, '%02d · %s' % (nomor, nama)))

def latar_bab(i, sisi='kanan'):
    """Supergrafis halus di sudut halaman — bidang tint, bukan garis yang memotong isi."""
    c = BAB_W[i]
    if sisi == 'kanan':
        return heks(r=-268, b=-232, d=520, warna=c, tebal=0, op='.05', z=1)
    return heks(x=-268, b=-232, d=520, warna=c, tebal=0, op='.05', z=1)

def bagian(no, baris, ringkas='', x=M, y=104, w=400, uk=46, warna=INK, redup=REDUP, th='.95'):
    s = mata(x, y, 'Bagian ' + no, redup) if no else ''
    yy = y + (26 if no else 0)
    s += tajuk(x, yy, w, baris, uk, warna, -2, th)
    yy += int(uk * float(th)) * len(baris) + 18
    if ringkas:
        s += teks(x, yy, w, ringkas, 12, redup, 400, '1.6')
    return s

def catatan(x, y, w, isi, jarak=92):
    return ''.join(kartu_teks(x, y + i * jarak, w, a, b) for i, (a, b) in enumerate(isi))

def kartu_aturan(x, y, w, h, atas, isi, bg=PUTIH, tepi=GARIS, fg=REDUP):
    return blok(x, y, w, h, dv(P(x=18, y=16, w=w - 36, lain=font(PJ, 9, 700, fg, 2)), atas.upper())
                + dv(P(x=18, y=38, w=w - 36, lain=font(PJ, 11, 400, INK, None, '1.5')), isi),
                bg, 16, 6, tepi)

# ================================================================ 01 sampul
s = (dv(P(x=0, y=0, w=W, h=H, z=1, lain='overflow:hidden;'), sarang(KRIM, '.07', 3))
     + heks(r=-200, y=-96, d=470, warna=MINT, tebal=2, op='.34', z=2)
     + heks(r=-56, b=-160, d=310, warna=MINT, tebal=2, op='.22', z=2)
     + heks(x=-104, b=-186, d=280, warna=EMAS_M, tebal=0, op='.13', z=2)
     + dv(P(x=M, y=44, z=8), lambang(38, KRIM, EMAS_M))
     + mata(None, 50, 'Graphic Standard Manual', rgba(MINT_M, '.85'), r=M, rt='right')
     + mata(None, 68, 'Edisi 01 · 2026', rgba(MINT_M, '.5'), r=M, rt='right')
     + mata(M, 192, 'Identitas Visual Aplikasi', rgba(MINT_M, '.7'))
     + tajuk(M, 214, 728, [[('BALIKIN', '')]], 150, KRIM, -7, '1', z=8)
     + garis(M, 386, 728, rgba(MINT_M, '.28'), z=8)
     + tajuk(M, 406, 700, [[('Yang hilang, ', ''), ('balik pulang.', 'c')]], 34, KRIM, -1, '1.1')
     + teks(M, 458, 380, 'Panduan baku pemakaian logo, warna, huruf, ikon, dan penerapan '
            'identitas Balikin.', 12, rgba(MINT_M, '.72'))
     + garis(M, 516, 728, rgba(MINT_M, '.2'), z=8)
     + teks(None, None, 320, 'Uldan Pamungkas &middot; 20210060127<br>'
            'Desain Komunikasi Visual &middot; Universitas Nusa Putra Sukabumi',
            11, rgba(MINT_M, '.62'), 500, '1.55', r=M, b=42, rt='right')
     + mata(M, None, '24 halaman · A5 lanskap', rgba(MINT_M, '.5'), b=48))
simpan(1, 'Sampul', s, 'linear-gradient(150deg,' + TEAL_G + ' 0%,' + TEAL_X + ' 100%)')

# ================================================================ 02 daftar isi
BAB = [('I', 'Tentang Balikin', '03', '05', TEAL,
        'Produk, pengguna, tagline, dan kepribadian.'),
       ('II', 'Identitas Utama', '06', '13', TEAL_G,
        'Logogram, konstruksi, ruang aman, ukuran, konfigurasi, warna, larangan.'),
       ('III', 'Elemen Visual', '14', '21', EMAS,
        'Palet, huruf, Sudut Enam, ikon, pola, maskot, tulisan tangan.'),
       ('IV', 'Penerapan', '22', '24', TERRA,
        'Layar, cetak, merchandise, dan meja pameran.')]
baris = ''
for i, (a, t, h1, h2, c, ket) in enumerate(BAB):
    baris += (dv(P(x=0, y=i * 106, w=436, h=1, lain='background:' + GARIS + ';'))
              + dv(P(x=0, y=i * 106 + 22, lain=font(AR, 30, 700, c, -1, 1)), a)
              + dv(P(x=64, y=i * 106 + 20, lain=font(AR, 22, 700, INK, -.5)), t)
              + dv(P(x=64, y=i * 106 + 50, w=300, lain=font(PJ, 11, 400, REDUP, None, '1.5')), ket)
              + dv(P(r=0, y=i * 106 + 24, lain=font(PJ, 11, 700, REDUP, 1)), h1 + '–' + h2))
s = (latar_bab(0)
     + mata(M, 44, 'Balikin · Graphic Standard Manual')
     + dv(P(r=M, y=38, z=8, lain=font(AR, 15, 700, REDUP)), '02')
     + garis(M, 72, KOL)
     + tajuk(M, 118, 280, [[('Daftar', '')], [('Isi', 'm')]], 58, INK, -2, '.94')
     + teks(M, 260, 250, 'Manual ini mengunci cara memakai identitas Balikin — apa yang boleh, '
            'apa yang tidak, dan kenapa.', 12, REDUP)
     + dv(P(x=348, y=104, w=436, z=8), baris)
     + dv(P(x=348, y=528, w=436, h=1, z=8, lain='background:' + GARIS + ';'))
     + dv(P(x=M, b=52, z=8), lambang(30, TEAL, EMAS))
     + mata(M + 44, None, '24 halaman · A5 lanskap 210 × 148 mm', REDUP, b=60))
simpan(2, 'Daftar Isi', s)

# ================================================================ pembatas bab
def pembatas(nomor, angka_, judul_, ringkas, daftar, c1, c2, aksen=EMAS_M):
    rows = ''
    for i, (h, t) in enumerate(daftar):
        rows += (dv(P(x=0, y=i * 42, w=300, h=1, lain='background:' + rgba(KRIM, '.22') + ';'))
                 + dv(P(x=0, y=i * 42 + 13, lain=font(PJ, 11, 700, aksen, 1)), h)
                 + dv(P(x=42, y=i * 42 + 12, lain=font(PJ, 12, 500, KRIM)), t))
    n = len(daftar)
    isi = (dv(P(x=0, y=0, w=W, h=H, z=1, lain='overflow:hidden;'), sarang(KRIM, '.08', 3))
           + heks(r=-180, y=-120, d=420, warna=KRIM, tebal=2, op='.2', z=2)
           + heks(x=-120, b=-160, d=300, warna=KRIM, tebal=2, op='.14', z=2)
           + angka(M - 8, None, angka_, 300, KRIM, '.13', 2, b=-64, sp=-10)
           + dv(P(x=M, y=44, z=8), lambang(34, KRIM, aksen))
           + mata(None, 50, 'Bab ' + angka_, rgba(KRIM, '.6'), r=M, rt='right')
           + mata(M, 168, 'Bab ' + angka_, aksen)
           + tajuk(M, 192, 360, judul_, 60, KRIM, -2, '.94')
           + teks(M, 192 + 56 * len(judul_) + 20, 320, ringkas, 12, rgba(KRIM, '.72'))
           + dv(P(r=M, y=300 - n * 21, w=300, z=8), rows)
           + dv(P(r=M, y=300 - n * 21 + n * 42, w=300, h=1, z=8,
                  lain='background:' + rgba(KRIM, '.22') + ';'))
           + mata(None, None, 'Balikin · Graphic Standard Manual', rgba(KRIM, '.45'),
                  r=M, b=54, rt='right'))
    return isi, 'linear-gradient(145deg,' + c1 + ' 0%,' + c2 + ' 100%)'

s, bg = pembatas(3, 'I', [[('Tentang', '')], [('Balikin', 'm')]],
                 'Apa itu Balikin, untuk siapa dibuat, dan bagaimana ia ingin terdengar.',
                 [('04', 'Produk dan pengguna'), ('05', 'Tagline & kepribadian')], TEAL_T, TEAL_G)
simpan(3, 'Pembatas Bab I', s, bg)

# ================================================================ 04 produk & pengguna
fitur = ''
for i, (n, a, b) in enumerate((('cari', 'Melapor kehilangan', 'Empat langkah, dua menit.'),
                               ('bag', 'Melapor temuan', 'Foto, kategori, titik lokasi.'),
                               ('bintang', 'Reputasi komunitas', 'Poin dan lencana, bukan uang.'))):
    y = i * 76
    fitur += (dv(P(x=0, y=y, w=38, h=42, z=7, lain='background:' + MINT_M + ';' + HEKS
                   + 'display:grid;place-items:center;'), ik(n, 18, TEAL))
              + dv(P(x=56, y=y + 4, lain=font(AR, 15, 700, INK, -.2)), a)
              + dv(P(x=56, y=y + 26, w=260, lain=font(PJ, 11, 400, REDUP, None, '1.5')), b))
s = (latar_bab(0)
     + bingkai('Bab I · Tentang Balikin', 4)
     + bagian('01', [[('Produk', '')], [('dan pengguna', 'm')]],
              'Aplikasi lost and found untuk warga Sukabumi. Penemu melapor, pemilik mencari, '
              'keduanya bertemu di titik aman yang disepakati.', w=340)
     + dv(P(x=M, y=316, w=340, z=8), fitur)
     + gambar(444, 104, 340, 424, 'Placeholder — ganti tangkapan layar asli',
              ponsel(38, 52, 118, layar_app(118 - 12, 118 * 61 // 30 - 12, TEAL), -5)
              + ponsel(180, 116, 118, layar_app(118 - 12, 118 * 61 // 30 - 12, TEAL_G), 6)))
simpan(4, 'Produk dan pengguna', s)

# ================================================================ 05 tagline
sifat = ''
for i, (t, k) in enumerate((('Hangat', 'bukan formal'), ('Jelas', 'bukan pintar'),
                            ('Rendah hati', 'bukan pamer'), ('Tenang', 'bukan heboh'))):
    sifat += blok(i * 186, 0, 170, 116,
                  dv(P(x=18, y=22, lain=font(AR, 19, 700, TEAL, -.4)), t)
                  + dv(P(x=18, y=52, lain=font(PJ, 11, 400, REDUP)), k)
                  + dv(P(x=18, b=18, w=24, h=2, lain='background:' + EMAS_M + ';')),
                  PUTIH, 18, 6, GARIS)
s = (latar_bab(0, 'kiri')
     + bingkai('Bab I · Tentang Balikin', 5)
     + mata(M, 104, 'Bagian 02 · Tagline & kepribadian')
     + blok(M, 130, KOL, 216,
            tengah(KOL, 216,
                   tajuk(None, None, 660, [[('Yang hilang, ', ''), ('balik pulang.', 'c')]],
                         62, INK, -2, '1.05', rt='center'))
            + dv(P(x=0, y=0, w=KOL, h=216, z=1, lain='overflow:hidden;'), sarang(TEAL, '.07', 3, w=KOL, h=216)),
            MINT_M, 28, 4)
     + teks(M, 362, KOL, 'Kalimat penutup di tiap materi. Selalu diakhiri titik, tidak pernah '
            'diterjemahkan, tidak pernah dipotong.', 12, REDUP, 400, '1.6', rt='center')
     + dv(P(x=M, y=412, w=KOL, z=8), sifat)
     + garis(M, H - 78, KOL)
     + mata(M, None, 'Kepribadian merek', REDUP, b=44)
     + tangan(None, None, 'Small things make a big difference', TEAL, 26, -2, 9, r=M, b=38))
simpan(5, 'Tagline & kepribadian', s)

# ================================================================ 06 pembatas II
s, bg = pembatas(6, 'II', [[('Identitas', '')], [('Utama', 'm')]],
                 'Logogram dan seluruh aturan yang menjaganya tetap dikenali.',
                 [('07', 'Logogram'), ('08', 'Konstruksi'), ('09', 'Ruang aman'),
                  ('10', 'Ukuran minimum'), ('11', 'Konfigurasi'), ('12', 'Warna logo'),
                  ('13', 'Larangan')], TEAL, TEAL_X)
simpan(6, 'Pembatas Bab II', s, bg)

# ================================================================ 07 logogram
gag = ''
for i, (n, a, b) in enumerate((('warga', 'Sel sarang', 'Satu warga, satu sel. Komunitas dibangun '
                                'dari orang yang mau repot sedikit.'),
                               ('coin', 'Sel emas di tengah', 'Barang yang kembali. Selalu emas, '
                                'tidak pernah warna lain.'),
                               ('perisai', 'Heksagon terbuka', 'Bergaris, bukan padat — '
                                'komunitas yang masih bisa dimasuki.'))):
    x = i * 252
    gag += (dv(P(x=x, y=0, w=36, h=40, z=7, lain='background:' + EMAS_M + ';' + HEKS
                 + 'display:grid;place-items:center;'), ik(n, 19, TEAL_X))
            + dv(P(x=x, y=54, lain=font(AR, 15, 700, INK, -.2)), a)
            + dv(P(x=x, y=76, w=210, lain=font(PJ, 11, 400, REDUP, None, '1.5')), b))
s = (latar_bab(1)
     + bingkai('Bab II · Identitas Utama', 7)
     + bagian('01', [[('Logogram', '')]],
              'Satu bentuk, dibaca dua arah: sarang yang menampung, dan barang yang kembali ke '
              'tengahnya.', w=320)
     + blok(M, 282, 340, 106,
            dv(P(x=22, y=22, w=296, lain=font(PJ, 11, 400, INK, None, '1.55')),
               'Logogram tidak pernah dipakai tanpa ruang aman. Aturannya di halaman 09.'),
            MINT_M, 20, 4)
     + blok(432, 96, 352, 296, tengah(352, 296, lambang(148, TEAL, EMAS)), PUTIH, 26, 4, GARIS)
     + mata(432, 348, 'Logogram utama', REDUP, z=9, w=352, rt='center')
     + garis(M, 416, KOL)
     + mata(M, 432, 'Lambang ini menggabungkan tiga gagasan', INK)
     + dv(P(x=M, y=462, w=KOL, z=8), gag))
simpan(7, 'Logogram', s)

# ================================================================ 08 konstruksi
kisi = ''.join('<path d="M' + str(46 + i * 30) + ' 0V330" stroke="' + TEAL + '" stroke-width="1" '
               'opacity=".16"/>' for i in range(11))
kisi += ''.join('<path d="M0 ' + str(24 + i * 30) + 'H384" stroke="' + TEAL + '" stroke-width="1" '
                'opacity=".16"/>' for i in range(10))
s = (latar_bab(1, 'kiri')
     + bingkai('Bab II · Identitas Utama', 8)
     + bagian('02', [[('Konstruksi', '')]],
              'Semua ukuran diturunkan dari satu satuan X — setengah lebar heksagon. '
              'Tidak ada angka yang dikarang.', w=300)
     + blok(400, 96, 384, 400,
            '<svg width="384" height="400" viewBox="0 0 384 400" style="display:block">'
            + '<g transform="translate(0 10)">' + kisi + '</g>'
            + '<path d="M192 60L286 115V225L192 280L98 225V115Z" fill="none" stroke="' + TEAL
            + '" stroke-width="9" stroke-linejoin="miter"/>'
            '<path d="M218 148L205 170H179L166 148L179 126H205Z" fill="' + EMAS + '"/>'
            '<path d="M98 316H286" stroke="' + TERRA + '" stroke-width="2"/>'
            '<path d="M98 308V324M286 308V324" stroke="' + TERRA + '" stroke-width="2"/>'
            '<text x="192" y="346" font-family="' + PJ + '" font-size="11" font-weight="700" '
            'fill="' + TERRA + '" text-anchor="middle">2X</text>'
            '<path d="M62 115V225" stroke="' + TERRA + '" stroke-width="2"/>'
            '<path d="M54 115H70M54 225H70" stroke="' + TERRA + '" stroke-width="2"/>'
            '<text x="40" y="176" font-family="' + PJ + '" font-size="11" font-weight="700" '
            'fill="' + TERRA + '" text-anchor="middle">2X</text></svg>', PUTIH, 26, 4, GARIS)
     + catatan(M, 286, 300, (('Satuan X', 'Setengah lebar heksagon. Semua jarak kelipatan X.'),
                             ('Sudut 60°', 'Kisi isometrik. Tidak ada sudut lain di dalam logo.'),
                             ('Tebal garis', 'X ÷ 6. Ikut mengecil kalau logonya mengecil.')), 76)
     + garis(M, H - 78, 300)
     + mata(M, None, 'Jangan menggambar ulang — pakai berkas vektor', TERRA, b=44))
simpan(8, 'Konstruksi', s)

# ================================================================ 09 ruang aman
s = (latar_bab(1)
     + bingkai('Bab II · Identitas Utama', 9)
     + bagian('03', [[('Ruang ', ''), ('aman', 'm')]],
              'Tidak ada apa pun di dalam kotak putus-putus: teks, gambar, tepi kertas, '
              'atau logo lain.', x=472, w=312)
     + blok(M, 96, 384, 400,
            dv(P(x=52, y=46, w=280, h=298, lain='border:2px dashed ' + TERRA + ';'))
            + dv(P(x=122, y=116, lain='display:grid;place-items:center;'), lambang(140, TEAL, EMAS))
            + ''.join(dv(P(x=x, y=y, lain=font(PJ, 11, 700, TERRA, 1)), 'X')
                      for x, y in ((82, 70), (82, 296), (290, 70), (290, 296)))
            + ''.join(dv(P(x=x, y=y, w=w, h=h, lain='background:' + TERRA_M + ';opacity:.5;'))
                      for x, y, w, h in ((122, 46, 140, 70), (122, 273, 140, 71),
                                         (52, 116, 70, 157), (262, 116, 70, 157)))
            + dv(P(x=0, y=0, w=384, h=400, z=1, lain='overflow:hidden;'), halftone(TEAL, '.06', 9, 1, 384, 400))
            + mata(0, None, 'Ruang aman = 1X di semua sisi', TERRA, z=9, uk=9, sp=2, w=384,
                   rt='center', b=28), PUTIH, 26, 4, GARIS)
     + catatan(472, 282, 312,
               (('Satu X di semua sisi', 'Kalau logonya membesar, ruang amannya ikut membesar. '
                 'Perbandingan tidak pernah berubah.'),
                ('Di atas foto', 'Pakai bidang warna solid di belakang logo. Jangan menaruh logo '
                 'langsung di atas foto ramai.')), 112))
simpan(9, 'Ruang aman', s)

# ================================================================ 10 ukuran minimum
uk = ''
for i, (px_, lab, ket) in enumerate(((104, '18 mm', 'Cetak'), (62, '32 px', 'Layar'),
                                     (34, '16 px', 'Favicon'))):
    x = i * 243
    uk += (dv(P(x=x, y=0, w=242, h=136, lain='display:grid;place-items:center;'),
              lambang(px_, TEAL, EMAS))
           + dv(P(x=x, y=150, w=242, lain=font(AR, 20, 700, INK, -.5, None, 'center')), lab)
           + dv(P(x=x, y=178, w=242, lain=font(PJ, 9, 700, REDUP, 2, None, 'center')), ket.upper())
           + (dv(P(x=x - 1, y=14, w=1, h=180, lain='background:' + GARIS + ';')) if i else ''))
s = (latar_bab(1, 'kiri')
     + bingkai('Bab II · Identitas Utama', 10)
     + bagian('04', [[('Ukuran ', ''), ('minimum', 'm')]], x=M, w=340, uk=44)
     + teks(400, 112, 384, 'Di bawah ukuran ini sel emasnya menutup dan heksagonnya jadi '
            'gumpalan. Jangan dipaksakan.', 12, REDUP, 400, '1.6', rt='right')
     + blok(M, 196, KOL, 214, dv(P(x=0, y=16, w=KOL, z=6), uk), PUTIH, 26, 4, GARIS)
     + dv(P(x=M, y=436, w=KOL, z=8), ''.join(
         kartu_aturan(i * 243, 0, 228, 92, a, b, KRIM_2, None)
         for i, (a, b) in enumerate((('CETAK 18 MM', 'Diukur dari lebar heksagon, bukan tinggi.'),
                                     ('LAYAR 32 PX', 'Di bawah ini logogram saja, tanpa wordmark.'),
                                     ('FAVICON 16 PX', 'Versi padat khusus — bukan logo diperkecil.'))))))
simpan(10, 'Ukuran minimum', s)

# ================================================================ 11 konfigurasi
def sel(x, y, w, h, isi, lab, n):
    return blok(x, y, w, h,
                dv(P(x=0, y=0, w=w, h=h - 40, lain='display:grid;place-items:center;'), isi)
                + dv(P(x=18, b=16, lain=font(PJ, 10, 700, REDUP, 1)), lab)
                + dv(P(r=18, b=14, lain=font(AR, 13, 700, MINT, 0)), n), PUTIH, 22, 4, GARIS)
s = (latar_bab(1)
     + bingkai('Bab II · Identitas Utama', 11)
     + bagian('05', [[('Konfigurasi', '')]], w=340, uk=44)
     + sel(M, 166, 356, 176, kunci(44), 'Mendatar — utama', '01')
     + sel(428, 166, 356, 176,
           dv('text-align:center;', lambang(46, TEAL, EMAS) + dv('height:10px;')
              + tk(font(AR, 30, 700, INK, 1), 'BALIKIN')), 'Bertumpuk', '02')
     + sel(M, 358, 356, 176, lambang(60, TEAL, EMAS), 'Logogram saja', '03')
     + sel(428, 358, 356, 176,
           dv('text-align:center;', tk(font(AR, 28, 700, INK, 1), 'BALIKIN')
              + dv('font-family:' + CV + ';font-size:22px;font-weight:600;color:' + TEAL
                   + ';margin-top:2px;', 'Yang hilang, balik pulang.')), 'Dengan tagline', '04'))
simpan(11, 'Konfigurasi', s)

# ================================================================ 12 warna logo
def selw(x, bg, isi, lab, tepi=None):
    return blok(x, 196, 173, 230,
                dv(P(x=0, y=0, w=173, h=176, lain='background:' + bg + ';display:grid;'
                     'place-items:center;'), isi)
                + dv(P(x=16, y=194, lain=font(PJ, 10, 700, INK, .5)), lab), PUTIH, 20, 4,
                tepi or GARIS)
s = (latar_bab(1, 'kiri')
     + bingkai('Bab II · Identitas Utama', 12)
     + bagian('06', [[('Warna ', ''), ('logo', 'm')]], x=M, w=340, uk=44)
     + teks(400, 112, 384, 'Empat versi resmi. Di luar empat ini tidak ada.',
            12, REDUP, 400, '1.6', rt='right')
     + selw(M, KRIM, lambang(64, TEAL, EMAS), 'Utama di krem')
     + selw(M + 185, TEAL_X, lambang(64, KRIM, EMAS_M), 'Di latar gelap')
     + selw(M + 370, KRIM, lambang(64, INK, INK), 'Mono tinta')
     + selw(M + 555, INK, lambang(64, KRIM, KRIM), 'Mono krem')
     + blok(M, 446, KOL, 90,
            dv(P(x=26, y=20, w=KOL - 52, lain=font(PJ, 12, 400, INK, None, '1.6')),
               'Sel emas hanya boleh hilang di versi mono. Di versi berwarna sel emas '
               '<b>wajib ada</b> — itu yang membedakan logo Balikin dari heksagon biasa.'),
            MINT_M, 20, 4))
simpan(12, 'Warna logo', s)

# ================================================================ 13 larangan
LARANG = ['Diregangkan', 'Diputar', 'Diganti warna', 'Diberi bayangan', 'Ditumpuk teks',
          'Ditambah efek']
def salah(i):
    if i == 0: return lambang(46, TEAL, EMAS, rentang=1.45)
    if i == 1: return lambang(46, TEAL, EMAS, 'transform:rotate(22deg);')
    if i == 2: return lambang(46, TERRA, TEAL)
    if i == 3: return (dv(P(x=4, y=5, z=1, lain='opacity:.3;'), lambang(46, INK, INK))
                       + dv(P(x=0, y=0, z=2), lambang(46, TEAL, EMAS)))
    if i == 5: return lambang(46, TEAL, EMAS, 'opacity:.4;')
    return lambang(46, TEAL, EMAS)
kis = ''
for i, t in enumerate(LARANG):
    x, y = M + (i % 3) * 248, 162 + (i // 3) * 176
    kis += blok(x, y, 232, 160,
                dv(P(x=0, y=0, w=232, h=112,
                     lain='display:grid;place-items:center;' if i != 3 else ''),
                   dv(P(x=93, y=34) if i == 3 else '', salah(i)))
                + (dv(P(x=76, y=48, z=8, lain=font(AR, 15, 700, INK, 0)), 'BALIKIN') if i == 4 else '')
                + dv(P(x=18, b=18, lain=font(PJ, 11, 600, TERRA)), t)
                + dv(P(r=16, y=14, w=22, h=22, z=8, lain='background:' + TERRA + ';border-radius:'
                       '12px;display:grid;place-items:center;' + font(PJ, 13, 700, PUTIH)),
                     '&times;'), PUTIH, 18, 4, GARIS)
s = (latar_bab(1)
     + bingkai('Bab II · Identitas Utama', 13)
     + bagian('07', [[('Larangan', '')]], x=M, w=300, uk=44)
     + teks(360, 112, 424, 'Enam hal yang membuat logo berhenti jadi logo Balikin. Kalau ragu, '
            'pakai berkas aslinya tanpa diubah apa pun.', 12, REDUP, 400, '1.6', rt='right')
     + kis)
simpan(13, 'Larangan', s)

# ================================================================ 14 pembatas III
s, bg = pembatas(14, 'III', [[('Elemen', '')], [('Visual', 'm')]],
                 'Warna, huruf, bahasa bentuk, ikon, pola, maskot, dan tulisan tangan.',
                 [('15', 'Palet warna'), ('16', 'Tipografi'), ('17', 'Sudut Enam'),
                  ('18', 'Pustaka ikon'), ('19', 'Pola sarang'), ('20', 'Maskot'),
                  ('21', 'Tulisan tangan')], EMAS, EMAS_X, KRIM)
simpan(14, 'Pembatas Bab III', s, bg)

# ================================================================ 15 palet
PALET = [('Teal', TEAL, '#1B7A63', 'Warna utama', KRIM),
         ('Teal tua', TEAL_X, '#0B4638', 'Latar gelap', KRIM),
         ('Mint', MINT, '#8FD4C4', 'Aksen lembut', INK),
         ('Emas', EMAS, '#C8952E', 'Penghargaan', KRIM),
         ('Terakota', TERRA, '#C05C33', 'Peringatan', KRIM),
         ('Krem', KRIM, '#FBF8F3', 'Latar terang', INK),
         ('Tinta', INK, '#12332C', 'Teks', KRIM)]
sw = ''
for i, (nama, warna, kode, guna, fg) in enumerate(PALET):
    x, y = (i % 4) * 185, (i // 4) * 192
    sw += blok(x, y, 176, 178,
               dv(P(x=18, b=48, lain=font(AR, 18, 700, fg, -.4)), nama)
               + dv(P(x=18, b=28, lain=font(PJ, 10, 700, fg, 1) + 'opacity:.75;'), kode)
               + mata(18, None, guna, fg, z=7, uk=8, sp=2, b=14) .replace('position:absolute;',
                      'position:absolute;opacity:.55;'), warna, 20, 4,
               GARIS if warna == KRIM else None)
sw += blok(3 * 185, 192, 176, 178,
           dv(P(x=18, y=20, lain=font(PJ, 9, 700, REDUP, 2)), 'PERBANDINGAN')
           + dv(P(x=18, y=42, w=140, lain=font(PJ, 11, 400, INK, None, '1.5')),
                'Teal 60% · krem 30% · emas dan terakota 10%.')
           + dv(P(x=18, b=26, w=140, h=10, lain='display:flex;overflow:hidden;border-radius:5px;'),
                dv('flex:6;background:' + TEAL + ';') + dv('flex:3;background:' + KRIM_3 + ';')
                + dv('flex:1;background:' + EMAS + ';')), KRIM_2, 20, 4)
s = (latar_bab(2, 'kiri')
     + bingkai('Bab III · Elemen Visual', 15)
     + bagian('01', [[('Palet ', ''), ('warna', 'm')]], x=M, w=300, uk=44)
     + teks(400, 112, 384, 'Tujuh warna. Teal untuk aksi, emas untuk penghargaan, terakota untuk '
            'peringatan — perannya tidak pernah ditukar.', 12, REDUP, 400, '1.6', rt='right')
     + dv(P(x=M, y=186, w=KOL, z=6), sw))
simpan(15, 'Palet warna', s)

# ================================================================ 16 tipografi
spek = ''
for i, (contoh, gaya, nama, ket, huruf) in enumerate((
        ('Aa', font(AR, 46, 700, INK, -2), 'Archivo', 'Judul, angka besar, wordmark. Tebal 700, '
         'spasi huruf rapat.', 'AaBbCc 0123456789'),
        ('Aa', font(PJ, 44, 600, INK, -1), 'Plus Jakarta Sans', 'Teks isi, label, antarmuka. '
         'Tebal 400–700.', 'AaBbCc 0123456789'),
        ('Aa', 'font-family:' + CV + ';font-size:46px;font-weight:600;color:' + EMAS + ';',
         'Caveat', 'Satu kalimat tulisan tangan saja. Tidak untuk teks isi.', 'Yang hilang'))):
    y = i * 122
    spek += blok(0, y, 340, 112,
                 dv(P(x=20, y=20, lain=gaya), contoh)
                 + dv(P(x=104, y=18, lain=font(AR, 16, 700, INK, -.3)), nama)
                 + dv(P(x=104, y=40, w=216, lain=font(PJ, 10, 400, REDUP, None, '1.45')), ket)
                 + dv(P(x=104, b=12, lain=font(PJ, 10, 500, MINT, .5)), huruf), PUTIH, 20, 4, GARIS)
s = (bingkai('Bab III · Elemen Visual', 16)
     + blok(M, 96, 340, 432,
            dv(P(x=0, y=0, w=340, h=432, z=1, lain='overflow:hidden;'), sarang(KRIM, '.08', 3, w=340, h=432))
            + dv(P(x=28, y=48, z=6, lain=font(AR, 200, 700, KRIM, -10, '.8')), 'Aa')
            + mata(28, None, 'Archivo · 700', rgba(KRIM, '.6'), b=84)
            + dv(P(x=28, b=40, z=6, lain=font(AR, 22, 700, KRIM, -.5)), 'Huruf judul')
            + heks(r=-90, b=-80, d=220, warna=KRIM, tebal=2, op='.2', z=2), TEAL, 26, 4)
     + bagian('02', [[('Tipografi', '')]], x=444, y=96, w=340, uk=44)
     + dv(P(x=444, y=180, w=340, z=6), spek))
simpan(16, 'Tipografi', s)

# ================================================================ 17 sudut enam
s = (latar_bab(2)
     + bingkai('Bab III · Elemen Visual', 17)
     + bagian('03', [[('Sudut ', ''), ('Enam', 'm')]],
              'Bahasa bentuk Balikin: kisi 60°, sudut dipangkas bukan dibulatkan, '
              'sambungan mitre.', x=488, w=296, uk=44)
     + blok(M, 96, 408, 400,
            '<svg width="408" height="400" viewBox="0 0 408 400" style="display:block">'
            + ''.join('<path d="M' + str(-180 + i * 56) + ' 0L' + str(16 + i * 56) + ' 340" '
                      'stroke="' + TEAL + '" stroke-width="1" opacity=".13"/>' for i in range(12))
            + ''.join('<path d="M' + str(588 - i * 56) + ' 0L' + str(392 - i * 56) + ' 340" '
                      'stroke="' + TEAL + '" stroke-width="1" opacity=".13"/>' for i in range(12))
            + '<path d="M108 116H220L264 196L220 276H108L64 196Z" fill="' + MINT_M + '" stroke="'
            + TEAL + '" stroke-width="6" stroke-linejoin="miter"/>'
            '<path d="M288 116H384V276H288Z" fill="none" stroke="' + TERRA + '" stroke-width="2" '
            'stroke-dasharray="7 6"/>'
            '<path d="M314 116H384V250L358 276H288V142Z" fill="' + KRIM + '" stroke="' + TERRA
            + '" stroke-width="6" stroke-linejoin="miter"/>'
            '<text x="336" y="310" font-family="' + PJ + '" font-size="11" font-weight="700" '
            'fill="' + TERRA + '" text-anchor="middle">SUDUT DIPANGKAS</text>'
            '<text x="164" y="310" font-family="' + PJ + '" font-size="11" font-weight="700" '
            'fill="' + TEAL + '" text-anchor="middle">KISI 60°</text></svg>'
            + mata(0, None, 'Bahasa bentuk — Sudut Enam (Hexcut)', REDUP, z=9, uk=9, sp=2, w=408,
                   rt='center', b=30), PUTIH, 26, 4, GARIS)
     + catatan(488, 268, 296,
               (('Pangkas, jangan bulatkan', 'Radius membulat tidak dipakai di grafis identitas. '
                 'Antarmuka aplikasi boleh membulat — dua bahasa, dua tugas.'),
                ('Sambungan mitre', 'Semua sudut garis bertemu tajam, tidak pernah round.'),
                ('Besar pangkasan', 'Seperenam sisi terpendek, dibulatkan ke bilangan bulat.')), 88))
simpan(17, 'Sudut Enam', s)

# ================================================================ 18 pustaka ikon
IK16 = ['cari', 'wallet', 'kunci', 'ponsel', 'dokumen', 'kartu', 'peta', 'pin',
        'lonceng', 'gembok', 'obrolan', 'warga', 'bintang', 'perisai', 'jam', 'check']
kis = ''
for i, n in enumerate(IK16):
    x, y = (i % 8) * 92, (i // 8) * 92
    kis += blok(x, y, 84, 84, tengah(84, 84, ik(n, 34, TEAL)), PUTIH, 16, 4, GARIS)
s = (latar_bab(2, 'kiri')
     + bingkai('Bab III · Elemen Visual', 18)
     + bagian('04', [[('Pustaka ', ''), ('ikon', 'm')]], x=M, w=300, uk=44)
     + dv(P(r=M, y=104, w=314, h=62, z=8),
          ''.join(blok(i * 108, 0, 98, 62,
                       dv(P(x=0, y=12, w=98, lain=font(AR, 22, 700, TEAL, -1, None, 'center')), a)
                       + dv(P(x=0, y=40, w=98, lain=font(PJ, 8, 700, REDUP, 2, None, 'center')), b),
                       PUTIH, 16, 6, GARIS)
                  for i, (a, b) in enumerate((('98', 'BENTUK'), ('2', 'VARIAN'),
                                              ('196', 'KOMPONEN')))))
     + dv(P(x=M, y=204, w=KOL, z=6), kis)
     + dv(P(x=M, y=414, w=KOL, z=8), ''.join(
         kartu_aturan(i * 243, 0, 228, 88, a, b, KRIM_2, None)
         for i, (a, b) in enumerate((('KOTAK', 'Semua ikon digambar di kotak 100 × 100.'),
                                     ('TEBAL GARIS', '6–7 satuan, tidak menipis waktu diperkecil.'),
                                     ('VARIAN', 'Garis untuk biasa, padat untuk keadaan aktif.')))))
     + mata(M, None, '16 dari 98 bentuk — lembar lengkap ada di lampiran', REDUP, b=42))
simpan(18, 'Pustaka ikon', s)

# ================================================================ 19 pola sarang
def ubin(x, bg, warna, op, k, lab, fg=REDUP, tepi=GARIS):
    return blok(x, 180, 232, 268,
                dv(P(x=0, y=0, w=232, h=268, z=1, lain='overflow:hidden;'), sarang(warna, op, k, w=232, h=268))
                + mata(0, None, lab, fg, z=6, uk=8, sp=2, w=232, rt='center', b=18), bg, 22, 4, tepi)
s = (latar_bab(2)
     + bingkai('Bab III · Elemen Visual', 19)
     + bagian('05', [[('Pola ', ''), ('sarang', 'm')]], x=M, w=300, uk=44)
     + teks(400, 112, 384, 'Pola latar resmi. Selalu transparan di atas bidang warna, tidak '
            'pernah jadi warna sendiri.', 12, REDUP, 400, '1.6', rt='right')
     + ubin(M, PUTIH, TEAL, '.2', 1, 'Rapat · 13 mm')
     + ubin(M + 248, PUTIH, TEAL, '.16', 2, 'Sedang · 26 mm')
     + ubin(M + 496, TEAL_X, KRIM, '.2', 2, 'Di latar gelap · 26 mm', rgba(KRIM, '.7'), None)
     + garis(M, 478, KOL)
     + dv(P(x=M, y=496, w=KOL, z=8, lain='display:flex;justify-content:space-between;'),
          mata(None, None, 'Opasitas 8–16% di latar gelap · 4–8% di latar terang', REDUP)
              .replace('position:absolute;', '')
          + mata(None, None, 'Tidak pernah lebih pekat', TERRA).replace('position:absolute;', '')))
simpan(19, 'Pola sarang', s)

# ================================================================ 20 maskot
s = (latar_bab(2, 'kiri')
     + bingkai('Bab III · Elemen Visual', 20)
     + blok(M, 96, 384, 432,
            dv(P(x=0, y=0, w=384, h=432, z=1, lain='overflow:hidden;'), sarang(EMAS, '.16', 3, w=384, h=432))
            + tengah(384, 432, bee(250))
            + mata(0, None, 'Lebah Sarang', rgba(INK, '.45'), z=6, uk=9, sp=2, w=384, rt='center',
                   b=22), EMAS_M, 26, 4)
     + bagian('06', [[('Maskot', '')], [('Lebah Sarang', 'c')]], x=472, y=96, w=312, uk=42)
     + catatan(472, 232, 312,
               (('Kapan dipakai', 'Materi yang ramah: stiker, standee, x-banner. Tidak pernah '
                 'di dalam antarmuka aplikasi.'),
                ('Ukuran minimum', '20 mm cetak. Di bawah itu sayapnya hilang.'),
                ('Larangan', 'Jangan diubah warnanya, jangan diberi mulut lain, jangan dipakai '
                 'sebagai logo.')), 86)
     + dv(P(x=472, y=460, w=312, z=6), ''.join(
         blok(i * 106, 0, 98, 68, tengah(98, 68, bee(54, r)), PUTIH, 16, 6, GARIS)
         for i, r in enumerate((-14, 0, 14)))))
simpan(20, 'Maskot', s)

# ================================================================ 21 tulisan tangan
s = (latar_bab(2)
     + bingkai('Bab III · Elemen Visual', 21)
     + bagian('07', [[('Tulisan ', ''), ('tangan', 'm')]], x=M, w=300, uk=44)
     + mata(None, 118, 'Caveat · 600 · miring −3°', REDUP, r=M, rt='right')
     + blok(M, 190, KOL, 216,
            dv(P(x=0, y=0, w=KOL, h=216, z=1, lain='overflow:hidden;'), halftone(TEAL, '.05', 9, 1, KOL, 216))
            + dv(P(x=0, y=52, w=KOL, z=6, lain='font-family:' + CV + ';font-size:62px;'
                   'font-weight:600;color:' + TEAL_X + ';text-align:center;line-height:1.08;'
                   'transform:rotate(-2deg);'), 'Small things make<br>a big difference')
            + heks(x=-60, b=-70, d=180, warna=TEAL, tebal=2, op='.12', z=2)
            + heks(r=-50, y=-60, d=150, warna=EMAS, tebal=2, op='.18', z=2), PUTIH, 26, 4, GARIS)
     + dv(P(x=M, y=436, w=KOL, z=8), ''.join(
         kartu_aturan(i * 243, 0, 228, 92, a, b, KRIM_2, None)
         for i, (a, b) in enumerate((('SATU PER MATERI', 'Cukup sekali di tiap lembar. Dua kali '
                                      'jadi ramai.'),
                                     ('SELALU MIRING', 'Putaran −6° sampai −2°. Tidak pernah lurus.'),
                                     ('WARNA', 'Teal tua, emas, atau krem. Tidak pernah terakota.'))))))
simpan(21, 'Tulisan tangan', s)

# ================================================================ 22 pembatas IV
s, bg = pembatas(22, 'IV', [[('Penerapan', '')]],
                 'Bagaimana semuanya bertemu di layar, di cetakan, dan di meja pameran.',
                 [('23', 'Layar dan cetak'), ('24', 'Merchandise & booth')], '#D2713F', TERRA_X)
simpan(22, 'Pembatas Bab IV', s, bg)

# ================================================================ 23 layar & cetak
s = (latar_bab(3)
     + bingkai('Bab IV · Penerapan', 23)
     + bagian('01', [[('Layar ', ''), ('dan cetak', 'm')]], x=M, w=340, uk=44)
     + teks(440, 112, 344, 'Semua mockup di halaman ini placeholder — diganti foto cetakan asli '
            'sebelum naik cetak.', 12, REDUP, 400, '1.6', rt='right')
     + gambar(M, 196, 356, 332, 'Aplikasi',
              ponsel(46, 30, 108, layar_app(96, 207, TEAL), -5)
              + ponsel(186, 74, 108, layar_app(96, 207, TEAL_G), 6))
     + gambar(428, 196, 172, 332, 'X-banner',
              dv(P(x=32, y=36, w=108, h=222, z=6,
                   lain='background:' + TEAL + ';border-radius:6px;overflow:hidden;'
                        'box-shadow:0 12px 28px ' + rgba(INK, '.18') + ';'),
                 sarang(KRIM, '.16', 1, w=108, h=222)
                 + dv(P(x=0, y=0, w=108, h=222, lain='display:grid;place-items:center;'),
                      lambang(40, KRIM, EMAS_M))),
              'linear-gradient(150deg,' + KRIM_2 + ' 0%,' + KRIM_3 + ' 100%)', pola=False)
     + gambar(612, 196, 172, 332, 'Poster & kartu',
              dv(P(x=26, y=40, w=120, h=170, z=6, lain='background:' + KRIM
                   + ';border-radius:5px;box-shadow:0 10px 24px ' + rgba(INK, '.16') + ';'))
              + dv(P(x=38, y=56, w=96, h=58, z=7, lain='background:' + TERRA + ';border-radius:3px;'))
              + dv(P(x=38, y=124, w=96, h=7, z=7, lain='background:' + KRIM_3 + ';'))
              + dv(P(x=38, y=140, w=64, h=7, z=7, lain='background:' + KRIM_3 + ';'))
              + dv(P(x=40, y=226, w=112, h=66, z=8, lain='background:' + TEAL_X
                     + ';border-radius:5px;box-shadow:0 10px 22px ' + rgba(INK, '.2') + ';'
                     'display:grid;place-items:center;'), lambang(24, KRIM, EMAS_M)),
              'linear-gradient(150deg,' + KRIM_2 + ' 0%,' + KRIM_3 + ' 100%)', pola=False))
simpan(23, 'Layar dan cetak', s)

# ================================================================ 24 merchandise & booth
barang = ''
for i, (c, bentuk) in enumerate(((MINT, 'heks'), (EMAS_M, 'bulat'), (TERRA_M, 'heks'),
                                 (TEAL, 'bulat'), (KRIM, 'heks'), (EMAS, 'bulat'))):
    x, y = 32 + (i % 3) * 100, 44 + (i // 3) * 122
    g = (HEKS if bentuk == 'heks' else 'border-radius:16px;')
    barang += dv(P(x=x, y=y, w=84, h=96, z=6, lain='background:' + c + ';' + g
                   + 'display:grid;place-items:center;'),
                 lambang(28, TEAL_X if c in (MINT, EMAS_M, KRIM, TERRA_M) else KRIM,
                         EMAS if c in (MINT, KRIM, TERRA_M) else EMAS_M))
s = (latar_bab(3, 'kiri')
     + bingkai('Bab IV · Penerapan', 24)
     + bagian('02', [[('Merchandise ', ''), ('& booth', 'm')]], x=M, w=400, uk=44)
     + gambar(M, 196, 356, 300, 'Gantungan kunci · stiker · kartu', barang,
              'linear-gradient(150deg,' + KRIM_2 + ' 0%,' + KRIM_3 + ' 100%)', pola=False)
     + blok(428, 196, 356, 300,
            dv(P(x=26, y=28, w=304, h=170, lain='background:' + KRIM_2 + ';border-radius:12px;'))
            + dv(P(x=42, y=44, w=86, h=138, z=6, lain='background:' + TEAL + ';border-radius:6px;'
                   'overflow:hidden;'), sarang(KRIM, '.18', 1, w=86, h=138))
            + dv(P(x=142, y=44, w=170, h=62, z=6, lain='background:' + PUTIH + ';border:1px solid '
                   + GARIS + ';border-radius:6px;'))
            + dv(P(x=142, y=118, w=80, h=64, z=6, lain='background:' + EMAS_M + ';border-radius:6px;'))
            + dv(P(x=232, y=118, w=80, h=64, z=6, lain='background:' + TERRA_M + ';border-radius:6px;'))
            + dv(P(x=26, y=218, w=304, z=6, lain=font(PJ, 11, 400, REDUP, None, '1.55')),
                 'Denah meja: x-banner di belakang, kotak barang temuan di tengah, standee QR '
                 'dan kartu barang di depan.')
            + mata(26, None, 'Denah booth', REDUP, z=6, uk=8, sp=2, b=18), PUTIH, 22, 4, GARIS)
     + garis(M, 520, KOL)
     + tangan(M, 534, 'Yang hilang, balik pulang.', TEAL, 26, -2)
     + mata(None, 544, 'Balikin · Graphic Standard Manual · Edisi 01', REDUP, r=M, rt='right'))
simpan(24, 'Merchandise & booth', s)

# ================================================================ kanvas
papan = [{"file": b, "x": (i % 6) * 900, "y": (i // 6) * 700, "w": W, "h": H, "title": j}
         for i, (b, j) in enumerate(HAL)]
kanvas = {"artboards": papan,
  "annotations": [{"id": "catatan", "x": 0, "y": -170, "w": 1040,
    "text": "GSM Balikin — 24 halaman A5 lanskap 210 × 148 mm (840 × 592 px, 4 satuan = 1 mm).\n"
            "Gaya presentasi brand identity: tipografi besar bercampur, blok warna penuh, "
            "kartu bersudut membulat, supergrafis heksagon.\n"
            "Tangkapan layar aplikasi dan foto cetakan masih placeholder. "
            "Urut membaca kiri ke kanan, enam halaman per baris."}],
  "launch": {"view": "canvas"}}
open(os.path.join(DIR, 'canvas.json'), 'w', encoding='utf-8').write(
    json.dumps(kanvas, indent=2, ensure_ascii=False))
print('%d halaman + canvas.json' % len(HAL))
