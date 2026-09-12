# -*- coding: utf-8 -*-
"""Empat artboard A3 (1122 x 1587 px = A3 pada 96 ppi): dua poster penelitian,
dua infografis. Jalankan ulang setiap ada perubahan."""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'xbanner'))
from build import (CREAM, INK, TEAL, TEALD, GOLD, GOLDL, TERRA, WASH, LINE, MUTED, FILL, MINT,
                   ICONS, LEBAH, AR, PJ, CV, FONTS, qr, mark, hexpath)
import isi as D

OUT = os.path.dirname(os.path.abspath(__file__))
W, H = 1122, 1587
M = 60
GOLDW, TERRAW = '#F6EEDC', '#F6E7E1'

def doc(root, latar=CREAM):
    return ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
            '  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n  %s\n'
            '  <style>\n    body { margin: 0; font-family: %s; background: %s; }\n'
            '    a { color: %s; } a:hover { color: %s; }\n  </style>\n</helmet>\n%s\n</x-dc>\n</body>\n</html>\n'
            ) % (FONTS, PJ, latar, TEAL, TEALD, root)

HEX = 'clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%)'

SARANG = ('<svg style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none" aria-hidden="true">'
 '<defs><pattern id="sr" width="104" height="180" patternUnits="userSpaceOnUse">'
 '<g fill="none" stroke="#FBF8F3" stroke-width="2" opacity=".075">'
 '<path d="M52 0L104 30V90L52 120L0 90V30Z"/><path d="M0 90L52 120V180L0 210L-52 180V120Z"/>'
 '<path d="M104 90L156 120V180L104 210L52 180V120Z"/></g></pattern></defs>'
 '<rect width="100%" height="100%" fill="url(#sr)"/></svg>')

# versi yang aman dipakai di dalam format string (tanda % dilolos-kan)
SARANG_F = SARANG.replace('%', '%%')

IKON_LENCANA = ['check', 'grid', 'scan', 'camera', 'wallet', 'pin', 'coin', 'bag', 'bintang']

def ic(n, px, c):
    if n == 'bintang':
        return ('<svg width="%d" height="%d" viewBox="0 0 100 100" fill="none" style="display:block">'
                '<path d="M50 14L59 41L86 50L59 59L50 86L41 59L14 50L41 41Z" fill="%s"/></svg>') % (px, px, c)
    return ('<svg width="%d" height="%d" viewBox="0 0 100 100" fill="none" stroke-linejoin="miter" '
            'stroke-miterlimit="8" style="color:%s;display:block">%s</svg>') % (px, px, c, ICONS[n])

def bee(px, rot=0):
    return ('<svg width="%d" height="%d" viewBox="0 0 200 200" style="display:block;transform:rotate(%sdeg)">%s</svg>'
            ) % (px, px, rot, LEBAH)

def hexbox(px, bg, inner):
    return ('<div style="width:%dpx;height:%dpx;display:grid;place-items:center;background:%s;%s">%s</div>'
            ) % (px, int(px * 1.15), bg, HEX, inner)

def logo(c, acc, size=40, sub=None, subc=None):
    s = ('<div style="display:flex;align-items:center;gap:14px">'
         '<svg width="%d" height="%d" viewBox="0 0 100 100" fill="none">'
         '<path d="M50 8L86.4 29V71L50 92L13.6 71V29Z" stroke="%s" stroke-width="8" stroke-linejoin="miter"/>'
         '<path d="M61 44L55.5 53.53H44.5L39 44L44.5 34.47H55.5Z" fill="%s"/></svg>'
         '<span style="font-family:%s;font-weight:700;font-size:%dpx;letter-spacing:2px;color:%s">BALIKIN</span>'
         ) % (size, int(size * 1.15), c, acc, AR, int(size * 0.9), c)
    if sub:
        s += ('<span style="margin-left:auto;font-size:14px;font-weight:600;letter-spacing:3px;color:%s">%s</span>'
              ) % (subc, sub)
    return s + '</div>'

def tab(label, warna=TEAL, fg=CREAM):
    return ('<div style="display:flex;align-items:center;gap:12px;margin-bottom:16px">'
            '<span style="width:20px;height:23px;background:%s;%s;flex:none"></span>'
            '<span style="font-family:%s;font-size:23px;font-weight:700;letter-spacing:-.4px;color:%s">%s</span>'
            '<span style="flex:1;height:2px;background:%s"></span></div>'
            ) % (warna, HEX, AR, INK if fg == CREAM else fg, label, LINE)

