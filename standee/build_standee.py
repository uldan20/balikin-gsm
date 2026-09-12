# -*- coding: utf-8 -*-
"""Standee QR meja Balikin — berkas potong (die-cut) untuk akrilik 3 mm.

Ditulis langsung sebagai SVG, bukan lewat pengonversi HTML, supaya garis
potongnya satu jalur utuh dan seluruh koordinat bilangan bulat.

Skala: 4 satuan = 1 mm. Kanvas 600 x 860 = 150 x 215 mm.
"""
import os, sys
_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_here, '..', 'xbanner'))
from build import LEBAH, AR, PJ, CV
from rapi import bakar_fragmen, bidang

S = 4                                   # satuan per mm
W, H = 150 * S, 215 * S

CREAM, INK = '#FBF8F3', '#12332C'
TEAL, TEAL_T, TEAL_G, TEAL_X = '#1B7A63', '#25946F', '#0F5A48', '#0B4638'
MINT, EMAS, EMAS_M, TERRA = '#8FD4C4', '#C8952E', '#F3D77C', '#C05C33'
POTONG = '#FF00FF'                      # garis potong, tidak ikut dicetak

def N(v):
    v = int(round(v))
    return str(0 if v == 0 else v)

def teks(x, y, isi, ukuran, huruf=PJ, tebal=400, warna=INK, spasi=0, rata='middle'):
    ls = ' letter-spacing="' + N(spasi) + '"' if spasi else ''
    return ('<text x="' + N(x) + '" y="' + N(y) + '" font-family="' + huruf + '" font-size="'
            + N(ukuran) + '" font-weight="' + str(tebal) + '" fill="' + warna + '" text-anchor="'
            + rata + '"' + ls + '>' + isi + '</text>')

