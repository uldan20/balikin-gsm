# -*- coding: utf-8 -*-
"""Perkakas halaman GSM Balikin — register editorial: bersih, modern, tebal.

Acuan: presentasi brand identity di Behance. Tipografi besar bercampur
(Archivo tebal + Archivo miring + Caveat), ruang kosong murah hati, blok warna
penuh halaman, kartu bersudut membulat besar, dan supergrafis heksagon yang
keluar tepi halaman.

A5 lanskap 210 x 148 mm, 4 satuan = 1 mm (840 x 592).
"""
import os, sys
_here = os.path.dirname(os.path.abspath(__file__))
DIR = _here
for _sub in ('xbanner', 'infografis'):
    sys.path.insert(0, os.path.join(_here, '..', _sub))
from build import AR, PJ, CV, LEBAH
from ikon import IKON

W, H = 840, 592
M = 56                                     # tepi halaman
KOL = W - M * 2                            # 728 — lebar isi

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Archivo:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&'
         'family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&'
         'family=Caveat:wght@500;600;700&display=swap">')

# ----------------------------------------------------------------- warna
KRIM, KRIM_2, KRIM_3 = '#FBF8F3', '#F2ECE1', '#E8E0D1'
PUTIH = '#FFFFFF'
INK, REDUP, GARIS = '#12332C', '#6E8078', '#E2DACB'
TEAL, TEAL_T, TEAL_G, TEAL_X = '#1B7A63', '#25946F', '#0F5A48', '#0B4638'
MINT, MINT_M = '#8FD4C4', '#CFE6E0'
EMAS, EMAS_M, EMAS_X = '#C8952E', '#F3D77C', '#A87722'
TERRA, TERRA_M, TERRA_X = '#C05C33', '#EDCFC2', '#A2421D'

HEKS = 'clip-path:polygon(25% 0,75% 0,100% 50%,75% 100%,25% 100%,0 50%);'
HEKS_T = 'clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%);'

def rgba(hx, a):
    h = hx.lstrip('#')
    return 'rgba(%d,%d,%d,%s)' % (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)

# ----------------------------------------------------------------- dasar
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

def font(f, uk, tb=400, w=INK, sp=None, th=None, rt=None, miring=False):
    s = 'font-family:' + f + ';font-size:' + str(uk) + 'px;font-weight:' + str(tb) + ';color:' + w + ';'
    if sp is not None: s += 'letter-spacing:' + str(sp) + 'px;'
    if th is not None: s += 'line-height:' + str(th) + ';'
    if rt: s += 'text-align:' + rt + ';'
    if miring: s += 'font-style:italic;'
    return s

def ik(n, px, c):
    return ('<svg width="' + str(px) + '" height="' + str(px) + '" viewBox="0 0 100 100" fill="none" '
            'stroke-linejoin="miter" stroke-miterlimit="8" style="color:' + c + ';display:block">'
            + IKON[n] + '</svg>')

def bee(px, rot=0):
    return ('<svg width="' + str(px) + '" height="' + str(px) + '" viewBox="0 0 200 200" '
            'style="display:block;transform:rotate(' + str(rot) + 'deg)">' + LEBAH + '</svg>')

# ----------------------------------------------------------------- tekstur
def _pola(pid, uw, uh, dalam, w, h):
    """Bungkus satu ubin pola. Ukurannya ditulis tegas dan kotak isiannya diberi
    jangkar x/y — kalau dibiarkan 100% pola hilang waktu halaman diekspor ke SVG."""
    return ('<svg width="%d" height="%d" viewBox="0 0 %d %d" '
            'style="position:absolute;left:0;top:0;pointer-events:none" aria-hidden="true">'
            '<defs><pattern id="%s" width="%d" height="%d" patternUnits="userSpaceOnUse">%s'
            '</pattern></defs><rect x="0" y="0" width="%d" height="%d" fill="url(#%s)"/></svg>'
            % (w, h, w, h, pid, uw, uh, dalam, w, h, pid))

def sarang(warna=TEAL, op='.1', k=2, tebal=2, w=W, h=H):
    """Pola sarang lebah — supergrafis latar. Selalu transparan."""
    uw, uh = 52 * k, 90 * k
    Pp = lambda pts: 'M' + 'L'.join(str(x * k) + ' ' + str(y * k) for x, y in pts) + 'Z'
    sel = [Pp([(26, 0), (52, 15), (52, 45), (26, 60), (0, 45), (0, 15)]),
           Pp([(0, 45), (26, 60), (26, 90), (0, 105), (-26, 90), (-26, 60)]),
           Pp([(52, 45), (78, 60), (78, 90), (52, 105), (26, 90), (26, 60)])]
    dalam = ('<g fill="none" stroke="' + warna + '" stroke-width="' + str(tebal) + '" opacity="'
             + op + '">' + ''.join('<path d="' + c + '"/>' for c in sel) + '</g>')
    return _pola('sr' + str(k) + str(tebal) + warna.replace('#', ''), uw, uh, dalam, w, h)

