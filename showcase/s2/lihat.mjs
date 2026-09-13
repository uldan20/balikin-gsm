import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1200, height: 1660 }, deviceScaleFactor: 1 });
for (const f of process.argv.slice(2)) {
  await p.goto('file://' + f, { waitUntil: 'domcontentloaded' });
  await p.waitForTimeout(1400);
  const el = await p.$('x-dc > div');
  await (el || p).screenshot({ path: f.replace(/\.dc\.html$/, '.png') });
}
console.log('selesai');
await b.close();
