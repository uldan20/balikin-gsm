# -*- coding: utf-8 -*-
"""Ekspor layar dan kartu beranda ke SVG.

    for f in Main BerandaB Kartu1 Kartu2 Kartu3A Kartu3B; do
      node ../showcase/ekstrak.mjs $PWD/$f.dc.html /tmp/claude-0/br-$f.json
    done
    python3 ke_svg_app.py
"""
import os, sys, re, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'showcase'))
from ke_svg import bangun

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'svg')
KET = 'Satuan piksel logis. Huruf: Archivo, Plus Jakarta Sans.'

# ekstraktor memakai lebar badan halaman, jadi ukuran artboard ditulis di sini
BERKAS = [
  ('Main', 'Balikin — Beranda hub, kartu ketiga reputasi', 'beranda-a-reputasi', 384, 844),
  ('BerandaB', 'Balikin — Beranda hub, kartu ketiga jelajahi', 'beranda-b-jelajahi', 384, 844),
  ('Kartu1', 'Balikin — Kartu 1 Barang di sekitarmu', 'kartu-1-barang-di-sekitarmu', 390, 254),
  ('Kartu2', 'Balikin — Kartu 2 Mau lapor apa hari ini', 'kartu-2-lapor', 390, 162),
  ('Kartu3A', 'Balikin — Kartu 3A Reputasimu', 'kartu-3a-reputasi', 390, 254),
  ('Kartu3B', 'Balikin — Kartu 3B Jelajahi peta', 'kartu-3b-jelajahi', 390, 254),
]

if __name__ == '__main__':
    for berkas, judul, nama, lw, lh in BERKAS:
        jalur = '/tmp/claude-0/br-' + berkas + '.json'
        d = json.load(open(jalur, encoding='utf-8'))
        d['w'], d['h'] = lw, lh
        jalur2 = '/tmp/claude-0/br-' + berkas + '-pas.json'
        json.dump(d, open(jalur2, 'w', encoding='utf-8'))
        svg = bangun(jalur2, judul, (str(lw), str(lh)), KET)
        keluar = os.path.join(OUT, nama + '.svg')
        open(keluar, 'w', encoding='utf-8').write(svg)
        sisa = sorted(set(re.findall(r'-?\d+\.\d+', svg)))
        print('%-32s %4dx%-4d %4d KB  desimal: %d %s'
              % (nama + '.svg', lw, lh, len(svg) // 1024, len(sisa), sisa[:7]))