def halftone(warna=TEAL, op='.1', jarak=7, r=1, w=W, h=H):
    dalam = ('<circle cx="%d" cy="%d" r="%d" fill="%s" opacity="%s"/>' % (r, r, r, warna, op))
    return _pola('ht' + str(jarak) + str(r) + warna.replace('#', ''), jarak, jarak, dalam, w, h)

# ----------------------------------------------------------------- supergrafis
def heks_path(d):
    """Jalur heksagon runcing-atas selebar d, tinggi 4/3 d."""
    h = d * 4 // 3
    return ('M%d 0L%d %dV%dL%d %dL0 %dV%dZ'
            % (d // 2, d, h // 4, h * 3 // 4, d // 2, h, h * 3 // 4, h // 4))

def heks(x=None, y=None, d=200, warna=TEAL, tebal=0, op='1', z=1, r=None, b=None):
    """Heksagon besar — padat kalau tebal=0, bergaris kalau tebal>0. Boleh keluar tepi."""
    h = d * 4 // 3
    svg = ('<svg width="%d" height="%d" viewBox="0 0 %d %d" fill="none" '
           'style="display:block;opacity:%s"><path d="%s" fill="%s" stroke="%s" '
           'stroke-width="%d" stroke-linejoin="miter"/></svg>'
           % (d, h, d, h, op, heks_path(d), 'none' if tebal else warna,
              warna if tebal else 'none', tebal))
    return dv(P(x=x, y=y, z=z, r=r, b=b), svg)

def cincin(x=None, y=None, d=200, warna=TEAL, tebal=2, op='.2', z=1, r=None, b=None):
    """Lingkaran bergaris — supergrafis lembut, boleh keluar tepi."""
    return dv(P(x=x, y=y, z=z, r=r, b=b,
                lain='width:%dpx;height:%dpx;border:%dpx solid %s;border-radius:%dpx;'
                     'opacity:%s;box-sizing:border-box;' % (d, d, tebal, warna, d // 2, op)))

def busur(x=None, y=None, d=200, warna=TEAL, tebal=2, op='.25', z=1, r=None, b=None, arah='ka'):
    """Seperempat busur — sudut membulat besar khas tata letak modern."""
    sudut = {'ka': '0 0 %dpx 0', 'ki': '0 0 0 %dpx', 'kia': '%dpx 0 0 0', 'kaa': '0 %dpx 0 0'}[arah]
    return dv(P(x=x, y=y, z=z, r=r, b=b,
                lain='width:%dpx;height:%dpx;border:%dpx solid %s;border-radius:%s;opacity:%s;'
                     'box-sizing:border-box;' % (d, d, tebal, warna, sudut % d, op)))

# ----------------------------------------------------------------- tipografi
def mata(x=None, y=None, teks='', warna=REDUP, z=8, uk=9, sp=3, r=None, b=None, w=None, rt=None):
    """Kata-mata: huruf kecil tebal berspasi lebar, selalu huruf besar."""
    return dv(P(x=x, y=y, z=z, r=r, b=b, w=w, lain=font(PJ, uk, 700, warna, sp, None, rt)),
              teks.upper())

def _seg(t, g, uk, warna):
    if g == 'c':                                   # Caveat — aksen tulis tangan
        return tk('font-family:' + CV + ';font-weight:600;font-size:' + str(int(uk * 1.15))
                  + 'px;color:' + warna + ';letter-spacing:0px;', t)
    if g == 'm':                                   # Archivo miring — kontras
        return tk('font-family:' + AR + ';font-weight:400;font-style:italic;font-size:' + str(uk)
                  + 'px;color:' + warna + ';', t)
    if g == 'r':                                   # Archivo ringan
        return tk('font-family:' + AR + ';font-weight:400;font-size:' + str(uk) + 'px;color:'
                  + warna + ';', t)
    return tk('font-family:' + AR + ';font-weight:700;font-size:' + str(uk) + 'px;color:'
              + warna + ';', t)

def tajuk(x=None, y=None, w=None, baris=(), uk=62, warna=INK, sp=-2, th='.98', z=8, rt=None,
          r=None, b=None):
    """Judul besar bercampur. baris = daftar baris, tiap baris daftar (teks, gaya).
    gaya: '' tebal · 'r' ringan · 'm' miring · 'c' Caveat."""
    isi = ''
    for ln in baris:
        if isinstance(ln, str):
            ln = ((ln, ''),)
        isi += dv('', ''.join(_seg(t, g, uk, warna) for t, g in ln))
    return dv(P(x=x, y=y, w=w, z=z, r=r, b=b,
                lain='line-height:' + str(th) + ';letter-spacing:' + str(sp) + 'px;'
                     + ('text-align:' + rt + ';' if rt else '')), isi)

def teks(x=None, y=None, w=None, isi='', uk=12, warna=REDUP, tb=400, th='1.65', z=8, rt=None,
         r=None, b=None):
    return dv(P(x=x, y=y, w=w, z=z, r=r, b=b, lain=font(PJ, uk, tb, warna, None, th, rt)), isi)

def tangan(x=None, y=None, teks_='', warna=EMAS, uk=26, rot=-3, z=9, w=None, r=None, b=None, rt=None):
    return dv(P(x=x, y=y, w=w, z=z, r=r, b=b,
                lain='font-family:' + CV + ';font-size:' + str(uk) + 'px;font-weight:600;color:'
                     + warna + ';line-height:1.15;'
                     + ('transform:rotate(' + str(rot) + 'deg);' if rot else '')
                     + ('text-align:' + rt + ';' if rt else '')), teks_)

def angka(x=None, y=None, teks_='', uk=180, warna=None, op='.1', z=2, r=None, b=None, sp=-8):
    """Angka hantu besar — penanda halaman di latar."""
    return dv(P(x=x, y=y, z=z, r=r, b=b,
                lain=font(AR, uk, 700, warna or INK, sp, 1) + 'opacity:' + op + ';'), teks_)

# ----------------------------------------------------------------- garis & blok
def garis(x=None, y=None, w=KOL, warna=GARIS, z=6, tebal=1, r=None, b=None):
    return dv(P(x=x, y=y, w=w, h=tebal, z=z, r=r, b=b, lain='background:' + warna + ';'))

def garis_v(x=None, y=None, h=100, warna=GARIS, z=6, tebal=1, r=None, b=None):
    return dv(P(x=x, y=y, w=tebal, h=h, z=z, r=r, b=b, lain='background:' + warna + ';'))

def blok(x=None, y=None, w=None, h=None, isi='', bg=PUTIH, rad=22, z=4, tepi=None, lain='',
         r=None, b=None):
    g = ('background:' + bg + ';border-radius:' + str(rad) + 'px;box-sizing:border-box;'
         'overflow:hidden;')
    if tepi:
        g += 'border:1px solid ' + tepi + ';'
    return dv(P(x=x, y=y, w=w, h=h, z=z, r=r, b=b, lain=g + lain), isi)

def tengah(w, h, isi, lain=''):
    return dv(P(x=0, y=0, w=w, h=h, lain='display:grid;place-items:center;' + lain), isi)

def gambar(x, y, w, h, lab='', isi='', bg=None, rad=22, z=4, warna=None, pola=True, tepi=None):
    """Blok gambar/mockup. Placeholder-nya sengaja tenang: gradasi lembut + sarang tipis."""
    bg = bg or ('linear-gradient(150deg,' + MINT_M + ' 0%,' + KRIM_2 + ' 100%)')
    warna = warna or REDUP
    dalam = (dv(P(x=0, y=0, w=w, h=h, z=1, lain='overflow:hidden;'),
                sarang(TEAL, '.09', 2, w=w, h=h) if pola else '') + isi)
    if lab:
        dalam += mata(0, None, lab, warna, z=9, uk=8, sp=2, w=w, rt='center', b=14)
    return blok(x, y, w, h, dalam, bg, rad, z, tepi)

def kartu_teks(x, y, w, judul, isi, z=8, uk_j=15, uk_i=11, warna_j=INK, warna_i=REDUP, h=None):
    return dv(P(x=x, y=y, w=w, h=h, z=z),
              dv(font(AR, uk_j, 700, warna_j, -.2), judul)
              + dv(font(PJ, uk_i, 400, warna_i, None, '1.55') + 'margin-top:6px;', isi))

def pil(teks_, bg=MINT_M, fg=INK, uk=10, sp=1, pad='6px 14px 7px'):
    return tk('display:inline-block;background:' + bg + ';border-radius:20px;padding:' + pad
              + ';' + font(PJ, uk, 700, fg, sp), teks_.upper())

# ----------------------------------------------------------------- lambang
def lambang(px, warna=TEAL, aksen=EMAS, gaya='', rentang=None):
    """Logogram. rentang= merentangkan heksagon lewat koordinatnya sendiri, bukan
    transform — supaya bentuknya tetap utuh waktu halaman diekspor ke SVG."""
    t = max(3, px // 12)
    r = rentang or 1
    X = lambda v: int(round(v * r))
    jalur = 'M%d 8L%d 30V82L%d 104L%d 82V30Z' % (X(50), X(86), X(50), X(14))
    sel = 'M%d 50L%d 60H%dL%d 50L%d 40H%dZ' % (X(61), X(55), X(45), X(39), X(45), X(55))
    return ('<svg width="%d" height="%d" viewBox="0 0 %d 112" fill="none" '
            'style="display:block;%s"><path d="%s" stroke="%s" stroke-width="%d" '
            'stroke-linejoin="miter"/><path d="%s" fill="%s"/></svg>'
            % (X(px), int(px * 1.12), X(100), gaya, jalur, warna, t, sel, aksen))

def kunci(px, warna=TEAL, aksen=EMAS, w=INK, sp=1):
    """Logo mendatar — logogram + wordmark."""
    return dv('display:flex;align-items:center;gap:' + str(max(6, px // 3)) + 'px;',
              lambang(px, warna, aksen) + tk(font(AR, int(px * .78), 700, w, sp), 'BALIKIN'))

# ----------------------------------------------------------------- purwarupa
def ponsel(x, y, w, isi='', rot=0, z=6, bg=None, bingkai_warna=INK, lab=None):
    """Bingkai ponsel — tinggi ≈ 2,03 × lebar."""
    h = w * 61 // 30
    t = max(4, w // 18)
    rad = max(12, w // 6)
    layar = dv(P(x=t, y=t, w=w - t * 2, h=h - t * 2, z=2,
                 lain='background:' + (bg or KRIM) + ';border-radius:' + str(rad - t // 2)
                      + 'px;overflow:hidden;'), isi)
    poni = dv(P(x=(w - w // 3) // 2, y=t, w=w // 3, h=max(5, w // 22), z=4,
                lain='background:' + bingkai_warna + ';border-radius:0 0 8px 8px;'))
    badan = dv(P(x=0, y=0, w=w, h=h, z=1,
                 lain='background:' + bingkai_warna + ';border-radius:' + str(rad)
                      + 'px;box-shadow:0 18px 40px ' + rgba(INK, '.18') + ';'))
    return dv(P(x=x, y=y, w=w, h=h, z=z,
                lain='transform:rotate(' + str(rot) + 'deg);' if rot else ''),
              badan + layar + poni)

def layar_app(w, h, warna_atas=TEAL, isi=''):
    """Isi layar ponsel placeholder — kepala warna + kartu-kartu."""
    kh = h // 4
    kartu = ''
    for i in range(3):
        kartu += dv(P(x=w // 12, y=kh + 14 + i * (h // 6), w=w - w // 6, h=h // 7 - 6,
                      lain='background:' + PUTIH + ';border-radius:10px;'))
    return (dv(P(x=0, y=0, w=w, h=kh, lain='background:' + warna_atas + ';overflow:hidden;'),
               sarang(KRIM, '.16', 1, w=w, h=kh))
            + dv(P(x=0, y=kh, w=w, h=h - kh, lain='background:' + KRIM_2 + ';'))
            + kartu + isi)

# ----------------------------------------------------------------- kerangka halaman
def bingkai(bab, hal, warna=REDUP, gr=GARIS, kanan=None):
    """Kepala halaman isi: label bab kiri atas, nomor kanan atas, garis rambut."""
    return (mata(M, 44, bab, warna)
            + (mata(None, 44, kanan, warna, r=M + 34) if kanan else '')
            + dv(P(r=M, y=38, z=8, lain=font(AR, 15, 700, warna, 0)), str(hal).zfill(2))
            + garis(M, 72, KOL, gr))

def halaman(isi, latar=KRIM):
    return ('<div style="width:' + str(W) + 'px;height:' + str(H) + 'px;position:relative;'
            'overflow:hidden;background:' + latar + '">' + isi + '</div>')

def doc_gsm(root, latar=KRIM):
    return ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
            '  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n  ' + FONTS
            + '\n  <style>\n    body { margin: 0; font-family: ' + PJ + '; background: ' + latar
            + '; -webkit-font-smoothing: antialiased; }\n'
            '    div { box-sizing: border-box; }\n'
            '  </style>\n</helmet>\n' + root + '\n</x-dc>\n</body>\n</html>\n')

def tulis(nama, isi, latar=KRIM):
    open(os.path.join(_here, nama), 'w', encoding='utf-8').write(doc_gsm(isi, latar))
