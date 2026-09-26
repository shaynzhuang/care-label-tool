p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

s = s.replace('.care-label .half-top{height:130px;display:flex;flex-direction:column;justify-content:center;padding:8px;line-height:1.4;overflow:hidden}', '.care-label .half-top{height:150px;display:flex;flex-direction:column;justify-content:center;padding:8px;line-height:1.4;overflow:hidden}')
s = s.replace('.care-label .half-bot{height:130px;display:flex;flex-direction:column;justify-content:center;padding:8px;line-height:1.4;overflow:hidden}', '.care-label .half-bot{height:150px;display:flex;flex-direction:column;justify-content:center;padding:8px;line-height:1.4;overflow:hidden}')
s = s.replace('.tpl-b .half-top{height:160px;display:flex;flex-direction:column;justify-content:center;padding:8px 10px;line-height:1.4;overflow:hidden}', '.tpl-b .half-top{height:180px;display:flex;flex-direction:column;justify-content:center;padding:8px 10px;line-height:1.4;overflow:hidden}')
s = s.replace('.tpl-b .half-bot{height:160px;display:flex;flex-direction:column;justify-content:center;padding:8px 10px;line-height:1.4;overflow:hidden}', '.tpl-b .half-bot{height:180px;display:flex;flex-direction:column;justify-content:center;padding:8px 10px;line-height:1.4;overflow:hidden}')

open(p, 'w', encoding='utf-8').write(s)
print('done')
