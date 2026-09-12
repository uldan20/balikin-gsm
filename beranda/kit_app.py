# -*- coding: utf-8 -*-
"""Perkakas UI aplikasi Balikin — dipakai untuk merancang beranda hub.

Palet dan bentuknya diambil dari tangkapan layar prototipe: latar gradasi
mint ke krem, kartu putih sudut membulat, panel teal tua, heksagon bersisi
datar untuk lencana dan tombol utama.
"""
import os, sys
_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_here, '..', 'xbanner'))
sys.path.insert(0, os.path.join(_here, '..', 'infografis'))
from build import AR, PJ, CV, FONTS
from ikon import IKON

W, H = 384, 844                      # sesuai berkas beranda yang dikirim

# ---------------- palet aplikasi ----------------
LATAR_A, LATAR_B, LATAR_C = '#DCE9E1', '#EDE8DE', '#F6F2EA'
PUTIH = '#FFFFFF'
KRIM = '#FBF8F3'
TINTA = '#12332C'                    # teks utama
REDUP = '#6B8A81'                    # teks sekunder
GELAP_A, GELAP_B = '#17463D', '#0D2F29'   # panel teal tua
TEAL = '#1B7A63'
TEAL_T = '#25946F'                   # teal terang
TEAL_G = '#0F5A48'
MINT = '#8FD4C4'
MINT_M = '#CFE6E0'
TERRA = '#C05C33'
TERRA_G = '#A2421D'
EMAS = '#D8A43C'
EMAS_M = '#F0D79B'
KABUT = '#E7E2D7'

HEKS = 'clip-path:polygon(25% 0,75% 0,100% 50%,75% 100%,25% 100%,0 50%);'   # sisi datar
HEKS_T = 'clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%);'  # ujung atas

# ---------------- penempatan ----------------
def P(x=None, y=None, w=None, h=None, z=None, r=None, b=None, lain=''):
    s = 'position:absolute;'
    for k, v in (('left', x), ('top', y), ('right', r), ('bottom', b), ('width', w), ('height', h)):
        if v is not None:
            s += k + ':' + str(v) + 'px;'
    if z is not None:
        s += 'z-index:' + str(z) + ';'
    return s + lain

def dv(gaya, isi=''):
    return '<div style="' + gaya + '">' + isi + '</div>'

def teks(gaya, isi):
    return '<span style="' + gaya + '">' + isi + '</span>'

def font(keluarga, ukuran, tebal=400, warna=TINTA, spasi=None, tinggi=None, rata=None):
    s = ('font-family:' + keluarga + ';font-size:' + str(ukuran) + 'px;font-weight:' + str(tebal)
         + ';color:' + warna + ';')
    if spasi is not None: s += 'letter-spacing:' + str(spasi) + 'px;'
    if tinggi is not None: s += 'line-height:' + str(tinggi) + ';'
    if rata: s += 'text-align:' + rata + ';'
    return s

def ik(nama, px, warna, tebal=None):
    frag = IKON[nama]
    return ('<svg width="' + str(px) + '" height="' + str(px) + '" viewBox="0 0 100 100" fill="none" '
            'stroke-linejoin="miter" stroke-miterlimit="8" style="color:' + warna + ';display:block">'
            + frag + '</svg>')

def kartu(x, y, w, h, isi, bg=PUTIH, radius=26, bayang='0 10px 30px rgba(18,51,44,.09)', z=5, lain=''):
    return dv(P(x=x, y=y, w=w, h=h, z=z,
                lain='background:' + bg + ';border-radius:' + str(radius) + 'px;box-shadow:' + bayang
                     + ';overflow:hidden;box-sizing:border-box;' + lain), isi)

def judul_kartu(judul, sub, y=22, warna=TINTA, warna_sub=REDUP, ukuran=19):
    return (dv(P(x=0, y=y, w=None, z=3, lain='left:0;right:0;' + font(AR, ukuran, 700, warna, -.3, 1.2, 'center')), judul)
            + dv(P(x=0, y=y + ukuran + 7, z=3, lain='left:0;right:0;' + font(PJ, 12, 500, warna_sub, None, 1.2, 'center')), sub))

# ---------------- kerangka layar ----------------
def bar_status(gelap=False):
    fg = KRIM if gelap else TINTA
    sinyal = ''.join('<rect x="' + str(i * 5) + '" y="' + str(9 - i * 3) + '" width="3" height="'
                     + str(3 + i * 3) + '" rx="1" fill="' + fg + '"/>' for i in range(4))
    return (dv(P(x=24, y=16, z=20, lain=font(PJ, 15, 700, fg, -.2)), '11:05')
            + dv(P(r=22, y=18, z=20, lain='display:flex;align-items:center;gap:6px;'),
                 '<svg width="18" height="12" viewBox="0 0 18 12" fill="none">' + sinyal + '</svg>'
                 '<svg width="16" height="12" viewBox="0 0 16 12" fill="none">'
                 '<path d="M1 4.5A10 10 0 0 1 15 4.5" stroke="' + fg + '" stroke-width="2" fill="none"/>'
                 '<path d="M4 7.5A6 6 0 0 1 12 7.5" stroke="' + fg + '" stroke-width="2" fill="none"/>'
                 '<circle cx="8" cy="10.5" r="1.4" fill="' + fg + '"/></svg>'
                 '<svg width="25" height="12" viewBox="0 0 25 12" fill="none">'
                 '<rect x="0.5" y="0.5" width="21" height="11" rx="3.5" stroke="' + fg
                 + '" stroke-opacity=".4"/><rect x="2" y="2" width="18" height="8" rx="2" fill="' + fg + '"/>'
                 '<path d="M23 4.5V7.5C24 7.2 24.5 6.7 24.5 6C24.5 5.3 24 4.8 23 4.5Z" fill="' + fg
                 + '" fill-opacity=".4"/></svg>'))

