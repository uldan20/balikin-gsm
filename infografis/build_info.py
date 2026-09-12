# -*- coding: utf-8 -*-
"""Tiga lembar infografis A3 untuk pameran Balikin.

I1 · Pustaka Ikon Sudut Enam   — isi kotak: 98 bentuk, 196 komponen
I2 · Perjalanan Sebuah Dompet  — tujuh langkah dari hilang ke pulang
I3 · Naik Tingkat              — poin dan lima tingkat komunitas

Semua angka diambil dari repo aplikasi dan naskah skripsi. Lihat README.md.
"""
import os, json
from kit_info import *

OUT = os.path.dirname(os.path.abspath(__file__))

def tulis(nama, isi_, latar):
    open(os.path.join(OUT, nama), 'w', encoding='utf-8').write(doc(lembar(latar, isi_), latar))
    print(nama)

def potong(n=14):
    return ('clip-path:polygon(' + str(n) + 'px 0,100% 0,100% calc(100% - ' + str(n) + 'px),'
            'calc(100% - ' + str(n) + 'px) 100%,0 100%,0 ' + str(n) + 'px);')

def svg_lapis(isi_, z=2):
    return ('<svg style="position:absolute;left:0;top:0;width:' + str(W) + 'px;height:' + str(H)
            + 'px;z-index:' + str(z) + '" viewBox="0 0 ' + str(W) + ' ' + str(H) + '" fill="none">'
            + isi_ + '</svg>')

# ============================================================ I1 · PUSTAKA IKON
# 98 ikon garis, dihitung dari src/icons/hexcut di repo uldan20/balikin.
KELUARGA = [
  # (label, jumlah, warna, ikon, keterangan)
  ('AKSI',       18, MINT, ['cari', 'tambah', 'obrolan', 'panah', 'camera', 'scan'],
   'Cari, lapor, kirim, bagikan, pindai.'),
  ('BARANG',     13, TERL, ['kunci', 'ponsel', 'dokumen', 'bag'], None),
  ('SISTEM',     12, CREAM, ['peta', 'lonceng', 'gembok'], 'Peta, notifikasi, keamanan.'),
  ('LENCANA',    11, GOLDL, ['bintang', 'perisai'], 'Sembilan pencapaian dan wadahnya.'),
  ('FORMULIR',   11, MINT, ['kartu', 'camera', 'check'], 'Isian laporan dan verifikasi.'),
  ('PENCAPAIAN',  9, GOLDL, ['bintang', 'jam'], None),
  ('NAVIGASI',    8, CREAM, ['grid', 'warga', 'peta'], None),
  ('STATUS',      6, CREAM, ['jam', 'check'], None),
  ('BAYAR',       5, TERL, ['coin', 'wallet'], None),
  ('TINGKAT',     5, GOLDL, ['perisai'], None),
]
# tata letak petak: tiga baris, luas sebanding jumlah ikon (98 total)
PETAK = [  # (x, y, w, h) urut sesuai KELUARGA
  (184, 544, 309, 303), (501, 544, 223, 303), (732, 544, 206, 303),
  (184, 855, 262, 218), (454, 855, 262, 218), (724, 855, 214, 218),
  (184, 1081, 243, 169), (435, 1081, 183, 169), (626, 1081, 152, 169), (786, 1081, 152, 169),
]

def blok_ikon(i):
    lab, jml, bg, ikon_, ket = KELUARGA[i]
    x, y, w, h = PETAK[i]
    besar = 64 if h > 300 else (54 if h > 200 else 42)
    px = 34 if h > 300 else (34 if h > 200 else 30)
    dalam = [dv(font(PJ, 13, 700, INK, 2) + 'opacity:.62;', lab),
             dv(font(AR, besar, 700, INK, -2, 1) + 'margin-top:2px;', str(jml))]
    if ket and h > 200:
        dalam.append(dv(font(PJ, 14, 400, INK, None, 1.4) + 'opacity:.72;margin-top:6px;', ket))
    baris_ikon = dv('display:flex;flex-wrap:wrap;gap:12px;margin-top:auto;',
                    ''.join(ik(n, px, INK) for n in ikon_))
    isi_ = ''.join(dalam) + baris_ikon
    if lab == 'BARANG':
        # 8 dari 13 kategori tampil di onboarding — petak putus-putus, luasnya sebanding
        th = int(round((h - 24) * 8 / 13))
        anak = dv(P(x=0, b=0, w=w - 24, h=th,
                    lain='border:2px dashed ' + TERRA + ';background:rgba(188,90,60,.14);'
                         'box-sizing:border-box;padding:12px 14px;'),
                  dv(font(AR, 34, 700, INK, -1, 1), '8')
                  + dv(font(PJ, 13, 400, INK, None, 1.35) + 'opacity:.78;margin-top:4px;',
                       'kategori tampil di onboarding')
                  + dv('display:flex;gap:10px;margin-top:10px;',
                       ''.join(ik(n, 30, INK) for n in ikon_)))
        isi_ = ''.join(dalam) + anak
    return dv(P(x=x, y=y, w=w, h=h, z=5,
                lain='background:' + bg + ';' + potong(14) + 'box-sizing:border-box;'
                     'padding:16px 18px;display:flex;flex-direction:column;overflow:hidden;'), isi_)