def p(t, size=16, c='#4F4740', lh=1.5, mt=0):
    return '<p style="margin:%dpx 0 0;font-size:%dpx;line-height:%s;color:%s">%s</p>' % (mt, size, lh, c, t)

def daftar(items, c=TEAL, size=16):
    return '<div style="display:flex;flex-direction:column;gap:10px;margin-top:4px">%s</div>' % ''.join(
      '<div style="display:flex;gap:12px;align-items:baseline">'
      '<span style="flex:none;width:9px;height:11px;background:%s;%s"></span>'
      '<span style="font-size:%dpx;line-height:1.45;color:#4F4740">%s</span></div>' % (c, HEX, size, t)
      for t in items)

def kartu(isi_, bg=CREAM, pad=26, br=LINE):
    return '<div style="background:%s;border:2px solid %s;padding:%dpx">%s</div>' % (bg, br, pad, isi_)

def kredit(fg, rule, bg=None):
    gaya = 'background:%s;' % bg if bg else ''
    return ('<div style="%spadding:26px %dpx;display:flex;align-items:center;gap:28px;border-top:2px solid %s">'
            '<div style="flex:1;display:flex;flex-direction:column;gap:5px">'
            '<span style="font-family:%s;font-size:19px;font-weight:700;color:%s">%s · %s</span>'
            '<span style="font-size:14px;line-height:1.45;color:%s;opacity:.85">%s<br>%s</span>'
            '<span style="font-size:13px;line-height:1.45;color:%s;opacity:.7">%s · %s</span></div>'
            '<div style="display:flex;align-items:center;gap:18px">%s'
            '<div style="display:flex;flex-direction:column;gap:3px">'
            '<span style="font-size:13px;font-weight:700;color:%s">Pindai prototipenya</span>'
            '<span style="font-size:13px;font-weight:700;letter-spacing:2px;color:%s;opacity:.8">BALIKIN.ID</span>'
            '</div></div></div>'
            ) % (gaya, M, rule, AR, fg, D.PENULIS, D.NIM, fg, D.PRODI, D.FAKULTAS, fg,
                 D.BIMBING[0], D.BIMBING[1], qr(86, TEALD, CREAM), fg, fg)

def judul_blok(size=44, c=CREAM, acc=GOLDL):
    return ('<h1 style="margin:0;font-family:%s;font-weight:700;font-size:%dpx;line-height:1.08;'
            'letter-spacing:-1.2px;color:%s">%s</h1>'
            '<p style="margin:14px 0 0;font-size:19px;letter-spacing:2px;color:%s">%s</p>'
            ) % (AR, size, c, D.JUDUL, acc, D.SUBJUDUL.upper())

# =============== P1 · KOLOM ===============
kiri = [tab('Latar Belakang'), p(D.LATAR),
        '<div style="height:28px"></div>', tab('Rumusan Masalah'), daftar(D.RUMUSAN),
        '<div style="height:28px"></div>', tab('Tujuan Penelitian'), daftar(D.TUJUAN, GOLD),
        '<div style="height:28px"></div>', tab('Landasan Teori'),
        '<div style="display:flex;flex-direction:column;gap:12px">%s</div>' % ''.join(
          '<div><b style="font-size:16px;color:%s">%s</b>'
          '<div style="font-size:14px;line-height:1.4;color:#6B6258;margin-top:2px">%s</div></div>' % (INK, a, b)
          for a, b in D.TEORI)]

tahap_ringkas = ''.join(
  '<div style="display:flex;gap:11px;align-items:baseline">'
  '<span style="flex:none;width:26px;height:30px;background:%s;%s;display:grid;place-items:center;'
  'font-family:%s;font-size:13px;font-weight:700;color:%s">%d</span>'
  '<span style="font-size:14px;line-height:1.4;color:#6B6258">'
  '<b style="color:%s">%s</b> \u2014 %s</span></div>'
  % (TEAL, HEX, AR, CREAM, i + 1, INK, n, out) for i, (n, _, out) in enumerate(D.TAHAP))

