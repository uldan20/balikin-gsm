# -*- coding: utf-8 -*-
"""Tambahan fragmen ikon gaya Sudut Enam (Hexcut) untuk infografis.

Aturan yang dipakai sama dengan pustaka aplikasi: kotak 100x100, sudut
dipangkas bukan dibulatkan, sambungan mitre, tebal garis bilangan bulat.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'xbanner'))
from build import ICONS as IKON_DASAR

S = 'stroke="currentColor" stroke-width="%d"'

IKON = {
 'kunci': '<path d="M36 28L52 19L68 28V46L52 55L36 46Z" stroke="currentColor" stroke-width="7"/>'
          '<path d="M52 55V85" stroke="currentColor" stroke-width="7"/>'
          '<path d="M52 65H70" stroke="currentColor" stroke-width="6"/>'
          '<path d="M52 75H64" stroke="currentColor" stroke-width="6"/>',
 'ponsel': '<path d="M32 10H68L74 20V80L68 90H32L26 80V20Z" stroke="currentColor" stroke-width="7"/>'
           '<path d="M42 22H58" stroke="currentColor" stroke-width="6"/>'
           '<path d="M40 78H60" stroke="currentColor" stroke-width="6"/>',
 'dokumen': '<path d="M24 18L32 10H58L78 30V82L70 90H32L24 82Z" stroke="currentColor" stroke-width="7"/>'
            '<path d="M56 12V32H76" stroke="currentColor" stroke-width="6"/>'
            '<path d="M38 50H64M38 64H64M38 76H54" stroke="currentColor" stroke-width="6"/>',
 'kartu': '<path d="M14 24H86L92 36V70L86 82H14L8 70V36Z" stroke="currentColor" stroke-width="7"/>'
          '<path d="M34 40L44 46V58L34 64L24 58V46Z" stroke="currentColor" stroke-width="6"/>'
          '<path d="M56 46H78M56 58H70" stroke="currentColor" stroke-width="6"/>',
 'lonceng': '<path d="M32 66V44L42 26H58L68 44V66L78 80H22Z" stroke="currentColor" stroke-width="7"/>'
            '<path d="M42 88H58" stroke="currentColor" stroke-width="6"/>',
 'cari': '<path d="M44 14L68 28V56L44 70L20 56V28Z" stroke="currentColor" stroke-width="7"/>'
         '<path d="M62 64L86 86" stroke="currentColor" stroke-width="8"/>',
 'obrolan': '<path d="M12 22H88L94 34V64L88 76H50L30 90V76H12L6 64V34Z" stroke="currentColor" stroke-width="7"/>'
            '<path d="M32 43L38 49L32 55L26 49Z" fill="currentColor"/>'
            '<path d="M50 43L56 49L50 55L44 49Z" fill="currentColor"/>'
            '<path d="M68 43L74 49L68 55L62 49Z" fill="currentColor"/>',
 'warga': '<path d="M50 16L64 24V40L50 48L36 40V24Z" stroke="currentColor" stroke-width="7"/>'
          '<path d="M18 88V74L34 58H66L82 74V88" stroke="currentColor" stroke-width="7"/>',
 'peta': '<path d="M8 26L36 14L64 26L92 14V74L64 86L36 74L8 86Z" stroke="currentColor" stroke-width="7"/>'
         '<path d="M36 14V74M64 26V86" stroke="currentColor" stroke-width="6"/>',
 'bintang': '<path d="M50 12L61 39L88 50L61 61L50 88L39 61L12 50L39 39Z" stroke="currentColor" stroke-width="7"/>',
 'perisai': '<path d="M50 10L84 22V48L50 90L16 48V22Z" stroke="currentColor" stroke-width="7"/>'
            '<path d="M34 48L46 60L68 36" stroke="currentColor" stroke-width="7"/>',
 'jam': '<path d="M50 12L83 31V69L50 88L17 69V31Z" stroke="currentColor" stroke-width="7"/>'
        '<path d="M50 34V52H66" stroke="currentColor" stroke-width="7"/>',
 'tambah': '<path d="M50 24V76M24 50H76" stroke="currentColor" stroke-width="9"/>',
 'kurang': '<path d="M24 50H76" stroke="currentColor" stroke-width="9"/>',
 'panah': '<path d="M16 50H78M58 30L78 50L58 70" stroke="currentColor" stroke-width="8"/>',
 'gembok': '<path d="M34 44V32L42 22H58L66 32V44" stroke="currentColor" stroke-width="6"/>'
           '<path d="M22 44H78L84 56V78L78 88H22L16 78V56Z" stroke="currentColor" stroke-width="7"/>'
           '<path d="M50 58L57 62V70L50 74L43 70V62Z" fill="currentColor"/>',
 'hewan': '<path d="M50 46L66 55V73L50 82L34 73V55Z" stroke="currentColor" stroke-width="7"/>'
          '<path d="M30 22L38 26V34L30 38L22 34V26Z" stroke="currentColor" stroke-width="6"/>'
          '<path d="M50 16L58 20V28L50 32L42 28V20Z" stroke="currentColor" stroke-width="6"/>'
          '<path d="M70 22L78 26V34L70 38L62 34V26Z" stroke="currentColor" stroke-width="6"/>',
 'tumbler': '<path d="M40 10H60V24L68 38V80L60 90H40L32 80V38L40 24Z" stroke="currentColor" stroke-width="7"/>'
            '<path d="M32 52H68" stroke="currentColor" stroke-width="6"/>',
 'rumah': '<path d="M12 48L50 16L88 48" stroke="currentColor" stroke-width="7"/>'
          '<path d="M24 42V76L32 84H68L76 76V42" stroke="currentColor" stroke-width="7"/>'
          '<path d="M42 84V62H58V84" stroke="currentColor" stroke-width="6"/>',
 'kompas': '<path d="M50 12L83 31V69L50 88L17 69V31Z" stroke="currentColor" stroke-width="7"/>'
           '<path d="M64 36L54 54L36 64L46 46Z" stroke="currentColor" stroke-width="6"/>',
 # lima wadah tingkat — siluetnya mengikuti Tiers.tsx di repo aplikasi
 'tk1': '<path d="M50 17L78 33V67L50 83L22 67V33Z" stroke="currentColor" stroke-width="7" '
        'stroke-dasharray="9 8" opacity=".8"/>'
        '<path d="M50 42L58 46V54L50 58L42 54V46Z" fill="currentColor" opacity=".7"/>',
 'tk2': '<path d="M20 12H80L88 22V78L80 88H20L12 78V22Z" stroke="currentColor" stroke-width="7"/>'
        '<path d="M50 72L32 55V45L40 37H46L50 41L54 37H60L68 45V55Z" stroke="currentColor" stroke-width="6"/>',
 'tk3': '<path d="M50 14L79 31V69L50 86L21 69V31Z" stroke="currentColor" stroke-width="7"/>'
        '<path d="M50 30L60 36V48L50 54L40 48V36Z" fill="currentColor"/>'
        '<path d="M32 58L40 62V70L32 74L24 70V62Z" stroke="currentColor" stroke-width="5"/>'
        '<path d="M68 58L76 62V70L68 74L60 70V62Z" stroke="currentColor" stroke-width="5"/>',
 'tk4': '<path d="M50 8L88 21V49L50 92L12 49V21Z" stroke="currentColor" stroke-width="7"/>'
        '<path d="M50 30L61 36V50L50 56L39 50V36Z" fill="currentColor"/>',
 'tk5': '<path d="M50 10L58 22L72 18L74 32L88 36L80 48L88 60L74 64L72 78L58 74L50 86L42 74L28 78'
        'L26 64L12 60L20 48L12 36L26 32L28 18L42 22Z" stroke="currentColor" stroke-width="6"/>'
        '<path d="M50 32L56 44L68 50L56 56L50 68L44 56L32 50L44 44Z" fill="currentColor"/>',
}
IKON.update(IKON_DASAR)

def ik(nama, px, warna):
    return ('<svg width="%d" height="%d" viewBox="0 0 100 100" fill="none" stroke-linejoin="miter" '
            'stroke-miterlimit="8" style="color:%s;display:block">%s</svg>') % (px, px, warna, IKON[nama])
