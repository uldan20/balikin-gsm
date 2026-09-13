# -*- coding: utf-8 -*-
"""S2 Editorial dirombak — tiga arah latar, supergrafis, dan tata letak.

Isi teksnya sama persis dengan versi lama; yang diganti bidang latar, elemen
grafis besar, dan susunan blok. Layar ponsel tetap placeholder.
"""
import os, json, math
from kit import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's2')
AB = lambda **k: abs_p(**k)

def abs_p(x=None, y=None, r=None, b=None, w=None, h=None, z=1, lain=''):
    s = 'position:absolute;z-index:' + str(z) + ';'
    for k, v in (('left', x), ('top', y), ('right', r), ('bottom', b), ('width', w), ('height', h)):
        if v is not None:
            s += k + ':' + str(v) + 'px;'
    return s + lain

def dv(g, isi=''):
    return '<div style="' + g + '">' + isi + '</div>'

def tk(g, isi):
    return '<span style="' + g + '">' + isi + '</span>'

def ft(f, uk, tb=400, wr=CREAM, sp=None, th=None, rt=None):
    s = 'font-family:' + f + ';font-size:' + str(uk) + 'px;font-weight:' + str(tb) + ';color:' + wr + ';'
    if sp is not None: s += 'letter-spacing:' + str(sp) + 'px;'
    if th is not None: s += 'line-height:' + str(th) + ';'
    if rt: s += 'text-align:' + rt + ';'
    return s

