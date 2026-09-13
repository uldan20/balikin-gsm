# -*- coding: utf-8 -*-
"""Kartu Barang (case card) untuk Meja Barang Temuan — 90 x 120 mm.

Satu kasus contoh, empat arah desain. Skala 4 satuan = 1 mm (360 x 480).
Ditulis langsung sebagai SVG supaya jalur potong utuh dan koordinat bulat.
"""
import os, sys, re
_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_here, '..', 'xbanner'))
sys.path.insert(0, os.path.join(_here, '..', 'infografis'))
sys.path.insert(0, os.path.join(_here, '..', 'standee'))
from build import AR, PJ, CV, LEBAH
from rapi import bakar_fragmen, bidang
from ikon import IKON
from build_standee import N, teks, heks, qr_kotak, sarang_def, POTONG, \
    CREAM, INK, TEAL, TEAL_T, TEAL_G, TEAL_X, MINT, EMAS, EMAS_M, TERRA

S = 4
W, H = 90 * S, 120 * S                 # 360 x 480
FILL, REDUP, GARIS = '#F1ECE3', '#6B8A81', '#DED8CB'

# ---------------- isi kartu contoh ----------------
KODE = 'BLK-P042'
KATEGORI, IKON_BARANG = 'DOMPET', 'wallet'
NAMA = 'Dompet kulit cokelat'
CIRI = ['Jahitan sisi kanan lepas', 'Ada stiker kucing di dalam']
LOKASI = 'Halte Cisaat, Sukabumi'
WAKTU = 'Sabtu 16.20'
STATUS = 'MENUNGGU PEMILIK'
POIN = '+150'

def ikon(nama, x, y, px, warna):
    """Ikon Sudut Enam, transform dibakar supaya tidak ada scale() tersisa."""
    return ('<g color="' + warna + '" fill="none" stroke-linejoin="miter" stroke-miterlimit="8">'
            + bidang(px, px, x, y) + bakar_fragmen(IKON[nama], px / 100.0, x, y) + '</g>')

