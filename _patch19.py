p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# EdgeHill: 上下两半固定等高
old = """.tpl-b{font-family:Georgia,serif;border:2px solid #3399cc}
.tpl-b .fold{border-top:2px dashed #3399cc;flex-shrink:0}
.tpl-b .half-top,.tpl-b .half-bot{flex:1;min-height:80px;display:flex;flex-direction:column;justify-content:center;padding:8px 10px}"""

new = """.tpl-b{font-family:Georgia,serif;border:2px solid #3399cc}
.tpl-b .fold{border-top:2px dashed #3399cc;flex-shrink:0}
.tpl-b .half-top,.tpl-b .half-bot{height:110px;display:flex;flex-direction:column;justify-content:center;padding:6px 10px;overflow:hidden}"""

s = s.replace(old, new)

# 同样给模板A上下两半固定高度
old2 = """.care-label .half-top{flex:1;display:flex;flex-direction:column;justify-content:center;padding:10px 8px}
.care-label .half-bot{flex:1;display:flex;flex-direction:column;justify-content:center;padding:10px 8px}"""
new2 = """.care-label .half-top{height:90px;display:flex;flex-direction:column;justify-content:center;padding:6px 8px;overflow:hidden}
.care-label .half-bot{height:90px;display:flex;flex-direction:column;justify-content:center;padding:6px 8px;overflow:hidden}"""
s = s.replace(old2, new2)

open(p, 'w', encoding='utf-8').write(s)
print('done')
