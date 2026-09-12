# -*- coding: utf-8 -*-
"""Perkakas bersama untuk tiga lembar infografis A3.

Semua diletakkan dengan koordinat mutlak bilangan bulat — lihat CLAUDE.md.
"""
import os, sys
_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_here, '..', 'showcase'))
from kit import (W, H, CREAM, INK, TEAL, TEALD, TEALB, TEALX, GOLD, GOLDL, TERRA, WASH,
                 LINE, MUTED, FILL, MINT, AR, PJ, CV, HEX, doc, sarang, bee, logo)
from ikon import ik, IKON

TERL = '#EDCFC2'          # terakota muda — turunan untuk blok data
GOLDD = '#A87722'         # emas tua
KRIM = '#E6DDCD'          # krem tingkat pertama
MINTT = '#8FD4C4'         # mint tingkat kedua

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

def font(keluarga, ukuran, tebal=400, warna=INK, spasi=None, tinggi=None, rata=None):
    s = ('font-family:' + keluarga + ';font-size:' + str(ukuran) + 'px;font-weight:' + str(tebal)
         + ';color:' + warna + ';')
    if spasi is not None:
        s += 'letter-spacing:' + str(spasi) + 'px;'
    if tinggi is not None:
        s += 'line-height:' + str(tinggi) + ';'
    if rata:
        s += 'text-align:' + rata + ';'
    return s

# ---------------- kepala lembar ----------------
def kepala(atas, bawah, sub, y=56, aksen=TERRA, lebar_sub=840):
    """Judul dua baris + satu kalimat pembuka. Rata tengah, seperti acuan."""
    h1 = dv(P(x=0, w=W, y=y, z=9,
              lain=font(AR, 104, 700, aksen, -3, 1, 'center')), atas)
    h2 = dv(P(x=0, w=W, y=y + 108, z=9,
              lain=font(AR, 58, 700, INK, -1, 1, 'center')), bawah)
    p = dv(P(x=(W - lebar_sub) // 2, w=lebar_sub, y=y + 186, z=9,
             lain=font(PJ, 20, 400, INK, None, 1.5, 'center') + 'opacity:.88;'), sub)
    return h1 + h2 + p

def legenda(baris, y, x=None):
    """Deret keping warna. baris = [(warna, label, garis_tepi)]"""
    keping = []
    for w_, lab, tepi in baris:
        kotak = dv('width:22px;height:22px;background:' + w_ + ';flex:none;'
                   + ('border:2px solid ' + LINE + ';' if tepi else '') + HEX)
        keping.append(dv('display:flex;align-items:center;gap:9px;',
                         kotak + teks(font(PJ, 16, 600, INK) + 'white-space:nowrap;', lab)))
    isi = dv('display:flex;justify-content:center;gap:30px;', ''.join(keping))
    return dv(P(x=x if x is not None else 0, w=W if x is None else None, y=y, z=9), isi)

# ---------------- kartu catatan ----------------
def panah_kecil(warna=TERRA):
    return dv('width:0;height:0;border-top:7px solid transparent;border-bottom:7px solid transparent;'
              'border-left:11px solid ' + warna + ';flex:none;margin-top:5px;')

def kartu_catatan(catatan, x, y=None, lebar=430, rot=-3, z=12, lebah=True, judul_kartu=None,
                  sisi='kanan', bawah=None):
    """Kartu putih miring berisi dua catatan, dipegang maskot lebah."""
    baris = []
    for t in catatan:
        baris.append(dv('display:flex;gap:12px;margin-top:15px;',
                        panah_kecil() + dv(font(PJ, 15, 400, INK, None, 1.45), t)))
    kepala_kartu = dv('display:flex;align-items:center;gap:10px;padding-bottom:14px;'
                      'border-bottom:2px solid ' + FILL + ';',
                      logo(INK, TERRA, 22, 1) if judul_kartu is None else
                      teks(font(AR, 17, 700, INK, 2), judul_kartu))
    kartu = dv('width:' + str(lebar) + 'px;background:' + CREAM + ';padding:24px 26px 28px;'
               'box-shadow:0 26px 54px rgba(12,40,36,.22);transform:rotate(' + str(rot) + 'deg);',
               kepala_kartu + ''.join(baris))
    if not lebah:
        ekor = ''
    elif sisi == 'kiri':
        ekor = dv(P(x=-46, y=-54, z=-1), bee(118, -14))
    else:
        ekor = dv(P(r=-46, y=-52, z=-1), bee(118, 14))
    return dv(P(x=x, y=y, b=bawah, z=z), kartu + ekor)

# ---------------- kaki ----------------
def kaki_info(sumber, y=1490, fg=INK, kiri=True):
    nama = ('Uldan Pamungkas · 20210060127<br>'
            'Desain Komunikasi Visual · Universitas Nusa Putra Sukabumi')
    if kiri:
        a = dv(P(x=70, y=y, w=520, z=9, lain=font(PJ, 15, 400, fg, None, 1.5) + 'opacity:.72;'), nama)
        b = dv(P(r=70, y=y + 4, z=9, lain=font(PJ, 15, 600, fg, None, 1.5, 'right') + 'opacity:.8;'),
               'Sumber: ' + sumber)
        return a + b
    a = dv(P(r=70, y=y, w=520, z=9, lain=font(PJ, 15, 400, fg, None, 1.5, 'right') + 'opacity:.72;'), nama)
    b = dv(P(r=70, y=y + 54, z=9, lain=font(PJ, 15, 600, fg, None, 1.5, 'right') + 'opacity:.85;'),
           'Sumber: ' + sumber)
    return a + b

def pita(warna=TERRA, isi_teks='BALIKIN · YANG HILANG, BALIK PULANG', fg=CREAM, tinggi=34):
    return dv(P(x=0, w=W, b=0, h=tinggi, z=10,
                lain='background:' + warna + ';display:flex;align-items:center;justify-content:center;'),
              teks(font(AR, 15, 700, fg, 5), isi_teks))

# ---------------- lain-lain ----------------
def bayang_alas(x, y, w, h=26, op='.16'):
    return dv(P(x=x, y=y, w=w, h=h, z=1,
                lain='background:rgba(12,40,36,' + op + ');filter:blur(16px);border-radius:50%;'))

def stiker_heks(isi_, px, bg=GOLD, rot=0, x=None, y=None, z=14, r=None):
    s = dv('width:' + str(px) + 'px;height:' + str(int(px * 1.15)) + 'px;background:' + bg + ';' + HEX
           + ';display:grid;place-items:center;transform:rotate(' + str(rot) + 'deg);'
           'filter:drop-shadow(0 0 5px ' + CREAM + ') drop-shadow(0 16px 26px rgba(12,40,36,.28));', isi_)
    return dv(P(x=x, y=y, r=r, z=z), s)

def lembar(latar, isi):
    return ('<div style="width:' + str(W) + 'px;height:' + str(H) + 'px;position:relative;'
            'overflow:hidden;background:' + latar + '">' + isi + '</div>')
