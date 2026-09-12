# -*- coding: utf-8 -*-
"""Bangun versi SVG dari X-banner E · Sarang, pada ukuran cetak 600 x 1600 mm."""
import os, math, json
from build import (CREAM, INK, TEAL, TEALD, GOLD, GOLDL, TERRA, WASH, MUTED, FILL,
                   ICONS, LEBAH, hexpath, qr, AR, PJ, CV)

OUT = os.path.dirname(os.path.abspath(__file__))
W, H = 600, 1600
E = lambda s: (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))

def txt(x, y, s, size, fam, weight=400, fill=CREAM, ls=0, anchor='start', op=None):
    a = ' text-anchor="%s"' % anchor if anchor != 'start' else ''
    l = ' letter-spacing="%s"' % ls if ls else ''
    o = ' opacity="%s"' % op if op else ''
    return ('<text x="%s" y="%s" font-family="%s" font-size="%s" font-weight="%s" '
            'fill="%s"%s%s%s>%s</text>') % (x, y, fam, size, weight, fill, l, a, o, s)

def icon(cx, cy, name, px, color):
    return ('<g transform="translate(%s,%s) scale(%s)" fill="none" stroke-linejoin="miter" '
            'stroke-miterlimit="8" style="color:%s">%s</g>'
            ) % (round(cx-px/2, 2), round(cy-px/2, 2), round(px/100.0, 4), color, ICONS[name])

# ---- latar: sarang penuh ----
def comb_paths(r):
    cells, k, y = [], 0, 0.0
    s = r * math.sqrt(3)
    while y < H + r:
        y = r + k * 1.5 * r
        off = 0 if k % 2 == 0 else s / 2
        x = off - s
        while x < W + s:
            cells.append(hexpath(round(x, 1), round(y, 1), r)); x += s
        k += 1
    return cells

L = []
L.append('<g id="latar"><rect width="%d" height="%d" fill="%s"/>' % (W, H, TEALD))
L.append('<g fill="none" stroke="%s" stroke-width="1.6" opacity="0.11">%s</g></g>'
         % (CREAM, ''.join('<path d="%s"/>' % c for c in comb_paths(86))))

# ---- kepala ----
L.append('<g id="kepala">'
 '<path d="M50 8L86.4 29V71L50 92L13.6 71V29Z" fill="none" stroke="%s" stroke-width="8" '
 'stroke-linejoin="miter" transform="translate(46,44) scale(0.34)"/>'
 '<path d="M61 44L55.5 53.53H44.5L39 44L44.5 34.47H55.5Z" fill="%s" transform="translate(46,44) scale(0.34)"/>'
 '%s%s</g>' % (CREAM, GOLD,
   txt(92, 73.4, 'BALIKIN', 31, AR, 700, CREAM, '1.7'),
   txt(554, 71.9, 'KOMUNITAS SUKABUMI', 13, PJ, 600, CREAM, '2.6', 'end', '.55')))

# ---- judul ----
L.append('<g id="judul">%s%s</g>' % (
  txt(46, 164.5, 'Yang hilang,', 58, AR, 700, CREAM, '-2.3'),
  txt(46, 218.4, 'balik pulang.', 58, AR, 700, GOLDL, '-2.3')))

PARA = ['Satu sel hanya berdiri kalau sel di', 'sebelahnya ikut menahan. Begitu juga', 'kota.']
L.append('<g id="paragraf" opacity="0.8">%s</g>' % ''.join(
  txt(46, 276.1 + i*25.5, t, 17, PJ, 400, CREAM) for i, t in enumerate(PARA)))

# ---- tulisan tangan ----
MK = ['Small', 'Things', 'Make a', 'Big Difference']
mk = ''.join(txt(0, 22 + i*29.6, t, 29, CV, 600, GOLDL) for i, t in enumerate(MK))
mk += ('<path d="M2 134C32 125 88 123 128 128c14 2 24 5 28 1" fill="none" stroke="%s" '
       'stroke-width="2.6" stroke-linecap="round"/>') % GOLDL
L.append('<g id="tulisan-tangan" transform="translate(404,205) rotate(-5)">%s</g>' % mk)

# ---- sarang tengah + lebah ----
CX, CY, R = 300, 575.4, 74
RING = [(-128.2, 0, 'wallet'), (128.2, 0, 'scan'), (-64.1, -111, 'camera'),
        (64.1, -111, 'bag'), (-64.1, 111, 'coin'), (64.1, 111, 'check')]
sel = ''.join('<path d="%s" fill="%s" fill-opacity="0.07" stroke="%s" stroke-opacity="0.5" '
              'stroke-width="2.4"/>%s' % (hexpath(CX+dx, CY+dy, R), CREAM, CREAM,
                                          icon(CX+dx, CY+dy, n, 54, '#CFE6E0'))
              for dx, dy, n in RING)