kanan = [tab('Metode Penelitian'), p(D.METODE),
         p('<b style="color:%s">Lokasi observasi</b> · %s' % (INK, D.LOKASI), 14, '#6B6258', 1.45, 12),
         '<div style="height:22px"></div>',
         '<div style="display:flex;flex-direction:column;gap:9px">%s</div>' % tahap_ringkas,
         '<div style="height:28px"></div>', tab('Temuan'),
         '<div style="display:flex;flex-direction:column;gap:12px">%s</div>' % ''.join(
           '<div><b style="font-size:16px;color:%s">%s</b>'
           '<div style="font-size:14px;line-height:1.4;color:#6B6258;margin-top:2px">%s</div></div>' % (INK, a, b)
           for a, b in D.TEMUAN),
         '<div style="height:28px"></div>', tab('Kesimpulan', GOLD),
         kartu('<span style="font-family:%s;font-size:12px;font-weight:700;letter-spacing:2px;color:%s">'
               'MENUNGGU DATA</span>%s' % (PJ, GOLD, p(D.KESIMPULAN_PENDING, 15, '#4F4740', 1.5, 8)),
               GOLDW, 22, GOLD)]

p1 = ('<div style="width:%dpx;height:%dpx;background:%s;display:flex;flex-direction:column;overflow:hidden">'
      '<div style="position:relative;background:%s;padding:%dpx %dpx 40px">' + SARANG_F +
      '<div style="position:relative">%s<div style="height:34px"></div>%s</div></div>'
      '<div style="flex:1;padding:40px %dpx 0;display:flex;gap:%dpx;overflow:hidden">'
      '<div style="width:471px">%s</div><div style="width:471px">%s</div></div>%s</div>'
      ) % (W, H, CREAM, TEALD, 46, M,
           logo(CREAM, GOLD, 40, 'POSTER PENELITIAN', 'rgba(251,248,243,.55)'),
           judul_blok(), M, M, ''.join(kiri), ''.join(kanan), kredit(INK, LINE, FILL))
open(os.path.join(OUT, 'Main.dc.html'), 'w', encoding='utf-8').write(doc(p1))
print('Main.dc.html  — P1 · Kolom')

# =============== P2 · LIMA TAHAP ===============
band = ''.join(
  '<div style="width:180px;display:flex;flex-direction:column;align-items:center;gap:12px;text-align:center">'
  '<div style="width:56px;height:64px;background:%s;%s;display:grid;place-items:center;'
  'font-family:%s;font-size:22px;font-weight:700;color:%s">%d</div>'
  '<span style="font-family:%s;font-size:20px;font-weight:700;color:%s">%s</span>'
  '<span style="font-size:12.5px;line-height:1.4;color:%s;border-top:1px solid rgba(251,248,243,.25);'
  'padding-top:10px;margin-top:2px">%s</span></div>'
  % (GOLD if i == 4 else CREAM, HEX, AR, INK, i + 1, AR, CREAM, n, GOLDL, out)
  for i, (n, desc, out) in enumerate(D.TAHAP))

