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
});

test('each experience section uses its dedicated image and PhDessert uses the lowercase Pages path', () => {
  for (const ref of [
    'assets/images/hero-tang.avif',
    'assets/images/dynasty-han.avif',
    'assets/images/dynasty-tang.avif',
    'assets/images/dynasty-song.avif',
    'assets/images/dynasty-ming.avif',
    'assets/images/styling.avif',
    'assets/images/jewellery.avif',
    'assets/images/ceremonial.avif',
    'assets/images/tea.avif',
    'assets/images/pastry.avif',
    'assets/images/coming.avif'
  ]) assert.ok(html.includes(ref), `missing image reference: ${ref}`);

  assert.ok(html.includes('https://haoyyw.github.io/phdessert/'), 'PhDessert link should use lowercase repo path');
  assert.ok(!html.includes('https://haoyyw.github.io/PHDESSERT/'), 'uppercase PhDessert Pages path must be removed');
});
