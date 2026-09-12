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
  ('Main', 'Balikin — Beranda A: lapor terang + reputasi', 'beranda-a-reputasi', 384, 844),
  ('BerandaB', 'Balikin — Beranda B: lapor teal + pintu jelajahi', 'beranda-b-jelajahi', 384, 844),
  ('BerandaC', 'Balikin — Beranda C: versi kartu peta', 'beranda-c-peta', 384, 844),
  ('Kartu1', 'Balikin — Kartu 1 Barang di sekitarmu', 'kartu-1-barang-di-sekitarmu', 390, 272),
  ('Kartu2A', 'Balikin — Kartu 2A Lapor, versi terang', 'kartu-2a-lapor-terang', 390, 180),
  ('Kartu2B', 'Balikin — Kartu 2B Lapor, versi teal', 'kartu-2b-lapor-teal', 390, 180),
  ('Kartu3A', 'Balikin — Kartu 3A Reputasimu', 'kartu-3a-reputasi', 390, 248),
  ('Kartu3C', 'Balikin — Kartu 3C Pintu ke halaman Jelajahi', 'kartu-3c-pintu-jelajahi', 390, 248),
  ('Kartu3B', 'Balikin — Kartu 3B Jelajahi peta (disimpan)', 'kartu-3b-jelajahi-peta', 390, 248),
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
