# -*- coding: utf-8 -*-
"""Infografis penelitian A3 — lima bagian wajib untuk papan pameran:
latar belakang, temuan permasalahan, tujuan penelitian, metode penelitian &
perancangan, dan kesimpulan.

Dua versi: Terang (latar wash) dan Gelap (latar teal tua bersarang).
Isi dikutip dari naskah lewat isi_riset.py.
"""
import os, json
from kit_info import *
from isi_riset import *

# ---------------------------------------------------------------- potongan isi
def kepala_lembar(gelap=False):
    fg = CREAM if gelap else INK
    fg2 = 'rgba(251,248,243,.72)' if gelap else 'rgba(33,28,22,.7)'
    aksen = GOLDL if gelap else TERRA
    return ''.join([
      dv(P(x=0, w=W, y=34, z=9, lain=font(PJ, 12, 700, fg, 4, 1, 'center') + 'opacity:.6;'),
         'TUGAS AKHIR &middot; DESAIN KOMUNIKASI VISUAL'),
      dv(P(x=0, w=W, y=56, z=9, lain=font(AR, 23, 700, fg, -1, 1.2, 'center')), JUDUL_ATAS),
      dv(P(x=0, w=W, y=80, z=9, lain=font(AR, 80, 700, aksen, -3, 1, 'center')), JUDUL_NAMA),
      dv(P(x=131, w=860, y=166, z=9, lain=font(PJ, 19, 500, fg, None, 1.35, 'center')), JUDUL_BAWAH),
      dv(P(x=131, w=860, y=194, z=9, lain=font(PJ, 15, 400, fg2, None, 1.3, 'center')),
         '(' + JUDUL_KASUS + ')'),
    ])

def pita_meta(y, bg, fg=CREAM):
    pisah = teks(font(PJ, 13, 400, fg) + 'opacity:.45;flex:none;', '|')
    isi_ = dv('display:flex;align-items:center;justify-content:center;gap:20px;height:100%;'
              'white-space:nowrap;',
              teks(font(PJ, 13, 700, fg, 1), PENULIS + ' &middot; ' + NIM) + pisah
              + teks(font(PJ, 13, 400, fg) + 'opacity:.9;', BIMBING[0]) + pisah
              + teks(font(PJ, 13, 400, fg) + 'opacity:.9;', BIMBING[1]))
    return dv(P(x=70, y=y, w=982, h=40, z=8, lain='background:' + bg + ';' + potong(10)), isi_)

def isi_latar(fg, fg2):
    kol = lambda t: dv('flex:1;' + font(PJ, 14, 400, fg, None, 1.5), t)
    return dv('display:flex;gap:24px;', ''.join(kol(t) for t in LATAR))

def isi_temuan(fg, fg2, warna=TERRA):
    baris = []
    for judul_, ikon_, ket in TEMUAN:
        baris.append(dv('display:flex;gap:13px;margin-top:15px;',
                        dv('width:38px;height:44px;background:' + warna + ';' + HEX
                           + ';display:grid;place-items:center;flex:none;', ik(ikon_, 20, CREAM))
                        + dv('flex:1;',
                             dv(font(AR, 17, 700, fg, -1, 1.15), judul_)
                             + dv(font(PJ, 13, 400, fg2, None, 1.4) + 'margin-top:4px;', ket))))
    return ''.join(baris)

def isi_tujuan(fg, fg2, warna=TEAL):
    baris = []
    for i, t in enumerate(TUJUAN):
        baris.append(dv('display:flex;gap:12px;margin-top:14px;',
                        dv('width:30px;height:35px;background:' + warna + ';' + HEX
                           + ';display:grid;place-items:center;flex:none;',
                           teks(font(AR, 15, 700, CREAM), '0' + str(i + 1)))
                        + dv('flex:1;' + font(PJ, 14, 400, fg, None, 1.45), t)))
    teori = dv('margin-top:15px;padding-top:12px;border-top:2px dashed '
               + ('rgba(251,248,243,.28)' if fg == CREAM else FILL) + ';',
               dv(font(PJ, 11, 700, fg2, 2), 'LANDASAN TEORI')
               + ''.join(dv(font(PJ, 12, 400, fg2, None, 1.4) + 'margin-top:5px;', t) for t in TEORI))
    return ''.join(baris) + teori

