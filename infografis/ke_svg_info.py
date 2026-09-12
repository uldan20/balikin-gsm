# -*- coding: utf-8 -*-
"""Mengubah tiga lembar infografis dari .dc.html menjadi SVG A3.

Dua tahap, sama seperti poster showcase:
    node ../showcase/ekstrak.mjs <lembar>.dc.html /tmp/inf-<lembar>.json
    python3 ke_svg_info.py
"""
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'showcase'))
from ke_svg import bangun

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'svg')

if __name__ == '__main__':
    for berkas, judul, nama in [
        ('Main', 'Infografis Balikin — I1 Pustaka Ikon Sudut Enam', 'infografis-i1-pustaka-ikon'),
        ('Perjalanan', 'Infografis Balikin — I2 Perjalanan Sebuah Dompet', 'infografis-i2-perjalanan'),
        ('Tingkat', 'Infografis Balikin — I3 Naik Tingkat', 'infografis-i3-naik-tingkat')]:
        svg = bangun('/tmp/claude-0/inf-' + berkas + '.json', judul)
        keluar = os.path.join(OUT, nama + '.svg')
        open(keluar, 'w', encoding='utf-8').write(svg)
        sisa = sorted(set(re.findall(r'-?\d+\.\d+', svg)))
        print('%-34s %5d KB  desimal: %d %s' % (nama + '.svg', len(svg) // 1024, len(sisa), sisa[:8]))
