# -*- coding: utf-8 -*-
"""Lima poster showcase A3. Isi layar masih placeholder."""
import os, json
from kit import *

OUT = os.path.dirname(os.path.abspath(__file__))
def tulis(nama, isi_, latar=CREAM):
    open(os.path.join(OUT, nama), 'w', encoding='utf-8').write(doc(isi_, latar)); print(nama)
def abs_(x=None, y=None, r=None, b=None, z=1, extra=''):
    s = 'position:absolute;z-index:%d;' % z
    for k, v in (('left', x), ('top', y), ('right', r), ('bottom', b)):
        if v is not None: s += '%s:%dpx;' % (k, v)
    return s + extra

# ================= S1 · KARTU MELAYANG =================
s1 = ['<div style="width:%dpx;height:%dpx;position:relative;overflow:hidden;'
      'background:linear-gradient(160deg,%s 0%%,%s 46%%,%s 100%%)">' % (W, H, TEALB, TEAL, TEALX),
  sarang(CREAM, '.07', 3),
  '<div style="%s">%s</div>' % (abs_(x=70, y=62, z=8), logo(CREAM, GOLDL, 38)),
  # ponsel terpotong di atas
  '<div style="%s">%s</div>' % (abs_(x=341, y=-56, z=2), ponsel(440, -4)),
  # kartu melayang kiri
  '<div style="%s">%s</div>' % (abs_(x=42, y=612, z=5), pil('Dompet kulit cokelat', 'Donat G. menemukan', 'wallet', -4)),
  '<div style="%s">%s</div>' % (abs_(x=96, y=744, z=5), pin(104, 'wallet', TEAL, -6)),
  '<div style="%s">%s</div>' % (abs_(x=30, y=352, z=5), pil('Kunci motor', 'Loki L. menemukan', 'pin', 3, True)),
  # kartu melayang kanan
  '<div style="%s">%s</div>' % (abs_(r=36, y=430, z=5), pil('Tas ransel hitam', 'Dimas M. mencari', 'bag', 4)),
  '<div style="%s">%s</div>' % (abs_(r=104, y=566, z=5), pin(112, 'bag', TERRA, 5)),
  '<div style="%s">%s</div>' % (abs_(r=52, y=760, z=5), pil('Kartu pelajar', 'Sari W. menemukan', 'grid', -3, True)),
  '<div style="%s">%s</div>' % (abs_(r=64, y=250, z=6), bee(132, -12)),
  # blok bawah
  '<div style="%s">'
  '<div style="font-family:%s;font-weight:700;font-size:82px;line-height:.96;letter-spacing:-3px;color:%s;'
  'text-align:center">Yang hilang,<br><span style="color:%s">balik pulang.</span></div>'
  '<p style="margin:24px auto 0;max-width:640px;text-align:center;font-size:21px;line-height:1.5;'
  'color:rgba(251,248,243,.82)">Lapor barang hilang atau barang temuan di sekitarmu. '
  'Warga yang menolong dapat poin dan lencana — bukan uang.</p>'
  '<div style="margin-top:40px">%s</div></div>'
  % (abs_(x=70, r=70, b=64, z=7), AR, CREAM, GOLDL, kaki(CREAM, '.7')),
  '</div>']
tulis('Main.dc.html', ''.join(s1))

# ================= S2 · EDITORIAL =================
def meta(a, b, c=CREAM, op='.55'):
    return ('<div><div style="font-size:14px;color:rgba(251,248,243,%s)">%s</div>'
            '<div style="font-size:17px;font-weight:600;color:%s;margin-top:3px">%s</div></div>') % (op, a, c, b)