def pil(x, y, w, h, isi, bg, fg, ukuran=13, huruf=PJ, spasi=2):
    return ('<g><rect x="' + N(x) + '" y="' + N(y) + '" width="' + N(w) + '" height="' + N(h)
            + '" rx="' + N(h // 2) + '" fill="' + bg + '"/>'
            + teks(x + w // 2, y + h // 2 + ukuran // 3, isi, ukuran, huruf, 700, fg, spasi) + '</g>')

def garis(x1, y, x2, warna=GARIS, tebal=2):
    return ('<path d="M' + N(x1) + ' ' + N(y) + 'H' + N(x2) + '" stroke="' + warna
            + '" stroke-width="' + N(tebal) + '"/>')

def bungkus(judul, isi, jalur_potong=None, w=W, h=H):
    potong = ('<g id="POTONG"><path d="' + jalur_potong + '" fill="none" stroke="' + POTONG
              + '" stroke-width="2"/></g>') if jalur_potong else (
              '<g id="POTONG"><rect x="0" y="0" width="' + N(w) + '" height="' + N(h)
              + '" fill="none" stroke="' + POTONG + '" stroke-width="2"/></g>')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<svg xmlns="http://www.w3.org/2000/svg" width="' + N(w // S) + 'mm" height="'
            + N(h // S) + 'mm" viewBox="0 0 ' + N(w) + ' ' + N(h) + '" role="img" aria-label="'
            + judul + '">\n<title>' + judul + '</title>\n'
            '<desc>Kartu Barang 90 x 120 mm. 4 satuan = 1 mm. Lapisan POTONG tidak dicetak.</desc>\n'
            + isi + '\n' + potong + '\n</svg>\n')

# ======================================================== A · ARSIP
def kartu_a():
    d = ['<rect x="0" y="0" width="' + N(W) + '" height="' + N(H) + '" fill="' + CREAM + '"/>',
         '<rect x="14" y="14" width="' + N(W - 28) + '" height="' + N(H - 28)
         + '" fill="none" stroke="' + INK + '" stroke-width="2" stroke-opacity=".35"/>',
         teks(W // 2, 46, 'KARTU BARANG TEMUAN', 11, PJ, 700, REDUP, 4),
         garis(40, 58, W - 40),
         teks(W // 2, 96, KODE, 30, AR, 700, INK, 2),
         # bidang barang
         '<rect x="40" y="118" width="' + N(W - 80) + '" height="150" fill="' + FILL + '"/>',
         '<path d="' + heks(W // 2, 193, 54, 46) + '" fill="' + MINT + '" fill-opacity=".5"/>',
         ikon(IKON_BARANG, W // 2 - 32, 161, 64, TEAL_G),
         teks(W - 48, 136, KATEGORI, 10, PJ, 700, REDUP, 3, 'end'),
         teks(W // 2, 298, NAMA, 21, AR, 700, INK),
         teks(W // 2, 320, ' · '.join(CIRI), 11, PJ, 400, REDUP),
         garis(40, 336, W - 40),
         teks(40, 358, 'DITEMUKAN', 9, PJ, 700, REDUP, 2, 'start'),
         teks(40, 376, LOKASI, 12, PJ, 600, INK, 0, 'start'),
         teks(40, 392, WAKTU, 12, PJ, 400, REDUP, 0, 'start'),
         pil(40, 406, 150, 26, STATUS, EMAS_M, INK, 10),
         qr_kotak(216, 336, 4),
         teks(270, 462, 'PINDAI, LALU BALIKIN', 9, PJ, 700, REDUP, 2),
         ]
    return bungkus('Balikin — Kartu Barang A, Arsip', '\n'.join(d))

# ======================================================== B · KARTU APLIKASI
def kartu_b():
    r = 24
    kartu_jalur = ('M' + N(r) + ' 0H' + N(W - r) + 'C' + N(W - 8) + ' 0 ' + N(W) + ' 8 ' + N(W) + ' '
                   + N(r) + 'V' + N(H - r) + 'C' + N(W) + ' ' + N(H - 8) + ' ' + N(W - 8) + ' ' + N(H)
                   + ' ' + N(W - r) + ' ' + N(H) + 'H' + N(r) + 'C8 ' + N(H) + ' 0 ' + N(H - 8)
                   + ' 0 ' + N(H - r) + 'V' + N(r) + 'C0 8 8 0 ' + N(r) + ' 0Z')
    d = ['<defs><linearGradient id="atas" x1="0%" y1="0%" x2="40%" y2="100%">'
         '<stop offset="0%" stop-color="#CFE6E0"/><stop offset="100%" stop-color="#A6D6C6"/>'
         '</linearGradient>' + sarang_def(TEAL, '0.16') + '</defs>',
         '<path d="' + kartu_jalur + '" fill="#FFFFFF"/>',
         '<g clip-path="url(#klip)"></g>',
         '<defs><clipPath id="klip"><path d="' + kartu_jalur + '"/></clipPath></defs>',
         '<g clip-path="url(#klip)">'
         '<rect x="0" y="0" width="' + N(W) + '" height="196" fill="url(#atas)"/>'
         '<rect x="0" y="0" width="' + N(W) + '" height="196" fill="url(#sarang)"/>'
         '<path d="' + heks(W // 2, 100, 60, 52) + '" fill="#FFFFFF" fill-opacity=".55"/>'
         + ikon(IKON_BARANG, W // 2 - 36, 64, 72, TEAL_G)
         + '<rect x="0" y="392" width="' + N(W) + '" height="88" fill="' + TEAL_X + '"/></g>',
         # keping kategori menumpang tepi gambar
         '<g><rect x="24" y="176" width="116" height="30" rx="15" fill="' + CREAM + '"/>'
         + ikon(IKON_BARANG, 34, 183, 16, TEAL) + teks(94, 196, KATEGORI, 11, PJ, 700, INK, 2) + '</g>',
         teks(24, 244, NAMA, 20, AR, 700, INK, 0, 'start'),
         teks(24, 266, CIRI[0] + ',', 11, PJ, 400, REDUP, 0, 'start'),
         teks(24, 282, CIRI[1], 11, PJ, 400, REDUP, 0, 'start'),
         ikon('pin', 24, 300, 15, TERRA),
         teks(46, 313, LOKASI + ' · ' + WAKTU, 11, PJ, 500, INK, 0, 'start'),
         pil(24, 336, 156, 28, STATUS, '#F5DCCE', '#A2421D', 10),
         teks(W - 24, 358, KODE, 13, AR, 700, REDUP, 1, 'end'),
         # pita bawah
         qr_kotak(20, 398, 3),
         teks(116, 428, 'Pindai untuk balikin', 13, PJ, 700, CREAM, 0, 'start'),
         teks(116, 446, 'Kembalikan dalam 90 detik', 10, PJ, 400, 'rgba(207,230,224,.75)', 0, 'start'),
         teks(W - 24, 440, POIN, 22, AR, 700, EMAS_M, 0, 'end'),
         ]
    return bungkus('Balikin — Kartu Barang B, Kartu Aplikasi', '\n'.join(d), kartu_jalur)

# ======================================================== C · KOLEKSI GELAP
def kartu_c():
    c = 40   # sudut dipangkas, tanda tangan Sudut Enam
    jalur = ('M' + N(c) + ' 0H' + N(W) + 'V' + N(H - c) + 'L' + N(W - c) + ' ' + N(H)
             + 'H0V' + N(c) + 'Z')
    d = ['<defs><linearGradient id="badan" x1="0%" y1="0%" x2="30%" y2="100%">'
         '<stop offset="0%" stop-color="' + TEAL_T + '"/><stop offset="60%" stop-color="' + TEAL
         + '"/><stop offset="100%" stop-color="' + TEAL_X + '"/></linearGradient>'
         + sarang_def(CREAM, '0.1') + '</defs>',
         '<path d="' + jalur + '" fill="url(#badan)"/>',
         '<path d="' + jalur + '" fill="url(#sarang)"/>',
         teks(28, 44, 'BALIKIN', 14, AR, 700, CREAM, 3, 'start'),
         teks(W - 28, 44, KODE, 13, AR, 700, EMAS_M, 1, 'end'),
         garis(28, 58, W - 28, 'rgba(251,248,243,.25)'),
         '<path d="' + heks(W // 2, 158, 76, 66) + '" fill="none" stroke="' + EMAS_M
         + '" stroke-width="3"/>',
         '<path d="' + heks(W // 2, 158, 62, 54) + '" fill="rgba(251,248,243,.1)"/>',
         ikon(IKON_BARANG, W // 2 - 40, 118, 80, CREAM),
         teks(W // 2, 262, KATEGORI, 10, PJ, 700, EMAS_M, 4),
         teks(W // 2, 290, NAMA, 21, AR, 700, CREAM),
         teks(W // 2, 312, CIRI[0] + ' · ' + CIRI[1], 10, PJ, 400, 'rgba(207,230,224,.8)'),
         teks(W // 2, 336, LOKASI + ' · ' + WAKTU, 11, PJ, 600, MINT),
         # panel bawah
         '<path d="M0 356H' + N(W) + 'V' + N(H - c) + 'L' + N(W - c) + ' ' + N(H) + 'H0Z" fill="'
         + CREAM + '"/>',
         qr_kotak(24, 372, 3),
         teks(148, 398, STATUS, 10, PJ, 700, TERRA, 2, 'start'),
         teks(148, 428, POIN + ' POIN', 22, AR, 700, INK, 0, 'start'),
         teks(148, 448, 'untuk penemunya', 10, PJ, 400, REDUP, 0, 'start'),
         ]
    return bungkus('Balikin — Kartu Barang C, Koleksi', '\n'.join(d), jalur)

# ======================================================== D · TAG GANTUNG
def kartu_d():
    jalur = ('M60 0H' + N(W - 24) + 'C' + N(W - 8) + ' 0 ' + N(W) + ' 10 ' + N(W) + ' 26V'
             + N(H - 26) + 'C' + N(W) + ' ' + N(H - 10) + ' ' + N(W - 8) + ' ' + N(H) + ' '
             + N(W - 24) + ' ' + N(H) + 'H24C8 ' + N(H) + ' 0 ' + N(H - 10) + ' 0 ' + N(H - 26)
             + 'V60Z')
    lubang = '<circle cx="44" cy="44" r="14" fill="none" stroke="' + POTONG + '" stroke-width="2"/>'
    d = ['<defs>' + sarang_def(TERRA, '0.12') + '</defs>',
         '<path d="' + jalur + '" fill="' + CREAM + '"/>',
         '<path d="' + jalur + '" fill="url(#sarang)"/>',
         '<path d="M60 0H' + N(W - 24) + 'C' + N(W - 8) + ' 0 ' + N(W) + ' 10 ' + N(W)
         + ' 26V96H0V60Z" fill="' + TERRA + '"/>',
         '<circle cx="44" cy="44" r="16" fill="' + CREAM + '"/>',
         '<circle cx="44" cy="44" r="11" fill="' + TERRA + '"/>',
         teks(W - 24, 52, 'BARANG TEMUAN', 10, PJ, 700, 'rgba(251,248,243,.85)', 3, 'end'),
         teks(W - 24, 82, KODE, 24, AR, 700, CREAM, 2, 'end'),
         # isi
         ikon(IKON_BARANG, 24, 116, 52, TERRA),
         teks(88, 140, KATEGORI, 10, PJ, 700, REDUP, 3, 'start'),
         teks(88, 164, NAMA, 19, AR, 700, INK, 0, 'start'),
         teks(24, 198, CIRI[0] + ' · ' + CIRI[1], 11, PJ, 400, REDUP, 0, 'start'),
         garis(24, 216, W - 24),
         teks(24, 240, 'DITEMUKAN', 9, PJ, 700, REDUP, 2, 'start'),
         teks(24, 258, LOKASI, 12, PJ, 600, INK, 0, 'start'),
         teks(24, 274, WAKTU, 12, PJ, 400, REDUP, 0, 'start'),
         pil(24, 292, 150, 26, STATUS, '#F5DCCE', '#A2421D', 10),
         # garis sobek
         '<path d="M12 340H' + N(W - 12) + '" stroke="' + GARIS
         + '" stroke-width="3" stroke-dasharray="8 8"/>',
         qr_kotak(24, 356, 3),
         teks(148, 386, 'PINDAI DI SINI', 10, PJ, 700, TEAL, 3, 'start'),
         teks(148, 412, 'Balikin ke pemiliknya', 15, AR, 700, INK, 0, 'start'),
         teks(148, 434, POIN + ' poin untuk penemu', 11, PJ, 500, REDUP, 0, 'start'),
         teks(148, 456, 'balikin.id/prototipe', 10, PJ, 700, TEAL, 0, 'start'),
         lubang,
         ]
    return bungkus('Balikin — Kartu Barang D, Tag Gantung', '\n'.join(d), jalur)

# ======================================================== C · BELAKANG
# Sudut pangkas dicerminkan (kanan atas + kiri bawah) supaya pas waktu
# dicetak bolak-balik dan dipotong sekali.
LANGKAH = [('Pindai QR di kartu ini', 'Prototipe Balikin terbuka di HP-mu.'),
           ('Isi laporan temuan', 'Foto, kategori, lokasi. Empat langkah, dua menit.'),
           ('Cocokkan kode serah terima', 'Empat huruf dari penjaga meja, lalu barang berpindah.')]

def kartu_c_belakang():
    c = 40
    jalur = ('M0 0H' + N(W - c) + 'L' + N(W) + ' ' + N(c) + 'V' + N(H) + 'H' + N(c)
             + 'L0 ' + N(H - c) + 'Z')
    pita = ('M0 0H' + N(W - c) + 'L' + N(W) + ' ' + N(c) + 'V88H0Z')
    d = ['<defs>' + sarang_def(TEAL, '0.1') + '</defs>',
         '<path d="' + jalur + '" fill="' + CREAM + '"/>',
         '<path d="' + jalur + '" fill="url(#sarang)"/>',
         '<path d="' + pita + '" fill="' + TEAL_X + '"/>',
         # lambang + wordmark
         '<path d="M44 30L68 44V72L44 86L20 72V44Z" fill="none" stroke="' + CREAM
         + '" stroke-width="5" stroke-linejoin="miter"/>'
         '<path d="M52 52L48 59H40L36 52L40 45H48Z" fill="' + EMAS_M + '"/>',
         teks(84, 52, 'BALIKIN', 19, AR, 700, CREAM, 3, 'start'),
         teks(84, 70, 'KARTU BARANG TEMUAN', 9, PJ, 700, 'rgba(207,230,224,.75)', 3, 'start'),
         '<g id="maskot">' + bidang(58, 58, 268, 16)
         + bakar_fragmen(LEBAH, 0.29, 268, 16) + '</g>',
         teks(W // 2, 122, 'TIGA LANGKAH MEMBALIKIN', 10, PJ, 700, REDUP, 3),
         ]
    for i, (judul, ket) in enumerate(LANGKAH):
        y = 146 + i * 56
        d.append('<path d="' + heks(46, y + 10, 20, 17) + '" fill="' + TEAL + '"/>')
        d.append(teks(46, y + 16, str(i + 1), 15, AR, 700, CREAM))
        d.append(teks(78, y + 8, judul, 14, AR, 700, INK, 0, 'start'))
        d.append(teks(78, y + 26, ket, 10, PJ, 400, REDUP, 0, 'start'))
    d.append(garis(24, 310, W - 24))
    # kotak kode serah terima
    d.append(teks(W // 2, 334, 'KODE SERAH TERIMA', 9, PJ, 700, REDUP, 3))
    for i in range(4):
        x = 74 + i * 56
        d.append('<rect x="' + N(x) + '" y="344" width="44" height="44" rx="10" fill="#FFFFFF" '
                 'stroke="' + TEAL + '" stroke-width="2" stroke-dasharray="7 6"/>')
    d.append(teks(W // 2, 402, 'diisi penjaga meja saat barang diserahkan', 9, PJ, 400, REDUP))
    # ajakan tukar
    d.append(pil(24, 412, W - 48, 28, 'TUKAR KARTU INI DENGAN LENCANA', EMAS_M, INK, 10))
    d.append('<text x="' + N(W // 2) + '" y="464" font-family="' + CV + '" font-size="17" '
             'font-weight="600" fill="' + TEAL + '" text-anchor="middle">'
             'Small things make a big difference</text>')
    return bungkus('Balikin — Kartu Barang C, belakang', '\n'.join(d), jalur)

if __name__ == '__main__':
    OUT = os.path.join(_here, 'svg')
    for nama, isi in (('kartu-barang-a-arsip', kartu_a()),
                      ('kartu-barang-b-aplikasi', kartu_b()),
                      ('kartu-barang-c-koleksi', kartu_c()),
                      ('kartu-barang-d-tag', kartu_d()),
                      ('kartu-barang-c-belakang', kartu_c_belakang())):
        open(os.path.join(OUT, nama + '.svg'), 'w', encoding='utf-8').write(isi)
        sisa = sorted(set(re.findall(r'-?\d+\.\d+', isi)))
        print('%-30s %5d B  desimal: %s' % (nama + '.svg', len(isi), sisa or 'tidak ada'))
