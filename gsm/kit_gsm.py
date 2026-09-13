# -*- coding: utf-8 -*-
"""Perkakas halaman GSM — A5 lanskap 210 x 148 mm, 4 satuan = 1 mm (840 x 592).

Gaya mengikuti poster showcase: bidang besar, tipografi tegas, heksagon, dan
banyak ruang kosong. Isi teks masih placeholder; yang dikunci tata letaknya.
"""
import os, sys
_here = os.path.dirname(os.path.abspath(__file__))
for sub in ('xbanner', 'infografis'):
    sys.path.insert(0, os.path.join(_here, '..', sub))
from build import AR, PJ, CV, FONTS
from ikon import IKON

W, H = 840, 592
M = 48                                   # margin 12 mm

CREAM, PUTIH, INK = '#FBF8F3', '#FFFFFF', '#12332C'
FILL, GARIS, REDUP = '#F1ECE3', '#E2DCD0', '#6B8A81'
TEAL, TEAL_T, TEAL_G, TEAL_X = '#1B7A63', '#25946F', '#0F5A48', '#0B4638'
MINT, MINT_M, EMAS, EMAS_M, TERRA = '#8FD4C4', '#CFE6E0', '#C8952E', '#F3D77C', '#C05C33'
HEKS = 'clip-path:polygon(25% 0,75% 0,100% 50%,75% 100%,25% 100%,0 50%);'
HEKS_T = 'clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%);'

def P(x=None, y=None, w=None, h=None, z=None, r=None, b=None, lain=''):
    s = 'position:absolute;'
    for k, v in (('left', x), ('top', y), ('right', r), ('bottom', b), ('width', w), ('height', h)):
        if v is not None:
            s += k + ':' + str(v) + 'px;'
    if z is not None:
        s += 'z-index:' + str(z) + ';'
    return s + lain

def dv(g, isi=''):
    return '<div style="' + g + '">' + isi + '</div>'

def tk(g, isi):
    return '<span style="' + g + '">' + isi + '</span>'

def font(f, uk, tb=400, w=INK, sp=None, th=None, rt=None):
    s = 'font-family:' + f + ';font-size:' + str(uk) + 'px;font-weight:' + str(tb) + ';color:' + w + ';'
    if sp is not None: s += 'letter-spacing:' + str(sp) + 'px;'
    if th is not None: s += 'line-height:' + str(th) + ';'
    if rt: s += 'text-align:' + rt + ';'
    return s

def ik(n, px, c):
    return ('<svg width="' + str(px) + '" height="' + str(px) + '" viewBox="0 0 100 100" fill="none" '
            'stroke-linejoin="miter" stroke-miterlimit="8" style="color:' + c + ';display:block">'
            + IKON[n] + '</svg>')

def sarang(warna=TEAL, op='.08', k=2):
    w, h = 52 * k, 90 * k
    P_ = lambda pts: 'M' + 'L'.join(str(x * k) + ' ' + str(y * k) for x, y in pts) + 'Z'
    sel = [P_([(26,0),(52,15),(52,45),(26,60),(0,45),(0,15)]),
           P_([(0,45),(26,60),(26,90),(0,105),(-26,90),(-26,60)]),
           P_([(52,45),(78,60),(78,90),(52,105),(26,90),(26,60)])]
    pid = 'sr' + str(k) + warna.replace('#', '')
    return ('<svg style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none" '
            'aria-hidden="true"><defs><pattern id="' + pid + '" width="' + str(w) + '" height="'
            + str(h) + '" patternUnits="userSpaceOnUse"><g fill="none" stroke="' + warna
            + '" stroke-width="2" opacity="' + op + '">'
            + ''.join('<path d="' + c + '"/>' for c in sel) + '</g></pattern></defs>'
            '<rect width="100%" height="100%" fill="url(#' + pid + ')"/></svg>')