s2 = ['<div style="width:%dpx;height:%dpx;position:relative;overflow:hidden;'
      'background:linear-gradient(175deg,%s 0%%,%s 34%%,%s 72%%,%s 100%%)">' % (W, H, TEALX, TEAL, GOLD, '#F0DCA8'),
  # wordmark hantu
  '<div style="%sfont-family:%s;font-weight:700;font-size:300px;letter-spacing:-14px;color:%s;opacity:.13;'
  'white-space:nowrap">BALIKIN</div>' % (abs_(x=-40, y=880, z=1), AR, CREAM),
  # meta sudut
  '<div style="%sdisplay:flex;gap:90px">%s%s%s</div>'
  % (abs_(x=64, y=56, z=5, extra='color:%s;' % CREAM),
     '<div><div style="font-size:14px;color:rgba(251,248,243,.55)">UI/UX</div>'
     '<div style="font-size:16px;font-weight:600;color:%s;margin-top:3px">Aplikasi Mobile</div></div>' % CREAM,
     '<div><div style="font-size:14px;color:rgba(251,248,243,.55)">Kategori</div>'
     '<div style="font-size:16px;font-weight:600;color:%s;margin-top:3px">Lost &amp; Found</div></div>' % CREAM,
     '<div><div style="font-size:14px;color:rgba(251,248,243,.55)">Metode</div>'
     '<div style="font-size:16px;font-weight:600;color:%s;margin-top:3px">Design Thinking</div></div>' % CREAM),
  '<div style="%s">%s</div>' % (abs_(r=64, y=56, z=5), logo(CREAM, GOLDL, 30, 1)),
  # judul + paragraf
  '<div style="%s"><h1 style="margin:0;font-family:%s;font-weight:700;font-size:92px;line-height:.94;'
  'letter-spacing:-4px;color:%s">Barang yang<br>hilang punya<br>'
  '<span style="color:rgba(251,248,243,.45)">alamat pulang</span></h1></div>'
  % (abs_(x=64, y=168, z=5), AR, CREAM),
  '<div style="%sfont-size:23px;line-height:1.45;color:rgba(251,248,243,.9)">'
  'Balikin mempertemukan pemilik dan penemu lewat satu sistem — dengan verifikasi '
  'ciri rahasia, titik serah terima yang aman, dan reputasi yang tumbuh dari menolong.</div>'
  % abs_(r=64, y=186, z=5, extra='width:300px;'),
  # ponsel melayang
  '<div style="%s">%s</div>' % (abs_(x=361, y=486, z=4), ponsel(400, 0, layar_kosong('gelap'))),
  # keterangan kiri
  '<div style="%s">%s%s</div>'
  % (abs_(x=64, y=560, z=5, extra='display:flex;flex-direction:column;gap:26px;'),
     meta('Studi Kasus', 'Sukabumi'), meta('Luaran', 'Prototipe Figma')),
  # daftar proses kanan bawah
  '<div style="%sdisplay:flex;flex-direction:column;gap:9px">%s</div>'
  % (abs_(r=64, y=1108, z=5), ''.join(
      '<span style="font-size:19px;color:%s">%s</span>' % (INK, t)
      for t in ('Riset', 'Wireframe', 'Desain Antarmuka', 'Prototipe', 'Uji Usability'))),
  '<div style="%s">%s</div>' % (abs_(x=64, b=64, z=6), kaki(INK, '.72')),
  '</div>']
tulis('Editorial.dc.html', ''.join(s2))

# ================= S3 · SAKU =================
def jahitan(top, warna=GOLDL, op='.9'):
    return ('<div style="position:absolute;left:0;right:0;top:%dpx;height:0;border-top:4px dashed %s;'
            'opacity:%s"></div>') % (top, warna, op)
def keling(x, y):
    return ('<div style="position:absolute;left:%dpx;top:%dpx;width:34px;height:39px;background:%s;%s;'
            'box-shadow:0 6px 14px rgba(0,0,0,.25)"></div>') % (x, y, GOLD, HEX)

saku = ('<div style="position:absolute;left:-90px;right:-90px;top:0;bottom:-200px;background:%s;'
        'box-shadow:0 -18px 44px rgba(0,0,0,.28)">%s%s%s%s</div>'
        ) % (TEAL, jahitan(30), jahitan(56), keling(150, 104), keling(1038, 104))

s3 = ['<div style="width:%dpx;height:%dpx;position:relative;overflow:hidden;background:%s">' % (W, H, TEALD),
  sarang(CREAM, '.10', 2),
  '<div style="%s">%s</div>' % (abs_(x=70, y=64, z=9), logo(CREAM, GOLDL, 40)),
  # ponsel di belakang saku
  '<div style="%s">%s</div>' % (abs_(x=331, y=176, z=2), ponsel(460, 3)),
  # saku miring
  '<div style="%s">%s</div>' % (abs_(x=0, y=760, z=5, extra='width:%dpx;height:900px;transform:rotate(-3.2deg);' % W), saku),
  '<div style="%s">%s</div>' % (abs_(r=74, y=596, z=7), bee(142, 10)),
  # blok bawah
  '<div style="%s">'
  '<h1 style="margin:0;font-family:%s;font-weight:700;font-size:86px;line-height:.95;letter-spacing:-3px;'
  'color:%s;text-align:center">Yang hilang,<br><span style="color:%s">balik pulang.</span></h1>'
  '<p style="margin:22px auto 0;max-width:620px;text-align:center;font-size:21px;line-height:1.5;'
  'color:rgba(251,248,243,.86)">Satu aplikasi untuk melapor, mencocokkan, dan menyerahkan '
  'kembali barang \u2014 di titik yang aman.</p>'
  '<div style="display:flex;justify-content:center;gap:16px;margin-top:34px">%s</div>'
  '<div style="margin-top:44px">%s</div></div>'
  % (abs_(x=70, r=70, b=60, z=8), AR, CREAM, GOLDL,
     ''.join('<span style="background:rgba(251,248,243,.14);border:2px solid rgba(251,248,243,.34);'
             'border-radius:30px;padding:14px 26px;font-size:17px;font-weight:600;color:%s">%s</span>' % (CREAM, t)
             for t in ('Prototipe Figma', 'Studi kasus Sukabumi', 'balikin.id')),
     kaki(CREAM, '.7')),
  '</div>']