def isi_metode(fg, fg2, gelap=False):
    garis = 'rgba(251,248,243,.22)' if gelap else FILL
    # tiga cara pengumpulan data
    kartu_kecil = []
    for nama, ikon_, cap, ket in PENGUMPULAN:
        kartu_kecil.append(dv('flex:1;background:' + ('rgba(251,248,243,.08)' if gelap else WASH)
                              + ';' + potong(10) + 'padding:13px 15px;box-sizing:border-box;',
                              dv('display:flex;align-items:center;gap:9px;',
                                 ik(ikon_, 19, GOLDL if gelap else TEAL)
                                 + teks(font(AR, 15, 700, fg, -1), nama))
                              + dv(font(PJ, 11, 700, GOLDL if gelap else TEAL, 1) + 'margin-top:6px;', cap)
                              + dv(font(PJ, 11, 400, fg2, None, 1.4) + 'margin-top:4px;', ket)))
    # lima tahap design thinking
    sel = []
    for i, (nama, ket) in enumerate(TAHAP):
        sel.append(dv('flex:1;text-align:center;',
                      dv('width:44px;height:51px;background:' + (GOLDL if gelap else TEAL) + ';' + HEX
                         + ';display:grid;place-items:center;margin:0 auto;',
                         teks(font(AR, 17, 700, INK if gelap else CREAM), str(i + 1)))
                      + dv(font(AR, 14, 700, fg, -1) + 'margin-top:7px;', nama)
                      + dv(font(PJ, 10, 400, fg2, None, 1.35) + 'margin-top:3px;', ket)))
    cip = lambda t: dv('background:' + ('rgba(251,248,243,.12)' if gelap else FILL) + ';'
                       + potong(7) + 'padding:5px 11px;' + font(PJ, 11, 600, fg), t)
    lab = lambda t: teks(font(PJ, 11, 700, fg2, 2) + 'flex:none;', t)
    return ''.join([
      dv('display:flex;gap:13px;', ''.join(kartu_kecil)),
      dv('display:flex;align-items:center;gap:8px;margin-top:13px;flex-wrap:wrap;',
         lab('PENDEKATAN') + ''.join(cip(a) for a in PENDEKATAN) + lab('ANALISIS')
         + ''.join(cip(a) for a in ANALISIS)),
      dv('display:flex;align-items:center;gap:8px;margin-top:7px;flex-wrap:wrap;',
         lab('PENGUJIAN') + cip(PENGUJIAN)),
      dv('display:flex;gap:10px;align-items:flex-start;margin-top:12px;padding-top:12px;'
         'border-top:2px solid ' + garis + ';', ''.join(sel)),
    ])

def isi_kesimpulan(fg, fg2, gelap=False):
    garis = 'rgba(251,248,243,.22)' if gelap else FILL
    aksen = GOLDL if gelap else TEAL
    # takaran SEQ
    isi_takar = []
    for i in range(7):
        penuh = i < 6
        isi_takar.append(dv('flex:1;height:12px;background:'
                            + (aksen if penuh else ('rgba(251,248,243,.18)' if gelap else FILL)) + ';'))
    seq = dv('flex:none;width:270px;',
             dv('display:flex;align-items:baseline;gap:6px;',
                teks(font(AR, 58, 700, aksen, -3, 1), SEQ_NILAI)
                + teks(font(AR, 22, 700, fg2, -1), '/ ' + SEQ_MAKS))
             + dv('display:flex;gap:4px;margin-top:10px;', ''.join(isi_takar))
             + dv(font(PJ, 11, 700, fg2, 2) + 'margin-top:8px;', 'RATA-RATA SEQ &middot; 50 RESPONDEN')
             + dv(font(PJ, 13, 400, fg, None, 1.4) + 'margin-top:5px;', SEQ_KET))
    angka = []
    for nilai, ket in ANGKA:
        angka.append(dv('flex:1;',
                        dv(font(AR, 34, 700, fg, -2, 1), nilai)
                        + dv(font(PJ, 12, 400, fg2, None, 1.4) + 'margin-top:5px;', ket)))
    kanan = dv('flex:1;',
               dv('display:flex;gap:18px;', ''.join(angka))
               + dv('margin-top:15px;padding-top:13px;border-top:2px solid ' + garis + ';'
                    + font(PJ, 13, 400, fg, None, 1.45), KESIMPULAN[0])
               + dv(font(PJ, 13, 400, fg2, None, 1.45) + 'margin-top:8px;', KESIMPULAN[1]))
    return (dv('display:flex;gap:24px;', seq + kanan)
            + dv('margin-top:11px;padding-top:9px;border-top:2px dashed ' + garis + ';'
                 + font(PJ, 12, 400, fg2, None, 1.4), BATAS))

