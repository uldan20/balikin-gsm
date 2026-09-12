# -*- coding: utf-8 -*-
"""Beranda Balikin sebagai hub — tiga kartu besar.

Kartu 1  Barang di sekitarmu   (judul tengah + tumpukan folder, pola dari acuan)
Kartu 2  Mau lapor apa hari ini (pintu masuk ke pilih jenis laporan)
Kartu 3A Reputasimu             (tingkat, poin, lencana)
Kartu 3B Jelajahi peta          (pintu masuk ke halaman Jelajahi)

Tiap kartu juga ditulis sebagai artboard mandiri supaya gampang ditempel ke
berkas beranda yang sudah ada.
"""
import os, json
from kit_app import *

KX, KW = 22, 340                      # kotak kosong di berkas beranda
JARAK = 16                            # antar kartu dan ke panel navigasi
K1Y, K1H = 128, 232
K2Y, K2H = 376, 140
K3Y, K3H = 532, 208                   # 532 + 208 = 740, tombol navigasi mulai 756

# =============================================================== kartu 1
def folder_svg():
    """Tumpukan folder — satu potongan SVG utuh supaya rapi waktu diekspor."""
    def grad(id_, a, b):
        return ('<linearGradient id="' + id_ + '" x1="0%" y1="0%" x2="30%" y2="100%">'
                '<stop offset="0%" stop-color="' + a + '"/>'
                '<stop offset="100%" stop-color="' + b + '"/></linearGradient>')
    def folder(id_, x, y, w, h, rot, gelap, label='', ukuran=10, warna_label='rgba(255,255,255,.62)'):
        cx, cy = x + w // 2, y + h // 2
        t = ' transform="rotate(' + str(rot) + ' ' + str(cx) + ' ' + str(cy) + ')"'
        isi = ('<rect x="' + str(x + 6) + '" y="' + str(y) + '" width="' + str(w - 34)
               + '" height="26" rx="9" fill="' + gelap + '"/>'
               '<rect x="' + str(x) + '" y="' + str(y + 12) + '" width="' + str(w) + '" height="'
               + str(h) + '" rx="15" fill="url(#' + id_ + ')"/>')
        if label:
            isi += ('<text x="' + str(x + w - 14) + '" y="' + str(y + h - 26) + '" text-anchor="end" '
                    'font-family="' + AR + '" font-size="' + str(ukuran) + '" font-weight="700" '
                    'letter-spacing="0" fill="' + warna_label + '">' + label + '</text>')
        return '<g' + t + ' filter="url(#bay)">' + isi + '</g>'

    catatan = ('<g transform="rotate(-8 228 42)" filter="url(#bay)">'
               '<rect x="172" y="4" width="118" height="82" rx="12" fill="#FFFFFF"/>'
               '<text x="184" y="24" font-family="' + AR + '" font-size="9" font-weight="700" '
               'letter-spacing="1" fill="' + TINTA + '">DI SEKITARMU</text>'
               '<rect x="184" y="32" width="88" height="1" fill="#E4E0D6"/>')
    baris = [('Dompet kulit cokelat', TERRA), ('Kunci motor', EMAS), ('Kartu pelajar', TEAL)]
    for i, (t, c) in enumerate(baris):
        yy = 48 + i * 15
        catatan += ('<rect x="184" y="' + str(yy - 5) + '" width="5" height="5" rx="2" fill="' + c + '"/>'
                    '<text x="195" y="' + str(yy) + '" font-family="' + PJ + '" font-size="8" '
                    'fill="#5C7A72">' + t + '</text>')
    catatan += '</g>'

    return ('<svg width="340" height="170" viewBox="0 0 340 170" fill="none" '
            'style="display:block;position:absolute;left:0;bottom:-4px">'
            '<defs>'
            '<filter id="bay" x="-40%" y="-40%" width="180%" height="180%">'
            '<feDropShadow dx="0" dy="5" stdDeviation="7" flood-color="#123B34" flood-opacity="0.2"/></filter>'
            + grad('f1', '#D9713F', TERRA) + grad('f2', '#E9BC5A', EMAS)
            + grad('f3', '#A8DFCE', '#7CC3AE') + grad('f4', '#F2ECE0', '#DDD5C6')
            + grad('f5', '#2E9A7C', TEAL_G) + '</defs>'
            + folder('f1', 4, 74, 108, 80, -17, '#B04A22')
            + folder('f4', 228, 74, 108, 80, 17, '#C9C0AE')
            + folder('f2', 44, 58, 116, 86, -10, '#C99A2C')
            + folder('f3', 180, 58, 116, 86, 10, '#5FB29A')
            + folder('f5', 98, 68, 144, 102, -2, '#0B463A', '42', 28)
            + catatan
            + '</svg>')

