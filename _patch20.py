p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# 去掉固定height和overflow，改用min-height让内容自然撑开
old = """.care-label .half-top{height:90px;display:flex;flex-direction:column;justify-content:center;padding:6px 8px;overflow:hidden}
.care-label .half-bot{height:90px;display:flex;flex-direction:column;justify-content:center;padding:6px 8px;overflow:hidden}"""
new = """.care-label .half-top{min-height:100px;display:flex;flex-direction:column;justify-content:center;padding:8px}
.care-label .half-bot{min-height:100px;display:flex;flex-direction:column;justify-content:center;padding:8px}"""
s = s.replace(old, new)

old2 = """.tpl-b .half-top,.tpl-b .half-bot{height:110px;display:flex;flex-direction:column;justify-content:center;padding:6px 10px;overflow:hidden}"""
new2 = """.tpl-b .half-top,.tpl-b .half-bot{min-height:120px;display:flex;flex-direction:column;justify-content:center;padding:8px 10px}"""
s = s.replace(old2, new2)

open(p, 'w', encoding='utf-8').write(s)
print('done')
