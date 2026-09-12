# -*- coding: utf-8 -*-
"""Menerjemahkan hasil ekstraksi jadi SVG. Seluruh koordinat dibulatkan ke
bilangan bulat sesuai aturan di CLAUDE.md."""
import json, math, re, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'xbanner'))
from rapi import I, N, bakar_fragmen

E = lambda s: s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def urai_warna(c):
    """'rgba(r, g, b, a)' -> ('#rrggbb', alpha)"""
    if not c: return None, 1.0
    m = re.match(r'rgba?\(([^)]+)\)', c)
    if not m: return c, 1.0
    b = [x.strip() for x in m.group(1).replace('/', ' ').split(',')]
    if len(b) == 1: b = m.group(1).split()
    r, g, bl = (int(round(float(x))) for x in b[:3])
    a = float(b[3]) if len(b) > 3 else 1.0
    return '#%02X%02X%02X' % (r, g, bl), a

def urai_transform(t, kotak):
    """matrix(a,b,c,d,e,f) -> atribut transform SVG, pusat putar di tengah kotak."""
    m = re.match(r'matrix\(([^)]+)\)', t or '')
    if not m: return ''
    a, b, c, d, e, f = [float(x) for x in m.group(1).split(',')]
    sudut = round(math.degrees(math.atan2(b, a)), 3)
    cx = I(kotak['x'] + kotak['w'] / 2); cy = I(kotak['y'] + kotak['h'] / 2)
    bagian = []
    if abs(e) > .01 or abs(f) > .01: bagian.append('translate(%s %s)' % (N(e), N(f)))
    if abs(sudut) > .01: bagian.append('rotate(%g %s %s)' % (sudut, cx, cy))
    return ' transform="%s"' % ' '.join(bagian) if bagian else ''

def _pecah(pas):
    """Pisah 'X Y' jadi dua bagian, spasi di dalam kurung diabaikan."""
    dalam, bag, kini = 0, [], ''
    for ch in pas.strip():
        if ch == '(': dalam += 1
        elif ch == ')': dalam -= 1
        if ch.isspace() and dalam == 0:
            if kini: bag.append(kini); kini = ''
        else: kini += ch
    if kini: bag.append(kini)
    return bag

def titik_clip(clip, k):
    m = re.match(r'polygon\((.+)\)\s*$', clip or '')
    if not m: return None
    p = []
    for pas in m.group(1).split(','):
        bag = _pecah(pas)
        if len(bag) != 2: return None
        xs, ys = bag
        def v(s, ukuran):
            if s.endswith('%'): return float(s[:-1]) / 100 * ukuran
            if s.startswith('calc'):
                mm = re.match(r'calc\(\s*([\d.]+)(%|px)\s*([-+])\s*([\d.]+)(%|px)\s*\)', s)
                if mm:
                    a = float(mm.group(1)) / 100 * ukuran if mm.group(2) == '%' else float(mm.group(1))
                    b_ = float(mm.group(4)) / 100 * ukuran if mm.group(5) == '%' else float(mm.group(4))
                    return a + b_ if mm.group(3) == '+' else a - b_
            return float(s.rstrip('px'))
        p.append((k['x'] + v(xs, k['w']), k['y'] + v(ys, k['h'])))
    return 'M' + 'L'.join('%s %s' % (N(a), N(b)) for a, b in p) + 'Z'

def bungkus(rantai, s, kotak_self):
    """Bangun grup bersarang dari rantai leluhur: transform di luar, clip di dalam,
    supaya putaran dan pemotongan menurun persis seperti di CSS."""
    buka, tutup, jalur_self = '', '', None
    entri = [dict(e) for e in rantai]
    if entri:
        e = entri[-1]
        sendiri = (abs(e['kotak']['x'] - kotak_self['x']) < 0.6 and
                   abs(e['kotak']['w'] - kotak_self['w']) < 0.6 and
                   abs(e['kotak']['h'] - kotak_self['h']) < 0.6)
        if sendiri and e.get('clip'):
            jalur_self = titik_clip(e['clip'], e['kotak'])
            if jalur_self: e['clip'] = None      # digambar sebagai path, bukan clipPath
    for e in entri:
        if e.get('tf'):
            t = urai_transform(e['tf'], e['kotak'])
            if t:
                buka += '<g%s>' % t; tutup = '</g>' + tutup
        if e.get('clip'):
            d = titik_clip(e['clip'], e['kotak'])
            if d:
                cid = s.id('c')
                s.defs.append('<clipPath id="%s"><path d="%s"/></clipPath>' % (cid, d))
                buka += '<g clip-path="url(#%s)">' % cid; tutup = '</g>' + tutup
    return buka, tutup, jalur_self

