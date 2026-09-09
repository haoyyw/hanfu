from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')


def replace_once(old: str, new: str, label: str) -> None:
    global s
    if new in s:
        return
    if old not in s:
        raise SystemExit(f'missing expected fragment: {label}')
    s = s.replace(old, new, 1)


css_marker = '/* locale-hierarchy-v2 */'
if css_marker not in s:
    anchor = '@media(max-width:900px){'
    if anchor not in s:
        raise SystemExit('missing CSS media-query anchor')
    css = r'''/* locale-hierarchy-v2 */
.bilabel{display:flex;align-items:baseline;gap:.32em;flex-wrap:wrap}.bilabel .en{font-family:var(--serif)}.bilabel .zh{font-family:var(--zh)}
html[data-locale="en"] .bilabel .en{order:1;font-size:1em;font-weight:500;opacity:1}html[data-locale="en"] .bilabel .zh{order:2;font-size:.62em;font-weight:400;opacity:.54}
html[data-locale="zh"] .bilabel .zh{order:1;font-size:1em;font-weight:500;opacity:1}html[data-locale="zh"] .bilabel .en{order:2;font-size:.62em;font-weight:400;opacity:.56}
.brand-copy .bilabel{font-size:25px;line-height:1}.hero .hero-brand{font-size:clamp(72px,9vw,132px);line-height:.78;letter-spacing:-.045em;margin:0}.hero .hero-brand .zh{letter-spacing:.08em}.service .bilabel{font-size:38px;margin:34px 0 13px}.feature-label{font-size:12px;letter-spacing:.16em;text-transform:uppercase}.tab-bilabel{justify-content:center;font-size:30px;line-height:1}.tab-bilabel .en{letter-spacing:.08em}.dynasty-bilabel{font-size:inherit}.pastry-item{background:#211711;padding:15px}.pastry-item .bilabel{font-size:20px}.pastry-gallery{margin:0;aspect-ratio:4/5;overflow:hidden;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:2px;background:rgba(247,241,231,.15)}.pastry-gallery img{width:100%;height:100%;object-fit:cover;display:block}.footer .bilabel{font-size:24px;line-height:1}
'''
    s = s.replace(anchor, css + anchor, 1)

replace_once(
    '<strong>華裳 · HUASHANG</strong>',
    '<strong class="bilabel"><span class="en">HUASHANG</span><span class="zh">華裳</span></strong>',
    'header brand',
)
replace_once(
    '<h1><span>華裳</span><em>HUASHANG</em></h1>',
    '<h1 class="bilabel hero-brand"><span class="en">HUASHANG</span><span class="zh">華裳</span></h1>',
    'hero brand',
)

for dynasty, zh, en, active in [
    ('han', '漢', 'HAN', ''),
    ('tang', '唐', 'TANG', ' class="active"'),
    ('song', '宋', 'SONG', ''),
    ('ming', '明', 'MING', ''),
]:
    old = f'<button{active} data-dynasty="{dynasty}"><span>{zh}</span><small>{en}</small></button>'
    # Existing markup places class after data-dynasty for Tang.
    if dynasty == 'tang':
        old = '<button class="active" data-dynasty="tang"><span>唐</span><small>TANG</small></button>'
        new = '<button class="active" data-dynasty="tang"><span class="bilabel tab-bilabel"><span class="en">TANG</span><span class="zh">唐</span></span></button>'
    else:
        new = f'<button data-dynasty="{dynasty}"><span class="bilabel tab-bilabel"><span class="en">{en}</span><span class="zh">{zh}</span></span></button>'
    replace_once(old, new, f'{dynasty} tab')

for old, en, zh, label in [
    ('<h3>Hanfu · 汉服</h3>', 'Hanfu', '汉服', 'Hanfu service'),
    ('<h3>Make-up · 妆</h3>', 'Make-up', '妆', 'Make-up service'),
    ('<h3>Hair · 发</h3>', 'Hair', '发', 'Hair service'),
]:
    replace_once(old, f'<h3 class="bilabel"><span class="en">{en}</span><span class="zh">{zh}</span></h3>', label)