def kartu1(x=KX, y=K1Y, w=KW, h=K1H):
    return kartu(x, y, w, h,
                 judul_kartu('Barang di sekitarmu', '42 barang menunggu pemiliknya', 22, ukuran=19)
                 + folder_svg())

# =============================================================== kartu 2
# Satu kartu = satu pintu ke halaman "Mau lapor apa hari ini?".
# Bukan dua tombol pilihan — pilihannya ada di halaman tujuan.

def folder_mini():
    """Dua folder menyembul di tepi kanan: isyarat dua folder tujuan laporan."""
    def grad(id_, a_, b_):
        return ('<linearGradient id="' + id_ + '" x1="0%" y1="0%" x2="30%" y2="100%">'
                '<stop offset="0%" stop-color="' + a_ + '"/>'
                '<stop offset="100%" stop-color="' + b_ + '"/></linearGradient>')
    def fol(id_, x, y, w, h, rot, gelap):
        cx, cy = x + w // 2, y + h // 2
        return ('<g transform="rotate(' + str(rot) + ' ' + str(cx) + ' ' + str(cy) + ')" filter="url(#bm)">'
                '<rect x="' + str(x + 5) + '" y="' + str(y) + '" width="' + str(w - 28)
                + '" height="20" rx="7" fill="' + gelap + '"/>'
                '<rect x="' + str(x) + '" y="' + str(y + 9) + '" width="' + str(w) + '" height="'
                + str(h) + '" rx="13" fill="url(#' + id_ + ')"/></g>')
    return ('<svg width="150" height="140" viewBox="0 0 150 140" fill="none" '
            'style="display:block;position:absolute;right:0;top:0">'
            '<defs><filter id="bm" x="-40%" y="-40%" width="180%" height="180%">'
            '<feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#123B34" flood-opacity="0.2"/></filter>'
            + grad('m1', '#D9713F', TERRA) + grad('m2', '#2E9A7C', TEAL_G) + '</defs>'
            + fol('m1', 14, 22, 96, 66, -12, '#B04A22')
            + fol('m2', 44, 50, 104, 72, 8, '#0B463A') + '</svg>')

def kartu2a(x=KX, y=K2Y, w=KW, h=K2H):
    """Versi A — terang, senada kartu 1, folder menyembul di kanan."""
    isi = (folder_mini()
           + dv(P(x=18, y=20, z=4, lain=font(PJ, 9, 700, TEAL, 1.3)), 'LAPORAN BARU')
           + dv(P(x=18, y=34, w=200, z=4, lain=font(AR, 16, 700, TINTA, -.4, 1.15)),
                'Mau lapor apa hari ini?')
           + dv(P(x=18, y=60, w=172, z=4, lain=font(PJ, 10, 500, REDUP, None, 1.35)),
                'Barang hilang atau barang temuan, mulai dari sini.')
           + dv(P(x=18, y=100, z=4, lain='display:flex;align-items:center;gap:8px;'),
                dv('background:' + TEAL + ';border-radius:15px;padding:7px 13px;display:flex;'
                   'align-items:center;gap:6px;box-shadow:0 6px 14px rgba(27,122,99,.28);',
                   teks(font(PJ, 11, 700, PUTIH, -.1), 'Buat laporan') + ik('panah', 12, PUTIH))
                + dv('background:' + MINT_M + ';border-radius:12px;padding:5px 9px;',
                     teks(font(PJ, 9, 700, TEAL, .6), '&plusmn;3 MENIT'))))
    return kartu(x, y, w, h, isi)