p2 = ('<div style="width:%dpx;height:%dpx;background:%s;display:flex;flex-direction:column;overflow:hidden">'
      # kepala
      '<div style="position:relative;background:%s;padding:36px %dpx 30px">' + SARANG_F +
      '<div style="position:relative">%s<div style="height:22px"></div>%s</div></div>'
      # latar + rumusan
      '<div style="padding:28px %dpx 26px;display:flex;gap:%dpx">'
      '<div style="width:612px">%s%s</div><div style="width:330px">%s%s</div></div>'
      # pita lima tahap
      '<div style="background:%s;padding:30px %dpx 32px">'
      '<div style="display:flex;align-items:center;gap:12px;margin-bottom:22px">'
      '<span style="font-family:%s;font-size:12px;font-weight:700;letter-spacing:3px;color:%s">METODE PERANCANGAN</span>'
      '<span style="flex:1;height:1px;background:rgba(251,248,243,.25)"></span>'
      '<span style="font-size:13px;color:rgba(251,248,243,.7)">Design Thinking · lima tahap iteratif</span></div>'
      '<div style="display:flex;gap:25px;position:relative">'
      '<div style="position:absolute;left:28px;right:28px;top:32px;height:2px;background:rgba(251,248,243,.28)"></div>'
      '<div style="display:flex;gap:25px;position:relative">%s</div></div></div>'
      # temuan + tujuan
      '<div style="padding:28px %dpx 0;display:flex;gap:%dpx;flex:1">'
      '<div style="width:612px">%s%s</div>'
      '<div style="width:330px">%s%s<div style="height:24px"></div>%s</div></div>'
      # kesimpulan
      '<div style="padding:20px %dpx 24px"><div style="background:%s;border:2px solid %s;padding:18px 24px;'
      'display:flex;gap:22px;align-items:flex-start">'
      '<span style="flex:none;font-family:%s;font-size:12px;font-weight:700;letter-spacing:2px;color:%s;'
      'padding-top:3px">KESIMPULAN<br>MENUNGGU DATA</span>'
      '<span style="font-size:15px;line-height:1.5;color:#4F4740">%s</span></div></div>%s</div>'
      ) % (W, H, CREAM,
           TEALD, M, logo(CREAM, GOLD, 36, 'POSTER PENELITIAN', 'rgba(251,248,243,.55)'), judul_blok(34),
           M, M, tab('Latar Belakang'), p(D.LATAR), tab('Rumusan Masalah'), daftar(D.RUMUSAN, TEAL, 15),
           TEALD, M, PJ, GOLDL, band,
           M, M, tab('Temuan'),
           '<div style="display:flex;flex-direction:column;gap:12px">%s</div>' % ''.join(
             '<div><b style="font-size:16px;color:%s">%s</b>'
             '<div style="font-size:14px;line-height:1.4;color:#6B6258;margin-top:2px">%s</div></div>' % (INK, a, b)
             for a, b in D.TEMUAN),
           tab('Tujuan'), daftar(D.TUJUAN, GOLD, 15),
           '<div style="font-size:13px;line-height:1.45;color:#6B6258">%s</div>' % ' · '.join(
             '<b style="color:%s">%s</b> (%s)' % (INK, a, b) for a, b in D.TEORI),
           M, GOLDW, GOLD, PJ, GOLD, D.KESIMPULAN_PENDING, kredit(INK, LINE, FILL))
open(os.path.join(OUT, 'LimaTahap.dc.html'), 'w', encoding='utf-8').write(doc(p2))
print('LimaTahap.dc.html — P2 · Lima Tahap')

# =============== I1 · PERJALANAN ===============
WARNA = {'terra': TERRA, 'teal': TEAL, 'gold': GOLD}
def henti(i, label, teks, ikon, w, kiri_):
    c = WARNA[w]
    kartu_ = ('<div style="width:432px;background:%s;border:2px solid %s;padding:20px 22px;'
              'text-align:%s">'
              '<span style="font-family:%s;font-size:12px;font-weight:700;letter-spacing:2.5px;color:%s">%s</span>'
              '<div style="font-size:16px;line-height:1.45;color:#4F4740;margin-top:8px">%s</div></div>'
              ) % (CREAM, LINE, 'right' if kiri_ else 'left', PJ, c, label, teks)
    simpul = ('<div style="flex:none;width:74px;display:grid;place-items:center">'
              '<div style="width:62px;height:71px;background:%s;%s;display:grid;place-items:center">%s</div></div>'
              ) % (c, HEX, ic(ikon, 30, CREAM))
    kosong = '<div style="width:432px"></div>'
    return ('<div style="display:flex;align-items:center;gap:28px">%s</div>'
            ) % ((kartu_ + simpul + kosong) if kiri_ else (kosong + simpul + kartu_))

i1 = ('<div style="width:%dpx;height:%dpx;background:%s;display:flex;flex-direction:column;overflow:hidden">'
      '<div style="padding:44px %dpx 0">%s'
      '<div style="display:flex;align-items:flex-end;gap:26px;margin-top:30px">'
      '<div style="flex:1">'
      '<h1 style="margin:0;font-family:%s;font-weight:700;font-size:58px;line-height:.98;letter-spacing:-2px;'
      'color:%s">Perjalanan<br>sebuah <span style="color:%s">dompet</span>.</h1>'
      '<p style="margin:16px 0 0;font-size:18px;line-height:1.5;color:#4F4740;max-width:560px">'
      'Tujuh perhentian, dari tertinggal di angkot sampai kembali ke tangan pemiliknya — '
      'persis seperti yang dijalankan aplikasi Balikin.</p></div>%s</div></div>'
      '<div style="position:relative;padding:34px %dpx 0;flex:1">'
      '<div style="position:absolute;left:%dpx;top:0;bottom:110px;width:0;border-left:3px dashed %s;opacity:.4"></div>'
      '<div style="position:relative;display:flex;flex-direction:column;gap:18px">%s</div></div>%s</div>'
      ) % (W, H, CREAM, M, logo(INK, GOLD, 38, 'INFOGRAFIS', MUTED), AR, INK, TEAL, bee(150, -14),
           M, M + 432 + 28 + 37, TEAL,
           ''.join(henti(i, l, t, ik, w, i % 2 == 0) for i, (l, t, ik, w) in enumerate(D.PERJALANAN)),
           kredit(INK, LINE, FILL))
