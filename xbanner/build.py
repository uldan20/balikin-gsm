# -*- coding: utf-8 -*-
"""Membangun keempat artboard X-banner Balikin. Jalankan ulang setiap kali ada perubahan."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
CREAM, INK, TEAL, TEALD, GOLD, GOLDL, TERRA = '#FBF8F3','#211C16','#1B7A6E','#15655B','#C8952E','#F3D77C','#BC5A3C'
WASH, LINE, MUTED, FILL, MINT = '#E4F0ED','#E0D8CA','#9A8F80','#F1ECE3','#CFE6E0'

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
  'family=Archivo:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700'
  '&family=Caveat:wght@500;600;700&display=swap">')
AR = "Archivo,'Arial Narrow',Helvetica,sans-serif"
PJ = "'Plus Jakarta Sans',ui-sans-serif,system-ui,sans-serif"
CV = "Caveat,'Bradley Hand',cursive"

def qr(px, dark, light):
    N, seed, bits = 25, 0x9E3779B9, []
    for _ in range(N*N):
        seed = (seed * 1103515245 + 12345) & 0x7FFFFFFF
        bits.append((seed >> 17) & 1)
    def fnd(r, c): return (r < 8 and c < 8) or (r < 8 and c >= N-8) or (r >= N-8 and c < 8)
    cells = ''.join('<rect x="%d" y="%d" width="1" height="1"/>' % (c, r)
                    for r in range(N) for c in range(N) if not fnd(r, c) and bits[r*N+c])
    f = ''
    for fr, fc in ((0,0), (0,N-7), (N-7,0)):
        f += ('<rect x="%.1f" y="%.1f" width="6" height="6" fill="none" stroke="%s" stroke-width="1"/>'
              '<rect x="%d" y="%d" width="3" height="3" fill="%s"/>') % (fc+.5, fr+.5, dark, fc+2, fr+2, dark)
    return ('<svg width="%d" height="%d" viewBox="-1 -1 %d %d" style="display:block;background:%s">'
            '<g fill="%s">%s</g>%s</svg>') % (px, px, N+2, N+2, light, dark, cells, f)

SWASH = ('<svg viewBox="0 0 200 22" style="display:block;width:100%%;height:13px;margin-top:-3px" fill="none">'
         '<path d="M3 15C40 5 110 3 160 8c18 2 30 6 36 1" stroke="%s" stroke-width="2.6" '
         'stroke-linecap="round"/></svg>')

def mark(color, size=42, rot=-5, stacked=True, align='left'):
    if stacked:
        body = ''.join('<span style="display:block">%s</span>' % t
                       for t in ('Small', 'Things', 'Make a', 'Big Difference'))
        w = 'max-width:212px;'
    else:
        body = '<span style="display:block;white-space:nowrap">Small Things Make a Big Difference</span>'
        w = ''
    return ('<div style="font-family:%s;font-weight:600;font-size:%dpx;line-height:1.02;color:%s;'
            'text-align:%s;transform:rotate(%ddeg);%s">%s%s</div>'
            ) % (CV, size, color, align, rot, w, body, SWASH % color)

ICONS = {
 'camera':'<path d="M35 32 41 20h18l6 12" stroke="currentColor" stroke-width="6.5"/><path d="M19 32H81L89 45.86V66.14L81 80H19L11 66.14V45.86Z" stroke="currentColor" stroke-width="7"/><path d="M65 56L57.5 68.99L42.5 68.99L35 56L42.5 43.01L57.5 43.01Z" stroke="currentColor" stroke-width="6.5"/>',
 'grid':'<path d="M18 12H39L45 22.39V34.61L39 45H18L12 34.61V22.39Z" stroke="currentColor" stroke-width="6.5"/><path d="M61 12H82L88 22.39V34.61L82 45H61L55 34.61V22.39Z" stroke="currentColor" stroke-width="6.5"/><path d="M18 55H39L45 65.39V77.61L39 88H18L12 77.61V65.39Z" stroke="currentColor" stroke-width="6.5"/><path d="M61 55H82L88 65.39V77.61L82 88H61L55 77.61V65.39Z" fill="currentColor"/>',
 'pin':'<path d="M38 20h24l12 16v18L50 86 26 54V36L38 20Z" stroke="currentColor" stroke-width="7"/><path d="M58 42L54 48.93L46 48.93L42 42L46 35.07L54 35.07Z" fill="currentColor"/>',
 'check':'<path d="M18 52 41 78 84 24" stroke="currentColor" stroke-width="9"/>',
 'wallet':'<path d="M30 32 34 20h24l-3 12" stroke="currentColor" stroke-width="6"/><path d="M21 32H79L87 45.86V64.14L79 78H21L13 64.14V45.86Z" stroke="currentColor" stroke-width="7"/><path d="M55 46h32v18H55z" stroke="currentColor" stroke-width="6"/>',
 'bag':'<path d="M36 38V28l7-9h14l7 9v10" stroke="currentColor" stroke-width="6.5"/><path d="M26 38H74L82 51.86V72.14L74 86H26L18 72.14V51.86Z" stroke="currentColor" stroke-width="7"/><path d="M31 86V62h38v24" stroke="currentColor" stroke-width="6"/>',
 'scan':'<path d="M14 38V22h16M70 22h16v16M86 62v16H70M30 78H14V62" stroke="currentColor" stroke-width="7"/><path d="M22 46h56v8H22z" fill="currentColor"/>',
 'coin':'<path d="M50 14L81.2 32V68L50 86L18.8 68V32Z" stroke="currentColor" stroke-width="7"/><path d="M50 34L62.1 41V55L50 62L37.9 55V41Z" fill="currentColor"/>',
}
def ic(name, px, color):
    return ('<svg width="%d" height="%d" viewBox="0 0 100 100" fill="none" stroke-linejoin="miter" '
            'stroke-miterlimit="8" style="color:%s;display:block">%s</svg>') % (px, px, color, ICONS[name])

HEKSA = ('<path d="M83 128v46" stroke="#0F4A42" stroke-width="15" stroke-linecap="round" fill="none"/>'
 '<path d="M117 128v46" stroke="#0F4A42" stroke-width="15" stroke-linecap="round" fill="none"/>'
 '<path d="M58 104L20 124" stroke="#0F4A42" stroke-width="14" stroke-linecap="round" fill="none"/>'
 '<path d="M142 86L180 56" stroke="#0F4A42" stroke-width="14" stroke-linecap="round" fill="none"/>'
 '<path d="M100 30L153.7 61V123L100 154L46.3 123V61Z" fill="#34A28F"/>'
 '<path d="M128 50L131 57L138 60L131 63L128 70L125 63L118 60L125 57Z" fill="#F3D77C"/>'
 '<ellipse cx="69" cy="105" rx="9" ry="5.5" fill="#F3D77C" opacity=".45"/>'
 '<ellipse cx="131" cy="105" rx="9" ry="5.5" fill="#F3D77C" opacity=".45"/>'
 '<circle cx="84" cy="90" r="7.5" fill="#123E38"/><circle cx="116" cy="90" r="7.5" fill="#123E38"/>'
 '<path d="M88 110q12 12 24 0" stroke="#123E38" stroke-width="5" stroke-linecap="round" fill="none"/>')

def logo(color, accent, size=34, sub=None, subcolor=None):
    s = ('<div style="display:flex;align-items:center;gap:12px">'
         '<svg width="%d" height="%d" viewBox="0 0 100 100" fill="none">'
         '<path d="M50 8L86.4 29V71L50 92L13.6 71V29Z" stroke="%s" stroke-width="8" stroke-linejoin="miter"/>'
         '<path d="M61 44L55.5 53.53H44.5L39 44L44.5 34.47H55.5Z" fill="%s"/></svg>'
         '<span style="font-family:%s;font-weight:700;font-size:%dpx;letter-spacing:.055em;color:%s">BALIKIN</span>'
         ) % (size, int(size*1.15), color, accent, AR, int(size*.94), color)
    if sub:
        s += ('<span style="margin-left:auto;font-family:%s;font-size:13px;font-weight:600;'
              'letter-spacing:.2em;color:%s">%s</span>') % (PJ, subcolor, sub)
    return s + '</div>'

HONEY = ('<svg style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none" aria-hidden="true">'
 '<defs><pattern id="hc" width="52" height="90" patternUnits="userSpaceOnUse">'
 '<g fill="none" stroke="#FBF8F3" stroke-width="1.4" opacity=".085">'
 '<path d="M26 0L52 15V45L26 60L0 45V15Z"/><path d="M0 45L26 60V90L0 105L-26 90V60Z"/>'
 '<path d="M52 45L78 60V90L52 105L26 90V60Z"/></g></pattern></defs>'
 '<rect width="100%" height="100%" fill="url(#hc)"/></svg>')

def doc(root):
    return ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
            '  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n  %s\n'
            '  <style>\n    body { margin: 0; font-family: %s; }\n'
            '    a { color: %s; } a:hover { color: %s; }\n  </style>\n</helmet>\n%s\n</x-dc>\n</body>\n</html>\n'
            ) % (FONTS, PJ, TEAL, TEALD, root)

def credit(color, rule):
    return ('<div style="border-top:1px solid %s;padding-top:18px;display:flex;justify-content:space-between;'
            'gap:16px;font-size:12.5px;line-height:1.4;color:%s"><span>[Nama Lengkap · NIM]</span>'
            '<span style="text-align:right">[Program Studi] · [Universitas]</span></div>') % (rule, color)

def step(icon, no, label, tint, fg):
    return ('<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center">'
            '<div style="width:64px;height:73px;display:grid;place-items:center;background:%s;'
            'clip-path:polygon(50%% 0,100%% 25%%,100%% 75%%,50%% 100%%,0 75%%,0 25%%)">%s</div>'
            '<span style="font-family:%s;font-size:11px;font-weight:700;letter-spacing:.16em;color:%s">%s</span>'
            '<span style="font-size:14.5px;font-weight:600;line-height:1.25;color:%s">%s</span></div>'
            ) % (tint, ic(icon, 34, fg), PJ, MUTED, no, INK, label)

STEPS = [('camera','01','Foto barangnya'), ('grid','02','Pilih kategori'),
         ('pin','03','Tandai lokasi'), ('check','04','Kirim laporan')]

def qrbox(bg, rule, dark, light, title, body, ink, sub):
    return ('<div style="display:flex;align-items:center;gap:22px;background:%s;padding:22px 24px;'
            'border:1.5px solid %s">%s<div style="display:flex;flex-direction:column;gap:6px">'
            '<span style="font-family:%s;font-weight:700;font-size:23px;color:%s">%s</span>'
            '<span style="font-size:15px;line-height:1.4;color:%s">%s</span>'
            '<span style="font-family:%s;font-size:13px;font-weight:700;letter-spacing:.14em;color:%s">BALIKIN.ID</span>'
            '</div></div>') % (bg, rule, qr(118, dark, light), AR, ink, title, sub, body, PJ, dark)

# ============ A · MASKOT ============
a = ['<div style="width:600px;height:1600px;position:relative;overflow:hidden;background:%s;'
     'display:flex;flex-direction:column">' % CREAM,
  '<div style="position:relative;background:%s;padding:46px 46px 0;display:flex;flex-direction:column;'
  'height:1040px;box-sizing:border-box">' % TEALD, HONEY,
  '<div style="position:relative">%s</div>' % logo(CREAM, GOLD, 34, 'KOMUNITAS SUKABUMI', 'rgba(251,248,243,.55)'),
  '<h1 style="position:relative;margin:56px 0 0;font-family:%s;font-weight:700;font-size:68px;line-height:.94;'
  'letter-spacing:-.035em;color:%s">Yang hilang,<br>balik pulang.</h1>' % (AR, CREAM),
  '<p style="position:relative;margin:24px 0 0;max-width:430px;font-size:19px;line-height:1.5;'
  'color:rgba(251,248,243,.82)">Lapor barang hilang atau barang temuan di sekitarmu. Empat langkah, tanpa biaya.</p>',
  '<div style="position:relative;flex-grow:1;margin-top:10px">'
  '<svg style="position:absolute;left:-14px;bottom:10px;width:352px;height:352px" viewBox="0 0 200 200">%s</svg>'
  '<div style="position:absolute;right:0;top:104px;width:200px">%s</div></div>' % (HEKSA, mark(GOLDL, 41)),
  '</div>',
  '<div style="padding:46px 46px 38px;display:flex;flex-direction:column;justify-content:space-between;'
  'gap:30px;flex-grow:1">',
  '<div style="display:flex;gap:12px">%s</div>' % ''.join(step(i, n, l, WASH, TEAL) for i, n, l in STEPS),
  qrbox(FILL, LINE, TEALD, CREAM, 'Pindai, coba sendiri.',
        'Prototipe Balikin — lapor, cocokkan, serah terima.', INK, '#6B6258'),
  credit(MUTED, LINE), '</div></div>']
open(os.path.join(OUT, 'Main.dc.html'), 'w', encoding='utf-8').write(doc(''.join(a)))

# ============ B · TIPOGRAFI ============
def feat(icon, title, body):
    return ('<div style="display:flex;gap:20px;align-items:flex-start">'
            '<div style="flex:none;width:74px;height:85px;display:grid;place-items:center;background:%s;'
            'clip-path:polygon(50%% 0,100%% 25%%,100%% 75%%,50%% 100%%,0 75%%,0 25%%)">%s</div>'
            '<div style="display:flex;flex-direction:column;gap:5px">'
            '<span style="font-family:%s;font-weight:700;font-size:26px;letter-spacing:-.02em;color:%s">%s</span>'
            '<span style="font-size:18px;line-height:1.45;color:#4F4740">%s</span></div></div>'
            ) % (WASH, ic(icon, 39, TEAL), AR, INK, title, body)

b = ['<div style="width:600px;height:1600px;position:relative;overflow:hidden;background:%s;'
     'display:flex;flex-direction:column">' % CREAM,
  '<div style="padding:46px 46px 0">%s</div>' % logo(INK, GOLD, 34, 'SUKABUMI', MUTED),
  '<div style="position:relative;padding:0 46px">',
  '<h1 style="margin:52px 0 0;font-family:%s;font-weight:700;font-size:116px;line-height:.86;'
  'letter-spacing:-.05em;color:%s">Yang<br>hilang,<br>balik<br><span style="color:%s">pulang.</span></h1>'
  % (AR, INK, TEAL),
  '<div style="position:absolute;right:28px;top:10px;width:190px">%s</div>' % mark(TERRA, 38, -7),
  '</div>',
  '<div style="padding:46px 46px 0"><div style="height:3px;background:%s;width:96px"></div>'
  '<p style="margin:26px 0 0;font-size:20px;line-height:1.5;color:#4F4740;max-width:460px">'
  'Lost &amp; found untuk warga Sukabumi. Yang membedakannya bukan petanya — '
  'tapi tiga hal ini.</p></div>' % GOLD,
  '<div style="padding:52px 46px 0;display:flex;flex-direction:column;gap:42px">',
  feat('scan','Ciri rahasia','Pemilik mengunci satu ciri yang tidak difoto. Yang mengaku-ngaku tidak bisa menebaknya.'),
  feat('pin','Titik aman','Serah terima di tempat ramai ber-CCTV, dengan kode empat huruf yang dicocokkan di lokasi.'),
  feat('coin','Tip 100%','Kalau kamu memberi tip ke penolong, semuanya masuk ke dia. Balikin tak memungut potongan.'),
  '</div>',
  '<div style="margin-top:auto;background:%s;padding:56px 46px 36px;display:flex;flex-direction:column;gap:30px">'
  % TEALD,
  '<div style="display:flex;align-items:center;gap:22px">%s'
  '<div style="display:flex;flex-direction:column;gap:7px">'
  '<span style="font-family:%s;font-weight:700;font-size:26px;color:%s;line-height:1.1">Pindai,<br>coba sendiri.</span>'
  '<span style="font-family:%s;font-size:13px;font-weight:700;letter-spacing:.14em;color:%s">BALIKIN.ID</span>'
  '</div></div>' % (qr(124, TEALD, CREAM), AR, CREAM, PJ, GOLDL),
  '<div style="border-top:1px solid rgba(251,248,243,.2);padding-top:18px;display:flex;'
  'justify-content:space-between;gap:16px;font-size:12.5px;line-height:1.4;color:rgba(251,248,243,.6)">'
  '<span>[Nama Lengkap · NIM]</span><span style="text-align:right">[Program Studi] · [Universitas]</span></div>',
  '</div></div>']
open(os.path.join(OUT, 'Tipografi.dc.html'), 'w', encoding='utf-8').write(doc(''.join(b)))

# ============ C · KARTU BARANG ============
def card(accent, status, statusbg, statusfg, icon, title, code, meta, who, tier, tiercol, rot, w=296):
    return ('<div style="width:%dpx;background:#FFFFFF;border:3px solid %s;border-radius:24px;overflow:hidden;'
            'box-shadow:0 20px 44px rgba(33,28,22,.16);transform:rotate(%sdeg)">'
            '<div style="height:186px;background:%s;display:grid;place-items:center;position:relative">%s'
            '<span style="position:absolute;top:15px;left:15px;background:%s;color:%s;font-family:%s;'
            'font-size:11px;font-weight:700;letter-spacing:.14em;padding:6px 11px;border-radius:999px">%s</span>'
            '<span style="position:absolute;top:15px;right:15px;background:rgba(255,255,255,.9);color:#4F4740;'
            'font-size:12px;font-weight:700;padding:6px 11px;border-radius:999px">%s</span></div>'
            '<div style="padding:17px 19px 18px;display:flex;flex-direction:column;gap:11px">'
            '<span style="font-family:%s;font-weight:700;font-size:21px;line-height:1.2;letter-spacing:-.02em;'
            'color:%s">%s</span>'
            '<span style="font-size:12px;font-weight:600;letter-spacing:.1em;color:%s">%s</span>'
            '<div style="display:flex;align-items:center;gap:10px;border-top:1px solid #EFE8DC;padding-top:12px">'
            '<span style="width:26px;height:30px;background:%s;display:block;'
            'clip-path:polygon(50%% 0,100%% 25%%,100%% 75%%,50%% 100%%,0 75%%,0 25%%)"></span>'
            '<span style="font-size:14px;font-weight:700;color:%s">%s</span>'
            '<span style="margin-left:auto;font-size:10px;font-weight:700;letter-spacing:.1em;color:%s">%s</span>'
            '</div></div></div>'
            ) % (w, accent, rot, statusbg, ic(icon, 88, accent), accent, statusfg, PJ, status, meta,
                 AR, INK, title, MUTED, code, tiercol, INK, who, tiercol, tier)

c = ['<div style="width:600px;height:1600px;position:relative;overflow:hidden;background:%s;'
     'display:flex;flex-direction:column">' % CREAM,
  '<div style="position:relative;background:%s;height:720px;box-sizing:border-box;padding:46px 46px 0;'
  'display:flex;flex-direction:column">' % MINT,
  '<div style="position:absolute;inset:0;opacity:.5">%s</div>' % HONEY.replace('#FBF8F3', TEAL),
  '<div style="position:relative">%s</div>' % logo(TEALD, GOLD, 34, 'SUKABUMI', 'rgba(21,101,91,.6)'),
  '<h1 style="position:relative;margin:44px 0 0;font-family:%s;font-weight:700;font-size:62px;line-height:.95;'
  'letter-spacing:-.035em;color:%s">Yang hilang,<br>balik pulang.</h1>' % (AR, TEALD),
  '<p style="position:relative;margin:20px 0 0;max-width:400px;font-size:18px;line-height:1.5;color:#2C5A53">'
  'Tiap barang punya kodenya sendiri. Pemiliknya tahu begitu ada yang menemukan.</p>',
  '<div style="position:relative;right:-6px;margin-top:14px;width:196px;align-self:flex-end">%s</div>'
  % mark(TEALD, 34, -6),
  '</div>',
  '<div style="position:relative;height:470px;margin-top:-150px">',
  '<div style="position:absolute;right:8px;top:0">%s</div>' % card(
     TERRA, 'HILANG', '#F6E7E1', TERRA, 'bag', 'Tas ransel hitam', 'BLK-2E08 · 1,2 KM',
     '4 hari', 'Dimas M.', 'PENJAGA KOTA', TERRA, '3', 252),
  '<div style="position:absolute;left:8px;top:112px">%s</div>' % card(
     TEAL, 'DITEMUKAN', WASH, TEAL, 'wallet', 'Dompet kulit cokelat', 'BLK-2F71 · 180 M',
     '18 menit', 'Donat G.', 'LEGENDA BALIKIN', GOLD, '-2', 310),
  '</div>',
  '<div style="padding:44px 46px 38px;display:flex;flex-direction:column;justify-content:space-between;'
  'gap:30px;flex-grow:1">',
  '<div style="display:flex;gap:12px">%s</div>' % ''.join(step(i, n, l, FILL, TEAL) for i, n, l in STEPS),
  qrbox(WASH, '#BFDCD5', TEALD, CREAM, 'Pindai, coba sendiri.',
        'Prototipe Balikin — lapor, cocokkan, serah terima.', INK, '#3F6B64'),
  credit(MUTED, LINE), '</div></div>']
open(os.path.join(OUT, 'KartuBarang.dc.html'), 'w', encoding='utf-8').write(doc(''.join(c)))

# ============ ELEMEN GRAFIS ============
def swatch(bg, color, label, stacked, size, rot):
    return ('<div style="display:flex;flex-direction:column;gap:12px">'
            '<div style="background:%s;height:172px;display:grid;place-items:center;padding:20px;'
            'box-sizing:border-box"><div style="width:%dpx">%s</div></div>'
            '<span style="font-size:12.5px;line-height:1.4;color:#6B6258">%s</span></div>'
            ) % (bg, 196 if stacked else 300, mark(color, size, rot, stacked), label)

g = ['<div style="width:600px;height:760px;background:%s;padding:40px 44px;box-sizing:border-box;'
     'display:flex;flex-direction:column;gap:22px">' % CREAM,
  '<div style="display:flex;flex-direction:column;gap:7px">'
  '<span style="font-family:%s;font-size:11px;font-weight:700;letter-spacing:.18em;color:%s">ELEMEN GRAFIS</span>'
  '<span style="font-family:%s;font-weight:700;font-size:28px;letter-spacing:-.025em;color:%s">'
  'Small Things Make a Big Difference</span>'
  '<span style="font-size:14.5px;line-height:1.5;color:#4F4740;max-width:460px">'
  'Tulisan tangan pendamping, dipakai sekali di tiap desain — tidak pernah dua kali dalam satu bidang, '
  'dan tidak pernah lebih besar dari tagline utama.</span></div>' % (PJ, MUTED, AR, INK),
  '<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px">',
  swatch(TEALD, GOLDL, 'Bentuk tumpuk · emas muda di atas teal tua', True, 32, -5),
  swatch(CREAM, TERRA, 'Bentuk tumpuk · terakota di atas kertas', True, 32, -7),
  '</div>',
  '<div style="display:flex;flex-direction:column;gap:11px">'
  '<div style="background:%s;height:104px;display:grid;place-items:center;padding:16px;box-sizing:border-box">'
  '<div style="width:300px">%s</div></div>'
  '<span style="font-size:12.5px;line-height:1.4;color:#6B6258">'
  'Bentuk satu baris · untuk pita mendatar dan bagian bawah poster</span></div>' % (FILL, mark(TEALD, 24, -3, False)),
  '<div style="border-top:1px solid %s;padding-top:18px;display:flex;gap:26px;font-size:13px;'
  'line-height:1.5;color:#4F4740">'
  '<span style="flex:1"><b>Huruf.</b> Caveat 600. Kalau nanti dibakukan di GSM, ganti dengan tulisan '
  'tanganmu sendiri yang di-scan — lebih jujur untuk karya TA.</span>'
  '<span style="flex:1"><b>Garis bawah.</b> Satu tarikan, ujung membulat, sedikit naik di akhir. '
  'Selalu di bawah baris terakhir, tidak pernah menyentuh hurufnya.</span>'
  '<span style="flex:1"><b>Kemiringan.</b> −3° sampai −7°. Jangan lurus, jangan lebih miring dari itu.</span>'
  '</div>' % LINE,
  '</div>']
open(os.path.join(OUT, 'Grafik.dc.html'), 'w', encoding='utf-8').write(doc(''.join(g)))

# ============ canvas.json ============
import json
canvas = {
  "artboards": [
    {"file": "Main.dc.html",        "x": 0,    "y": 0, "w": 600, "h": 1600, "title": "A · Maskot",       "print": "fixed"},
    {"file": "Tipografi.dc.html",   "x": 760,  "y": 0, "w": 600, "h": 1600, "title": "B · Tipografi",    "print": "fixed"},
    {"file": "KartuBarang.dc.html", "x": 1520, "y": 0, "w": 600, "h": 1600, "title": "C · Kartu Barang", "print": "fixed"},
    {"file": "Grafik.dc.html",      "x": 0,    "y": 1780, "w": 600, "h": 760, "title": "Elemen grafis",  "print": "fixed"}
  ],
  "annotations": [
    {"id": "skala", "x": 0, "y": -150, "w": 600,
     "text": "X-banner 60 × 160 cm. Artboard 600 × 1600 px — 1 px = 1 mm, jadi ukuran di sini bisa dibaca langsung sebagai milimeter cetak.\nTagline: “Yang hilang, balik pulang.”"},
    {"id": "qr-catatan", "x": 1520, "y": 1680, "w": 600,
     "text": "QR di ketiga banner masih placeholder — ganti dengan QR pendek dinamis yang mengarah ke prototipe sebelum naik cetak."},
    {"id": "foto-catatan", "x": 760, "y": 1680, "w": 600,
     "text": "Versi C memakai ikon Sudut Enam sebagai isi kartu. Kalau ada foto barang yang bagus, tukar — kartunya jadi jauh lebih meyakinkan."}
  ],
  "launch": {"view": "canvas"}
}
open(os.path.join(OUT, 'canvas.json'), 'w', encoding='utf-8').write(json.dumps(canvas, indent=2, ensure_ascii=False))
print('selesai:', ', '.join(sorted(os.listdir(OUT))))
