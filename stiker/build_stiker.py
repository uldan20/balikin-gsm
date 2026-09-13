# -*- coding: utf-8 -*-
"""Sticker pack — satu lembar vinyl A3 kiss-cut, 25 keping.

Isinya seluruh dunia Balikin: wordmark, logogram, maskot, lima lencana
tingkat, enam kategori barang, gelembung percakapan dari aplikasi, tagline,
tulisan tangan, pin titik aman, dan kode barang.

Skala 4 satuan = 1 mm. Lembar 297 x 420 mm = 1188 x 1680.
"""
import os, sys, re, math
_here = os.path.dirname(os.path.abspath(__file__))
for sub in ('xbanner', 'infografis', 'standee', 'gantungan'):
    sys.path.insert(0, os.path.join(_here, '..', sub))
from build import LEBAH, AR, PJ, CV
from rapi import bakar_fragmen, bidang
from ikon import IKON
from build_standee import N, teks, heks, POTONG, CREAM, INK, TEAL, TEAL_T, TEAL_G, \
    TEAL_X, MINT, EMAS, EMAS_M, TERRA
from build_gantungan import siluet, lambang, TINGKAT, letusan_path, heks_path, bulat_path

S = 4
W, H = 297 * S, 420 * S
TEPI = 12                                  # tepi putih 3 mm
REDUP = '#6B8A81'

GAMBAR, POT = [], []

def taruh(jalur, isi, tepi=TEPI):
    """Satu keping: tepi putih, isi, lalu jalur potong dicatat."""
    GAMBAR.append('<path d="' + jalur + '" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="'
                  + N(tepi * 2) + '" stroke-linejoin="round"/>' + isi)
    POT.append('<path d="' + jalur + '" fill="none" stroke="' + POTONG + '" stroke-width="2"/>')

def pil_path(x, y, w, h):
    r = h // 2
    return ('M' + N(x + r) + ' ' + N(y) + 'H' + N(x + w - r) + 'A' + N(r) + ' ' + N(r)
            + ' 0 0 1 ' + N(x + w - r) + ' ' + N(y + h) + 'H' + N(x + r) + 'A' + N(r) + ' '
            + N(r) + ' 0 0 1 ' + N(x + r) + ' ' + N(y) + 'Z')

def gelembung_path(x, y, w, h=112):
    """Pil dengan ekor yang menyatu — satu subjalur, tepi putihnya mulus."""
    r = h // 2
    return ('M' + N(x + r) + ' ' + N(y) + 'H' + N(x + w - r) + 'A' + N(r) + ' ' + N(r)
            + ' 0 0 1 ' + N(x + w - r) + ' ' + N(y + h) + 'H' + N(x + 110)
            + 'L' + N(x + 52) + ' ' + N(y + h + 36) + 'L' + N(x + 70) + ' ' + N(y + h)
            + 'H' + N(x + r) + 'A' + N(r) + ' ' + N(r) + ' 0 0 1 ' + N(x + r) + ' ' + N(y) + 'Z')

def kotak_path(x, y, w, h, r):
    return ('M' + N(x + r) + ' ' + N(y) + 'H' + N(x + w - r) + 'Q' + N(x + w) + ' ' + N(y) + ' '
            + N(x + w) + ' ' + N(y + r) + 'V' + N(y + h - r) + 'Q' + N(x + w) + ' ' + N(y + h)
            + ' ' + N(x + w - r) + ' ' + N(y + h) + 'H' + N(x + r) + 'Q' + N(x) + ' ' + N(y + h)
            + ' ' + N(x) + ' ' + N(y + h - r) + 'V' + N(y + r) + 'Q' + N(x) + ' ' + N(y) + ' '
            + N(x + r) + ' ' + N(y) + 'Z')

def lebah(x, y, px_):
    return ('<g>' + bidang(px_, px_, x, y) + bakar_fragmen(LEBAH, px_ / 200.0, x, y) + '</g>')

def ikon(nama, x, y, px, warna, ):
    return ('<g color="' + warna + '" fill="none" stroke-linejoin="miter" stroke-miterlimit="8">'
            + bidang(px, px, x, y) + bakar_fragmen(IKON[nama], px / 100.0, x, y) + '</g>')

