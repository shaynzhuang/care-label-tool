p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# EdgeHill上下两半固定等高，内容垂直居中不撑大
old = """.tpl-b .half-top,.tpl-b .half-bot{min-height:120px;display:flex;flex-direction:column;justify-content:center;padding:8px 10px}"""
new = """.tpl-b .half-top,.tpl-b .half-bot{height:130px;display:flex;flex-direction:column;justify-content:center;padding:6px 10px;overflow:hidden}"""
s = s.replace(old, new)

# ADV/CC/SH也固定等高
old2 = """.care-label .half-top{min-height:100px;display:flex;flex-direction:column;justify-content:center;padding:8px}
.care-label .half-bot{min-height:100px;display:flex;flex-direction:column;justify-content:center;padding:8px}"""
new2 = """.care-label .half-top{height:110px;display:flex;flex-direction:column;justify-content:center;padding:6px 8px;overflow:hidden}
.care-label .half-bot{height:110px;display:flex;flex-direction:column;justify-content:center;padding:6px 8px;overflow:hidden}"""
s = s.replace(old2, new2)

open(p, 'w', encoding='utf-8').write(s)
print('done')
