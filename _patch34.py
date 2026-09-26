p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# RN和YS也改成斜体，和其他文字一致
s = s.replace('.tpl-b .rn-b,.tpl-b .ys-b{font-weight:bold;font-size:12px}', '.tpl-b .rn-b,.tpl-b .ys-b{font-weight:bold;font-style:italic;font-size:12px;text-align:center}')

open(p, 'w', encoding='utf-8').write(s)
print('done')
