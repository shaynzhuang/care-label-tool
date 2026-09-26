p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()
old = "if(tpl==='a_adv'||tpl==='a_sym')careArr=careArr.map(x=>x.toUpperCase())"
new = "if(tpl==='a_adv'||tpl==='a_sym'||tpl==='b')careArr=careArr.map(x=>x.toUpperCase())"
s = s.replace(old, new)
open(p, 'w', encoding='utf-8').write(s)
print('done')
