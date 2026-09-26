p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# 恢复flex:1让上下等高，去掉min-height
s = s.replace('.tpl-b .half-top{min-height:170px;display:flex;flex-direction:column;justify-content:center;padding:6px 10px}', '.tpl-b .half-top{flex:1;display:flex;flex-direction:column;justify-content:center;padding:6px 10px}')
s = s.replace('.tpl-b .half-bot{min-height:170px;display:flex;flex-direction:column;justify-content:center;padding:6px 10px}', '.tpl-b .half-bot{flex:1;display:flex;flex-direction:column;justify-content:center;padding:6px 10px}')
s = s.replace('.care-label .half-top{min-height:150px;display:flex;flex-direction:column;justify-content:center;padding:6px 8px}', '.care-label .half-top{flex:1;display:flex;flex-direction:column;justify-content:center;padding:6px 8px}')
s = s.replace('.care-label .half-bot{min-height:150px;display:flex;flex-direction:column;justify-content:center;padding:6px 8px}', '.care-label .half-bot{flex:1;display:flex;flex-direction:column;justify-content:center;padding:6px 8px}')

# 底部tail不要太大
s = s.replace('.tpl-b .tail{height:22px;flex-shrink:0}', '.tpl-b .tail{height:18px;flex-shrink:0}')

open(p, 'w', encoding='utf-8').write(s)
print('done')