kotak = svg_lapis(
  '<ellipse cx="561" cy="1344" rx="424" ry="17" fill="#0C2824" opacity=".16"/>'
  # dinding belakang — kita melihat sedikit ke dalam kotak
  '<path d="M176 478H946L898 384H224Z" fill="' + TEALX + '"/>'
  '<rect x="140" y="490" width="842" height="840" fill="' + TEAL + '"/>'
  # bibir kotak, sedikit lebih lebar dari badannya
  '<rect x="124" y="468" width="874" height="28" fill="' + TEALD + '"/>'
  '<rect x="124" y="468" width="874" height="8" fill="' + TEALB + '"/>'
  '<rect x="176" y="536" width="770" height="722" fill="' + TEALX + '"/>', z=2)

i1 = [kotak]
i1 += [blok_ikon(i) for i in range(len(KELUARGA))]
i1 += [
  kepala('Pustaka Ikon', 'Sudut Enam',
         'Balikin memakai 196 komponen ikon — 98 bentuk, masing-masing tersedia dalam varian '
         'garis dan padat. Semuanya digambar di kisi 60° yang sama.'),
  legenda([(MINT, 'Aksi & formulir', False), (TERL, 'Barang & bayar', False),
           (GOLDL, 'Reputasi', False), (CREAM, 'Navigasi & sistem', True)], 318),
  # keping "x2 varian padat"
  stiker_heks(dv(font(AR, 38, 700, INK, -1, 1, 'center'), '&times;2')
              + dv(font(PJ, 10, 700, INK, 2, 1, 'center') + 'margin-top:3px;', 'PADAT'),
              128, GOLDL, 9, x=892, y=398, z=14),
  # pita depan kotak
  dv(P(x=560, y=1272, w=386, h=46, z=6,
       lain='display:flex;align-items:center;justify-content:flex-end;gap:16px;'),
     teks(font(PJ, 14, 600, CREAM, 3) + 'opacity:.8;', 'KOTAK KOMPONEN') + logo(CREAM, GOLDL, 26, 2)),
  kartu_catatan(['Sudut dipangkas, bukan dibulatkan. Satu kisi 60° dan sambungan mitre — '
                 'itu yang membuat 196 komponen terbaca sebagai satu keluarga.',
                 '76 berkas SVG mandiri sudah siap dipakai di luar aplikasi: cetak, '
                 'signage, dan merchandise.'], 92, lebar=430, rot=-3, sisi='kiri', bawah=74),
  kaki_info('pustaka ikon Balikin · src/icons/hexcut', 1418, kiri=False),
  pita(TERRA, 'BALIKIN · SUDUT ENAM · 196 KOMPONEN'),
]
tulis('Main.dc.html', ''.join(i1), WASH)

# ==================================================== I2 · PERJALANAN
LANGKAH = [
  ('01', 'HILANG', 'Dompet tertinggal di angkot, sore hari.', TERRA, 'pin'),
  ('02', 'DILAPORKAN', 'Foto, kategori, lokasi, kirim. Empat langkah, dua menit.', TEAL, 'camera'),
  ('03', 'TAMPIL', 'Muncul di beranda warga dalam radius lima kilometer.', TEAL, 'grid'),
  ('04', 'DICOCOKKAN', 'Sistem menemukan laporan mirip dan menyodorkannya.', TEAL, 'scan'),
  ('05', 'DIVERIFIKASI', 'Tiga pertanyaan dari ciri rahasia yang dikunci pemiliknya.', TEAL, 'gembok'),
  ('06', 'DISERAHKAN', 'Titik aman ber-CCTV. Kode empat huruf dicocokkan di lokasi.', TEAL, 'bag'),
]

