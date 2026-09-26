p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

old = "const comp=$('composition').value,care=[$('wash').value,$('bleach').value,$('dry').value,$('iron').value,$('dryclean').value].join('<br>');"
new = "let careArr=[$('wash').value,$('bleach').value,$('dry').value,$('iron').value,$('dryclean').value];if(tpl==='a_adv'||tpl==='a_sym')careArr=careArr.map(x=>x.toUpperCase());const comp=$('composition').value,care=careArr.join('<br>');"
s = s.replace(old, new)

open(p, 'w', encoding='utf-8').write(s)
print('done')