open(os.path.join(OUT, 'Perjalanan.dc.html'), 'w', encoding='utf-8').write(doc(i1))
print('Perjalanan.dc.html — I1 · Perjalanan')

# =============== I2 · SARANG KEPERCAYAAN ===============
TINGGI = [110, 160, 210, 260, 310]
tangga = ''.join(
  '<div style="width:184px;display:flex;flex-direction:column;align-items:center;gap:9px;text-align:center">'
  '<div style="width:62px;height:71px;background:%s;%s;display:grid;place-items:center">'
  '<div style="width:24px;height:28px;background:%s;%s;opacity:.55"></div></div>'
  '<span style="font-family:%s;font-size:17px;font-weight:700;line-height:1.15;color:%s">%s</span>'
  '<span style="font-family:%s;font-size:13px;font-weight:700;letter-spacing:1.5px;color:%s">%s PN</span>'
  '<span style="font-size:12.5px;line-height:1.35;color:rgba(251,248,243,.7)">%s</span>'
  '<div style="width:64px;height:%dpx;background:%s;margin-top:6px"></div></div>'
  % (b, HEX, CREAM, HEX, AR, CREAM, n, PJ, GOLDL, amb, ket, TINGGI[i], g)
  for i, (n, amb, ket, b, g) in enumerate(D.TINGKAT))

lencana = ''.join(
  '<div style="width:160px;display:flex;flex-direction:column;align-items:center;gap:7px;text-align:center">'
  '<div style="width:46px;height:53px;background:%s;%s;display:grid;place-items:center">%s</div>'
  '<span style="font-size:11.5px;line-height:1.25;color:#4F4740">%s</span></div>'
  % (WASH, HEX, ic(IKON_LENCANA[i], 22, TEAL), nm)
  for i, nm in enumerate(D.LENCANA))

def poin(judul, baris, c, bg):
    return ('<div style="flex:1"><span style="font-family:%s;font-size:12px;font-weight:700;'
            'letter-spacing:2px;color:%s">%s</span>'
            '<div style="display:flex;flex-direction:column;gap:7px;margin-top:11px">%s</div></div>'
            ) % (PJ, c, judul, ''.join(
              '<div style="display:flex;align-items:baseline;gap:10px;background:%s;padding:8px 12px">'
              '<span style="font-family:%s;font-size:15px;font-weight:700;color:%s;min-width:46px">%s</span>'
              '<span style="font-size:13.5px;line-height:1.35;color:#4F4740">%s</span></div>' % (bg, AR, c, v, t)
              for t, v in baris))