tulis('Saku.dc.html', ''.join(s3))

# ================= S4 · STIKER =================
def sticker_ikon(n, bg, px=112, rot=0):
    return stiker(ic(n, int(px*0.44), CREAM if bg != GOLDL else INK), px, bg, rot)
s4 = ['<div style="width:%dpx;height:%dpx;position:relative;overflow:hidden;background:%s">' % (W, H, TEAL),
  sarang(CREAM, '.07', 2),
  '<div style="%s">%s</div>' % (abs_(x=70, y=62, z=9), logo(CREAM, GOLDL, 38)),
  # dua ponsel
  '<div style="%s">%s</div>' % (abs_(x=126, y=222, z=3), ponsel(352, -9)),
  '<div style="%s">%s</div>' % (abs_(x=476, y=142, z=4), ponsel(376, 7, layar_kosong('gelap'))),
  # stiker
  '<div style="%s">%s</div>' % (abs_(x=40, y=196, z=6), sticker_ikon('wallet', GOLD, 118, -14)),
  '<div style="%s">%s</div>' % (abs_(x=58, y=560, z=6), sticker_ikon('pin', TERRA, 104, 11)),
  '<div style="%s">%s</div>' % (abs_(r=36, y=316, z=6), sticker_ikon('scan', GOLDL, 110, 13)),
  '<div style="%s">%s</div>' % (abs_(r=64, y=640, z=6), sticker_ikon('check', CREAM, 98, -9)),
  '<div style="%s">%s</div>' % (abs_(x=452, y=906, z=7), bee(150, -8)),
  '<div style="%s">%s</div>' % (abs_(x=96, y=940, z=8),
     '<div style="background:%s;border-radius:26px;padding:14px 22px;transform:rotate(-6deg);'
     'box-shadow:0 0 0 5px %s,0 18px 30px rgba(12,40,36,.3);font-family:%s;font-size:22px;font-weight:700;'
     'color:%s">Ketemu!</div>' % (INK, CREAM, AR, CREAM)),
  '<div style="%s">%s</div>' % (abs_(r=86, y=978, z=8),
     '<div style="background:%s;border-radius:26px;padding:14px 22px;transform:rotate(8deg);'
     'box-shadow:0 0 0 5px %s,0 18px 30px rgba(12,40,36,.3);font-family:%s;font-size:22px;font-weight:700;'
     'color:%s">+150 poin</div>' % (GOLD, CREAM, AR, INK)),
  # bagian overview
  '<div style="%s">'
  '<div style="text-align:center;font-family:%s;font-weight:700;font-size:62px;color:%s;'
  'transform:rotate(-3deg)">Sekilas</div>'
  '<p style="margin:18px auto 0;max-width:760px;text-align:center;font-family:%s;font-weight:700;'
  'font-size:26px;line-height:1.35;color:%s">Kehilangan barang tidak harus berakhir di grup '
  'WhatsApp yang tidak ada yang baca.</p>'
  '<div style="display:flex;gap:46px;margin-top:30px">'
  '<p style="flex:1;margin:0;font-size:16px;line-height:1.5;color:rgba(251,248,243,.78)">'
  'Balikin mempertemukan pemilik dan penemu lewat satu sistem: laporan yang tersimpan, '
  'pencocokan otomatis, verifikasi ciri rahasia, dan serah terima di titik aman. '
  'Yang menolong mendapat poin dan lencana — bukan uang.</p>'
  '<p style="flex:1;margin:0;font-size:16px;line-height:1.5;color:rgba(251,248,243,.78)">'
  'Balikin connects owners and finders in one system: reports that persist, automatic matching, '
  'secret-detail verification, and handover at safe points. Helpers earn points and badges — '
  'not cash.</p></div>'
  '<div style="margin-top:34px">%s</div></div>'
  % (abs_(x=70, r=70, b=58, z=8), CV, GOLDL, AR, CREAM, kaki(CREAM, '.6')),
  '</div>']
