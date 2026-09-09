from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

marker = '/* locale-refinement-v3 */'
if marker not in s:
    anchor = '.footer .bilabel{font-size:24px;line-height:1}'
    if anchor not in s:
        raise SystemExit('missing bilingual CSS anchor')
    refinement = marker + '.hero .hero-brand>span{display:block;margin:0}.footer strong.bilabel{display:flex}.pastry-item .bilabel,.pastry-item .bilabel span{background:none;padding:0}.pastry-item .bilabel span{padding:0}'
    s = s.replace(anchor, anchor + refinement, 1)

required = [
    '.hero .hero-brand>span{display:block;margin:0}',
    '.footer strong.bilabel{display:flex}',
    '.pastry-item .bilabel span{background:none;padding:0}',
]
for token in required:
    if token not in s:
        raise SystemExit(f'locale refinement assertion failed: {token}')

p.write_text(s, encoding='utf-8')
print('locale refinement applied and assertions passed')