ATAS, PITCH, TINGGI = 456, 118, 112     # baris kartu langkah
JALAN_Y0, JALAN_Y1 = 452, 1166           # ujung jalan

def kartu_langkah(i):
    no, jdl, ket, warna, ikon_ = LANGKAH[i]
    y = ATAS + i * PITCH
    x = 76 if i % 2 == 0 else 700
    isi_ = (dv('flex:1;',
               dv(font(AR, 25, 700, INK, -1, 1), jdl)
               + dv(font(PJ, 15, 400, INK, None, 1.4) + 'opacity:.78;margin-top:6px;', ket))
            + dv('flex:none;', ik(ikon_, 46, warna)))
    return dv(P(x=x, y=y, w=346, h=TINGGI, z=6,
                lain='background:' + CREAM + ';' + potong(12) + 'border-left:8px solid ' + warna + ';'
                     'box-sizing:border-box;padding:15px 18px;display:flex;align-items:center;gap:14px;'
                     'box-shadow:0 18px 38px rgba(12,40,36,.15);'), isi_)

def penanda(i):
    """Heksagon bernomor di badan jalan, sejajar dengan kartunya."""
    no, jdl, ket, warna, ikon_ = LANGKAH[i]
    cy = ATAS + i * PITCH + TINGGI // 2
    px = 44 + i * 6
    return dv(P(x=561 - px // 2, y=cy - int(px * 1.15) // 2, w=px, h=int(px * 1.15), z=7,
                lain='background:' + CREAM + ';' + HEX + ';display:grid;place-items:center;'),
              teks(font(AR, int(px * 0.4), 700, TEALX, -1), no))

