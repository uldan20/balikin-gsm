# -*- coding: utf-8 -*-
"""Gantungan kunci akrilik — lima lencana Tingkat Komunitas.

Siluet potongnya mengikuti bentuk lencana di aplikasi: bulat, kotak membulat,
heksagon, perisai berletusan, dan letusan. Akrilik 3 mm, cetak UV dua sisi,
lubang cincin 4 mm.

Skala 4 satuan = 1 mm. Lembar 174 x 126 mm (3 + 2).
"""
import os, sys, re, math
_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_here, '..', 'xbanner'))
sys.path.insert(0, os.path.join(_here, '..', 'standee'))
from build import AR, PJ, CV
from build_standee import N, teks, POTONG, CREAM, INK, TEAL, MINT, EMAS, TERRA

S = 4
LEBAR_MM, TINGGI_MM = 174, 126
W, H = LEBAR_MM * S, TINGGI_MM * S
R = 96                                   # setengah lebar lencana (48 mm)
LUBANG = 8                               # jari-jari lubang cincin (4 mm)

# pusat tiap sel: tiga di atas, dua di bawah
PUSAT = [(108, 124), (348, 124), (588, 124), (228, 380), (468, 380)]

# nama, bentuk, warna atas, warna bawah, warna lambang, y lubang,
# lebar pita, tinggi pita, geser pita, baris teks
TINGKAT = [
  ('Warga Baru',      'bulat',   '#F4F0E8', '#D9D2C2', '#6E6A60', -70, 152, 30, 50, ['WARGA BARU']),
  ('Tetangga Baik',   'kotak',   '#B6E6D2', '#7FC9AE', '#FFFFFF', -72, 152, 30, 50, ['TETANGGA BAIK']),
  ('Penolong',        'heksagon','#79CBB2', '#1B7A63', '#FFFFFF', -70, 140, 30, 48, ['PENOLONG']),
  ('Penjaga Kota',    'perisai', '#DDA084', '#B4623C', '#FFFFFF', -62, 104, 28, 44, ['PENJAGA KOTA']),
  ('Legenda Balikin', 'letusan', '#F6D999', '#DFA63C', '#FFFFFF', -62, 84, 38, 36, ['LEGENDA', 'BALIKIN']),
]

def titik(pts):
    return 'M' + 'L'.join(N(x) + ' ' + N(y) for x, y in pts) + 'Z'

def bulat_path(cx, cy, r=R):
    """Lingkaran sebagai path, supaya jalur potong seragam."""
    k = int(round(r * 0.5523))
    return ('M' + N(cx - r) + ' ' + N(cy) + 'C' + N(cx - r) + ' ' + N(cy - k) + ' ' + N(cx - k)
            + ' ' + N(cy - r) + ' ' + N(cx) + ' ' + N(cy - r) + 'C' + N(cx + k) + ' ' + N(cy - r)
            + ' ' + N(cx + r) + ' ' + N(cy - k) + ' ' + N(cx + r) + ' ' + N(cy) + 'C' + N(cx + r)
            + ' ' + N(cy + k) + ' ' + N(cx + k) + ' ' + N(cy + r) + ' ' + N(cx) + ' ' + N(cy + r)
            + 'C' + N(cx - k) + ' ' + N(cy + r) + ' ' + N(cx - r) + ' ' + N(cy + k) + ' '
            + N(cx - r) + ' ' + N(cy) + 'Z')

def kotak_path(cx, cy, r=R, sudut=56):
    x, y, s2 = cx - r, cy - r, r * 2
    c, k = sudut, int(round(sudut * 0.45))
    return ('M' + N(x + c) + ' ' + N(y) + 'H' + N(x + s2 - c) + 'C' + N(x + s2 - k) + ' ' + N(y)
            + ' ' + N(x + s2) + ' ' + N(y + k) + ' ' + N(x + s2) + ' ' + N(y + c)
            + 'V' + N(y + s2 - c) + 'C' + N(x + s2) + ' ' + N(y + s2 - k) + ' ' + N(x + s2 - k)
            + ' ' + N(y + s2) + ' ' + N(x + s2 - c) + ' ' + N(y + s2) + 'H' + N(x + c)
            + 'C' + N(x + k) + ' ' + N(y + s2) + ' ' + N(x) + ' ' + N(y + s2 - k) + ' ' + N(x)
            + ' ' + N(y + s2 - c) + 'V' + N(y + c) + 'C' + N(x) + ' ' + N(y + k) + ' ' + N(x + k)
            + ' ' + N(y) + ' ' + N(x + c) + ' ' + N(y) + 'Z')