for old, en, zh, label in [
    ('<p class="eyebrow">JEWELLERY · 中式首饰</p>', 'JEWELLERY', '中式首饰', 'jewellery label'),
    ('<p class="eyebrow">A MOMENT FOR TEA · 一席茶</p>', 'A MOMENT FOR TEA', '一席茶', 'tea label'),
    ('<p class="eyebrow">TEA & PASTRY · 東方茶席 × PhDessert</p>', 'TEA & PASTRY × PhDessert', '东方茶席', 'pastry label'),
]:
    replace_once(old, f'<p class="eyebrow bilabel feature-label"><span class="en">{en}</span><span class="zh">{zh}</span></p>', label)

old_pastry = '<div class="pastry-list"><span>桃花酥<small>Peach Blossom Pastry</small></span><span>桂花糕<small>Osmanthus Cake</small></span><span>绿豆糕<small>Mung Bean Cake</small></span><span>米糕<small>Rice Cake</small></span></div>'
new_pastry = '<div class="pastry-list"><div class="pastry-item"><span class="bilabel"><span class="en">Peach Blossom Pastry</span><span class="zh">桃花酥</span></span></div><div class="pastry-item"><span class="bilabel"><span class="en">Osmanthus Cake</span><span class="zh">桂花糕</span></span></div><div class="pastry-item"><span class="bilabel"><span class="en">Mung Bean Cake</span><span class="zh">绿豆糕</span></span></div><div class="pastry-item"><span class="bilabel"><span class="en">Rice Cake</span><span class="zh">米糕</span></span></div></div>'
replace_once(old_pastry, new_pastry, 'pastry bilingual list')

# High-definition local imagery, with existing WebP fallbacks where useful.
replace_once(
    '<section class="hero" id="home"><img src="assets/images/hero-tang.webp" alt="Tang-inspired Hanfu in a refined Chinese cultural salon">',
    '<section class="hero" id="home"><img src="assets/images/dynasty-tang.avif" onerror="this.onerror=null;this.src=\'assets/images/hero-tang.webp\'" alt="Tang-inspired Hanfu in a refined Chinese cultural salon">',
    'hero image',
)
replace_once(
    '<figure><img src="assets/images/styling.webp" alt="Hanfu hair and make-up styling"></figure>',
    '<figure><img src="assets/images/styling.avif" onerror="this.onerror=null;this.src=\'assets/images/styling.webp\'" alt="Hanfu hair and make-up styling"></figure>',
    'styling image',
)
replace_once(
    '<figure><img src="assets/images/jewellery.webp" alt="Chinese hairpins, earrings, combs and jade ornaments"></figure>',
    '<figure><img src="assets/images/jewellery.avif" onerror="this.onerror=null;this.src=\'assets/images/jewellery.webp\'" alt="Chinese hairpins, earrings, combs and jade ornaments"></figure>',
    'jewellery image',
)
replace_once(
    '<figure><img src="assets/images/dynasty-ming.webp" alt="Ming-inspired red and green ceremonial styling"></figure>',
    '<figure><img src="assets/images/ceremonial.avif" onerror="this.onerror=null;this.src=\'assets/images/dynasty-ming.webp\'" alt="Chinese ceremonial and bridal styling"></figure>',
    'ceremonial image',
)
replace_once(
    '<section class="section" id="tea"><div class="shell tea-grid"><figure><img src="assets/images/dynasty-song.webp" alt="Song-inspired Hanfu in a scholarly interior"></figure>',
    '<section class="section" id="tea"><div class="shell tea-grid"><figure><img src="assets/images/dynasty-song.avif" onerror="this.onerror=null;this.src=\'assets/images/tea.webp\'" alt="Chinese tea experience in a refined Hanfu setting"></figure>',
    'tea image',
)
replace_once(
    '<section class="section" id="coming"><div class="shell coming-grid"><figure><img src="assets/images/dynasty-han.webp" alt="Han-inspired cultural atmosphere"></figure>',
    '<section class="section" id="coming"><div class="shell coming-grid"><figure><img src="assets/images/dynasty-han.avif" onerror="this.onerror=null;this.src=\'assets/images/dynasty-han.webp\'" alt="Chinese cultural atmosphere"></figure>',
    'coming image',
)

