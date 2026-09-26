p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# 上下两半相同min-height，等高，内容居中
s = s.replace('.care-label .half-top{min-height:110px;display:flex;flex-direction:column;justify-content:center;padding:8px;line-height:1.5}', '.care-label .half-top{min-height:130px;display:flex;flex-direction:column;justify-content:center;padding:8px;line-height:1.5}')
s = s.replace('.care-label .half-bot{min-height:130px;display:flex;flex-direction:column;justify-content:center;padding:8px;line-height:1.5}', '.care-label .half-bot{min-height:130px;display:flex;flex-direction:column;justify-content:center;padding:8px;line-height:1.5}')
s = s.replace('.tpl-b .half-top{min-height:110px;display:flex;flex-direction:column;justify-content:center;padding:8px 10px;line-height:1.5}', '.tpl-b .half-top{min-height:140px;display:flex;flex-direction:column;justify-content:center;padding:8px 10px;line-height:1.5}')
s = s.replace('.tpl-b .half-bot{min-height:130px;display:flex;flex-direction:column;justify-content:center;padding:8px 10px;line-height:1.5}', '.tpl-b .half-bot{min-height:140px;display:flex;flex-direction:column;justify-content:center;padding:8px 10px;line-height:1.5}')

open(p, 'w', encoding='utf-8').write(s)
print('done')