sel += '<path d="%s" fill="%s"/>' % (hexpath(CX, CY, R+6), GOLD)
L.append('<g id="sarang">%s<g id="lebah" transform="translate(239,513.4) scale(0.61)">%s</g></g>'
         % (sel, LEBAH))

# ---- temuan ----
TEM = [[('Penemu barang kerap ragu bertindak — ', 0), ('takut', 1)],
       [('dituduh mencuri', 1), (', atau tidak tahu cara', 0)],
       [('mengembalikannya dengan aman.', 0)]]
def rich(x, y, parts, size, fill):
    sp = ''.join('<tspan font-weight="%d">%s</tspan>' % (700 if b else 400, E(t)) for t, b in parts)
    return ('<text x="%s" y="%s" font-family="%s" font-size="%s" fill="%s">%s</text>'
            ) % (x, y, PJ, size, fill, sp)
L.append('<g id="temuan"><rect x="46" y="1175.9" width="508" height="148.1" fill="%s"/>%s%s</g>'
         % (CREAM, txt(70, 1214.7, 'TEMUAN AWAL', 11, PJ, 700, MUTED, '2.2'),
            ''.join(rich(70, 1245.2 + i*25.4, p, 17.5, INK) for i, p in enumerate(TEM))))

# ---- kotak QR ----
def qr_svg(x, y, px, dark, light):
    N, seed, bits = 25, 0x9E3779B9, []
    for _ in range(N*N):
        seed = (seed * 1103515245 + 12345) & 0x7FFFFFFF
        bits.append((seed >> 17) & 1)
    def fnd(r, c): return (r < 8 and c < 8) or (r < 8 and c >= N-8) or (r >= N-8 and c < 8)
    cells = ''.join('<rect x="%d" y="%d" width="1" height="1"/>' % (c, r)
                    for r in range(N) for c in range(N) if not fnd(r, c) and bits[r*N+c])
    f = ''
    for fr, fc in ((0,0), (0,N-7), (N-7,0)):
        f += ('<rect x="%.1f" y="%.1f" width="6" height="6" fill="none" stroke="%s" stroke-width="1"/>'
              '<rect x="%d" y="%d" width="3" height="3" fill="%s"/>') % (fc+.5, fr+.5, dark, fc+2, fr+2, dark)
    sc = px / float(N + 2)
    return ('<g id="kode-qr" transform="translate(%s,%s) scale(%s)">'
            '<rect x="-1" y="-1" width="%d" height="%d" fill="%s"/>'
            '<g fill="%s">%s</g>%s</g>') % (x, y, round(sc, 5), N+2, N+2, light, dark, cells, f)

qrsvg = qr_svg(69, 1367, 100, TEALD, CREAM)
L.append('<g id="qr"><rect x="46" y="1346" width="508" height="142" fill="%s" fill-opacity="0.09" '
         'stroke="%s" stroke-opacity="0.22" stroke-width="1.5"/>%s%s%s%s</g>'
         % (CREAM, CREAM, qrsvg,
            txt(189, 1405.2, 'Masuk ke sarangnya.', 21, AR, 700, CREAM, '-.4'),
            txt(189, 1426.1, 'Prototipe Balikin — pindai di sini.', 14, PJ, 400, CREAM, 0, 'start', '.75'),
            txt(189, 1449.7, 'BALIKIN.ID', 12.5, PJ, 700, GOLDL, '1.75')))

# ---- kredit ----
L.append('<g id="kredit"><path d="M46 1512H554" stroke="%s" stroke-opacity="0.2" stroke-width="1"/>'
         '%s%s%s%s</g>' % (CREAM,
   txt(46, 1540, 'Uldan Pamungkas ·', 12.5, PJ, 400, CREAM, 0, 'start', '.6'),
   txt(46, 1557.5, '20210060127', 12.5, PJ, 400, CREAM, 0, 'start', '.6'),
   txt(554, 1540, 'Desain Komunikasi Visual · Universitas Nusa Putra', 12.5, PJ, 400, CREAM, 0, 'end', '.6'),
   txt(554, 1557.5, 'Sukabumi', 12.5, PJ, 400, CREAM, 0, 'end', '.6')))

svg = ('<?xml version="1.0" encoding="UTF-8"?>\n'
       '<svg xmlns="http://www.w3.org/2000/svg" width="600mm" height="1600mm" '
       'viewBox="0 0 600 1600" role="img" aria-label="X-banner Balikin versi Sarang">\n'
       '<title>X-Banner Balikin — Sarang</title>\n'
       '<desc>60 x 160 cm. 1 satuan = 1 mm. Huruf: Archivo, Plus Jakarta Sans, Caveat.</desc>\n'
       + '\n'.join(L) + '\n</svg>\n')
open(os.path.join(OUT, 'xbanner-sarang.svg'), 'w', encoding='utf-8').write(svg)
print('xbanner-sarang.svg — %d KB' % (len(svg)//1024))