# ---------------------------------------------------------------- baris 1
# wordmark
taruh(pil_path(48, 48, 600, 184),
      '<path d="' + pil_path(48, 48, 600, 184) + '" fill="' + TEAL + '"/>'
      '<path d="M160 78L212 108V168L160 198L108 168V108Z" fill="none" stroke="' + CREAM
      + '" stroke-width="12" stroke-linejoin="miter"/>'
      '<path d="M178 126L169 141H151L142 126L151 111H169Z" fill="' + EMAS_M + '"/>'
      + teks(430, 168, 'BALIKIN', 78, AR, 700, CREAM, 6))
# logogram
taruh(heks(812, 140, 112, 96),
      '<path d="' + heks(812, 140, 112, 96) + '" fill="' + TEAL_X + '"/>'
      '<path d="M812 76L868 108V172L812 204L756 172V108Z" fill="none" stroke="' + CREAM
      + '" stroke-width="13" stroke-linejoin="miter"/>'
      '<path d="M832 126L822 143H802L792 126L802 109H822Z" fill="' + EMAS_M + '"/>')
# lebah kecil
taruh(bulat_path(1058, 140, 82), lebah(978, 60, 160))

# ---------------------------------------------------------------- baris 2 · lima lencana
for i, (nama, bentuk, c1, c2, fg, hy, pw, ph, pdy, baris) in enumerate(TINGKAT):
    cx, cy = 148 + i * 223, 392
    jalur = siluet(bentuk, cx, cy)
    py = cy + pdy
    pita = ('<rect x="' + N(cx - pw // 2) + '" y="' + N(py - ph // 2) + '" width="' + N(pw)
            + '" height="' + N(ph) + '" rx="' + N(ph // 2) + '" fill="' + CREAM
            + '" stroke="' + c2 + '" stroke-width="2"/>')
    for j, t in enumerate(baris):
        pita += teks(cx, py - (len(baris) - 1) * 8 + j * 16 + 4, t, 11, AR, 700, INK, 1)
    naik = -32 if len(baris) > 1 or bentuk == 'perisai' else -26
    taruh(jalur, '<path d="' + jalur + '" fill="' + c2 + '"/>'
          + lambang(bentuk, cx, cy + naik, fg, .8) + pita)

# ---------------------------------------------------------------- baris 3
# pita tagline
taruh(pil_path(48, 548, 640, 128),
      '<path d="' + pil_path(48, 548, 640, 128) + '" fill="' + CREAM + '" stroke="' + TEAL
      + '" stroke-width="7"/>'
      + teks(368, 632, 'Yang hilang, balik pulang.', 46, AR, 700, TEAL_X))
# letusan +150 poin
_l = letusan_path(796, 612, 12, 92, 62)
taruh(_l, '<path d="' + _l + '" fill="' + EMAS + '"/>'
      + teks(796, 604, '+150', 34, AR, 700, CREAM, -1)
      + teks(796, 632, 'POIN', 15, PJ, 700, CREAM, 3))
# pin titik aman
_pin = ('M1040 528L1104 564V636L1040 700L976 636V564Z')
taruh(_pin, '<path d="' + _pin + '" fill="' + TERRA + '"/>'
      + ikon('pin', 1004, 560, 72, CREAM))

# ---------------------------------------------------------------- baris 4 · enam kategori
BARANG = [('wallet', 'DOMPET', TERRA), ('kunci', 'KUNCI', EMAS), ('ponsel', 'HP', TEAL),
          ('dokumen', 'DOKUMEN', TEAL_X), ('bag', 'TAS', MINT), ('tumbler', 'BOTOL', EMAS_M)]
for i, (ik_, lab, warna) in enumerate(BARANG):
    x = 48 + i * 186
    jalur = kotak_path(x, 764, 160, 184, 40)
    fg = INK if warna in (MINT, EMAS_M) else CREAM
    taruh(jalur, '<path d="' + jalur + '" fill="' + warna + '"/>'
          + ikon(ik_, x + 40, 796, 80, fg)
          + teks(x + 80, 914, lab, 15, PJ, 700, fg, 2))

# ---------------------------------------------------------------- baris 5 · gelembung
KATA = [('Ketemu!', 216, TEAL, CREAM), ('Balikin, yuk', 296, EMAS_M, INK),
        ('Punyaku!', 236, TERRA, CREAM), ('Makasih ya', 276, CREAM, TEAL_X)]
x = 48
for kata, lw, bg, fg in KATA:
    y = 996
    jalur = gelembung_path(x, y, lw)
    taruh(jalur, '<path d="' + jalur + '" fill="' + bg + '"/>'
          + (('<path d="' + jalur + '" fill="none" stroke="' + TEAL
              + '" stroke-width="6"/>') if bg == CREAM else '')
          + teks(x + lw // 2, y + 72, kata, 34, AR, 700, fg, -1))
    x += lw + 22

# ---------------------------------------------------------------- baris 6
# lebah besar
taruh(bulat_path(196, 1320, 140), lebah(56, 1180, 280))
# sel sarang
_sel = heks(500, 1320, 124, 108)
taruh(_sel, '<path d="' + _sel + '" fill="' + MINT + '"/>'
      '<path d="' + heks(500, 1320, 86, 75) + '" fill="none" stroke="' + TEAL
      + '" stroke-width="9" stroke-linejoin="miter"/>'
      + teks(500, 1338, '42', 52, AR, 700, TEAL_X, -2))
# label kode barang
_kode = kotak_path(680, 1252, 300, 136, 26)
taruh(_kode, '<path d="' + _kode + '" fill="' + TEAL_X + '"/>'
      '<circle cx="716" cy="1320" r="16" fill="' + CREAM + '"/>'
      + teks(848, 1310, 'BLK-P042', 36, AR, 700, CREAM, 2)
      + teks(848, 1350, 'BARANG TEMUAN', 13, PJ, 700, MINT, 4))
# heksagon pindai
_pindai = heks(1078, 1320, 90, 78)
taruh(_pindai, '<path d="' + _pindai + '" fill="' + EMAS_M + '"/>'
      + teks(1078, 1308, 'PINDAI', 22, AR, 700, INK, 1)
      + teks(1078, 1340, 'AKU', 22, AR, 700, INK, 1))

# ---------------------------------------------------------------- baris 7
# tulisan tangan
_tt = pil_path(48, 1436, 856, 176)
taruh(_tt, '<path d="' + _tt + '" fill="' + CREAM + '" stroke="' + EMAS
      + '" stroke-width="6"/>'
      '<text x="476" y="1526" font-family="' + CV + '" font-size="46" font-weight="600" '
      'fill="' + TEAL_X + '" text-anchor="middle">Small things make a big difference</text>'
      '<path d="M214 1556Q476 1586 738 1552" stroke="' + EMAS + '" stroke-width="7" fill="none" '
      'stroke-linecap="round"/>')
# keping titik aman
_ta = pil_path(928, 1436, 212, 92)
taruh(_ta, '<path d="' + _ta + '" fill="' + TEAL + '"/>'
      + teks(1034, 1494, 'TITIK AMAN', 24, AR, 700, CREAM, 2))
# keping balikin.id
_bi = pil_path(928, 1548, 212, 76)
taruh(_bi, '<path d="' + _bi + '" fill="' + TERRA + '"/>'
      + teks(1034, 1598, 'balikin.id', 28, AR, 700, CREAM, 1))

def lembar():
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<svg xmlns="http://www.w3.org/2000/svg" width="297mm" height="420mm" '
            'viewBox="0 0 ' + N(W) + ' ' + N(H) + '" role="img" aria-label="Balikin — lembar stiker A3">\n'
            '<title>Balikin — lembar stiker vinyl A3 kiss-cut</title>\n'
            '<desc>25 keping. 4 satuan = 1 mm. Tepi putih 3 mm. Lapisan POTONG tidak dicetak.</desc>\n'
            '<rect x="0" y="0" width="' + N(W) + '" height="' + N(H) + '" fill="#F3F1EC"/>\n'
            + '\n'.join(GAMBAR) + '\n<g id="POTONG">' + ''.join(POT) + '</g>\n</svg>\n')

if __name__ == '__main__':
    keluar = os.path.join(_here, 'svg', 'stiker-lembar-a3.svg')
    isi = lembar()
    open(keluar, 'w', encoding='utf-8').write(isi)
    sisa = sorted(set(re.findall(r'-?\d+\.\d+', isi)))
    print('stiker-lembar-a3.svg  %d keping  %d B  desimal: %s'
          % (len(POT), len(isi), sisa or 'tidak ada'))
