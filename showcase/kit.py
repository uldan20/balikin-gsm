# -*- coding: utf-8 -*-
"""Perkakas bersama untuk poster showcase A3. Ponsel, layar placeholder, stiker,
pin, kartu pil, dan latar — semuanya vektor/CSS, tanpa foto."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'xbanner'))
from build import (CREAM, INK, TEAL, TEALD, GOLD, GOLDL, TERRA, WASH, LINE, MUTED, FILL, MINT,
                   ICONS, LEBAH, AR, PJ, CV, FONTS)

W, H = 1122, 1587           # A3 potret pada 96 ppi
TEALB = '#34A28F'           # teal terang
TEALX = '#12564D'           # teal paling tua
HEX = 'clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%)'

def doc(root, latar=CREAM):
    return ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
            '  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n  %s\n'
            '  <style>\n    body { margin: 0; font-family: %s; background: %s; }\n'
            '    a { color: %s; } a:hover { color: %s; }\n  </style>\n</helmet>\n%s\n</x-dc>\n</body>\n</html>\n'
            ) % (FONTS, PJ, latar, TEAL, TEALD, root)

def ic(n, px, c):
    return ('<svg width="%d" height="%d" viewBox="0 0 100 100" fill="none" stroke-linejoin="miter" '
            'stroke-miterlimit="8" style="color:%s;display:block">%s</svg>') % (px, px, c, ICONS[n])

def bee(px, rot=0):
    return ('<svg width="%d" height="%d" viewBox="0 0 200 200" style="display:block;transform:rotate(%sdeg)">%s</svg>'
            ) % (px, px, rot, LEBAH)

def sarang(warna=CREAM, op='.08', skala=2):
    """Pola sarang lebah sebagai latar. skala 1 = petak 52x90."""
    k = skala
    w, h = 52 * k, 90 * k
    def P(pts):
        return 'M' + 'L'.join('%d %d' % (x * k, y * k) for x, y in pts) + 'Z'
    sel = [P([(26,0),(52,15),(52,45),(26,60),(0,45),(0,15)]),
           P([(0,45),(26,60),(26,90),(0,105),(-26,90),(-26,60)]),
           P([(52,45),(78,60),(78,90),(52,105),(26,90),(26,60)])]
    pid = 'sr%d' % k
    return ('<svg style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none" aria-hidden="true">'
            '<defs><pattern id="' + pid + '" width="' + str(w) + '" height="' + str(h) + '" '
            'patternUnits="userSpaceOnUse"><g fill="none" stroke="' + warna + '" stroke-width="2" '
            'opacity="' + op + '">' + ''.join('<path d="%s"/>' % c for c in sel) + '</g></pattern></defs>'
            '<rect width="100%" height="100%" fill="url(#' + pid + ')"/></svg>')

def logo(c, acc, size=42, ls=2):
    return ('<div style="display:flex;align-items:center;gap:14px">'
            '<svg width="%d" height="%d" viewBox="0 0 100 100" fill="none">'
            '<path d="M50 8L86.4 29V71L50 92L13.6 71V29Z" stroke="%s" stroke-width="8" stroke-linejoin="miter"/>'
            '<path d="M61 44L55.5 53.53H44.5L39 44L44.5 34.47H55.5Z" fill="%s"/></svg>'
            '<span style="font-family:%s;font-weight:700;font-size:%dpx;letter-spacing:%dpx;color:%s">BALIKIN</span>'
            '</div>') % (size, int(size*1.15), c, acc, AR, int(size*0.92), ls, c)

# ---------------- ponsel ----------------
def layar_kosong(nada='terang'):
    """Rangka layar samar, cukup padat supaya komposisi poster terbaca.
    Diganti tangkapan layar asli nanti."""
    if nada == 'terang':
        bg, blok, blok2, garis, teks = CREAM, WASH, '#E8F1EF', '#BBD8D2', '#7FA8A0'
    else:
        bg, blok, blok2 = TEALX, 'rgba(251,248,243,.11)', 'rgba(251,248,243,.07)'
        garis, teks = 'rgba(251,248,243,.22)', 'rgba(251,248,243,.5)'
    def bar(w, h, r, c=None, mt=0):
        return ('<div style="width:%s;height:%dpx;border-radius:%dpx;background:%s;margin-top:%dpx"></div>'
                % (w, h, r, c or blok, mt))
    def heks(px, c):
        return '<div style="width:%dpx;height:%dpx;background:%s;%s"></div>' % (px, int(px*1.15), c, HEX)
    kepala = ('<div style="display:flex;align-items:center;gap:12px">%s<div style="flex:1">%s%s</div>%s</div>'
              % (heks(28, blok), bar('62%%', 13, 7), bar('40%%', 9, 5, blok2, 7),
                 '<div style="width:34px;height:34px;border-radius:17px;background:%s"></div>' % blok))
    isi = ('<div style="flex:1;border-radius:20px;background:%s;position:relative;margin-top:14px;overflow:hidden">'
           '<div style="position:absolute;left:14%%;top:16%%">%s</div>'
           '<div style="position:absolute;left:58%%;top:9%%">%s</div>'
           '<div style="position:absolute;left:34%%;top:40%%">%s</div>'
           '<div style="position:absolute;left:70%%;top:52%%">%s</div>'
           '<div style="position:absolute;left:0;right:0;bottom:26px;text-align:center">'
           '<span style="font-family:%s;font-size:12px;font-weight:700;letter-spacing:3px;color:%s">LAYAR APLIKASI</span>'
           '<div style="font-size:11px;color:%s;opacity:.8;margin-top:4px">ganti dengan tangkapan layar</div></div></div>'
           % (blok2, heks(30, blok), heks(24, blok), heks(38, garis), heks(26, blok), PJ, teks, teks))
    baris = ''.join(
        '<div style="display:flex;align-items:center;gap:11px;margin-top:11px">'
        '<div style="width:44px;height:44px;border-radius:12px;background:%s"></div>'
        '<div style="flex:1">%s%s</div></div>' % (blok, bar('74%%', 11, 6), bar('46%%', 8, 4, blok2, 6))
        for _ in range(2))
    tab = ('<div style="display:flex;justify-content:space-between;align-items:center;margin-top:14px;'
           'padding:12px 16px;border-radius:22px;background:%s">%s</div>'
           % (blok, ''.join('<div style="width:19px;height:22px;background:%s;%s"></div>' % (garis, HEX)
                            for _ in range(5))))
    return ('<div style="height:100%%;background:%s;display:flex;flex-direction:column;padding:58px 18px 18px">'
            '%s%s%s%s</div>') % (bg, kepala, isi, baris, tab)

def ponsel(w, rot=0, layar=None, bayang='0 44px 90px rgba(12,40,36,.34)', bingkai=INK):
    h = int(round(w * 2.1656)); r = int(round(w * 0.145)); b = max(9, int(round(w * 0.036)))
    isi = layar if layar is not None else layar_kosong()
    pulau_w, pulau_h = int(w * 0.27), int(w * 0.077)
    return ('<div style="width:%dpx;height:%dpx;background:%s;border-radius:%dpx;padding:%dpx;'
            'box-shadow:%s;transform:rotate(%sdeg);position:relative;flex:none">'
            '<div style="width:100%%;height:100%%;border-radius:%dpx;overflow:hidden;position:relative">%s</div>'
            '<div style="position:absolute;top:%dpx;left:50%%;transform:translateX(-50%%);width:%dpx;height:%dpx;'
            'background:%s;border-radius:%dpx"></div></div>'
            ) % (w, h, bingkai, r, b, bayang, rot, r - b, isi,
                 b + int(w * 0.033), pulau_w, pulau_h, bingkai, pulau_h // 2)

# ---------------- elemen melayang ----------------
def pil(judul, sub, ikon=None, rot=0, gelap=False):
    bg, fg, sfg = (INK, CREAM, 'rgba(251,248,243,.75)') if gelap else (CREAM, INK, '#6B6258')
    kiri = ('<span style="flex:none;width:26px;height:30px;background:%s;%s;display:grid;place-items:center">%s</span>'
            ) % (TEAL, HEX, ic(ikon, 14, CREAM)) if ikon else ''
    return ('<div style="background:%s;border-radius:24px;padding:13px 20px;box-shadow:0 16px 36px rgba(12,40,36,.22);'
            'transform:rotate(%sdeg);display:flex;flex-direction:column;gap:5px;flex:none">'
            '<span style="font-family:%s;font-size:21px;font-weight:700;letter-spacing:-.4px;color:%s">%s</span>'
            '<span style="display:flex;align-items:center;gap:9px;font-size:16px;color:%s">%s%s</span></div>'
            ) % (bg, rot, AR, fg, judul, sfg, kiri, sub)

def pin(px, ikon, warna=TEAL, rot=0):
    """Penanda peta: lingkaran bergambar dengan ekor runcing."""
    return ('<div style="position:relative;width:%dpx;transform:rotate(%sdeg);flex:none">'
            '<div style="width:%dpx;height:%dpx;border-radius:50%%;background:%s;border:5px solid %s;'
            'box-shadow:0 14px 30px rgba(12,40,36,.26);display:grid;place-items:center">%s</div>'
            '<div style="position:absolute;left:50%%;bottom:-13px;transform:translateX(-50%%);width:0;height:0;'
            'border-left:11px solid transparent;border-right:11px solid transparent;border-top:18px solid %s"></div>'
            '<div style="position:absolute;right:-8px;bottom:-4px;width:%dpx;height:%dpx;border-radius:50%%;'
            'background:%s;border:3px solid %s;display:grid;place-items:center">%s</div></div>'
            ) % (px, rot, px, px, WASH, CREAM, ic(ikon, int(px*0.56), warna), CREAM,
                 int(px*0.34), int(px*0.34), CREAM, CREAM, ic('check', int(px*0.17), warna))

def stiker(isi_, px=118, bg=GOLD, rot=0):
    return ('<div style="width:%dpx;height:%dpx;background:%s;%s;display:grid;place-items:center;'
            'transform:rotate(%sdeg);filter:drop-shadow(0 0 5px %s) drop-shadow(0 18px 26px rgba(12,40,36,.3));'
            'flex:none">%s</div>') % (px, int(px*1.15), bg, HEX, rot, CREAM, isi_)

def slot_foto(w, h, label, rot=0, radius=28):
    return ('<div style="width:%dpx;height:%dpx;border-radius:%dpx;background:%s;border:3px dashed %s;'
            'display:grid;place-items:center;transform:rotate(%sdeg);flex:none">'
            '<div style="text-align:center"><div style="width:44px;height:51px;border:3px solid %s;%s;margin:0 auto 10px"></div>'
            '<span style="font-family:%s;font-size:12px;font-weight:700;letter-spacing:2.5px;color:%s">%s</span></div></div>'
            ) % (w, h, radius, 'rgba(251,248,243,.10)', 'rgba(251,248,243,.34)', rot,
                 'rgba(251,248,243,.4)', HEX, PJ, 'rgba(251,248,243,.6)', label)

def kaki(fg, sub_op='.75'):
    return ('<div style="display:flex;align-items:flex-end;justify-content:space-between;gap:24px">'
            '<div style="font-size:15px;line-height:1.45;color:%s;opacity:%s">'
            'Uldan Pamungkas · 20210060127<br>Desain Komunikasi Visual · Universitas Nusa Putra Sukabumi</div>'
            '<div style="font-family:%s;font-size:14px;font-weight:700;letter-spacing:3px;color:%s;opacity:%s">'
            'BALIKIN.ID</div></div>') % (fg, sub_op, PJ, fg, sub_op)
