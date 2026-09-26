p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()
s = s.replace('.care-label .edge{border-left:1px solid #333;border-right:1px solid #333}', '.care-label.edge{border-left:1px solid #333;border-right:1px solid #333}')
open(p, 'w', encoding='utf-8').write(s)
print('done')
