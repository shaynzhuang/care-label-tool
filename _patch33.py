p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

s = s.replace('.tpl-b .care-text-b{font-style:italic;font-size:11.5px;white-space:pre-line;margin-bottom:10px;line-height:1.4}', '.tpl-b .care-text-b{font-style:italic;font-size:11.5px;margin-bottom:10px;line-height:1.4;text-align:center}')

open(p, 'w', encoding='utf-8').write(s)
print('done')
