p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# EdgeHill: 顶部空白 + 上半 + 中间虚线 + 下半 + 底部空白，上下两半等大
old = """.tpl-b{font-family:Georgia,serif;border:2px solid #3399cc}
.tpl-b .fold{border-top:2px dashed #3399cc}"""

new = """.tpl-b{font-family:Georgia,serif;border:2px solid #3399cc}
.tpl-b .fold{border-top:2px dashed #3399cc;flex-shrink:0}
.tpl-b .half-top,.tpl-b .half-bot{flex:1;min-height:80px;display:flex;flex-direction:column;justify-content:center;padding:8px 10px}"""

s = s.replace(old, new)

open(p, 'w', encoding='utf-8').write(s)
print('done')
