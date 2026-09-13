// Membaca satu artboard .dc.html lalu menuliskan geometrinya sebagai JSON.
// Transform dilucuti supaya yang terukur adalah kotak tata letak asli; rantai
// transform dan clip milik seluruh leluhur dicatat terpisah dan dipasang ulang
// sebagai grup bersarang di SVG, supaya putaran dan pemotongan tetap menurun.
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';

const b = await chromium.launch();
// Ukuran artboard boleh diberikan lewat argumen ke-3 dan ke-4; bawaannya A3 potret.
const VW = parseInt(process.argv[4]) || 1122, VH = parseInt(process.argv[5]) || 1587;
const p = await b.newPage({ viewport: { width: VW, height: VH }, deviceScaleFactor: 1 });
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(3200);

const data = await p.evaluate(() => {
  const root = document.body.firstElementChild;
  const semua = [...document.querySelectorAll('*')];
  const idx = new Map(semua.map((el, i) => [el, i]));

  // 1. catat transform & clip tiap elemen sebelum transform dilucuti
  const tf = new Map(), clip = new Map();
  semua.forEach(el => {
    const cs = getComputedStyle(el);
    if (cs.transform && cs.transform !== 'none') tf.set(el, cs.transform);
    if (cs.clipPath && cs.clipPath !== 'none') clip.set(el, cs.clipPath);
  });

  const kunci = el => {
    const k = [];
    for (let n = el; n && n !== document.body; n = n.parentElement) {
      const cs = getComputedStyle(n);
      const z = cs.position !== 'static' && cs.zIndex !== 'auto' ? parseInt(cs.zIndex) : 0;
      k.unshift(z, idx.get(n));
    }
    return k;
  };
  const kunciSemua = new Map(semua.map(el => [el, kunci(el)]));

  // 2. lucuti transform, ukur dalam ruang tata letak
  const st = document.createElement('style');
  st.textContent = '*{transform:none !important}';
  document.head.appendChild(st);
  const O = root.getBoundingClientRect();
  const rel = r => ({ x: r.x - O.x, y: r.y - O.y, w: r.width, h: r.height });

  const warna = c => (!c || c === 'rgba(0, 0, 0, 0)' || c === 'transparent') ? null : c;
  const num = v => Math.round(parseFloat(v) || 0);

  // rantai leluhur (terluar dulu) berisi transform dan clip masing-masing
  function rantai(el) {
    const r = [];
    for (let n = el; n && n !== document.body; n = n.parentElement) {
      const t = tf.get(n), c = clip.get(n);
      if (t || c) r.unshift({ tf: t || null, clip: c || null, kotak: rel(n.getBoundingClientRect()) });
    }
    return r;
  }

  // pecah simpul teks jadi baris berdasarkan perubahan posisi atas tiap huruf
  function baris(tn) {
    const s = tn.textContent;
    if (!s.trim()) return [];
    const r = document.createRange();
    const out = [];
    let kini = null;
    for (let i = 0; i < s.length; i++) {
      r.setStart(tn, i); r.setEnd(tn, i + 1);
      const q = r.getBoundingClientRect();
      const kosong = q.width === 0 && q.height === 0;
      if (kosong) { if (kini) kini.t += s[i]; continue; }
      if (!kini || Math.abs(q.top - kini.top) > 1.2) {
        if (/\s/.test(s[i])) continue;          // spasi di awal baris dibuang
        kini = { t: s[i], x: q.x, top: q.top, h: q.height };
        out.push(kini);
      } else {
        kini.t += s[i];
        if (q.x < kini.x) kini.x = q.x;
      }
    }
    return out.map(l => ({ t: l.t.replace(/\s+$/, ''), x: l.x - O.x, y: l.top - O.y, h: l.h }))
              .filter(l => l.t);
  }

  const simpul = [];
  for (const el of semua) {
    if (el.closest('svg') && el.tagName.toLowerCase() !== 'svg') continue;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const r = el.getBoundingClientRect();
    if (r.width < 0.5 || r.height < 0.5) continue;
    const kotak = rel(r);
    const n = { k: kunciSemua.get(el), kotak, tag: el.tagName.toLowerCase(),
                op: parseFloat(cs.opacity), rantai: rantai(el) };
    if (n.tag === 'svg') {
      n.jenis = 'svg';
      n.isi = el.outerHTML;
      n.vb = el.getAttribute('viewBox') || ('0 0 ' + r.width + ' ' + r.height);
      n.warnaTeks = cs.color;   // penentu currentColor di dalam potongan
    } else {
      n.jenis = 'kotak';
      n.bg = warna(cs.backgroundColor);
      if (cs.backgroundImage && cs.backgroundImage !== 'none') n.grad = cs.backgroundImage;
      n.radius = [cs.borderTopLeftRadius, cs.borderTopRightRadius,
                  cs.borderBottomRightRadius, cs.borderBottomLeftRadius].map(v =>
                    v.includes('%') ? parseFloat(v) / 100 * Math.min(r.width, r.height) : parseFloat(v) || 0);
      const lebar = [cs.borderTopWidth, cs.borderRightWidth, cs.borderBottomWidth, cs.borderLeftWidth].map(num);
      const sisi = [cs.borderTopColor, cs.borderRightColor, cs.borderBottomColor, cs.borderLeftColor];
      const gaya = [cs.borderTopStyle, cs.borderRightStyle, cs.borderBottomStyle, cs.borderLeftStyle];
      if (lebar.some((v, i) => v > 0 && gaya[i] !== 'none')) {
        const seragam = lebar.every(v => v === lebar[0]) && sisi.every(c => c === sisi[0]);
        n.border = { lebar, sisi, gaya, seragam };
      }
      if (cs.boxShadow && cs.boxShadow !== 'none') n.shadow = cs.boxShadow;
      if (cs.filter && cs.filter !== 'none') n.filter = cs.filter;
      const br = [];
      for (const c of el.childNodes) if (c.nodeType === 3) br.push(...baris(c));
      if (br.length) n.teks = { baris: br, ff: cs.fontFamily.split(',')[0].replace(/["']/g, ''),
                                fs: parseFloat(cs.fontSize), fw: cs.fontWeight, c: cs.color,
                                ls: parseFloat(cs.letterSpacing) || 0,
                                lh: parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) };
      if (!n.bg && !n.grad && !n.border && !n.teks) continue;
    }
    simpul.push(n);
  }
  const cmp = (a, b) => { for (let i = 0; i < Math.max(a.length, b.length); i++) {
    const x = a[i] ?? -1e9, y = b[i] ?? -1e9; if (x !== y) return x - y; } return 0; };
  simpul.sort((a, b) => cmp(a.k, b.k));
  return { w: Math.round(O.width), h: Math.round(O.height), simpul };
});
fs.writeFileSync(process.argv[3], JSON.stringify(data));
console.log(process.argv[2].split('/').pop(), '→', data.simpul.length, 'simpul');
await b.close();
