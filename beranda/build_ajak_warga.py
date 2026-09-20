# -*- coding: utf-8 -*-
"""Bangun kartu "Ajak warga" ke SVG.

Struktur tata letaknya meniru kartu ajakan berteman: gugus avatar bertumpuk,
dua baris teks, lalu satu pil aksi. Avatarnya digambar ulang dalam gaya warga
Balikin — datar, geometris — bukan meniru gaya avatar milik aplikasi lain.

Seluruh koordinat dibulatkan lewat I() dari rapi.py, dan tiap grup diberi
bidang() supaya Figma melaporkan W/H grup sebagai bilangan bulat.

    python3 build_ajak_warga.py
"""
import os, sys, re

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'xbanner'))
from rapi import I, N, hex6, bidang

# ---------- ukuran ----------
KANVAS_W, KANVAS_H = 380, 296
KARTU_X, KARTU_Y, KARTU_W, KARTU_H = 20, 20, 340, 256
TENGAH = KARTU_X + KARTU_W // 2          # 190

# ---------- palet Balikin ----------
LATAR      = '#EDE6DB'   # kream halaman
KARTU      = '#123932'   # teal tua, sama dengan panel reputasi
PIL        = '#1D5348'   # permukaan lebih terang di atas teal tua
MINT       = '#7BDCC4'
TINTA      = '#0E3B33'
PUTIH      = '#FFFFFF'

# tiap warga: (cx, cy, r, warna lingkaran, warna siluet)
# Tidak ada ragam rambut: di 16–31px detail rambut jadi bentuk yang salah baca.
# Perbedaan antarwarga dibawa warna dan ukuran, sesuai gaya datar Balikin.
WARGA = [
    (135,  68, 17, '#E5B551', '#123932'),
    (256,  72, 20, '#CF693C', '#FFF4EE'),
    (127, 118, 23, '#9CD8C6', '#123932'),
    (249, 126, 16, '#E8E1D4', '#123932'),
    (193,  94, 31, '#2E8A74', '#EAFBF5'),   # paling depan, digambar terakhir
]

BARIS = ['Makin banyak mata,', 'makin cepat barang balik.']
TOMBOL = 'Ajak warga'


def warga(cx, cy, r, bg, tinta, urut):
    """Satu avatar warga: lingkaran berwarna dengan siluet kepala dan bahu.

    Bahunya lingkaran berjari-jari 0,75r berpusat 0,92r di bawah pusat avatar,
    jadi ia meruncing dan warna lingkaran tetap terlihat mengelilinginya.
    Ini penting karena siluet di avatar terang memakai warna yang sama dengan
    latar kartu: kalau bahunya menyentuh tepi, siluetnya melebur ke kartu dan
    lingkarannya terbaca sebagai bulan sabit, bukan sebagai orang. Bahu
    berbentuk persegi juga ditolak — alasnya rata dan jadi garis cakrawala."""
    cx, cy, r = I(cx), I(cy), I(r)
    kid = 'potong-warga-%d' % urut
    kepala_cy = I(cy - r * 0.20)
    kepala_r  = I(r * 0.26)
    bahu_cy   = I(cy + r * 0.92)
    bahu_r    = I(r * 0.75)

    t = []
    t.append('<clipPath id="%s"><circle cx="%s" cy="%s" r="%s"/></clipPath>' % (kid, N(cx), N(cy), N(r)))
    t.append('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="3"/>'
             % (N(cx), N(cy), N(r), bg, KARTU))
    t.append('<g clip-path="url(#%s)">' % kid)
    t.append('<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (N(cx), N(bahu_cy), N(bahu_r), tinta))
    t.append('<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (N(cx), N(kepala_cy), N(kepala_r), tinta))
    t.append('</g>')
    return ''.join(t)


def bangun():
    o = []
    o.append('<?xml version="1.0" encoding="UTF-8"?>')
    o.append('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
             'role="img" aria-label="Balikin — Kartu ajak warga">'
             % (KANVAS_W, KANVAS_H, KANVAS_W, KANVAS_H))
    o.append('<title>Balikin — Kartu ajak warga</title>')
    o.append('<desc>Satuan piksel logis. Huruf: Plus Jakarta Sans.</desc>')

    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (KANVAS_W, KANVAS_H, LATAR))

    # ---- kartu ----
    o.append('<g id="Kartu ajak warga">')
    o.append(bidang(KARTU_W, KARTU_H, KARTU_X, KARTU_Y))
    o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="28" fill="%s"/>'
             % (KARTU_X, KARTU_Y, KARTU_W, KARTU_H, KARTU))

    # ---- gugus avatar ----
    kiri  = min(c - r for c, _, r, *_ in WARGA)
    kanan = max(c + r for c, _, r, *_ in WARGA)
    atas  = min(y - r for _, y, r, *_ in WARGA)
    bawah = max(y + r for _, y, r, *_ in WARGA)
    o.append('<g id="Gugus warga">')
    o.append(bidang(kanan - kiri, bawah - atas, kiri, atas))
    for i, (cx, cy, r, bg, tinta) in enumerate(WARGA):
        o.append(warga(cx, cy, r, bg, tinta, i + 1))
    o.append('</g>')

    # ---- dua baris teks ----
    o.append('<g id="Ajakan">')
    o.append(bidang(KARTU_W - 48, 44, KARTU_X + 24, 160))
    for i, baris in enumerate(BARIS):
        o.append('<text x="%d" y="%d" text-anchor="middle" fill="%s" '
                 'font-family="Plus Jakarta Sans, sans-serif" font-size="15" font-weight="700">%s</text>'
                 % (TENGAH, 178 + i * 22, PUTIH, baris))
    o.append('</g>')

    # ---- pil aksi ----
    pw, ph = 150, 42
    px, py = TENGAH - pw // 2, 218
    isi_w = 18 + 10 + 82                     # heksagon + jarak + teks
    isi_x = px + (pw - isi_w) // 2
    hx, hy = isi_x + 9, py + ph // 2
    o.append('<g id="Tombol ajak warga">')
    o.append(bidang(pw, ph, px, py))
    o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="21" fill="%s"/>' % (px, py, pw, ph, PIL))
    o.append('<path d="%s" fill="%s"/>' % (hex6(hx, hy, 9, 10), MINT))
    o.append('<path d="M%s %sH%sM%s %sV%s" stroke="%s" stroke-width="3" stroke-linecap="round"/>'
             % (N(hx - 5), N(hy), N(hx + 5), N(hx), N(hy - 5), N(hy + 5), TINTA))
    o.append('<text x="%d" y="%d" fill="%s" font-family="Plus Jakarta Sans, sans-serif" '
             'font-size="15" font-weight="700">%s</text>' % (isi_x + 28, py + 27, PUTIH, TOMBOL))
    o.append('</g>')

    o.append('</g>')
    o.append('</svg>')
    return '\n'.join(o)


if __name__ == '__main__':
    svg = bangun()
    keluar = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'svg', 'kartu-ajak-warga.svg')
    open(keluar, 'w', encoding='utf-8').write(svg)
    sisa = sorted(set(re.findall(r'-?\d+\.\d+', svg)))
    print('kartu-ajak-warga.svg  %dx%d  %d B' % (KANVAS_W, KANVAS_H, len(svg)))
    print('desimal tersisa: %d %s' % (len(sisa), sisa))
