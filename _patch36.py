p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# EdgeHill：固定等高，不用flex:1
s = s.replace('.tpl-b .half-top{flex:1;display:flex;flex-direction:column;justify-content:center;padding:6px 10px}', '.tpl-b .half-top{min-height:170px;display:flex;flex-direction:column;justify-content:center;padding:6px 10px}')
s = s.replace('.tpl-b .half-bot{flex:1;display:flex;flex-direction:column;justify-content:center;padding:6px 10px}', '.tpl-b .half-bot{min-height:170px;display:flex;flex-direction:column;justify-content:center;padding:6px 10px}')

# ADV/CC/SH也改
s = s.replace('.care-label .half-top{flex:1;display:flex;flex-direction:column;justify-content:center;padding:6px 8px}', '.care-label .half-top{min-height:150px;display:flex;flex-direction:column;justify-content:center;padding:6px 8px}')
s = s.replace('.care-label .half-bot{flex:1;display:flex;flex-direction:column;justify-content:center;padding:6px 8px}', '.care-label .half-bot{min-height:150px;display:flex;flex-direction:column;justify-content:center;padding:6px 8px}')

open(p, 'w', encoding='utf-8').write(s)
print('done')