# ================================================================ V1 · TERANG
G = INK
G2 = 'rgba(33,28,22,.72)'
v1 = [
  svg_lapis('<path d="M0 0H1122V272H0Z" fill="' + MINT + '" opacity=".5"/>', z=1),
  dv(P(x=0, y=0, w=W, h=272, z=1, lain='overflow:hidden;'), sarang(TEAL, '.1', 3)),
  kepala_lembar(),
  pita_meta(228, TEAL),
  dv(P(x=48, y=44, z=10), bee(92, -12)),
  dv(P(r=48, y=52, z=10), bee(80, 14)),
  dv(P(x=44, y=142, z=10), mark(TERRA, 19, -6)),
  kartu_bagian(70, 280, 982, 212, 'LATAR BELAKANG', TEAL, isi_latar(G, G2)),
  kartu_bagian(70, 512, 548, 356, 'TEMUAN PERMASALAHAN', TERRA, isi_temuan(G, G2)),
  kartu_bagian(642, 512, 410, 356, 'TUJUAN PENELITIAN', TEALB, isi_tujuan(G, G2)),
  kartu_bagian(70, 888, 982, 352, 'METODE PENELITIAN & PERANCANGAN', TEALX, isi_metode(G, G2)),
  kartu_bagian(70, 1260, 982, 256, 'KESIMPULAN', GOLD, isi_kesimpulan(G, G2), fg_tag=INK),
  pita(TERRA, 'BALIKIN &middot; YANG HILANG, BALIK PULANG'),
]
tulis('Main.dc.html', ''.join(v1), WASH)

# ================================================================ V2 · GELAP
D = CREAM
D2 = 'rgba(251,248,243,.72)'
KACA = 'rgba(251,248,243,.07)'
v2 = [
  dv(P(x=0, y=0, w=W, h=H, z=1, lain='overflow:hidden;'), sarang(TEALB, '.13', 3)),
  kepala_lembar(gelap=True),
  pita_meta(228, 'rgba(251,248,243,.1)', CREAM),
  dv(P(x=48, y=44, z=10), bee(92, -12)),
  dv(P(r=48, y=52, z=10), bee(80, 14)),
  dv(P(x=44, y=142, z=10), mark(GOLDL, 19, -6)),
  kartu_bagian(70, 280, 982, 212, 'LATAR BELAKANG', GOLDL, isi_latar(D, D2),
               bg=KACA, fg_tag=INK),
  kartu_bagian(70, 512, 548, 356, 'TEMUAN PERMASALAHAN', TERRA,
               isi_temuan(D, D2, TERRA), bg=KACA),
  kartu_bagian(642, 512, 410, 356, 'TUJUAN PENELITIAN', TEALB,
               isi_tujuan(D, D2, TEALB), bg=KACA, fg_tag=INK),
  kartu_bagian(70, 888, 982, 352, 'METODE PENELITIAN & PERANCANGAN', CREAM,
               isi_metode(D, D2, gelap=True), bg=KACA, fg_tag=INK),
  kartu_bagian(70, 1260, 982, 256, 'KESIMPULAN', GOLD,
               isi_kesimpulan(D, D2, gelap=True), bg=KACA, fg_tag=INK),
  pita(GOLD, 'BALIKIN &middot; YANG HILANG, BALIK PULANG', INK),
]
tulis('Gelap.dc.html', ''.join(v2), TEAL)

# ================================================================ kanvas
kanvas = {"artboards": [
  {"file": "Main.dc.html", "x": 0, "y": 0, "w": W, "h": H, "title": "A · Papan Penelitian (terang)"},
  {"file": "Gelap.dc.html", "x": 1280, "y": 0, "w": W, "h": H, "title": "B · Papan Penelitian (gelap)"},
  {"file": "Ikon.dc.html", "x": 2688, "y": 0, "w": W, "h": H, "title": "Cadangan · Pustaka Ikon"},
  {"file": "Perjalanan.dc.html", "x": 3968, "y": 0, "w": W, "h": H, "title": "Cadangan · Perjalanan"},
  {"file": "Tingkat.dc.html", "x": 5248, "y": 0, "w": W, "h": H, "title": "Cadangan · Naik Tingkat"}],
 "annotations": [
  {"id": "utama", "x": 0, "y": -210, "w": 1000,
   "text": "Dua versi papan infografis penelitian A3 (297 × 420 mm). Isi lima bagian wajib: "
           "latar belakang, temuan permasalahan, tujuan penelitian, metode penelitian & "
           "perancangan, kesimpulan.\nSeluruh angka dikutip dari REVISI_24_JUNI.docx — "
           "SEQ 6,1/7 pada 50 responden; kuesioner 60 responden; observasi 1–5 Mei 2025."},
  {"id": "cadangan", "x": 2688, "y": -150, "w": 900,
   "text": "Tiga lembar tematik dari putaran sebelumnya, disimpan sebagai cadangan — "
           "bisa dipakai sebagai papan pendukung di booth, bukan papan utama."}],
 "launch": {"view": "canvas"}}
open(os.path.join(OUT, 'canvas.json'), 'w', encoding='utf-8').write(
    json.dumps(kanvas, indent=2, ensure_ascii=False))
print('canvas.json — ' + str(len(kanvas['artboards'])) + ' artboard')