def kartu2b(x=KX, y=K2Y, w=KW, h=K2H):
    """Versi B — teal pekat, satu aksi besar, pola sarang samar."""
    sarang_ = ('<svg width="' + str(w) + '" height="' + str(h) + '" viewBox="0 0 ' + str(w) + ' '
               + str(h) + '" fill="none" style="display:block;position:absolute;left:0;top:0">'
               '<g fill="none" stroke="#FFFFFF" stroke-opacity="0.09" stroke-width="2">'
               '<path d="M262 -18L306 8V60L262 86L218 60V8Z"/>'
               '<path d="M330 30L374 56V108L330 134L286 108V56Z"/>'
               '<path d="M262 82L306 108V160L262 186L218 160V108Z"/></g></svg>')
    heks = dv(P(x=18, y=26, w=44, h=50, z=4,
                lain='background:rgba(251,248,243,.16);' + HEKS + 'display:grid;place-items:center;'),
              ik('tambah', 20, PUTIH))
    isi = (sarang_ + heks
           + dv(P(x=74, y=28, z=4, lain=font(PJ, 9, 700, MINT, 1.3)), 'LAPORAN BARU')
           + dv(P(x=74, y=44, w=200, z=4, lain=font(AR, 19, 700, KRIM, -.4, 1.15)),
                'Mau lapor apa hari ini?')
           + dv(P(x=18, y=92, w=210, z=4, lain=font(PJ, 10, 500, 'rgba(207,230,224,.8)', None, 1.35)),
                'Barang hilang atau barang temuan — dua-duanya mulai dari satu halaman.')
           + dv(P(r=18, b=18, z=4,
                  lain='background:' + PUTIH + ';border-radius:16px;padding:8px 14px;display:flex;'
                       'align-items:center;gap:7px;box-shadow:0 8px 18px rgba(13,47,41,.3);'),
                teks(font(PJ, 11, 700, TINTA, -.1), 'Pilih folder') + ik('panah', 12, TEAL)))
    return kartu(x, y, w, h, isi,
                 bg='linear-gradient(140deg,' + TEAL + ' 0%,' + TEAL_G + ' 78%,#0B4638 100%)',
                 bayang='0 12px 28px rgba(15,90,72,.26)')

kartu2 = kartu2a

# =============================================================== kartu 3A
def lencana_heks(px, isi_, a=MINT, b=TEAL, cincin=True):
    dalam = dv('width:' + str(px) + 'px;height:' + str(int(px * 0.88)) + 'px;'
               'background:linear-gradient(150deg,' + a + ' 0%,' + b + ' 100%);' + HEKS
               + 'display:grid;place-items:center;', isi_)
    return dv('filter:drop-shadow(0 0 14px rgba(143,212,196,.5));', dalam)

def kartu3a(x=KX, y=K3Y, w=KW, h=K3H):
    berlian = ('<svg width="24" height="24" viewBox="0 0 24 24" fill="none">'
               '<path d="M12 3L21 12L12 21L3 12Z" fill="#0E3A31" fill-opacity=".55"/>'
               '<path d="M12 7.5L16.5 12L12 16.5L7.5 12Z" fill="#EAF7F2"/></svg>')
    mini = []
    for nama, ikon_ in (('Balik Pertama', 'check'), ('10 Barang', 'grid'),
                        ('Balas Cepat', 'obrolan'), ('Mata Elang', 'cari')):
        mini.append(dv('width:26px;height:23px;background:rgba(143,212,196,.16);' + HEKS
                       + 'display:grid;place-items:center;flex:none;', ik(ikon_, 12, MINT)))
    isi = (dv(P(x=20, y=52, z=4), lencana_heks(84, berlian))
           + dv(P(x=120, y=30, z=4, lain=font(PJ, 9, 700, MINT, 1.4)), 'TINGKAT 3 DARI 5')
           + dv(P(x=120, y=46, z=4, lain=font(AR, 24, 700, KRIM, -.6, 1.1)), 'PENOLONG')
           + dv(P(x=120, y=78, z=4, lain='display:flex;align-items:baseline;gap:5px;'),
                teks(font(AR, 27, 700, PUTIH, -1, 1), '720')
                + teks(font(PJ, 10, 700, 'rgba(251,248,243,.6)', 1.2), 'POIN'))
           + dv(P(x=120, y=120, w=200, h=8, z=4,
                  lain='background:rgba(251,248,243,.16);border-radius:5px;overflow:hidden;'),
                dv(P(x=0, y=0, w=160, h=8, lain='background:linear-gradient(90deg,' + MINT + ' 0%,#B7E6D8 100%);'
                     'border-radius:5px;')))
           + dv(P(x=120, y=138, z=4, lain='display:flex;align-items:baseline;gap:4px;'),
                teks(font(PJ, 10, 500, 'rgba(207,230,224,.82)'), '180 poin lagi ke')
                + teks(font(PJ, 10, 700, MINT), 'Penjaga Kota'))
           + dv(P(x=20, y=160, w=300, h=1, z=4, lain='background:rgba(251,248,243,.1);'))
           + dv(P(x=20, y=172, z=4, lain='display:flex;align-items:center;gap:7px;'), ''.join(mini))
           + dv(P(r=20, y=176, z=4, lain='display:flex;align-items:center;gap:4px;'),
                teks(font(PJ, 10, 600, MINT), '5 dari 9 lencana') + ik('panah', 11, MINT)))
    return kartu(x, y, w, h, isi,
                 bg='linear-gradient(152deg,' + GELAP_A + ' 0%,' + GELAP_B + ' 100%)',
                 bayang='0 12px 30px rgba(13,47,41,.28)')

