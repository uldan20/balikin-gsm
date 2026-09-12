// Memotret artboard .dc.html jadi PNG untuk diperiksa.
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1122, height: 1587 }, deviceScaleFactor: 1 });
for (const f of process.argv.slice(2)) {
  await p.goto('file://' + f);
  await p.waitForTimeout(2600);
  await p.screenshot({ path: f.replace(/\.dc\.html$/, '.png'), fullPage: false });
  console.log(f.replace(/\.dc\.html$/, '.png'));
}
await b.close();