# ---------------- bagian halaman ----------------
def lambang(px, warna=TEAL, aksen=EMAS):
    t = max(4, px // 12)
    return ('<svg width="' + str(px) + '" height="' + str(int(px * 1.12)) + '" viewBox="0 0 100 112" '
            'fill="none" style="display:block"><path d="M50 8L86 30V82L50 104L14 82V30Z" stroke="'
            + warna + '" stroke-width="' + str(t) + '" stroke-linejoin="miter"/>'
            '<path d="M61 50L55 60H45L39 50L45 40H55Z" fill="' + aksen + '"/></svg>')

def kepala(bab, hal, fg=REDUP):
    kiri = dv(P(x=M, y=30, z=9, lain=font(PJ, 9, 700, fg, 3)), bab.upper())
    kanan = dv(P(r=M, y=26, z=9, lain=font(AR, 13, 700, fg, 1)), str(hal).zfill(2))
    return kiri + kanan

def judul_bagian(no, judul, sub=None, y=74, warna=INK, aksen=TEAL):
    o = dv(P(x=M, y=y, z=6, lain='display:flex;align-items:center;gap:12px;'),
           dv('width:28px;height:32px;background:' + aksen + ';' + HEKS
              + 'display:grid;place-items:center;flex:none;', tk(font(AR, 13, 700, PUTIH), no))
           + tk(font(AR, 30, 700, warna, -1), judul))
    if sub:
        o += dv(P(x=M, y=y + 48, w=520, z=6, lain=font(PJ, 13, 400, REDUP, None, 1.5)), sub)
    return o

def label(x, y, t, warna=REDUP, sp=3, uk=9):
    return dv(P(x=x, y=y, z=6, lain=font(PJ, uk, 700, warna, sp)), t.upper())

def kotak(x, y, w, h, isi='', bg=PUTIH, radius=14, z=5, lain=''):
    bayang = '' if 'box-shadow' in lain else 'box-shadow:0 10px 26px rgba(12,40,36,.07);'
    return dv(P(x=x, y=y, w=w, h=h, z=z,
                lain='background:' + bg + ';border-radius:' + str(radius) + 'px;box-sizing:border-box;'
                     'overflow:hidden;' + bayang + lain), isi)

def catatan(x, y, w, judul, isi, warna=INK):
    return dv(P(x=x, y=y, w=w, z=6),
              dv(font(AR, 13, 700, warna, -.2) + 'margin-bottom:5px;', judul)
              + dv(font(PJ, 11, 400, REDUP, None, 1.45), isi))

def ponsel(x, y, w, z=5, layar=None, rot=0):
    h = int(round(w * 2.05)); r = max(8, w // 7); b = max(4, w // 24)
    isi = layar if layar is not None else dv('width:100%;height:100%;background:linear-gradient(170deg,'
                                             + MINT_M + ' 0%,' + CREAM + ' 60%,' + FILL + ' 100%);')
    return dv(P(x=x, y=y, w=w, h=h, z=z,
                lain='background:' + INK + ';border-radius:' + str(r) + 'px;padding:' + str(b)
                     + 'px;box-shadow:0 12px 26px rgba(12,40,36,.2);transform:rotate(' + str(rot)
                     + 'deg);box-sizing:border-box;'),
              dv('width:100%;height:100%;border-radius:' + str(r - b) + 'px;overflow:hidden;', isi))

BAB_WARNA = [TEAL_T, TEAL, EMAS, TERRA]
BAB_ANGKA = ['I', 'II', 'III', 'IV']

def bidang_miring(sisi='kanan'):
    """Irisan 30° — sudut yang sama dengan sisi heksagon."""
    if sisi == 'kanan':
        return 'clip-path:polygon(840px 107px,840px 592px,0px 592px);'
    return 'clip-path:polygon(0px 107px,0px 592px,840px 592px);'

def latar_halaman(bab_idx, hantu='', sisi='kanan'):
    """Supergrafis halaman: bidang miring bertekstur sarang + angka hantu."""
    warna = BAB_WARNA[bab_idx]
    pot = bidang_miring(sisi)
    lapis = dv(P(x=0, y=0, w=W, h=H, z=1, lain='background:' + warna + ';opacity:.07;' + pot))
    pola = dv(P(x=0, y=0, w=W, h=H, z=1, lain=pot + 'overflow:hidden;'), sarang(warna, '.16', 2))
    tepi = dv(P(x=0, y=0, w=W, h=H, z=1, lain='overflow:hidden;'),
              '<svg width="' + str(W) + '" height="' + str(H) + '" viewBox="0 0 ' + str(W) + ' '
              + str(H) + '" fill="none" style="display:block">'
              + ('<path d="M840 107L0 592" stroke="' + warna + '" stroke-width="2" opacity=".3"/>'
                 if sisi == 'kanan' else
                 '<path d="M0 107L840 592" stroke="' + warna + '" stroke-width="2" opacity=".3"/>')
              + '</svg>')
    ang = ''
    if hantu:
        hx = (W - 210) if sisi == 'kiri' else -30
        ang = dv(P(x=hx, y=262, z=1, lain=font(AR, 300, 700, warna, -14, 1) + 'opacity:.06;'), hantu)
    return lapis + pola + tepi + ang

def garis_kepala(bab_idx):
    """Penanda heksagon + garis rambut di bawah kepala halaman."""
    warna = BAB_WARNA[bab_idx]
    return (dv(P(x=M - 22, y=27, w=12, h=14, z=7, lain='background:' + warna + ';' + HEKS))
            + dv(P(x=M, r=M, y=50, h=1, z=4, lain='background:' + warna + ';opacity:.28;')))

def indeks_tepi(bab_idx):
    """Penanda bab di tepi kanan — bertingkat, jadi terlihat waktu buku ditutup."""
    warna = BAB_WARNA[bab_idx]
    y = 72 + bab_idx * 124
    return (dv(P(r=0, y=y, w=16, h=112, z=4, lain='background:' + warna + ';'))
            + dv(P(r=0, y=y + 44, w=16, z=5,
                   lain=font(AR, 11, 700, PUTIH, 1, 1, 'center')), BAB_ANGKA[bab_idx]))

def halaman(isi, latar=CREAM, lain=''):
    return ('<div style="width:' + str(W) + 'px;height:' + str(H) + 'px;position:relative;'
            'overflow:hidden;background:' + latar + ';' + lain + '">' + isi + '</div>')

def doc_gsm(root, latar=CREAM):
    return ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
            '  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n  ' + FONTS
            + '\n  <style>\n    body { margin: 0; font-family: ' + PJ + '; background: ' + latar + '; }\n'
            '  </style>\n</helmet>\n' + root + '\n</x-dc>\n</body>\n</html>\n')

def tulis(nama, isi, latar=CREAM):
    open(os.path.join(_here, nama), 'w', encoding='utf-8').write(doc_gsm(isi, latar))