class Svg:
    def __init__(s, w, h):
        s.w, s.h, s.badan, s.defs, s.n = w, h, [], [], 0
    def id(s, p='d'):
        s.n += 1; return '%s%d' % (p, s.n)
    def gradien(s, css, k):
        m = re.match(r'linear-gradient\((-?[\d.]+)deg,\s*(.+)\)$', css.strip())
        if not m: return None
        sudut = float(m.group(1))
        henti = []
        for bag in re.findall(r'(rgba?\([^)]*\)|#[0-9a-fA-F]+)\s*([\d.]+%)?', m.group(2)):
            w, a = urai_warna(bag[0])
            henti.append((w, a, bag[1]))
        if len(henti) < 2: return None
        rad = math.radians(sudut)
        dx, dy = math.sin(rad), -math.cos(rad)
        L = abs(k['w'] * dx) + abs(k['h'] * dy)
        cx, cy = k['x'] + k['w'] / 2, k['y'] + k['h'] / 2
        gid = s.id('g')
        pos = lambda i, p: (p if p else '%d%%' % round(i / (len(henti) - 1) * 100))
        s.defs.append('<linearGradient id="%s" gradientUnits="userSpaceOnUse" x1="%s" y1="%s" x2="%s" y2="%s">%s</linearGradient>'
            % (gid, N(cx - dx * L / 2), N(cy - dy * L / 2), N(cx + dx * L / 2), N(cy + dy * L / 2),
               ''.join('<stop offset="%s" stop-color="%s" stop-opacity="%g"/>' % (pos(i, p), w, a)
                       for i, (w, a, p) in enumerate(henti))))
        return 'url(#%s)' % gid
    def urai_bayang(s, css):
        """Pecah box-shadow / filter drop-shadow jadi daftar lapisan."""
        lapis = []
        for bag in re.findall(r'drop-shadow\(([^)]*(?:\([^)]*\))?[^)]*)\)', css) or [css]:
            teks = bag
            for potong in re.split(r',(?![^(]*\))', teks):
                potong = potong.strip()
                if not potong: continue
                w, a = None, 1.0
                cm = re.search(r'(rgba?\([^)]*\)|#[0-9a-fA-F]{3,8})', potong)
                if cm:
                    w, a = urai_warna(cm.group(1))
                    potong = potong.replace(cm.group(1), ' ')
                angka = [float(x) for x in re.findall(r'(-?[\d.]+)px', potong)]
                if not angka or w is None: continue
                dx, dy = (angka + [0, 0])[:2]
                bl = angka[2] if len(angka) > 2 else 0
                sp = angka[3] if len(angka) > 3 else 0
                lapis.append({'dx': dx, 'dy': dy, 'blur': bl, 'spread': sp, 'w': w, 'a': a})
        return lapis

    def bayang(s, css):
        lapis = [l for l in s.urai_bayang(css) if not (l['blur'] == 0 and l['spread'] > 0
                                                       and l['dx'] == 0 and l['dy'] == 0)]
        if not lapis: return ''
        fid = s.id('f')
        prim, masuk = [], None
        for i, l in enumerate(lapis):
            hasil = ' result="b%d"' % i if i < len(lapis) - 1 else ''
            prim.append('<feDropShadow%s dx="%s" dy="%s" stdDeviation="%s" flood-color="%s" '
                        'flood-opacity="%g"%s/>' % (' in="%s"' % masuk if masuk else '',
                        N(l['dx']), N(l['dy']), N(l['blur'] / 2), l['w'], l['a'], hasil))
            masuk = 'b%d' % i
        s.defs.append('<filter id="%s" x="-60%%" y="-60%%" width="220%%" height="220%%">%s</filter>'
                      % (fid, ''.join(prim)))
        return ' filter="url(#%s)"' % fid

    def cincin(s, css, k, radius):
        """box-shadow 0 0 0 Npx: digambar sebagai bentuk yang dimekarkan, bukan filter."""
        keluar = []
        for l in s.urai_bayang(css):
            if l['blur'] == 0 and l['spread'] > 0 and l['dx'] == 0 and l['dy'] == 0:
                sp = l['spread']
                rx = ' rx="%s"' % N(radius + sp) if radius > .5 else ''
                keluar.append('<rect x="%s" y="%s" width="%s" height="%s"%s fill="%s"%s/>'
                    % (N(k['x'] - sp), N(k['y'] - sp), N(k['w'] + 2 * sp), N(k['h'] + 2 * sp), rx, l['w'],
                       ' fill-opacity="%g"' % l['a'] if l['a'] < .999 else ''))
        return keluar
    def keluar(s, judul):
        return ('<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" '
                'width="297mm" height="420mm" viewBox="0 0 %d %d" role="img" aria-label="%s">\n'
                '<title>%s</title>\n<desc>A3 potret 297 x 420 mm. Huruf: Archivo, Plus Jakarta Sans, Caveat.</desc>\n'
                '<defs>%s</defs>\n%s\n</svg>\n'
                ) % (s.w, s.h, judul, judul, ''.join(s.defs), '\n'.join(s.badan))

