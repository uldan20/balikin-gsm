# -*- coding: utf-8 -*-
"""X-banner E · Sarang sebagai SVG, 600 x 1600 mm.
Seluruh koordinat bilangan bulat: transform dibakar ke data path, tidak ada
scale() tersisa, dan tiap grup gambar diberi bidang tak terlihat supaya
bingkainya terbaca bulat di Figma."""
import os, math
from build import CREAM, INK, TEAL, TEALD, GOLD, GOLDL, MUTED, ICONS, LEBAH, AR, PJ, CV
from rapi import I, N, bakar_path, bakar_fragmen, hex6, bidang

OUT = os.path.dirname(os.path.abspath(__file__))
W, H = 600, 1600
E = lambda s: s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def txt(x, y, s, size, fam, weight=400, fill=CREAM, ls=0, anchor='start', op=None):
    return ('<text x="%s" y="%s" font-family="%s" font-size="%s" font-weight="%s" fill="%s"%s%s%s>%s</text>'
            ) % (N(x), N(y), fam, I(size), weight, fill,
                 (' letter-spacing="%s"' % N(ls)) if ls else '',
                 (' text-anchor="%s"' % anchor) if anchor != 'start' else '',
                 (' opacity="%s"' % op) if op else '', s)

def gambar(nama, frag, px, cx, cy, warna, sumber=100):
    """Tempel satu gambar pada ukuran px, berpusat di (cx,cy), transform dibakar."""
    s = px / float(sumber)
    x0, y0 = I(cx - px / 2), I(cy - px / 2)
    return ('<g id="%s" fill="none" stroke-linejoin="miter" stroke-miterlimit="8" '
            'style="color:%s">%s%s</g>'
            ) % (nama, warna, bidang(px, px, x0, y0), bakar_fragmen(frag, s, x0, y0))

L = []

# ---------- latar: sarang penuh ----------
S_LATAR, R_LATAR, BARIS = 75, 87, 130
sel_latar, k, y = [], 0, 0
while y < H + R_LATAR:
    y = R_LATAR + k * BARIS
    off = 0 if k % 2 == 0 else S_LATAR
    x = off - 2 * S_LATAR
    while x < W + 2 * S_LATAR:
        sel_latar.append(hex6(x, y, S_LATAR, R_LATAR)); x += 2 * S_LATAR
    k += 1
L.append('<g id="latar"><rect x="0" y="0" width="%d" height="%d" fill="%s"/>'
         '<g fill="none" stroke="%s" stroke-width="2" opacity="0.09">%s</g></g>'
         % (W, H, TEALD, CREAM, ''.join('<path d="%s"/>' % c for c in sel_latar)))

# ---------- kepala ----------
TANDA = ('<path d="M50 8L86.4 29V71L50 92L13.6 71V29Z" fill="none" stroke="%s" stroke-width="8" '
         'stroke-linejoin="miter"/><path d="M61 44L55.5 53.53H44.5L39 44L44.5 34.47H55.5Z" fill="%s"/>'
         ) % (CREAM, GOLD)
L.append('<g id="kepala">%s%s%s</g>' % (
  gambar('tanda-balikin', TANDA, 34, 63, 61, CREAM),
  txt(92, 73, 'BALIKIN', 31, AR, 700, CREAM, 2),
  txt(554, 72, 'KOMUNITAS SUKABUMI', 13, PJ, 600, CREAM, 3, 'end', '.55')))

# ---------- judul ----------
L.append('<g id="judul">%s%s%s</g>' % (
  bidang(330, 119, 46, 111),
  txt(46, 164, 'Yang hilang,', 58, AR, 700, CREAM, -2),
  txt(46, 218, 'balik pulang.', 58, AR, 700, GOLDL, -2)))

PARA = ['Satu sel hanya berdiri kalau sel di', 'sebelahnya ikut menahan. Begitu juga', 'kota.']
L.append('<g id="paragraf" opacity="0.8">%s%s</g>'
         % (bidang(330, 72, 46, 260),
            ''.join(txt(46, 276 + i * 26, t, 17, PJ, 400, CREAM) for i, t in enumerate(PARA))))

# ---------- tulisan tangan (satu-satunya yang dimiringkan) ----------
MK = ['Small', 'Things', 'Make a', 'Big Difference']
mk = bidang(180, 148, 0, -4)
mk += ''.join(txt(0, 22 + i * 30, t, 29, CV, 600, GOLDL) for i, t in enumerate(MK))
mk += ('<path d="M2 134C32 125 88 123 128 128c14 2 24 5 28 1" fill="none" stroke="%s" '
       'stroke-width="3" stroke-linecap="round"/>') % GOLDL
L.append('<g id="tulisan-tangan" transform="translate(404 205) rotate(-5)">%s</g>' % mk)

# ---------- sarang tengah + lebah ----------
CX, CY, S6, R6 = 300, 575, 64, 74
RING = [(-128, 0, 'wallet'), (128, 0, 'scan'), (-64, -111, 'camera'),
        (64, -111, 'bag'), (-64, 111, 'coin'), (64, 111, 'check')]
sel = ''.join(
  '<path d="%s" fill="%s" fill-opacity="0.07" stroke="%s" stroke-opacity="0.5" stroke-width="2"/>%s'
  % (hex6(CX + dx, CY + dy, S6, R6), CREAM, CREAM,
     gambar('ikon-' + n, ICONS[n], 54, CX + dx, CY + dy, '#CFE6E0'))
  for dx, dy, n in RING)