tulis('Stiker.dc.html', ''.join(s4))

# ================= S5 · IRISAN =================
IRIS = 'clip-path:polygon(78px 0,100% 0,calc(100% - 78px) 100%,0 100%);'
def iris(x, w, isi_, bg):
    return ('<div style="%s">%s</div>'
            ) % (abs_(x=x, y=-20, z=2, extra='width:%dpx;height:700px;background:%s;%s' % (w, bg, IRIS)), isi_)
s5 = ['<div style="width:%dpx;height:%dpx;position:relative;overflow:hidden;'
      'background:linear-gradient(200deg,%s 0%%,%s 52%%,%s 100%%)">' % (W, H, TEALX, TEALD, TEAL),
  iris(-70, 336, sarang(CREAM, '.2', 1), '#0E463E'),
  iris(256, 336, slot_foto(336, 700, 'SLOT FOTO'), 'rgba(251,248,243,.12)'),
  iris(582, 336, '<div style="width:100%%;height:100%%;background:linear-gradient(160deg,%s,%s)"></div>' % (TEALB, TEALD), TEALB),
  iris(890, 336, slot_foto(336, 700, 'SLOT FOTO'), 'rgba(251,248,243,.12)'),
  '<div style="%sbackground:linear-gradient(180deg,rgba(14,70,62,0) 52%%,%s 92%%)"></div>'
  % (abs_(x=0, y=0, r=0, z=3, extra='height:720px;'), TEALX),
  '<div style="%s">%s</div>' % (abs_(x=70, y=62, z=9), logo(CREAM, GOLDL, 36)),
  # tombol pil melayang
  ''.join('<div style="%s">%s</div>' % (abs_(x=x, y=y, z=7, extra='transform:rotate(%sdeg);' % r),
     '<div style="background:rgba(18,86,77,.86);border:2px solid rgba(251,248,243,.28);border-radius:40px;'
     'padding:18px 34px;display:flex;align-items:center;gap:15px;box-shadow:0 20px 40px rgba(0,0,0,.36)">'
     '%s<span style="font-family:%s;font-size:25px;font-weight:700;color:%s">%s</span></div>'
     % (ic(ik, 30, GOLDL), AR, CREAM, t))
    for x, y, r, ik, t in ((86, 300, -3, 'camera', 'Lapor'), (478, 214, 2, 'scan', 'Cocokkan'),
                           (150, 452, 3, 'grid', 'Verifikasi'), (592, 402, -2, 'check', 'Serah terima'))),
  # ponsel besar kanan bawah
  '<div style="%s">%s</div>' % (abs_(r=-62, y=690, z=6), ponsel(462, -8, layar_kosong('gelap'))),
  # teks kiri
  '<div style="%s">'
  '<h1 style="margin:0;font-family:%s;font-weight:700;font-size:84px;line-height:.94;letter-spacing:-3px;'
  'color:%s">Balikin,<br>tanpa<br><span style="color:%s">drama.</span></h1>'
  '<p style="margin:26px 0 0;max-width:400px;font-size:21px;line-height:1.5;color:rgba(251,248,243,.85)">'
  'Lapor, cocokkan, verifikasi, serah terima. Empat langkah, satu aplikasi, '
  'tanpa perlu saling menaruh curiga.</p></div>'
  % (abs_(x=70, y=800, z=8), AR, CREAM, GOLDL),
  '<div style="%sfont-size:15px;line-height:1.45;color:%s;opacity:.62">'
  'Uldan Pamungkas \u00b7 20210060127<br>Desain Komunikasi Visual \u00b7 Universitas Nusa Putra Sukabumi<br>'
  '<span style="font-family:%s;font-weight:700;letter-spacing:3px">BALIKIN.ID</span></div>'
  % (abs_(x=70, b=58, z=9, extra='max-width:430px;'), CREAM, PJ),
  '</div>']
tulis('Irisan.dc.html', ''.join(s5))

# ================= S6 · CAP LOGO =================
def heks_raksasa(px, isi_warna):
    h = int(px * 1.155)
    return ('<svg width="%d" height="%d" viewBox="0 0 100 100" style="display:block">'
            '<path d="M50 2L92.6 26.5V75.5L50 100L7.4 75.5V26.5Z" fill="%s"/></svg>') % (px, h, isi_warna)