# =============================================================== kartu 3B
def peta_svg(w=350, h=186):
    """Peta ringkas — bukan peta asli, digambar mengikuti warna aplikasi."""
    jalan = lambda d, lebar, warna: ('<path d="' + d + '" stroke="' + warna + '" stroke-width="'
                                     + str(lebar) + '" fill="none" stroke-linecap="round"/>')
    return ('<svg width="' + str(w) + '" height="' + str(h) + '" viewBox="0 0 ' + str(w) + ' ' + str(h)
            + '" fill="none" style="display:block;position:absolute;left:0;top:0">'
            '<defs><linearGradient id="pt" x1="0%" y1="0%" x2="0%" y2="100%">'
            '<stop offset="0%" stop-color="#CFE3D2"/><stop offset="100%" stop-color="#A9CDB4"/></linearGradient>'
            '<linearGradient id="tirai" x1="0%" y1="0%" x2="0%" y2="100%">'
            '<stop offset="0%" stop-color="#0D2F29" stop-opacity="0"/>'
            '<stop offset="60%" stop-color="#0D2F29" stop-opacity="0.72"/>'
            '<stop offset="100%" stop-color="#0D2F29" stop-opacity="0.92"/></linearGradient></defs>'
            '<rect x="0" y="0" width="' + str(w) + '" height="' + str(h) + '" fill="url(#pt)"/>'
            '<path d="M0 108L54 96L120 112L196 92L262 104L350 86V186H0Z" fill="#98C4A6" fill-opacity=".55"/>'
            '<path d="M228 0L286 34L350 22V0Z" fill="#9EC8D8" fill-opacity=".8"/>'
            + jalan('M-8 62L86 48L152 70L240 44L358 60', 7, '#F3F0E7')
            + jalan('M-8 124L70 108L150 128L236 100L358 120', 5, '#F3F0E7')
            + jalan('M40 -6L58 60L38 128L62 192', 5, '#F3F0E7')
            + jalan('M204 -6L192 68L214 132L198 192', 4, '#F3F0E7')
            + jalan('M290 -6L300 58L282 126L302 192', 4, '#F3F0E7')
            + '<rect x="0" y="0" width="' + str(w) + '" height="' + str(h) + '" fill="url(#tirai)"/>'
            '</svg>')

