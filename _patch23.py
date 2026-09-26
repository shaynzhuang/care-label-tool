p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# 不裁切，加大高度
s = s.replace('.care-label .half-top{height:110px;display:flex;flex-direction:column;justify-content:center;padding:6px 8px;overflow:hidden}', '.care-label .half-top{flex:1;display:flex;flex-direction:column;justify-content:center;padding:8px}')
s = s.replace('.care-label .half-bot{height:110px;display:flex;flex-direction:column;justify-content:center;padding:6px 8px;overflow:hidden}', '.care-label .half-bot{flex:1;display:flex;flex-direction:column;justify-content:center;padding:8px}')
s = s.replace('.tpl-b .half-top,.tpl-b .half-bot{height:130px;display:flex;flex-direction:column;justify-content:center;padding:6px 10px;overflow:hidden}', '.tpl-b .half-top,.tpl-b .half-bot{flex:1;display:flex;flex-direction:column;justify-content:center;padding:8px 10px}')

open(p, 'w', encoding='utf-8').write(s)
print('done')