i2 = ('<div style="width:%dpx;height:%dpx;background:%s;display:flex;flex-direction:column;overflow:hidden">'
      # kepala teal
      '<div style="background:%s;padding:44px %dpx 36px">%s'
      '<div style="display:flex;align-items:flex-end;gap:24px;margin-top:28px">'
      '<div style="flex:1"><h1 style="margin:0;font-family:%s;font-weight:700;font-size:56px;line-height:.98;'
      'letter-spacing:-2px;color:%s">Sarang<br><span style="color:%s">kepercayaan</span>.</h1>'
      '<p style="margin:15px 0 0;font-size:17px;line-height:1.5;color:rgba(251,248,243,.82);max-width:520px">'
      'Balikin tidak membayar orang untuk menolong. Yang tumbuh adalah rekam jejak — '
      'poin, tingkat, dan lencana yang terlihat di profil publik.</p></div>%s</div>'
      # tangga tingkat
      '<div style="display:flex;gap:20px;align-items:flex-end;margin-top:34px">%s</div>'
      '<div style="height:2px;background:rgba(251,248,243,.3);margin-top:-1px"></div></div>'
      # lencana + poin
      '<div style="flex:1;padding:32px %dpx 0;display:flex;gap:44px">'
      '<div style="width:520px">%s'
      '<div style="display:flex;flex-wrap:wrap;gap:14px 18px;margin-top:4px">%s</div></div>'
      '<div style="flex:1">%s<div style="display:flex;gap:20px;margin-top:4px">%s%s</div></div></div>'
      # pernyataan
      '<div style="padding:28px %dpx 30px"><div style="background:%s;border:2px solid %s;padding:24px 28px;'
      'display:flex;gap:26px;align-items:center">%s'
      '<div><span style="font-family:%s;font-size:26px;font-weight:700;letter-spacing:-.6px;color:%s">'
      'Pengakuan, bukan imbalan uang.</span>'
      '<p style="margin:8px 0 0;font-size:15px;line-height:1.5;color:#4F4740">'
      'Sistem reputasi dirancang mengacu pada <b>Self-Determination Theory</b> (Ryan &amp; Deci, 2000) — '
      'kebutuhan <b>kompetensi</b> (merasa diakui sebagai pengguna yang amanah) dan <b>keterhubungan</b> '
      '(merasa menjadi bagian dari komunitas) — sebagai dasar pengambilan keputusan desain, '
      'bukan variabel yang diukur.</p></div></div></div>%s</div>'
      ) % (W, H, CREAM,
           TEALD, M, logo(CREAM, GOLD, 38, 'INFOGRAFIS', 'rgba(251,248,243,.55)'), AR, CREAM, GOLDL, bee(140),
           tangga, M,
           tab('Sembilan Lencana Pencapaian'), lencana,
           tab('Poin Naik dan Turun'),
           poin('POIN NAIK', D.POIN_NAIK, TEAL, WASH), poin('POIN TURUN', D.POIN_TURUN, TERRA, TERRAW),
           M, GOLDW, GOLD, hexbox(76, GOLD, ic('coin', 36, CREAM)), AR, INK, kredit(INK, LINE, FILL))
open(os.path.join(OUT, 'Reputasi.dc.html'), 'w', encoding='utf-8').write(doc(i2))
print('Reputasi.dc.html — I2 · Sarang Kepercayaan')

# =============== canvas ===============
canvas = {
  "pages": [{"id": "page-1", "name": "Poster penelitian"}, {"id": "page-2", "name": "Infografis"}],
  "artboards": [
    {"file": "Main.dc.html",       "x": 0,    "y": 0, "w": W, "h": H, "title": "P1 · Kolom",      "page": "page-1"},
    {"file": "LimaTahap.dc.html",  "x": 1280, "y": 0, "w": W, "h": H, "title": "P2 · Lima Tahap", "page": "page-1"},
    {"file": "Perjalanan.dc.html", "x": 0,    "y": 0, "w": W, "h": H, "title": "I1 · Perjalanan Sebuah Dompet", "page": "page-2"},
    {"file": "Reputasi.dc.html",   "x": 1280, "y": 0, "w": W, "h": H, "title": "I2 · Sarang Kepercayaan",       "page": "page-2"}
  ],
  "annotations": [
    {"id": "ukuran-p", "x": 0, "y": -190, "w": 760, "page": "page-1",
     "text": "A3 potret 297 × 420 mm. Artboard 1122 × 1587 px (A3 pada 96 ppi).\nDua susunan berbeda dari isi yang sama: P1 membagi per bagian, P2 menjadikan lima tahap Design Thinking sebagai sumbu poster.\nBagian Kesimpulan sengaja ditandai MENUNGGU DATA — naskah sendiri menulis hasil usability diisi setelah data terkumpul."},
    {"id": "ukuran-i", "x": 0, "y": -190, "w": 760, "page": "page-2",
     "text": "A3 potret 297 × 420 mm. Infografis menjelaskan produknya, bukan penelitiannya.\nI1 menceritakan perjalanan satu barang; I2 membedah sistem reputasi yang jadi judul skripsi."}
  ],
  "launch": {"view": "canvas", "page": "page-1"}
}
open(os.path.join(OUT, 'canvas.json'), 'w', encoding='utf-8').write(json.dumps(canvas, indent=2, ensure_ascii=False))
print('canvas.json — 2 halaman')