def kartu3b(x=KX, y=K3Y, w=KW, h=K3H):
    def pin(px_, py, besar=False):
        s = 30 if besar else 20
        return dv(P(x=px_, y=py, z=4, lain='filter:drop-shadow(0 4px 10px rgba(13,47,41,.4));'),
                  dv('width:' + str(s) + 'px;height:' + str(int(s * 0.88)) + 'px;background:'
                     + (TEAL_T if besar else PUTIH) + ';' + HEKS + 'display:grid;place-items:center;',
                     ik('pin', int(s * 0.5), PUTIH if besar else TEAL)))
    avatar = lambda i, c: dv('width:22px;height:22px;border-radius:12px;background:' + c
                             + ';border:2px solid ' + PUTIH + ';margin-left:' + ('0' if i == 0 else '-8')
                             + 'px;flex:none;')
    isi = (peta_svg(w, h)
           + pin(66, 62) + pin(272, 34) + pin(168, 46, True) + pin(242, 74)
           + dv(P(x=20, y=22, z=5, lain='background:rgba(251,248,243,.9);border-radius:11px;'
                  'padding:4px 10px;'),
                teks(font(PJ, 9, 700, TINTA, 1.2), 'CISAAT, SUKABUMI'))
           + dv(P(x=20, y=108, w=210, z=5, lain=font(AR, 19, 700, PUTIH, -.4, 1.18)),
                'Jelajahi peta sekitarmu')
           + dv(P(x=20, y=150, z=5, lain=font(PJ, 10, 500, 'rgba(251,248,243,.76)')),
                '12 titik aktif &middot; diperbarui 2 menit lalu')
           + dv(P(x=20, y=162, z=5, lain='display:flex;align-items:center;'),
                avatar(0, '#E8C7A8') + avatar(1, '#B9CDE6') + avatar(2, '#D8B0A2') + avatar(3, MINT)
                + teks(font(PJ, 10, 600, 'rgba(251,248,243,.8)') + 'margin-left:8px;', '+18 warga')))
    # tombol buka peta
    isi += dv(P(r=20, b=22, z=6, lain='background:' + PUTIH + ';border-radius:19px;padding:9px 14px;'
                'display:flex;align-items:center;gap:7px;box-shadow:0 8px 18px rgba(13,47,41,.3);'),
              teks(font(PJ, 12, 700, TINTA, -.1), 'Buka peta') + ik('panah', 13, TEAL))
    return kartu(x, y, w, h, isi, bg=GELAP_B, bayang='0 12px 30px rgba(13,47,41,.26)')

# =============================================================== kartu 3C
# Pintu ke halaman Jelajahi secara utuh — cuplikan isinya, bukan peta.
UBIN = [('wallet', '#D9713F', TERRA, -10), ('kunci', '#E9BC5A', EMAS, -5),
        ('ponsel', '#2E9A7C', TEAL_G, 0), ('dokumen', '#A8DFCE', '#6FBCA4', 5),
        ('bag', '#F2ECE0', '#D9D0BF', 10), ('tumbler', '#8FD4C4', TEAL, 14)]