def stiker_bulat(teks, bg, fg, rot, px=132):
    return ('<div style="width:%dpx;height:%dpx;border-radius:50%%;background:%s;display:grid;'
            'place-items:center;transform:rotate(%sdeg);box-shadow:0 0 0 7px %s,0 20px 34px rgba(12,40,36,.3)">'
            '<span style="font-family:%s;font-weight:700;font-size:34px;color:%s">%s</span></div>'
            ) % (px, px, bg, rot, CREAM, CV, fg, teks)

s6 = ['<div style="width:%dpx;height:%dpx;position:relative;overflow:hidden;background:%s">' % (W, H, TEAL),
  # cap logo raksasa
  '<div style="%s">%s</div>' % (abs_(x=-59, y=52, z=1), heks_raksasa(1240, '#3CAE99')),
  '<div style="%s">%s</div>' % (abs_(x=70, y=62, z=9), logo(CREAM, GOLDL, 36)),
  # dua ponsel miring
  '<div style="%s">%s</div>' % (abs_(x=108, y=296, z=4), ponsel(344, -11)),
  '<div style="%s">%s</div>' % (abs_(r=92, y=372, z=5), ponsel(372, 9, layar_kosong('gelap'))),
  # stiker die-cut
  '<div style="%s">%s</div>' % (abs_(x=18, y=600, z=7), stiker(ic('wallet', 50, CREAM), 122, GOLD, -15)),
  '<div style="%s">%s</div>' % (abs_(r=14, y=286, z=7), stiker(ic('pin', 44, CREAM), 108, TERRA, 14)),
  '<div style="%s">%s</div>' % (abs_(x=36, y=1006, z=7), stiker_bulat('balik!', GOLDL, INK, -9)),
  '<div style="%s">%s</div>' % (abs_(x=468, y=1056, z=7), bee(152, 11)),
  '<div style="%s">%s</div>' % (abs_(x=476, y=172, z=7), stiker(ic('check', 38, INK), 92, CREAM, 10)),
  # wordmark + tagline
  '<div style="%s">'
  '<div style="font-family:%s;font-weight:700;font-size:126px;letter-spacing:-2px;color:%s;'
  'text-align:center;line-height:1">BALIKIN</div>'
  '<p style="margin:18px 0 0;text-align:center;font-family:%s;font-size:34px;font-weight:600;'
  'color:%s">Yang hilang, balik pulang.</p>'
  '<div style="margin-top:46px">%s</div></div>'
  % (abs_(x=70, r=70, b=62, z=8), AR, CREAM, AR, GOLDL, kaki(CREAM, '.66')),
  '</div>']
tulis('CapLogo.dc.html', ''.join(s6))

# ================= canvas =================
canvas = {"artboards": [
  {"file": "Main.dc.html",      "x": 0,    "y": 0, "w": W, "h": H, "title": "S1 · Kartu Melayang"},
  {"file": "Editorial.dc.html", "x": 1280, "y": 0, "w": W, "h": H, "title": "S2 · Editorial"},
  {"file": "Saku.dc.html",      "x": 2560, "y": 0, "w": W, "h": H, "title": "S3 · Saku"},
  {"file": "Stiker.dc.html",    "x": 3840, "y": 0, "w": W, "h": H, "title": "S4 · Stiker"},
  {"file": "Irisan.dc.html",    "x": 5120, "y": 0, "w": W, "h": H, "title": "S5 · Irisan"},
  {"file": "CapLogo.dc.html",   "x": 6400, "y": 0, "w": W, "h": H, "title": "S6 \u00b7 Cap Logo"}],
 "annotations": [{"id": "catatan", "x": 0, "y": -210, "w": 900,
   "text": "Enam arah poster showcase. A3 potret 297 × 420 mm — artboard 1122 × 1587 px (A3 pada 96 ppi).\n"
           "Isi layar masih rangka placeholder; tinggal diganti tangkapan layar asli.\n"
           "Foto tidak bisa dibuat di sini — di S5 disediakan dua slot foto bertanda, "
           "dan latar bertekstur pada S3 memakai pola sarang, bukan foto."}],
 "launch": {"view": "canvas"}}
open(os.path.join(OUT, 'canvas.json'), 'w', encoding='utf-8').write(json.dumps(canvas, indent=2, ensure_ascii=False))
print('canvas.json — %d artboard' % len(canvas['artboards']))
