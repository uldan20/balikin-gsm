# -*- coding: utf-8 -*-
"""Menulis 24 halaman GSM jadi SVG cetak A5 lanskap 210 x 148 mm.

Pakai pengonversi yang sama dengan poster showcase:

    for f in gsm/Main.dc.html gsm/H*.dc.html; do
      node showcase/ekstrak.mjs $PWD/$f /tmp/claude-0/gsmjson/$(basename $f .dc.html).json 840 592
    done
    python3 gsm/ke_svg_gsm.py
"""
import os, re, sys
DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(DIR, '..', 'showcase'))
from ke_svg import bangun

JSON = sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-0/gsmjson'
KELUAR = os.path.join(DIR, 'svg')
UKURAN = ('210mm', '148mm')
KET = ('A5 lanskap 210 x 148 mm, 4 satuan = 1 mm. '
       'Huruf: Archivo, Plus Jakarta Sans, Caveat.')

HAL = [('Main', 1, 'Sampul'), ('H02', 2, 'Daftar isi'), ('H03', 3, 'Pembatas Bab I'),
       ('H04', 4, 'Produk dan pengguna'), ('H05', 5, 'Tagline & kepribadian'),
       ('H06', 6, 'Pembatas Bab II'), ('H07', 7, 'Logogram'), ('H08', 8, 'Konstruksi'),
       ('H09', 9, 'Ruang aman'), ('H10', 10, 'Ukuran minimum'), ('H11', 11, 'Konfigurasi'),
       ('H12', 12, 'Warna logo'), ('H13', 13, 'Larangan'), ('H14', 14, 'Pembatas Bab III'),
       ('H15', 15, 'Palet warna'), ('H16', 16, 'Tipografi'), ('H17', 17, 'Sudut Enam'),
       ('H18', 18, 'Pustaka ikon'), ('H19', 19, 'Pola sarang'), ('H20', 20, 'Maskot'),
       ('H21', 21, 'Tulisan tangan'), ('H22', 22, 'Pembatas Bab IV'),
       ('H23', 23, 'Layar dan cetak'), ('H24', 24, 'Merchandise & booth')]

if __name__ == '__main__':
    os.makedirs(KELUAR, exist_ok=True)
    total, semua_sisa = 0, set()
    for berkas, nomor, nama in HAL:
        sumber = os.path.join(JSON, berkas + '.json')
        if not os.path.exists(sumber):
            print('lewat  %s — %s belum diekstrak' % (berkas, sumber)); continue
        judul = 'GSM Balikin — %02d %s' % (nomor, nama)
        svg = bangun(sumber, judul, UKURAN, KET)
        nm = 'gsm-%02d-%s.svg' % (nomor, re.sub(r'[^a-z0-9]+', '-', nama.lower()).strip('-'))
        open(os.path.join(KELUAR, nm), 'w', encoding='utf-8').write(svg)
        sisa = sorted(set(re.findall(r'-?\d+\.\d+', svg)))
        semua_sisa |= set(sisa)
        total += len(svg)
        print('%-34s %5d KB  desimal: %d %s' % (nm, len(svg) // 1024, len(sisa), sisa[:6]))
    print('\n%d berkas, %d KB. Desimal tersisa di seluruh berkas: %s'
          % (len(HAL), total // 1024, sorted(semua_sisa)[:20] or 'tidak ada'))