def ubin_svg(w=340, atas=116, px=96, pitch=60):
    grad = ''
    ubin = ''
    for i, (_, a_, b_, rot) in enumerate(UBIN):
        gid = 'u' + str(i)
        grad += ('<linearGradient id="' + gid + '" x1="0%" y1="0%" x2="20%" y2="100%">'
                 '<stop offset="0%" stop-color="' + a_ + '"/>'
                 '<stop offset="100%" stop-color="' + b_ + '"/></linearGradient>')
        x = -6 + i * pitch
        y = atas + abs(i - 2) * 4
        ubin += ('<g transform="rotate(' + str(rot) + ' ' + str(x + px // 2) + ' ' + str(y + px // 2)
                 + ')" filter="url(#bu)">'
                 '<rect x="' + str(x) + '" y="' + str(y) + '" width="' + str(px) + '" height="' + str(px)
                 + '" rx="24" fill="url(#' + gid + ')"/></g>')
    return ('<svg width="' + str(w) + '" height="208" viewBox="0 0 ' + str(w) + ' 208" fill="none" '
            'style="display:block;position:absolute;left:0;top:0">'
            '<defs><filter id="bu" x="-40%" y="-40%" width="180%" height="180%">'
            '<feDropShadow dx="0" dy="5" stdDeviation="7" flood-color="#123B34" flood-opacity="0.22"/>'
            '</filter>' + grad + '</defs>' + ubin + '</svg>')

def kartu3c(x=KX, y=K3Y, w=KW, h=K3H):
    ikon_ubin = ''
    for i, (nama, _, _, rot) in enumerate(UBIN):
        cx = -6 + i * 60 + 48
        cy = 116 + abs(i - 2) * 4 + 40
        putih = i in (0, 1, 2, 5)
        ikon_ubin += dv(P(x=cx - 13, y=cy - 13, z=6,
                          lain='transform:rotate(' + str(rot) + 'deg);'),
                        ik(nama, 26, 'rgba(255,255,255,.9)' if putih else 'rgba(18,51,44,.45)'))
    saring = []
    for lab, aktif in (('Semua', True), ('Dompet', False), ('Kunci', False), ('Kartu', False)):
        saring.append(dv('background:' + (TINTA if aktif else PUTIH) + ';border-radius:14px;'
                         'padding:6px 12px;flex:none;box-shadow:0 4px 10px rgba(18,51,44,.08);',
                         teks(font(PJ, 10, 700, KRIM if aktif else REDUP, .2), lab)))
    isi = (judul_kartu('Jelajahi sekitarmu', '12 titik aktif &middot; 18 warga ikut mencari', 20, ukuran=19)
           + dv(P(x=16, y=72, w=w - 32, z=5, lain='display:flex;gap:7px;overflow:hidden;'),
                ''.join(saring))
           + ubin_svg(w) + ikon_ubin)
    return kartu(x, y, w, h, isi, bg=MINT_M)

# =============================================================== layar penuh
def beranda(kartu2_, kartu3_):
    return layar(bar_status() + kepala() + kartu1() + kartu2_ + kartu3_ + bar_bawah('beranda'))

tulis('Main.dc.html', beranda(kartu2a(), kartu3a()))
tulis('BerandaB.dc.html', beranda(kartu2b(), kartu3c()))
tulis('BerandaC.dc.html', beranda(kartu2a(), kartu3b()))

# kartu mandiri — latar transparan supaya gampang ditempel
def mandiri(nama, f, h):
    tulis(nama, papan(390, h + 40, f(20, 20, KW, h)))

mandiri('Kartu1.dc.html', kartu1, K1H)
mandiri('Kartu2A.dc.html', kartu2a, K2H)
mandiri('Kartu2B.dc.html', kartu2b, K2H)
mandiri('Kartu3A.dc.html', kartu3a, K3H)
mandiri('Kartu3B.dc.html', kartu3b, K3H)
mandiri('Kartu3C.dc.html', kartu3c, K3H)

kanvas = {"artboards": [
  {"file": "Main.dc.html", "x": 0, "y": 0, "w": W, "h": H, "title": "Beranda A · kartu reputasi"},
  {"file": "BerandaB.dc.html", "x": 470, "y": 0, "w": W, "h": H, "title": "Beranda B · lapor teal + jelajahi"},
  {"file": "BerandaC.dc.html", "x": 940, "y": 0, "w": W, "h": H, "title": "Beranda C · versi peta"},
  {"file": "Kartu1.dc.html", "x": 1410, "y": 0, "w": 390, "h": K1H + 40, "title": "Kartu 1 · Barang di sekitarmu"},
  {"file": "Kartu2A.dc.html", "x": 1410, "y": 340, "w": 390, "h": K2H + 40, "title": "Kartu 2A · Lapor terang"},
  {"file": "Kartu2B.dc.html", "x": 1410, "y": 560, "w": 390, "h": K2H + 40, "title": "Kartu 2B · Lapor teal"},
  {"file": "Kartu3A.dc.html", "x": 1410, "y": 780, "w": 390, "h": K3H + 40, "title": "Kartu 3A · Reputasi"},
  {"file": "Kartu3C.dc.html", "x": 1410, "y": 1060, "w": 390, "h": K3H + 40, "title": "Kartu 3C · Pintu Jelajahi"},
  {"file": "Kartu3B.dc.html", "x": 1410, "y": 1340, "w": 390, "h": K3H + 40, "title": "Kartu 3B · Peta (disimpan)"}],
 "annotations": [{"id": "catatan", "x": 0, "y": -170, "w": 900,
   "text": "Beranda sebagai hub — layar 390 × 844. Dua versi kartu ketiga: A reputasi, B pintu ke Jelajahi.\n"
           "Empat kartu juga berdiri sendiri di kolom kanan supaya gampang ditempel ke berkas beranda yang sudah ada."}],
 "launch": {"view": "canvas"}}
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'canvas.json'), 'w',
     encoding='utf-8').write(json.dumps(kanvas, indent=2, ensure_ascii=False))
print('canvas.json — ' + str(len(kanvas['artboards'])) + ' artboard')
