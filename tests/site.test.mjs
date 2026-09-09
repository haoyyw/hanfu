import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

const html = fs.readFileSync(new URL('../index.html', import.meta.url), 'utf8');

test('bilingual labels promote the active language', () => {
  assert.match(html, /class="[^"]*bilabel[^"]*"/, 'expected reusable bilingual label markup');
  assert.match(html, /html\[data-locale="en"\][^{]*\.bilabel[^\n]*\.en/, 'EN locale must promote English labels');
  assert.match(html, /html\[data-locale="zh"\][^{]*\.bilabel[^\n]*\.zh/, 'ZH locale must promote Chinese labels');
  assert.match(html, /html\[data-locale="en"\][^{]*\.bilabel[^\n]*\.zh/, 'EN locale must demote Chinese labels');
  assert.match(html, /html\[data-locale="zh"\][^{]*\.bilabel[^\n]*\.en/, 'ZH locale must demote English labels');
  assert.match(html, /tab-bilabel/, 'dynasty tabs should follow the active-language hierarchy');
  assert.match(html, /dynasty-bilabel/, 'dynamic dynasty title should follow the active-language hierarchy');
});

test('bilingual hierarchy remains visually clean in hero, footer and pastry cards', () => {
  assert.match(html, /\.hero \.hero-brand>span\{[^}]*margin:0/, 'hero bilingual children must clear legacy margins');
  assert.match(html, /\.footer strong\.bilabel\{[^}]*display:flex/, 'footer bilingual brand must remain a flex ordering context');
  assert.match(html, /\.pastry-item \.bilabel span\{[^}]*padding:0/, 'pastry bilingual child labels must clear legacy padding');
});

test('HD assets and dedicated ceremonial visual are wired into the page', () => {
  for (const ref of [
    'assets/images/dynasty-han.avif',
    'assets/images/dynasty-tang.avif',
    'assets/images/dynasty-song.avif',
    'assets/images/dynasty-ming.avif',
    'assets/images/styling.avif',
    'assets/images/jewellery.avif',
    'assets/images/ceremonial.avif'
  ]) assert.ok(html.includes(ref), `missing HD image reference: ${ref}`);

  assert.match(html, /ceremonial\.avif[^>]+Chinese ceremonial and bridal styling/, 'ceremonial section must use its dedicated image');
});

test('PhDessert integration uses the live lowercase path and high-resolution pastry product images', () => {
  assert.ok(html.includes('https://haoyyw.github.io/phdessert/'), 'PhDessert link should use lowercase repo path');
  assert.ok(!html.includes('https://haoyyw.github.io/PHDESSERT/'), 'uppercase PhDessert Pages path must be removed');
  for (const product of ['peach-blossom.webp', 'osmanthus-cake.webp', 'mung-bean-cake.webp', 'rice-cake.webp']) {
    assert.ok(html.includes(product), `missing PhDessert product image: ${product}`);
  }
  assert.ok(!html.includes('chinese-tasting-box.webp'), 'obsolete broken tasting-box image should be removed');
});
