// Memotret artboard .dc.html jadi PNG. Ukuran diambil dari kotak akar.
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
for (const f of process.argv.slice(2)) {
  const p = await b.newPage({ viewport: { width: 1200, height: 1600 }, deviceScaleFactor: 2 });
  await p.goto('file://' + f);
  await p.waitForTimeout(2400);
  const el = await p.$('body > div, x-dc > div');
  await (el || p).screenshot({ path: f.replace(/\.dc\.html$/, '.png') });
  console.log(f.replace(/\.dc\.html$/, '.png'));
  await p.close();
}
await b.close();