# garis putus-putus di antara penanda, ikut menyempit ke arah cakrawala
_dash = ''
for dy in [470] + [ATAS + i * PITCH + TINGGI + 4 for i in range(5)] + [1122]:
    t = (dy - JALAN_Y0) / float(JALAN_Y1 - JALAN_Y0)
    dw = int(round(7 + t * 15)); dh = int(round(16 + t * 26))
    _dash += ('<rect x="' + str(561 - dw // 2) + '" y="' + str(dy) + '" width="' + str(dw)
              + '" height="' + str(dh) + '" fill="' + CREAM + '" opacity=".4"/>')

# penghubung putus-putus dari kartu ke penanda
_tali = ''
for i in range(6):
    cy = ATAS + i * PITCH + TINGGI // 2
    px = 44 + i * 6
    if i % 2 == 0:
        x1, x2 = 422, 561 - px // 2
    else:
        x1, x2 = 561 + px // 2, 700
    _tali += ('<path d="M' + str(x1) + ' ' + str(cy) + 'H' + str(x2) + '" stroke="' + TEAL
              + '" stroke-width="2" stroke-dasharray="6 6" opacity=".55"/>')

_kota = ('<g fill="' + TEALX + '" opacity=".2">'
  # kampus
  '<path d="M96 428V366H236V428Z"/><path d="M92 366L166 332L240 366Z"/>'
  # halte
  '<path d="M272 372H380V382H272Z"/><path d="M280 382H288V428H280Z"/><path d="M364 382H372V428H364Z"/>'
  '<path d="M294 402H358V410H294Z"/>'
  # taman
  '<path d="M424 366L444 378V402L424 414L404 402V378Z"/><path d="M420 412H428V428H420Z"/>'
  '<path d="M472 378L488 388V406L472 416L456 406V388Z"/><path d="M468 414H476V428H468Z"/>'
  '<path d="M516 384L530 392V408L516 416L502 408V392Z"/><path d="M512 414H520V428H512Z"/>'
  # masjid
  '<path d="M556 428V378H680V428Z"/><path d="M586 378L602 350H634L650 378Z"/>'
  '<path d="M618 336L624 350H612Z"/><path d="M662 344H678V428H662Z"/><path d="M664 344L670 332L676 344Z"/>'
  # pusat perbelanjaan
  '<path d="M724 428V388H1026V428Z"/><path d="M752 388V364H998V388Z"/>'
  '</g>'
  '<path d="M800 400H948V412H800Z" fill="' + CREAM + '" opacity=".5"/>')

i2 = [
  svg_lapis(_kota
            + '<path d="M538 452H584L682 1166H440Z" fill="' + TEALX + '"/>'
            + '<path d="M538 452H584L682 1166H440Z" fill="none" stroke="' + TEAL + '" stroke-width="6"/>'
            + _dash + _tali, z=2),
  dv(P(x=0, w=W, y=434, z=4, lain=font(PJ, 11, 700, INK, 3, 1, 'center') + 'opacity:.5;'),
     'LOKASI OBSERVASI &middot; KAMPUS &middot; HALTE &middot; TAMAN KOTA &middot; MASJID BESAR &middot; PUSAT PERBELANJAAN'),
]
i2 += [kartu_langkah(i) for i in range(len(LANGKAH))]
i2 += [penanda(i) for i in range(len(LANGKAH))]
i2 += [
  dv(P(x=872, y=452, z=5), bee(120, -12)),
  # langkah tujuh — barang pulang
  dv(P(x=231, y=1166, w=660, h=120, z=7,
       lain='background:' + GOLD + ';' + potong(16) + 'box-sizing:border-box;padding:0 26px;'
            'display:flex;align-items:center;gap:22px;box-shadow:0 22px 44px rgba(12,40,36,.2);'),
     dv('width:60px;height:69px;background:' + CREAM + ';' + HEX
        + ';display:grid;place-items:center;flex:none;', ik('check', 32, GOLDD))
     + dv('flex:1;',
          dv(font(PJ, 13, 700, INK, 3) + 'opacity:.7;', '07')
          + dv(font(AR, 27, 700, INK, -1, 1) + 'margin-top:4px;', 'PULANG')
          + dv(font(PJ, 15, 400, INK, None, 1.4) + 'opacity:.8;margin-top:5px;',
              'Barang kembali ke pemiliknya. Penemunya mendapat poin reputasi.'))
     + dv('flex:none;text-align:center;background:' + CREAM + ';' + potong(10)
          + 'padding:12px 18px;',
          dv(font(AR, 34, 700, GOLDD, -1, 1), '+150')
          + dv(font(PJ, 11, 700, INK, 2) + 'opacity:.6;margin-top:3px;', 'POIN'))),
  kepala('Perjalanan', 'Sebuah Dompet',
         'Tujuh langkah dari tertinggal di angkot sampai kembali ke pemiliknya — '
         'dan siapa yang bergerak di tiap langkah.'),
  legenda([(TERRA, 'Pemilik kehilangan', False), (TEAL, 'Aplikasi bekerja', False),
           (GOLD, 'Barang pulang', False)], 318),
  kartu_catatan(['Temuan lapangan: penemu kerap ragu bertindak — takut dituduh mencuri, '
                 'atau tidak tahu cara mengembalikan dengan aman.',
                 'Karena itu tiap langkah meninggalkan bukti: foto, ciri rahasia, titik serah '
                 'ber-CCTV, dan kode empat huruf.'], 92, lebar=430, rot=-3, sisi='kiri', bawah=74),
  kaki_info('naskah TA & prototipe Balikin', 1400, kiri=False),
  pita(TEAL, 'BALIKIN · YANG HILANG, BALIK PULANG'),
]
tulis('Perjalanan.dc.html', ''.join(i2), CREAM)

# ==================================================== I3 · NAIK TINGKAT
# Rentang poin dari layar Tingkat & Poin di prototipe; nama tingkat sama persis
# dengan Tiers.tsx. Luas tiap pita sebanding dengan lebar rentangnya.
TINGKAT_I = [  # (nama, rentang, y, tinggi, warna, warna teks, ikon)
  ('Legenda Balikin', '2.000 ke atas', 410, 120, GOLD, CREAM, 'tk5'),
  ('Penjaga Kota', '900 – 2.000', 530, 385, TERRA, CREAM, 'tk4'),
  ('Penolong', '400 – 900', 915, 175, TEAL, CREAM, 'tk3'),
  ('Tetangga Baik', '150 – 400', 1090, 88, MINTT, INK, 'tk2'),
  ('Warga Baru', '0 – 150', 1178, 53, KRIM, INK, 'tk1'),
]
NAIK = [('Barang kembali ke pemiliknya', '+150'), ('Laporan tepat dan terverifikasi', '+50'),
        ('KTP terverifikasi', '+40'), ('Foto wajah terverifikasi', '+30')]
TURUN = [('Laporan palsu', '−50'), ('Klaim berulang', '−30'),
         ('Batal janji temu tanpa kabar', '−20')]
LENCANA_I = [('Balik Pertama', 'check'), ('10 Barang', 'grid'), ('Balas Cepat', 'obrolan'),
             ('Mata Elang', 'cari'), ('Dokumen', 'dokumen'), ('Jaga Malam', 'jam'),
             ('Nol Sengketa', 'perisai'), ('Penggerak', 'warga'), ('Legenda', 'bintang')]

def pita_tingkat(t):
    nama, rentang, y, h, bg, fg, ikon_ = t
    lencana_px = 52 if h > 140 else (44 if h > 70 else 36)
    wadah = dv('width:' + str(lencana_px) + 'px;height:' + str(int(lencana_px * 1.15)) + 'px;'
               'background:rgba(251,248,243,.22);' + HEX + ';display:grid;place-items:center;flex:none;',
               ik(ikon_, int(lencana_px * 0.66), fg))
    if h < 70:
        kiri = dv('display:flex;align-items:baseline;gap:12px;flex:1;',
                  teks(font(AR, 19, 700, fg, -1), nama)
                  + teks(font(PJ, 13, 600, fg) + 'opacity:.8;', rentang + ' poin'))
    else:
        kiri = dv('flex:1;',
                  dv(font(AR, 26 if h > 140 else 21, 700, fg, -1, 1), nama)
                  + dv(font(PJ, 15 if h > 140 else 13, 600, fg, None, 1.3) + 'opacity:.85;margin-top:6px;',
                       rentang + ' poin'))
    return dv(P(x=300, y=y, w=400, h=h, z=6,
                lain='background:' + bg + ';box-sizing:border-box;padding:0 22px;'
                     'display:flex;align-items:center;gap:16px;'), kiri + wadah)

def sumbu():
    """Skala poin di sisi kiri toples."""
    isi_ = ['<path d="M270 410V1231" stroke="' + INK + '" stroke-width="2" opacity=".35"/>']
    lab = []
    for nilai, y in (('2.000', 530), ('900', 915), ('400', 1090), ('150', 1178), ('0', 1231)):
        isi_.append('<path d="M258 ' + str(y) + 'H282" stroke="' + INK + '" stroke-width="2" opacity=".45"/>')
        lab.append(dv(P(x=182, y=y - 11, w=74, z=5,
                        lain=font(PJ, 16, 700, INK, None, 1, 'right') + 'opacity:.7;'), nilai))
    lab.append(dv(P(x=182, y=384, w=74, z=5,
                    lain=font(PJ, 11, 700, INK, 2, 1, 'right') + 'opacity:.5;'), 'POIN'))
    return svg_lapis(''.join(isi_), z=4) + ''.join(lab)

def baris_poin(label, nilai, naik=True):
    warna = TEAL if naik else TERRA
    chip = dv('background:' + warna + ';' + potong(8) + 'padding:6px 12px;flex:none;min-width:62px;',
              teks(font(AR, 17, 700, CREAM, -1) + 'display:block;text-align:center;', nilai))
    return dv('display:flex;align-items:center;gap:14px;height:44px;',
              chip + teks(font(PJ, 14, 400, INK, None, 1.3), label))

def panel_poin():
    kepala_naik = dv('display:flex;align-items:center;gap:10px;',
                     ik('tambah', 18, TEAL) + teks(font(PJ, 13, 700, TEAL, 2), 'POIN NAIK'))
    kepala_turun = dv('display:flex;align-items:center;gap:10px;margin-top:6px;',
                      ik('kurang', 18, TERRA) + teks(font(PJ, 13, 700, TERRA, 2), 'POIN TURUN'))
    garis = dv('height:2px;background:' + FILL + ';margin:16px 0;')
    isi_ = (kepala_naik + ''.join(baris_poin(a, b, True) for a, b in NAIK) + garis
            + kepala_turun + ''.join(baris_poin(a, b, False) for a, b in TURUN))
    return dv(P(x=740, y=410, w=318, h=446, z=6,
                lain='background:' + CREAM + ';' + potong(14) + 'box-sizing:border-box;'
                     'padding:22px 22px 18px;box-shadow:0 20px 44px rgba(12,40,36,.14);'), isi_)

def panel_lencana():
    sel = []
    for nama, ikon_ in LENCANA_I:
        sel.append(dv('width:86px;text-align:center;',
                      dv('width:52px;height:60px;background:' + GOLDL + ';' + HEX
                         + ';display:grid;place-items:center;margin:0 auto;', ik(ikon_, 26, GOLDD))
                      + dv(font(PJ, 11, 600, INK, None, 1.25) + 'margin-top:7px;', nama)))
    return dv(P(x=740, y=886, w=318, h=354, z=6,
                lain='background:rgba(251,248,243,.7);' + potong(14) + 'box-sizing:border-box;'
                     'padding:20px 16px;border:2px solid rgba(33,28,22,.12);'),
              dv(font(PJ, 13, 700, INK, 2) + 'opacity:.6;text-align:center;', 'SEMBILAN LENCANA')
              + dv('display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:16px;',
                   ''.join(sel)))

i3 = [
  svg_lapis('<ellipse cx="500" cy="1260" rx="236" ry="14" fill="#0C2824" opacity=".14"/>'
            '<rect x="300" y="410" width="400" height="821" fill="' + CREAM + '"/>'
            '<rect x="278" y="1231" width="444" height="18" fill="' + TEALD + '"/>'
            '<rect x="278" y="1231" width="444" height="6" fill="' + TEALB + '"/>', z=2),
  sumbu(),
]
i3 += [pita_tingkat(t) for t in TINGKAT_I]
i3 += [
  # tepi atas terbuka — tingkat teratas tidak punya batas
  svg_lapis('<path d="M300 410H700" stroke="' + CREAM + '" stroke-width="6" stroke-dasharray="12 10"/>'
            '<rect x="300" y="410" width="400" height="821" fill="none" stroke="' + INK
            + '" stroke-width="4" opacity=".22"/>', z=8),
  dv(P(x=690, y=346, z=9), bee(116, 14)),
  panel_poin(), panel_lencana(),
  stiker_heks(dv(font(AR, 30, 700, INK, -1, 1, 'center'), '+150')
              + dv(font(PJ, 10, 700, INK, 1, 1, 'center') + 'margin-top:4px;', 'PER BARANG'),
              116, GOLDL, -8, x=62, y=566, z=14),
  kepala('Naik Tingkat', 'Lima Tingkat Komunitas',
         'Poin hanya bertambah kalau ada barang yang benar-benar kembali. Luas tiap pita di bawah '
         'sebanding dengan jarak poin yang harus ditempuh.'),
  legenda([(KRIM, 'Warga Baru', True), (MINTT, 'Tetangga Baik', False), (TEAL, 'Penolong', False),
           (TERRA, 'Penjaga Kota', False), (GOLD, 'Legenda Balikin', False)], 318),
  kartu_catatan(['Poin adalah bentuk pengakuan, bukan imbalan uang. Tip lewat QRIS bersifat '
                 'sukarela dan terpisah dari sistem poin.',
                 'Butuh sekitar 14 barang yang benar-benar pulang untuk sampai ke Legenda Balikin. '
                 'Tingkat tidak bisa dibeli.'], 92, lebar=430, rot=-3, sisi='kiri', bawah=74),
  kaki_info('Tiers.tsx & layar Tingkat dan Poin', 1400, kiri=False),
  pita(GOLD, 'BALIKIN · POIN UNTUK PENGAKUAN, BUKAN UANG', INK),
]
tulis('Tingkat.dc.html', ''.join(i3), MINT)

# ==================================================== kanvas
kanvas = {"artboards": [
  {"file": "Main.dc.html", "x": 0, "y": 0, "w": W, "h": H, "title": "I1 · Pustaka Ikon"},
  {"file": "Perjalanan.dc.html", "x": 1280, "y": 0, "w": W, "h": H, "title": "I2 · Perjalanan Sebuah Dompet"},
  {"file": "Tingkat.dc.html", "x": 2560, "y": 0, "w": W, "h": H, "title": "I3 · Naik Tingkat"}],
 "annotations": [{"id": "catatan", "x": 0, "y": -200, "w": 900,
   "text": "Tiga lembar infografis A3 potret 297 × 420 mm — artboard 1122 × 1587 px (A3 pada 96 ppi).\n"
           "Semua angka diambil dari repo aplikasi (src/icons/hexcut), layar prototipe, dan naskah TA.\n"
           "Angka yang perlu dicek ulang ke prototipe ditandai di README.md folder ini."}],
 "launch": {"view": "canvas"}}
open(os.path.join(OUT, 'canvas.json'), 'w', encoding='utf-8').write(
    json.dumps(kanvas, indent=2, ensure_ascii=False))
print('canvas.json — ' + str(len(kanvas['artboards'])) + ' artboard')