def heks_path(cx, cy, sw=83, sh=96):
    return titik([(cx, cy - sh), (cx + sw, cy - sh // 2), (cx + sw, cy + sh // 2),
                  (cx, cy + sh), (cx - sw, cy + sh // 2), (cx - sw, cy - sh // 2)])

def letusan_path(cx, cy, n, luar, dalam, putar=-90):
    pts = []
    for i in range(n * 2):
        r = luar if i % 2 == 0 else dalam
        a = math.radians(putar + i * 180.0 / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return titik(pts)

def perisai_path(cx, cy, w=74, h=96):
    return titik([(cx, cy - h), (cx + w, cy - h + 30), (cx + w, cy + 12),
                  (cx, cy + h), (cx - w, cy + 12), (cx - w, cy - h + 30)])

def siluet(bentuk, cx, cy):
    """Jalur potong tiap tingkat."""
    if bentuk == 'bulat':    return bulat_path(cx, cy)
    if bentuk == 'kotak':    return kotak_path(cx, cy)
    if bentuk == 'heksagon': return heks_path(cx, cy)
    if bentuk == 'perisai':  return letusan_path(cx, cy, 8, 100, 66)
    return letusan_path(cx, cy, 12, 100, 62)

# ---------------- lambang di dalam lencana ----------------
def lambang(bentuk, cx, cy, warna, k=1.0):
    q = lambda v: int(round(v * k))
    if bentuk == 'bulat':
        d = ''
        for i in range(16):
            a = math.radians(i * 22.5 - 90)
            d += ('<circle cx="' + N(cx + q(44) * math.cos(a)) + '" cy="' + N(cy + q(44) * math.sin(a))
                  + '" r="' + N(q(5)) + '" fill="' + warna + '"/>')
        return d
    if bentuk == 'kotak':
        return ('<path d="M' + N(cx) + ' ' + N(cy + q(42)) + 'L' + N(cx - q(42)) + ' ' + N(cy)
                + 'V' + N(cy - q(22)) + 'L' + N(cx - q(24)) + ' ' + N(cy - q(40)) + 'H' + N(cx - q(10))
                + 'L' + N(cx) + ' ' + N(cy - q(30)) + 'L' + N(cx + q(10)) + ' ' + N(cy - q(40))
                + 'H' + N(cx + q(24)) + 'L' + N(cx + q(42)) + ' ' + N(cy - q(22)) + 'V' + N(cy)
                + 'Z" fill="none" stroke="' + warna + '" stroke-width="' + N(q(11))
                + '" stroke-linejoin="miter"/>'
                + '<path d="' + heks_path(cx, cy - q(2), q(13), q(15)) + '" fill="none" stroke="'
                + warna + '" stroke-width="' + N(q(9)) + '"/>')
    if bentuk == 'heksagon':
        return ('<path d="' + heks_path(cx, cy, q(34), q(39)) + '" fill="none" stroke="' + warna
                + '" stroke-width="' + N(q(12)) + '" stroke-linejoin="miter"/>'
                '<path d="' + heks_path(cx, cy, q(14), q(16)) + '" fill="' + warna + '"/>')
    if bentuk == 'perisai':
        return ('<path d="M' + N(cx) + ' ' + N(cy - q(40)) + 'L' + N(cx + q(30)) + ' ' + N(cy - q(26))
                + 'V' + N(cy - q(2)) + 'L' + N(cx) + ' ' + N(cy + q(40)) + 'L' + N(cx - q(30)) + ' '
                + N(cy - q(2)) + 'V' + N(cy - q(26)) + 'Z" fill="none" stroke="' + warna
                + '" stroke-width="' + N(q(12)) + '" stroke-linejoin="miter"/>'
                '<path d="' + heks_path(cx, cy - q(12), q(9), q(10)) + '" fill="' + warna + '"/>')
    return ('<path d="' + letusan_path(cx, cy, 6, q(46), q(20), -90) + '" fill="none" stroke="'
            + warna + '" stroke-width="' + N(q(11)) + '" stroke-linejoin="miter"/>'
            '<path d="' + letusan_path(cx, cy, 4, q(17), q(6), -90) + '" fill="' + warna + '"/>')

def kepala(judul, isi):
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<svg xmlns="http://www.w3.org/2000/svg" width="' + str(LEBAR_MM) + 'mm" height="'
            + str(TINGGI_MM) + 'mm" viewBox="0 0 ' + N(W) + ' ' + N(H) + '" role="img" aria-label="'
            + judul + '">\n<title>' + judul + '</title>\n<desc>Akrilik 3 mm, cetak UV, potong '
            'mengikuti bentuk. Lubang cincin 4 mm. 4 satuan = 1 mm.</desc>\n' + isi + '\n</svg>\n')

def lembar_depan():
    d, potong = ['<defs>'], []
    for i, (nama, bentuk, c1, c2, fg, hy, pw, ph, pdy, baris) in enumerate(TINGKAT):
        d.append('<linearGradient id="g' + str(i) + '" x1="0%" y1="0%" x2="20%" y2="100%">'
                 '<stop offset="0%" stop-color="' + c1 + '"/>'
                 '<stop offset="100%" stop-color="' + c2 + '"/></linearGradient>')
    d.append('</defs>')
    for i, (nama, bentuk, c1, c2, fg, hy, pw, ph, pdy, baris) in enumerate(TINGKAT):
        cx, cy = PUSAT[i]
        jalur = siluet(bentuk, cx, cy)
        py = cy + pdy
        pita = ('<rect x="' + N(cx - pw // 2) + '" y="' + N(py - ph // 2) + '" width="' + N(pw)
                + '" height="' + N(ph) + '" rx="' + N(ph // 2) + '" fill="' + CREAM
                + '" stroke="' + c2 + '" stroke-width="2"/>')
        for j, t in enumerate(baris):
            ty = py - (len(baris) - 1) * 8 + j * 16 + 4
            pita += teks(cx, ty, t, 11, AR, 700, INK, 1)
        naik = -32 if len(baris) > 1 or bentuk == 'perisai' else -26
        d.append('<g id="' + nama.split()[0].lower() + '">'
                 '<path d="' + jalur + '" fill="url(#g' + str(i) + ')"/>'
                 + lambang(bentuk, cx, cy + naik, fg, .8) + pita + '</g>')
        potong.append('<path d="' + jalur + '" fill="none" stroke="' + POTONG + '" stroke-width="2"/>'
                      '<circle cx="' + N(cx) + '" cy="' + N(cy + hy) + '" r="' + N(LUBANG)
                      + '" fill="none" stroke="' + POTONG + '" stroke-width="2"/>')
        d.append('<circle cx="' + N(cx) + '" cy="' + N(cy + hy) + '" r="' + N(LUBANG)
                 + '" fill="#FFFFFF"/>')
    d.append('<g id="POTONG">' + ''.join(potong) + '</g>')
    return kepala('Balikin — Gantungan kunci lima tingkat, depan', '\n'.join(d))

def lembar_belakang():
    d, potong = [], []
    for i, (nama, bentuk, c1, c2, fg, hy, pw, ph, pdy, baris) in enumerate(TINGKAT):
        cx, cy = PUSAT[i]
        jalur = siluet(bentuk, cx, cy)
        kata = nama.split()
        d.append('<g id="' + kata[0].lower() + '-belakang">'
                 '<path d="' + jalur + '" fill="' + CREAM + '"/>'
                 '<path d="' + jalur + '" fill="none" stroke="' + c2 + '" stroke-width="5"/>'
                 + teks(cx, cy - 26, 'TINGKAT ' + str(i + 1), 11, PJ, 700, c2, 3)
                 + teks(cx, cy + 6, kata[0], 20, AR, 700, INK)
                 + (teks(cx, cy + 30, kata[1], 20, AR, 700, INK) if len(kata) > 1 else '')
                 + teks(cx, cy + 58, 'BALIKIN', 11, AR, 700, INK, 3) + '</g>')
        potong.append('<path d="' + jalur + '" fill="none" stroke="' + POTONG + '" stroke-width="2"/>'
                      '<circle cx="' + N(cx) + '" cy="' + N(cy + hy) + '" r="' + N(LUBANG)
                      + '" fill="none" stroke="' + POTONG + '" stroke-width="2"/>')
        d.append('<circle cx="' + N(cx) + '" cy="' + N(cy + hy) + '" r="' + N(LUBANG)
                 + '" fill="#FFFFFF"/>')
    d.append('<g id="POTONG">' + ''.join(potong) + '</g>')
    return kepala('Balikin — Gantungan kunci lima tingkat, belakang', '\n'.join(d))

if __name__ == '__main__':
    OUT = os.path.join(_here, 'svg')
    for nama, isi in (('gantungan-lima-tingkat-depan', lembar_depan()),
                      ('gantungan-lima-tingkat-belakang', lembar_belakang())):
        open(os.path.join(OUT, nama + '.svg'), 'w', encoding='utf-8').write(isi)
        sisa = sorted(set(re.findall(r'-?\d+\.\d+', isi)))
        print('%-36s %5d B  desimal: %s' % (nama + '.svg', len(isi), sisa or 'tidak ada'))