def heks_d(cx, cy, sw, sh):
    p = [(cx, cy - sh), (cx + sw, cy - sh // 2), (cx + sw, cy + sh // 2),
         (cx, cy + sh), (cx - sw, cy + sh // 2), (cx - sw, cy - sh // 2)]
    return 'M' + 'L'.join(str(int(a)) + ' ' + str(int(b)) for a, b in p) + 'Z'

def lapis(isi, z=2):
    return ('<svg style="position:absolute;left:0;top:0;width:' + str(W) + 'px;height:' + str(H)
            + 'px;z-index:' + str(z) + '" viewBox="0 0 ' + str(W) + ' ' + str(H) + '" fill="none">'
            + isi + '</svg>')

# ---------------- isi bersama ----------------
META = [('UI/UX', 'Aplikasi Mobile'), ('Kategori', 'Lost &amp; Found'), ('Metode', 'Design Thinking')]
JUDUL = ['Barang yang', 'hilang punya', 'alamat pulang']
PARA = ('Balikin mempertemukan pemilik dan penemu lewat satu sistem — dengan verifikasi '
        'ciri rahasia, titik serah terima yang aman, dan reputasi yang tumbuh dari menolong.')
PROSES = ['Riset', 'Wireframe', 'Desain Antarmuka', 'Prototipe', 'Uji Usability']
SISI = [('Studi Kasus', 'Sukabumi'), ('Luaran', 'Prototipe Figma')]

def blok_meta(x, y, fg=CREAM, op='.55', jarak=90, z=6):
    return dv(abs_p(x=x, y=y, z=z, lain='display:flex;gap:' + str(jarak) + 'px;'),
              ''.join(dv('', dv(ft(PJ, 14, 400, 'rgba(251,248,243,' + op + ')') if fg == CREAM
                                else ft(PJ, 14, 400, 'rgba(18,51,44,.5)'), a)
                         + dv(ft(PJ, 16, 600, fg) + 'margin-top:3px;', b)) for a, b in META))

def blok_sisi(x=None, y=None, r=None, fg=CREAM, z=6, jarak=26):
    return dv(abs_p(x=x, y=y, r=r, z=z, lain='display:flex;flex-direction:column;gap:'
                    + str(jarak) + 'px;'),
              ''.join(dv('', dv(ft(PJ, 14, 400, 'rgba(251,248,243,.55)') if fg == CREAM
                                else ft(PJ, 14, 400, 'rgba(18,51,44,.5)'), a)
                         + dv(ft(PJ, 17, 600, fg) + 'margin-top:3px;', b)) for a, b in SISI))

# ================================================================ A · IRISAN 60°
def s2a():
    # tepi miring 30° — searah sisi heksagon
    miring = 'M0 1180L1122 520V1587H0Z'
    miring2 = 'M0 1320L1122 660V1587H0Z'
    halftone = ''
    for i in range(9):
        t = i / 8.0
        cx = int(120 + t * 900)
        cy = int(1180 - t * 660) - 44
        sw = int(46 - t * 34)
        halftone += ('<path d="' + heks_d(cx, cy, sw, int(sw * 1.15)) + '" fill="' + GOLDL
                     + '" opacity="' + str(round(.9 - t * .5, 2)) + '"/>')
    isi = [
      dv(abs_p(x=0, y=0, w=W, h=H, z=1,
               lain='background:linear-gradient(160deg,' + TEALB + ' 0%,' + TEAL + ' 38%,'
                    + TEALX + ' 100%);')),
      dv(abs_p(x=0, y=0, w=W, h=H, z=1, lain='overflow:hidden;'), sarang(CREAM, '.07', 3)),
      lapis('<path d="' + miring2 + '" fill="' + GOLD + '" opacity=".9"/>'
            '<path d="' + miring + '" fill="' + CREAM + '"/>' + halftone, z=2),
      # heksagon raksasa terpotong di kanan atas
      lapis('<path d="' + heks_d(1090, 250, 300, 345) + '" fill="none" stroke="' + CREAM
            + '" stroke-width="3" opacity=".28"/>'
            '<path d="' + heks_d(1090, 250, 200, 230) + '" fill="none" stroke="' + GOLDL
            + '" stroke-width="3" opacity=".4"/>', z=3),
      blok_meta(64, 56),
      dv(abs_p(r=64, y=54, z=6), logo(CREAM, GOLDL, 30, 1)),
      dv(abs_p(x=64, y=196, z=6, lain=ft(AR, 92, 700, CREAM, -4, .94)),
         JUDUL[0] + '<br>' + JUDUL[1] + '<br>'
         + tk('color:' + GOLDL + ';', JUDUL[2])),
      dv(abs_p(r=64, y=200, w=282, z=6, lain=ft(PJ, 19, 400, 'rgba(251,248,243,.92)', None, 1.5)), PARA),
      blok_sisi(x=64, y=560),
      dv(abs_p(x=316, y=640, z=7), ponsel(360, -6, layar_kosong('gelap'))),
      dv(abs_p(r=64, y=920, z=8, lain='display:flex;flex-direction:column;gap:10px;align-items:flex-end;'),
         ''.join(dv('display:flex;align-items:center;gap:12px;',
                    tk(ft(PJ, 19, 500, INK), t)
                    + dv('width:9px;height:10px;background:' + TEALX + ';' + HEX + 'flex:none;'))
                 for t in PROSES)),
      dv(abs_p(r=64, b=150, z=8, lain=ft(AR, 30, 700, INK, -1, 1.2, 'right')),
         'Yang hilang,<br>balik pulang.'),
      dv(abs_p(x=64, b=64, z=8), kaki(INK, '.7')),
    ]
    return ''.join(isi)

# ================================================================ B · SEL SARANG
def s2b():
    sel, w_, h_ = '', 132, 152                       # setengah lebar / setengah tinggi sel
    for baris in range(-1, 12):
        for kol in range(-1, 6):
            cx = kol * w_ * 2 + (w_ if baris % 2 else 0)
            cy = baris * int(h_ * 1.5)
            gelap = cy < 940
            garis = 'rgba(251,248,243,.16)' if gelap else 'rgba(18,51,44,.12)'
            sel += ('<path d="' + heks_d(cx, cy, w_, h_) + '" fill="none" stroke="' + garis
                    + '" stroke-width="3"/>')
    penuh = [(132, 304, MINT, '.16'), (924, 152, GOLD, '.8'), (660, 456, TEALB, '.45'),
             (0, 760, GOLDL, '.28'), (1056, 1064, TERRA, '.9'), (396, 1368, MINT, '.5'),
             (924, 1520, TEAL, '.9')]
    for cx, cy, c, op in penuh:
        sel += ('<path d="' + heks_d(cx, cy, 132, 152) + '" fill="' + c + '" opacity="' + op + '"/>')
    isi = [
      dv(abs_p(x=0, y=0, w=W, h=H, z=1,
               lain='background:linear-gradient(180deg,' + TEALX + ' 0%,' + TEAL + ' 44%,'
                    + '#CFE6E0 58%,' + CREAM + ' 100%);')),
      lapis(sel, z=2),
      blok_meta(64, 56),
      dv(abs_p(r=64, y=54, z=6), logo(CREAM, GOLDL, 30, 1)),
      # judul bertangga mengikuti offset sel
      dv(abs_p(x=64, y=190, z=6, lain=ft(AR, 88, 700, CREAM, -3, 1.02)), JUDUL[0]),
      dv(abs_p(x=132, y=282, z=6, lain=ft(AR, 88, 700, CREAM, -3, 1.02)), JUDUL[1]),
      dv(abs_p(x=200, y=374, z=6, lain=ft(AR, 88, 700, GOLDL, -3, 1.02)), JUDUL[2]),
      dv(abs_p(r=64, y=196, w=270, z=6, lain=ft(PJ, 18, 400, 'rgba(251,248,243,.88)', None, 1.5)), PARA),
      blok_sisi(x=64, y=520),
      # ponsel duduk di jendela heksagon
      lapis('<path d="' + heks_d(561, 998, 336, 386) + '" fill="' + CREAM + '" opacity=".14"/>'
            '<path d="' + heks_d(561, 998, 336, 386) + '" fill="none" stroke="' + GOLDL
            + '" stroke-width="4" opacity=".75"/>', z=3),
      dv(abs_p(x=381, y=640, z=7), ponsel(360, 0, layar_kosong('gelap'))),
      dv(abs_p(x=64, y=1280, z=8, lain='display:flex;flex-wrap:wrap;gap:9px;width:290px;'),
         ''.join(dv('background:rgba(18,51,44,.07);border-radius:16px;padding:6px 14px;'
                    + ft(PJ, 16, 600, INK), t) for t in PROSES)),
      dv(abs_p(r=64, y=1290, z=8, lain=ft(AR, 32, 700, INK, -1.4, 1.15, 'right')),
         'Yang hilang,<br>balik pulang.'),
      dv(abs_p(x=64, b=64, z=8), kaki(INK, '.7')),
    ]
    return ''.join(isi)

# ================================================================ C · JEJAK
def s2c():
    jejak = 'M-40 470C240 470 300 690 560 690C820 690 900 1180 1180 1180'
    penanda = ''
    for t, sw in ((0.12, 16), (0.36, 22), (0.62, 18), (0.88, 26)):
        x = int(-40 + t * 1220)
        y = int(470 + (t ** 1.6) * 710)
        penanda += ('<path d="' + heks_d(x, y, sw, int(sw * 1.15)) + '" fill="' + GOLDL + '"/>')
    cincin = ''
    for r_, op in ((430, '.5'), (330, '.28'), (230, '.16')):
        cincin += ('<path d="' + heks_d(561, 980, r_, int(r_ * 1.15)) + '" fill="none" stroke="'
                   + GOLDL + '" stroke-width="3" opacity="' + op + '"/>')
    isi = [
      dv(abs_p(x=0, y=0, w=W, h=H, z=1,
               lain='background:radial-gradient(120% 80% at 50% 62%,' + TEAL + ' 0%,'
                    + TEALX + ' 58%,#07302A 100%);')),
      dv(abs_p(x=0, y=0, w=W, h=H, z=1, lain='overflow:hidden;'), sarang(CREAM, '.06', 4)),
      lapis(cincin, z=2),
      lapis('<path d="' + jejak + '" stroke="' + GOLDL + '" stroke-width="5" fill="none" '
            'stroke-dasharray="3 26" stroke-linecap="round" opacity=".8"/>' + penanda, z=3),
      # pita judul miring
      dv(abs_p(x=-30, y=250, w=1182, z=5,
               lain='background:' + CREAM + ';transform:rotate(-4deg);padding:26px 94px;'
                    'box-sizing:border-box;'),
         dv(ft(AR, 84, 700, INK, -3, .98), JUDUL[0] + ' ' + JUDUL[1]
            + ' ' + tk('color:' + TEAL + ';', JUDUL[2]))),
      blok_meta(64, 56),
      dv(abs_p(r=64, y=54, z=6), logo(CREAM, GOLDL, 30, 1)),
      dv(abs_p(x=64, y=520, w=272, z=6, lain=ft(PJ, 18, 400, 'rgba(251,248,243,.88)', None, 1.5)), PARA),
      blok_sisi(r=64, y=520),
      dv(abs_p(x=396, y=596, z=7), ponsel(330, 0, layar_kosong('gelap'))),
      dv(abs_p(r=64, y=1100, z=8), bee(118, 14)),
      # proses jadi deret mendatar bernomor
      dv(abs_p(x=64, b=196, w=994, z=8, lain='display:flex;justify-content:space-between;'),
         ''.join(dv('text-align:center;',
                    dv('width:34px;height:39px;background:rgba(243,215,124,.16);' + HEX
                       + 'display:grid;place-items:center;margin:0 auto;',
                       tk(ft(AR, 16, 700, GOLDL), '0' + str(i + 1)))
                    + dv(ft(PJ, 16, 500, 'rgba(251,248,243,.85)') + 'margin-top:10px;', t))
                  for i, t in enumerate(PROSES))),
      dv(abs_p(x=0, w=W, b=136, z=8, lain=ft(AR, 32, 700, GOLDL, -1.2, 1, 'center')),
         'Yang hilang, balik pulang.'),
      dv(abs_p(x=64, b=64, z=8), kaki(CREAM, '.66')),
    ]
    return ''.join(isi)

def bungkus(isi):
    return ('<div style="width:' + str(W) + 'px;height:' + str(H) + 'px;position:relative;'
            'overflow:hidden;background:' + CREAM + '">' + isi + '</div>')

for nama, f, judul in (('Main', s2a, 'S2a · Irisan 60°'), ('S2b', s2b, 'S2b · Sel Sarang'),
                       ('S2c', s2c, 'S2c · Jejak')):
    open(os.path.join(OUT, nama + '.dc.html'), 'w', encoding='utf-8').write(doc(bungkus(f()), CREAM))
    print(nama + '.dc.html —', judul)

kanvas = {"artboards": [
  {"file": "Main.dc.html", "x": 0, "y": 0, "w": W, "h": H, "title": "S2a · Irisan 60°"},
  {"file": "S2b.dc.html", "x": 1280, "y": 0, "w": W, "h": H, "title": "S2b · Sel Sarang"},
  {"file": "S2c.dc.html", "x": 2560, "y": 0, "w": W, "h": H, "title": "S2c · Jejak"}],
 "annotations": [{"id": "catatan", "x": 0, "y": -190, "w": 960,
   "text": "S2 Editorial dirombak — tiga arah latar, supergrafis, dan tata letak. "
           "Isi teks sama persis dengan versi lama.\nSemua supergrafis dibangun dari kisi 60°: "
           "irisan miring 30°, kisi sel sarang, dan cincin heksagon.\nLayar ponsel masih "
           "placeholder — tinggal ditempel tangkapan layar Jelajahi."}],
 "launch": {"view": "canvas"}}
open(os.path.join(OUT, 'canvas.json'), 'w', encoding='utf-8').write(
    json.dumps(kanvas, indent=2, ensure_ascii=False))
print('canvas.json')
