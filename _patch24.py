p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# 上下两半用min-height保证最小高度，内容居中，内容多的自然撑开
old = """.care-label .half-top{flex:1;display:flex;flex-direction:column;justify-content:center;padding:8px}
.care-label .half-bot{flex:1;display:flex;flex-direction:column;justify-content:center;padding:8px}"""
new = """.care-label .half-top{min-height:110px;display:flex;flex-direction:column;justify-content:center;padding:8px;line-height:1.5}
.care-label .half-bot{min-height:130px;display:flex;flex-direction:column;justify-content:center;padding:8px;line-height:1.5}"""
s = s.replace(old, new)

old2 = """.tpl-b .half-top,.tpl-b .half-bot{flex:1;display:flex;flex-direction:column;justify-content:center;padding:8px 10px}"""
new2 = """.tpl-b .half-top{min-height:110px;display:flex;flex-direction:column;justify-content:center;padding:8px 10px;line-height:1.5}
.tpl-b .half-bot{min-height:130px;display:flex;flex-direction:column;justify-content:center;padding:8px 10px;line-height:1.5}"""
s = s.replace(old2, new2)

open(p, 'w', encoding='utf-8').write(s)
print('done')
