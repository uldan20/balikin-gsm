# -*- coding: utf-8 -*-
"""Alat perapi koordinat: membakar transform ke dalam data path dan membulatkan
semua angka geometri ke bilangan bulat, supaya panel Figma tidak penuh desimal."""
import re, math

def I(v):
    """Bulatkan ke bilangan bulat, buang -0."""
    n = int(round(float(v)))
    return 0 if n == 0 else n

def N(v):
    return str(I(v))

# ---- pembakar transform pada data path ----
CMD = re.compile(r'([MmLlHhVvCcSsQqTtAaZz])|(-?\d*\.?\d+(?:[eE][-+]?\d+)?)')
# berapa angka per perintah, dan mana yang sumbu-x (True) / sumbu-y (False) / bukan koordinat (None)
SUMBU = {
 'M': [True, False], 'L': [True, False], 'T': [True, False],
 'H': [True], 'V': [False],
 'C': [True, False, True, False, True, False],
 'S': [True, False, True, False],
 'Q': [True, False, True, False],
 'A': [None, None, None, None, None, True, False],
 'Z': [],
}

def bakar_path(d, s, tx, ty):
    """Kalikan seluruh koordinat path dengan s lalu geser (tx,ty). Perintah huruf
    kecil (relatif) hanya diskalakan, tidak digeser."""
    tok = [(a or b) for a, b in CMD.findall(d)]
    out, i, cmd = [], 0, None
    while i < len(tok):
        t = tok[i]
        if re.match(r'[A-Za-z]', t):
            cmd = t; out.append(t); i += 1
            if cmd in 'Zz': continue
        if cmd is None:
            i += 1; continue
        besar = cmd.upper()
        pola = SUMBU[besar]
        if not pola:
            i += 1; continue
        rel = cmd.islower()
        for j, sumbu in enumerate(pola):
            if i >= len(tok) or re.match(r'[A-Za-z]', tok[i]): break
            v = float(tok[i])
            if sumbu is None:                 # bendera busur, jangan diubah
                out.append(('%g' % v))
            elif rel:
                out.append(N(v * s))
            else:
                out.append(N(v * s + (tx if sumbu else ty)))
            i += 1
        # perintah M yang berulang jadi L (aturan SVG); biarkan, cukup lanjut
        if besar == 'M': cmd = 'L' if cmd == 'M' else 'l'
    # rapikan: sisipkan spasi antar angka, tempel huruf
    hasil = ''
    for t in out:
        if re.match(r'[A-Za-z]', t): hasil += t
        else: hasil += (' ' if hasil and not hasil[-1].isalpha() else '') + t
    return hasil

ATTR = re.compile(r'(\w[\w-]*)="([^"]*)"')

def bakar_fragmen(frag, s, tx, ty):
    """Bakar transform ke seluruh elemen dalam potongan SVG (path/circle/ellipse/rect)."""
    def satu(m):
        tag = m.group(1); isi = m.group(2)
        def attr(am):
            k, v = am.group(1), am.group(2)
            try:
                if k == 'd':            return 'd="%s"' % bakar_path(v, s, tx, ty)
                if k in ('cx', 'x', 'x1', 'x2'): return '%s="%s"' % (k, N(float(v) * s + tx))
                if k in ('cy', 'y', 'y1', 'y2'): return '%s="%s"' % (k, N(float(v) * s + ty))
                if k in ('r', 'rx', 'ry', 'width', 'height', 'stroke-width'):
                    return '%s="%s"' % (k, N(float(v) * s))
                if k == 'transform':
                    rm = re.match(r'rotate\(([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\)', v.strip())
                    if rm:
                        a, ox, oy = rm.groups()
                        return 'transform="rotate(%s %s %s)"' % (
                            ('%g' % float(a)), N(float(ox) * s + tx), N(float(oy) * s + ty))
            except ValueError:
                pass
            return am.group(0)
        return '<%s %s' % (tag, ATTR.sub(attr, isi))
    return re.sub(r'<(\w+)\s([^>]*)', satu, frag)

# ---- heksagon dengan titik bulat ----
def hex6(cx, cy, s, r):
    """Heksagon ujung-atas dengan setengah-lebar s dan jari-jari r, seluruh titik bulat."""
    h = I(r / 2)
    p = [(cx, cy - r), (cx + s, cy - h), (cx + s, cy + h),
         (cx, cy + r), (cx - s, cy + h), (cx - s, cy - h)]
    return 'M' + 'L'.join('%s %s' % (N(a), N(b)) for a, b in p) + 'Z'

def bidang(w, h, x=0, y=0):
    """Kotak tak terlihat supaya bingkai grup terbaca bulat di Figma."""
    return '<rect x="%s" y="%s" width="%s" height="%s" fill="none" stroke="none"/>' % (
        N(x), N(y), N(w), N(h))