old_dessert_figure = '<figure><img src="https://haoyyw.github.io/PHDESSERT/assets/products/chinese-tasting-box.webp" alt="PhDessert Chinese tasting box"></figure>'
new_dessert_figure = '<figure class="pastry-gallery" aria-label="PhDessert Chinese pastry tasting selection"><img src="https://haoyyw.github.io/phdessert/assets/products/peach-blossom.webp" alt="Peach blossom pastry"><img src="https://haoyyw.github.io/phdessert/assets/products/osmanthus-cake.webp" alt="Osmanthus cake"><img src="https://haoyyw.github.io/phdessert/assets/products/mung-bean-cake.webp" alt="Mung bean cake"><img src="https://haoyyw.github.io/phdessert/assets/products/rice-cake.webp" alt="Rice cake"></figure>'
replace_once(old_dessert_figure, new_dessert_figure, 'PhDessert image gallery')
s = s.replace('https://haoyyw.github.io/PHDESSERT/', 'https://haoyyw.github.io/phdessert/')

# Dynamic dynasty images and bilingual dynasty title.
s = s.replace("img:'assets/images/dynasty-han.webp'", "img:'assets/images/dynasty-han.avif'")
s = s.replace("img:'assets/images/hero-tang.webp'", "img:'assets/images/dynasty-tang.avif'")
s = s.replace("img:'assets/images/dynasty-song.webp'", "img:'assets/images/dynasty-song.avif'")
s = s.replace("img:'assets/images/dynasty-ming.webp'", "img:'assets/images/dynasty-ming.avif'")
old_dynasty_set = "document.getElementById('dynasty-name').textContent=d.name[i];"
new_dynasty_set = "const dl={han:['HAN','漢'],tang:['TANG','唐'],song:['SONG','宋'],ming:['MING','明']}[k];document.getElementById('dynasty-name').innerHTML=`<span class=\"bilabel dynasty-bilabel\"><span class=\"en\">${dl[0]}</span><span class=\"zh\">${dl[1]}</span></span>`;"
replace_once(old_dynasty_set, new_dynasty_set, 'dynamic dynasty bilingual title')

# Footer bilingual hierarchy.
replace_once(
    '<footer class="footer dark"><div class="shell footer-grid"><div><strong>華裳 · HUASHANG</strong><span>HANFU CULTURE ATELIER</span></div>',
    '<footer class="footer dark"><div class="shell footer-grid"><div><strong class="bilabel"><span class="en">HUASHANG</span><span class="zh">華裳</span></strong><span>HANFU CULTURE ATELIER</span></div>',
    'footer brand',
)

# Release assertions: fail loudly if the expected upgrade is incomplete.
required = [
    'locale-hierarchy-v2',
    'class="bilabel',
    'assets/images/dynasty-han.avif',
    'assets/images/dynasty-tang.avif',
    'assets/images/dynasty-song.avif',
    'assets/images/dynasty-ming.avif',
    'assets/images/styling.avif',
    'assets/images/jewellery.avif',
    'assets/images/ceremonial.avif',
    'https://haoyyw.github.io/phdessert/',
    'peach-blossom.webp',
    'osmanthus-cake.webp',
    'mung-bean-cake.webp',
    'rice-cake.webp',
]
for token in required:
    if token not in s:
        raise SystemExit(f'upgrade assertion failed: {token}')
if 'https://haoyyw.github.io/PHDESSERT/' in s:
    raise SystemExit('uppercase PhDessert Pages path remains')

p.write_text(s, encoding='utf-8')
print('site upgrade applied and assertions passed')
