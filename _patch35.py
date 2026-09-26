p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# 统一EdgeHill字号和行高，解决基线不齐
s = s.replace('.tpl-b .comp-b{font-style:italic;font-size:13px;margin-bottom:14px}', '.tpl-b .comp-b{font-style:italic;font-size:12px;margin-bottom:12px;line-height:1.4}')
s = s.replace('.tpl-b .decor-b{font-style:italic;font-size:12.5px;margin-bottom:14px;line-height:1.3}', '.tpl-b .decor-b{font-style:italic;font-size:12px;margin-bottom:12px;line-height:1.4}')
s = s.replace('.tpl-b .origin-b{font-style:italic;font-size:13px;margin-bottom:10px}', '.tpl-b .origin-b{font-style:italic;font-size:12px;margin-bottom:10px;line-height:1.4}')
s = s.replace('.tpl-b .care-text-b{font-style:italic;font-size:11.5px;margin-bottom:10px;line-height:1.4;text-align:center}', '.tpl-b .care-text-b{font-style:italic;font-size:12px;margin-bottom:10px;line-height:1.4;text-align:center}')
s = s.replace('.tpl-b .style-b{font-style:italic;font-size:12px;margin-bottom:8px}', '.tpl-b .style-b{font-style:italic;font-size:12px;margin-bottom:8px;line-height:1.4}')
s = s.replace('.tpl-b .rn-b,.tpl-b .ys-b{font-weight:bold;font-style:italic;font-size:12px;text-align:center}', '.tpl-b .rn-b,.tpl-b .ys-b{font-weight:bold;font-style:italic;font-size:12px;text-align:center;line-height:1.4}')

open(p, 'w', encoding='utf-8').write(s)
print('done')