sel += '<path d="%s" fill="%s"/>' % (hex6(CX, CY, 69, 80), GOLD)
L.append('<g id="sarang">%s%s</g>' % (sel, gambar('lebah', LEBAH, 122, 300, 574, CREAM, 200)))

# ---------- temuan ----------
TEM = [[('Penemu barang kerap ragu bertindak — ', 0), ('takut', 1)],
       [('dituduh mencuri', 1), (', atau tidak tahu cara', 0)],
       [('mengembalikannya dengan aman.', 0)]]
def rich(x, y, parts, size, fill):
    return ('<text x="%s" y="%s" font-family="%s" font-size="%s" fill="%s">%s</text>'
            ) % (N(x), N(y), PJ, I(size), fill,
                 ''.join('<tspan font-weight="%d">%s</tspan>' % (700 if b else 400, E(t))
                         for t, b in parts))
L.append('<g id="temuan"><rect x="46" y="1176" width="508" height="148" fill="%s"/>%s%s</g>'
         % (CREAM, txt(70, 1215, 'TEMUAN AWAL', 11, PJ, 700, MUTED, 2),
            ''.join(rich(70, 1245 + i * 25, p, 17, INK) for i, p in enumerate(TEM))))

# ---------- kotak QR ----------
def qr_bulat(x, y, modul):
    n, seed, bit = 25, 0x9E3779B9, []
    for _ in range(n * n):
        seed = (seed * 1103515245 + 12345) & 0x7FFFFFFF
        bit.append((seed >> 17) & 1)
    def pojok(r, c): return (r < 8 and c < 8) or (r < 8 and c >= n - 8) or (r >= n - 8 and c < 8)
    px = lambda c: x + (c + 1) * modul
    py = lambda r: y + (r + 1) * modul
    isi = ''.join('<rect x="%s" y="%s" width="%s" height="%s"/>' % (px(c), py(r), modul, modul)
                  for r in range(n) for c in range(n) if not pojok(r, c) and bit[r * n + c])
    f = ''
    for fr, fc in ((0, 0), (0, n - 7), (n - 7, 0)):
        f += ('<rect x="%s" y="%s" width="%s" height="%s" fill="none" stroke="%s" stroke-width="%s"/>'
              '<rect x="%s" y="%s" width="%s" height="%s" fill="%s"/>'
              ) % (px(fc), py(fr), 7 * modul, 7 * modul, TEALD, modul,
                   px(fc + 2), py(fr + 2), 3 * modul, 3 * modul, TEALD)
    sisi = (n + 2) * modul
    return ('<g id="kode-qr"><rect x="%s" y="%s" width="%s" height="%s" fill="%s"/>'
            '<g fill="%s">%s</g>%s</g>') % (x, y, sisi, sisi, CREAM, TEALD, isi, f)

L.append('<g id="qr"><rect x="46" y="1346" width="508" height="142" fill="%s" fill-opacity="0.09" '
         'stroke="%s" stroke-opacity="0.22" stroke-width="2"/>%s%s%s%s</g>'
         % (CREAM, CREAM, qr_bulat(69, 1363, 4),
            txt(189, 1405, 'Masuk ke sarangnya.', 21, AR, 700, CREAM),
            txt(189, 1426, 'Prototipe Balikin — pindai di sini.', 14, PJ, 400, CREAM, 0, 'start', '.75'),
            txt(189, 1450, 'BALIKIN.ID', 13, PJ, 700, GOLDL, 2)))

# ---------- kredit ----------
L.append('<g id="kredit"><path d="M46 1512H554" stroke="%s" stroke-opacity="0.2" stroke-width="1"/>%s%s%s%s</g>'
         % (CREAM,
            txt(46, 1540, 'Uldan Pamungkas ·', 12, PJ, 400, CREAM, 0, 'start', '.6'),
            txt(46, 1558, '20210060127', 12, PJ, 400, CREAM, 0, 'start', '.6'),
            txt(554, 1540, 'Desain Komunikasi Visual · Universitas Nusa Putra', 12, PJ, 400, CREAM, 0, 'end', '.6'),
            txt(554, 1558, 'Sukabumi', 12, PJ, 400, CREAM, 0, 'end', '.6')))

svg = ('<?xml version="1.0" encoding="UTF-8"?>\n'
       '<svg xmlns="http://www.w3.org/2000/svg" width="600mm" height="1600mm" viewBox="0 0 600 1600" '
       'role="img" aria-label="X-banner Balikin versi Sarang">\n'
       '<title>X-Banner Balikin — Sarang</title>\n'
       '<desc>60 x 160 cm. 1 satuan = 1 mm. Seluruh koordinat bilangan bulat. '
       'Huruf: Archivo, Plus Jakarta Sans, Caveat.</desc>\n' + '\n'.join(L) + '\n</svg>\n')
open(os.path.join(OUT, 'xbanner-sarang.svg'), 'w', encoding='utf-8').write(svg)

import re
sisa = [m for m in re.findall(r'-?\d+\.\d+', svg)]
print('xbanner-sarang.svg — %d KB · angka berdesimal tersisa: %d %s'
      % (len(svg) // 1024, len(sisa), sorted(set(sisa))[:8]))