def bangun(jalur_json, judul):
    d = json.load(open(jalur_json, encoding='utf-8'))
    s = Svg(d['w'], d['h'])
    for n in d['simpul']:
        k = n['kotak']
        buka, tutup, jalur_self = bungkus(n.get('rantai', []), s, k)
        op = '' if n.get('op', 1) >= .999 else ' opacity="%g"' % n['op']
        if op: buka, tutup = buka + '<g%s>' % op, '</g>' + tutup
        if n['jenis'] == 'svg':
            vb = [float(x) for x in n['vb'].split()]
            sx = k['w'] / vb[2] if vb[2] else 1
            isi = re.sub(r'^<svg[^>]*>', '', n['isi']).replace('</svg>', '')
            # id di dalam potongan dibuat unik supaya beberapa salinan tidak bentrok
            akhiran = s.id('u')
            for lama in set(re.findall(r'id="([^"]+)"', isi)):
                isi = isi.replace('id="%s"' % lama, 'id="%s-%s"' % (lama, akhiran))
                isi = isi.replace('url(#%s)' % lama, 'url(#%s-%s)' % (lama, akhiran))
            isi = bakar_fragmen(isi, sx, k['x'] - vb[0] * sx, k['y'] - vb[1] * sx)
            # atribut penampilan milik <svg> pembungkus ikut hilang waktu tag dilucuti —
            # tanpa fill="none" tiap <path> bergaris akan terisi hitam. Pasang ulang
            # sebagai atribut grup. stroke-width sengaja tidak dibawa: skalanya sudah
            # dibakar ke dalam tiap path.
            pembuka = re.match(r'^<svg([^>]*)>', n['isi'])
            bawa = []
            for nama_atr in ('fill', 'stroke', 'stroke-linejoin', 'stroke-linecap',
                             'stroke-miterlimit', 'fill-rule'):
                m_atr = re.search(r'(?:^|\s)' + nama_atr + r'="([^"]*)"', pembuka.group(1) if pembuka else '')
                if m_atr: bawa.append('%s="%s"' % (nama_atr, m_atr.group(1)))
            if 'currentColor' in isi and n.get('warnaTeks'):
                bawa.insert(0, 'color="%s"' % urai_warna(n['warnaTeks'])[0])
            if bawa:
                isi = '<g %s>%s</g>' % (' '.join(bawa), isi)
            s.badan.append(buka + isi + tutup)
            continue
        bag = []
        isi_warna, isi_alpha = urai_warna(n.get('bg'))
        if n.get('grad'):
            g = s.gradien(n['grad'], k)
            if g: isi_warna, isi_alpha = g, 1.0
        jalur = jalur_self
        bayang = s.bayang(n['shadow']) if n.get('shadow') else ''
        if not bayang and n.get('filter') and 'drop-shadow' in n['filter']:
            bayang = s.bayang(n['filter'])
        if n.get('shadow'):
            r0 = (n.get('radius') or [0])[0]
            bag.extend(s.cincin(n['shadow'], k, r0))
        if isi_warna:
            if jalur:
                bag.append('<path d="%s" fill="%s"%s%s/>' % (jalur, isi_warna,
                    ' fill-opacity="%g"' % isi_alpha if isi_alpha < .999 else '', bayang))
            else:
                r = n.get('radius', [0, 0, 0, 0])
                rx = ' rx="%s"' % N(r[0]) if r and r[0] > .5 else ''
                bag.append('<rect x="%s" y="%s" width="%s" height="%s"%s fill="%s"%s%s/>'
                    % (N(k['x']), N(k['y']), N(k['w']), N(k['h']), rx, isi_warna,
                       ' fill-opacity="%g"' % isi_alpha if isi_alpha < .999 else '', bayang))
        b = n.get('border')
        if b:
            T, R, B, L = b['lebar']
            x, y, w, h = k['x'], k['y'], k['w'], k['h']
            if b['seragam'] and T > 0:
                bc, ba = urai_warna(b['sisi'][0])
                dash = ' stroke-dasharray="%d %d"' % (T * 2, T * 2) if b['gaya'][0] == 'dashed' else ''
                o = ' stroke-opacity="%g"' % ba if ba < .999 else ''
                r = n.get('radius', [0])
                rx = ' rx="%s"' % N(max(0, r[0] - T / 2)) if r and r[0] > .5 else ''
                bag.append('<rect x="%s" y="%s" width="%s" height="%s"%s fill="none" stroke="%s" '
                           'stroke-width="%s"%s%s/>' % (N(x + T / 2), N(y + T / 2),
                            N(w - T), N(h - T), rx, bc, N(T), dash, o))
            elif sum(1 for i, lb in enumerate(b['lebar']) if lb > 0 and b['gaya'][i] != 'none') == 1 \
                 and any(g in ('dashed', 'dotted') for g in b['gaya']):
                # hanya satu sisi dan bergaya putus-putus: gambar sebagai garis,
                # bukan bidang, supaya putus-putusnya tidak hilang (mis. jahitan saku)
                i = next(j for j, lb in enumerate(b['lebar']) if lb > 0 and b['gaya'][j] != 'none')
                lb = b['lebar'][i]
                c, a = urai_warna(b['sisi'][i])
                pola = (lb * 2, lb * 2) if b['gaya'][i] == 'dashed' else (lb, lb * 2)
                garis = {0: (x, y + lb / 2, x + w, y + lb / 2),
                         1: (x + w - lb / 2, y, x + w - lb / 2, y + h),
                         2: (x, y + h - lb / 2, x + w, y + h - lb / 2),
                         3: (x + lb / 2, y, x + lb / 2, y + h)}[i]
                bag.append('<path d="M%s %sL%s %s" stroke="%s" stroke-width="%s" fill="none" '
                           'stroke-dasharray="%d %d"%s/>'
                           % (N(garis[0]), N(garis[1]), N(garis[2]), N(garis[3]), c, N(lb),
                              pola[0], pola[1], ' stroke-opacity="%g"' % a if a < .999 else ''))
            else:
                # empat trapesium; sisi bening dilewati. Ini juga yang membentuk
                # segitiga CSS seperti ekor penanda peta.
                sisi = [
                    (T, [(x, y), (x + w, y), (x + w - R, y + T), (x + L, y + T)]),
                    (R, [(x + w, y), (x + w, y + h), (x + w - R, y + h - B), (x + w - R, y + T)]),
                    (B, [(x, y + h), (x + w, y + h), (x + w - R, y + h - B), (x + L, y + h - B)]),
                    (L, [(x, y), (x, y + h), (x + L, y + h - B), (x + L, y + T)])]
                for i, (lb, titik) in enumerate(sisi):
                    if lb <= 0 or b['gaya'][i] == 'none': continue
                    c, a = urai_warna(b['sisi'][i])
                    if not c or a < .02: continue
                    d = 'M' + 'L'.join('%s %s' % (N(px), N(py)) for px, py in titik) + 'Z'
                    bag.append('<path d="%s" fill="%s"%s/>' % (d, c,
                               ' fill-opacity="%g"' % a if a < .999 else ''))
        t = n.get('teks')
        if t:
            w, a = urai_warna(t['c'])
            ls = ' letter-spacing="%s"' % N(t['ls']) if abs(t['ls']) > .4 else ''
            ao = ' fill-opacity="%g"' % a if a < .999 else ''
            for ln in t['baris']:
                dasar = ln['y'] + (t['lh'] - t['fs']) / 2 + t['fs'] * 0.8
                bag.append('<text x="%s" y="%s" font-family="%s" font-size="%s" font-weight="%s" '
                           'fill="%s"%s%s>%s</text>' % (N(ln['x']), N(dasar), t['ff'], I(t['fs']),
                            t['fw'], w, ls, ao, E(ln['t'])))
        if bag:
            s.badan.append(buka + ''.join(bag) + tutup)
    return s.keluar(judul)

if __name__ == '__main__':
    for berkas, judul, nama in [
        ('Main', 'Poster Balikin — S1 Kartu Melayang', 'poster-s1-kartu-melayang'),
        ('Editorial', 'Poster Balikin — S2 Editorial', 'poster-s2-editorial'),
        ('Saku', 'Poster Balikin — S3 Saku', 'poster-s3-saku'),
        ('Stiker', 'Poster Balikin — S4 Stiker', 'poster-s4-stiker'),
        ('Irisan', 'Poster Balikin — S5 Irisan', 'poster-s5-irisan'),
        ('CapLogo', 'Poster Balikin — S6 Cap Logo', 'poster-s6-cap-logo')]:
        svg = bangun('/tmp/%s.json' % berkas, judul)
        keluar = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'svg', nama + '.svg')
        open(keluar, 'w', encoding='utf-8').write(svg)
        sisa = sorted(set(re.findall(r'-?\d+\.\d+', svg)))
        print('%-28s %5d KB  desimal: %d %s' % (nama + '.svg', len(svg) // 1024, len(sisa), sisa[:6]))