def heks(cx, cy, sw, sh):
    """Heksagon bersisi datar: titik di kiri dan kanan."""
    p = [(cx - sw, cy), (cx - sw // 2, cy - sh), (cx + sw // 2, cy - sh),
         (cx + sw, cy), (cx + sw // 2, cy + sh), (cx - sw // 2, cy + sh)]
    return 'M' + 'L'.join(N(a) + ' ' + N(b) for a, b in p) + 'Z'

def qr_kotak(x, y, modul, gelap=INK, terang=CREAM, n=25):
    """Pola QR contoh. Ganti dengan QR asli sebelum cetak."""
    seed, bit = 0x9E3779B9, []
    for _ in range(n * n):
        seed = (seed * 1103515245 + 12345) & 0x7FFFFFFF
        bit.append((seed >> 17) & 1)
    def pojok(r, c):
        return (r < 8 and c < 8) or (r < 8 and c >= n - 8) or (r >= n - 8 and c < 8)
    px = lambda c: x + (c + 1) * modul
    py = lambda r: y + (r + 1) * modul
    isi = ''.join('<rect x="' + N(px(c)) + '" y="' + N(py(r)) + '" width="' + N(modul)
                  + '" height="' + N(modul) + '"/>'
                  for r in range(n) for c in range(n) if not pojok(r, c) and bit[r * n + c])
    mata = ''
    for fr, fc in ((0, 0), (0, n - 7), (n - 7, 0)):
        mata += ('<rect x="' + N(px(fc)) + '" y="' + N(py(fr)) + '" width="' + N(7 * modul)
                 + '" height="' + N(7 * modul) + '" rx="' + N(modul) + '" fill="none" stroke="'
                 + gelap + '" stroke-width="' + N(modul) + '"/>'
                 '<rect x="' + N(px(fc + 2)) + '" y="' + N(py(fr + 2)) + '" width="' + N(3 * modul)
                 + '" height="' + N(3 * modul) + '" rx="' + N(modul // 2) + '" fill="' + gelap + '"/>')
    sisi = (n + 2) * modul
    return ('<g id="kode-qr"><rect x="' + N(x) + '" y="' + N(y) + '" width="' + N(sisi)
            + '" height="' + N(sisi) + '" fill="' + terang + '"/><g fill="' + gelap + '">'
            + isi + '</g>' + mata + '</g>')

def lebah(x, y, px_):
    """Maskot lebah. Transform dibakar ke data path — tidak ada scale() tersisa,
    dan bidang() membuat bingkai grup terbaca bulat di Figma."""
    return ('<g id="maskot">' + bidang(px_, px_, x, y)
            + bakar_fragmen(LEBAH, px_ / 200.0, x, y) + '</g>')

def kepala_svg(judul, lebar_mm, tinggi_mm, isi):
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<svg xmlns="http://www.w3.org/2000/svg" width="' + str(lebar_mm) + 'mm" height="'
            + str(tinggi_mm) + 'mm" viewBox="0 0 ' + N(lebar_mm * S) + ' ' + N(tinggi_mm * S)
            + '" role="img" aria-label="' + judul + '">\n<title>' + judul + '</title>\n'
            '<desc>Akrilik 3 mm, cetak UV. 4 satuan = 1 mm. Lapisan POTONG magenta tidak dicetak.</desc>\n'
            + isi + '\n</svg>\n')

def sarang_def(warna, opasitas):
    return ('<pattern id="sarang" width="96" height="166" patternUnits="userSpaceOnUse">'
            '<g fill="none" stroke="' + warna + '" stroke-width="3" opacity="' + opasitas + '">'
            '<path d="M48 0L96 28V83L48 111L0 83V28Z"/>'
            '<path d="M0 83L48 111V166L0 194L-48 166V111Z"/>'
            '<path d="M96 83L144 111V166L96 194L48 166V111Z"/></g></pattern>')

# ================================================================ A · KOTAK TEMUAN
def standee_a():
    jalur = ('M86 150L214 150C236 150 250 164 250 186L250 190L340 190'
             'C340 128 376 84 430 84C484 84 514 128 514 190'
             'C534 190 550 206 550 226L550 754C550 774 534 790 514 790'
             'L86 790C66 790 50 774 50 754L50 186C50 166 66 150 86 150Z')
    d = ['<defs>'
         '<linearGradient id="badan" x1="0%" y1="0%" x2="30%" y2="100%">'
         '<stop offset="0%" stop-color="' + TEAL_T + '"/>'
         '<stop offset="55%" stop-color="' + TEAL + '"/>'
         '<stop offset="100%" stop-color="' + TEAL_X + '"/></linearGradient>'
         + sarang_def(CREAM, '0.1') + '</defs>']
    # tepi putih die-cut
    d.append('<g id="tepi-putih"><path d="' + jalur + '" fill="#FFFFFF" stroke="#FFFFFF" '
             'stroke-width="24" stroke-linejoin="round"/></g>')
    d.append('<g id="badan"><path d="' + jalur + '" fill="url(#badan)"/>'
             '<path d="' + jalur + '" fill="url(#sarang)"/></g>')
    # lidah folder
    d.append('<g id="lidah">' + teks(150, 178, 'KOTAK TEMUAN', 15, PJ, 700, 'rgba(251,248,243,.85)', 3)
             + '</g>')
    # kepala
    d.append('<g id="kepala">'
             '<path d="M300 206L336 227V269L300 290L264 269V227Z" fill="none" stroke="' + CREAM
             + '" stroke-width="8" stroke-linejoin="miter"/>'
             '<path d="M312 242L306 252H294L288 242L294 232H306Z" fill="' + EMAS_M + '"/>'
             + teks(300, 330, 'BALIKIN', 44, AR, 700, CREAM, 3)
             + teks(300, 356, 'Pindai untuk mencoba prototipenya', 16, PJ, 500, 'rgba(207,230,224,.85)')
             + '</g>')
    # panel QR
    d.append('<g id="panel-qr"><rect x="130" y="372" width="340" height="352" rx="26" fill="' + CREAM + '"/>'
             + qr_kotak(152, 390, 11) + teks(300, 710, 'balikin.id/prototipe', 16, PJ, 700, INK, 1) + '</g>')
    # keping pindai miring
    d.append('<g id="keping" transform="rotate(-9 122 384)">'
             '<path d="' + heks(122, 384, 54, 46) + '" fill="' + EMAS_M + '"/>'
             + teks(122, 378, 'PINDAI', 15, PJ, 700, INK, 1)
             + teks(122, 398, 'AKU', 15, AR, 700, INK, 1) + '</g>')
    # pita bawah
    d.append('<g id="pita">'
             '<path d="M50 738H550V754C550 774 534 790 514 790H86C66 790 50 774 50 754Z" fill="'
             + CREAM + '"/>'
             + teks(300, 772, 'Yang hilang, balik pulang.', 24, AR, 700, TEAL_X) + '</g>')
    d.append(lebah(346, 96, 168))
    d.append('<g id="POTONG"><path d="' + jalur + '" fill="none" stroke="' + POTONG
             + '" stroke-width="2"/></g>')
    return kepala_svg('Balikin — Standee QR A, Kotak Temuan', 150, 215, '\n'.join(d))

# ================================================================ B · SEL SARANG
def standee_b():
    jalur = ('M40 490L170 200L250 200C250 138 288 94 336 94C384 94 420 138 420 200'
             'L430 200L560 490L430 780L170 780Z')
    d = ['<defs>'
         '<linearGradient id="badan" x1="0%" y1="0%" x2="20%" y2="100%">'
         '<stop offset="0%" stop-color="' + CREAM + '"/>'
         '<stop offset="100%" stop-color="#EFE7D8"/></linearGradient>'
         + sarang_def(TEAL, '0.14') + '</defs>']
    d.append('<g id="tepi-putih"><path d="' + jalur + '" fill="#FFFFFF" stroke="#FFFFFF" '
             'stroke-width="26" stroke-linejoin="round"/></g>')
    d.append('<g id="badan"><path d="' + jalur + '" fill="url(#badan)"/>'
             '<path d="' + jalur + '" fill="url(#sarang)"/>'
             '<path d="' + jalur + '" fill="none" stroke="' + TEAL + '" stroke-width="7"/></g>')
    d.append('<g id="kepala">'
             + teks(300, 276, 'BALIKIN', 44, AR, 700, INK, 3)
             + teks(300, 302, 'PINDAI PROTOTIPENYA', 14, PJ, 700, TEAL, 4) + '</g>')
    d.append('<g id="panel-qr">'
             '<path d="' + heks(300, 490, 198, 170) + '" fill="' + TEAL + '"/>'
             '<path d="' + heks(300, 490, 178, 152) + '" fill="#FFFFFF"/>'
             + qr_kotak(192, 382, 8) + '</g>')
    d.append('<g id="pita">'
             '<rect x="150" y="656" width="300" height="52" rx="26" fill="' + TEAL + '"/>'
             + teks(300, 690, 'Yang hilang, balik pulang.', 22, AR, 700, CREAM)
             + teks(300, 736, 'balikin.id/prototipe', 16, PJ, 700, INK, 1) + '</g>')
    # sel kecil di sisi kiri dan kanan
    d.append('<g id="sel-kecil" opacity=".9">'
             '<path d="' + heks(96, 596, 34, 30) + '" fill="' + EMAS_M + '"/>'
             '<path d="' + heks(504, 596, 34, 30) + '" fill="' + MINT + '"/></g>')
    d.append(lebah(252, 96, 168))
    d.append('<g id="POTONG"><path d="' + jalur + '" fill="none" stroke="' + POTONG
             + '" stroke-width="2"/></g>')
    return kepala_svg('Balikin — Standee QR B, Sel Sarang', 150, 215, '\n'.join(d))

# ================================================================ dudukan
def dudukan():
    w, h = 100 * S, 24 * S
    jalur = ('M12 0H' + N(w - 12) + 'C' + N(w - 4) + ' 0 ' + N(w) + ' 4 ' + N(w) + ' 12L'
             + N(w) + ' ' + N(h - 12) + 'C' + N(w) + ' ' + N(h - 4) + ' ' + N(w - 4) + ' ' + N(h)
             + ' ' + N(w - 12) + ' ' + N(h) + 'H12C4 ' + N(h) + ' 0 ' + N(h - 4) + ' 0 '
             + N(h - 12) + 'L0 12C0 4 4 0 12 0Z')
    slot = ('<rect x="60" y="42" width="280" height="13" rx="6" fill="#FFFFFF" stroke="' + POTONG
            + '" stroke-width="2"/>')
    d = ['<g id="badan"><path d="' + jalur + '" fill="' + TEAL_X + '"/>' + slot + '</g>',
         '<g id="teks">' + teks(w // 2, 30, 'BALIKIN', 15, AR, 700, 'rgba(251,248,243,.5)', 3) + '</g>',
         '<g id="POTONG"><path d="' + jalur + '" fill="none" stroke="' + POTONG + '" stroke-width="2"/></g>']
    return kepala_svg('Balikin — Dudukan standee, slot 3,25 mm', 100, 24, '\n'.join(d))

if __name__ == '__main__':
    import re
    OUT = os.path.join(_here, 'svg')
    for nama, isi in (('standee-a-kotak-temuan', standee_a()),
                      ('standee-b-sel-sarang', standee_b()),
                      ('standee-dudukan', dudukan())):
        open(os.path.join(OUT, nama + '.svg'), 'w', encoding='utf-8').write(isi)
        sisa = sorted(set(re.findall(r'-?\d+\.\d+', isi)))
        print('%-28s %5d B  desimal: %s' % (nama + '.svg', len(isi), sisa or 'tidak ada'))