def bar_bawah(aktif='beranda'):
    """Batang navigasi mengambang + tombol heksagon."""
    def tab(nama, ikon_, label=None, titik=False):
        on = nama == aktif
        if not on: label = None
        isi_ = ik(ikon_, 21, TEAL if on else '#8AA49C')
        if on and label:
            isi_ = dv('display:flex;align-items:center;gap:7px;', isi_
                      + teks(font(PJ, 13, 700, TEAL, -.2), label))
        bg = 'background:' + MINT_M + ';border-radius:19px;padding:0 14px;' if on and label else ''
        noktah = dv(P(r=-1, y=-1, w=7, h=7, z=3, lain='background:#D8503A;border-radius:4px;'
                      'border:2px solid ' + PUTIH + ';')) if titik else ''
        return dv('position:relative;height:38px;display:flex;align-items:center;justify-content:center;'
                  'padding:0 11px;' + bg, isi_ + noktah)
    batang = dv(P(x=18, b=26, w=228, h=58, z=14,
                  lain='background:' + PUTIH + ';border-radius:29px;display:flex;align-items:center;'
                       'justify-content:space-between;padding:0 8px;box-sizing:border-box;'
                       'box-shadow:0 12px 30px rgba(18,51,44,.16);'),
                 tab('beranda', 'rumah', 'Beranda') + tab('jelajah', 'kompas', 'Jelajah')
                 + tab('pesan', 'obrolan', 'Pesan', True) + tab('profil', 'warga', 'Profil'))
    tombol = dv(P(r=18, b=22, w=66, h=66, z=15,
                  lain='filter:drop-shadow(0 12px 24px rgba(15,90,72,.34));'),
                dv('width:66px;height:66px;background:linear-gradient(150deg,' + TEAL_T + ' 0%,'
                   + TEAL_G + ' 100%);' + HEKS + 'display:grid;place-items:center;',
                   ik('tambah', 26, PUTIH)))
    return batang + tombol

def pil_lokasi(x=74, y=65, w=176, lokasi='CISAAT, SUKABUMI'):
    """Pengisi bagian kosong di tengah tiga tombol header."""
    titik = ('<svg width="14" height="14" viewBox="0 0 14 14" fill="none">'
             '<circle cx="7" cy="7" r="6" fill="' + MINT + '" fill-opacity=".5"/>'
             '<circle cx="7" cy="7" r="3" fill="' + TEAL + '"/></svg>')
    return dv(P(x=x, y=y, w=w, h=34, z=12,
                lain='background:' + PUTIH + ';border-radius:18px;display:flex;align-items:center;'
                     'justify-content:center;gap:7px;padding:0 12px;box-sizing:border-box;'
                     'box-shadow:0 4px 14px rgba(18,51,44,.1);'),
              titik + teks(font(PJ, 11, 700, TINTA, .9) + 'white-space:nowrap;', lokasi)
              + ik('panah', 12, REDUP))

def kepala(lokasi=None):
    bulat = lambda isi_, titik=False: dv('position:relative;width:40px;height:40px;border-radius:21px;'
                                         'background:' + PUTIH + ';display:grid;place-items:center;'
                                         'box-shadow:0 4px 14px rgba(18,51,44,.1);',
                                         isi_ + (dv(P(r=9, y=9, w=7, h=7, lain='background:#D8503A;'
                                                      'border-radius:4px;border:2px solid ' + PUTIH + ';'))
                                                 if titik else ''))
    avatar = dv(P(x=22, y=62, w=40, h=40, z=12,
                  lain='border-radius:21px;background:linear-gradient(150deg,' + MINT + ',' + TEAL
                       + ');box-shadow:0 4px 14px rgba(18,51,44,.14);display:grid;place-items:center;'),
                ik('warga', 20, PUTIH))
    kanan = dv(P(r=22, y=62, z=12, lain='display:flex;gap:10px;'),
               bulat(ik('cari', 19, TINTA)) + bulat(ik('lonceng', 19, TINTA), True))
    return avatar + pil_lokasi() + kanan

def layar(isi, gradasi=None):
    g = gradasi or ('linear-gradient(178deg,' + LATAR_A + ' 0%,' + LATAR_B + ' 52%,' + LATAR_C + ' 100%)')
    return ('<div style="width:' + str(W) + 'px;height:' + str(H) + 'px;position:relative;'
            'overflow:hidden;background:' + g + '">' + isi + '</div>')

def papan(w, h, isi, latar=None):
    """Artboard bebas ukuran untuk kartu mandiri."""
    g = latar or ('linear-gradient(160deg,' + LATAR_A + ' 0%,' + LATAR_C + ' 100%)')
    return ('<div style="width:' + str(w) + 'px;height:' + str(h) + 'px;position:relative;'
            'overflow:hidden;background:' + g + '">' + isi + '</div>')

def doc_app(root, latar=LATAR_C):
    return ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
            '  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n  ' + FONTS
            + '\n  <style>\n    body { margin: 0; font-family: ' + PJ + '; background: ' + latar + '; }\n'
            '  </style>\n</helmet>\n' + root + '\n</x-dc>\n</body>\n</html>\n')

def tulis(nama, isi_, latar=LATAR_C):
    open(os.path.join(_here, nama), 'w', encoding='utf-8').write(doc_app(isi_, latar))
    print(nama)
