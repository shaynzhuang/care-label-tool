p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# 重写CSS：折痕区有高度，上下内容区等高
old_css = """.care-label{background:#fff;font-family:Arial,sans-serif;color:#000;text-align:center;font-size:10.5px;line-height:1.45;display:flex;flex-direction:column}
.care-label .half-top{min-height:150px;display:flex;flex-direction:column;justify-content:center;padding:8px;line-height:1.4}
.care-label .half-bot{min-height:150px;display:flex;flex-direction:column;justify-content:center;padding:8px;line-height:1.4}
.care-label .fold{border-top:1px dashed #999;flex-shrink:0}
.care-label .edge{border-left:1px solid #333;border-right:1px solid #333}"""

new_css = """.care-label{background:#fff;font-family:Arial,sans-serif;color:#000;text-align:center;font-size:10.5px;line-height:1.45;display:flex;flex-direction:column}
.care-label .tail{height:22px;flex-shrink:0}
.care-label .half-top{flex:1;display:flex;flex-direction:column;justify-content:center;padding:6px 8px}
.care-label .half-bot{flex:1;display:flex;flex-direction:column;justify-content:center;padding:6px 8px}
.care-label .fold{border-top:1px dashed #999;flex-shrink:0}
.care-label .edge{border-left:1px solid #333;border-right:1px solid #333}"""

s = s.replace(old_css, new_css)

# EdgeHill CSS
old_b = """.tpl-b{font-family:Georgia,serif;border:2px solid #3399cc}
.tpl-b .fold{border-top:2px dashed #3399cc;flex-shrink:0}
.tpl-b .half-top{min-height:180px;display:flex;flex-direction:column;justify-content:center;padding:8px 10px;line-height:1.4}
.tpl-b .half-bot{min-height:180px;display:flex;flex-direction:column;justify-content:center;padding:8px 10px;line-height:1.4}"""

new_b = """.tpl-b{font-family:Georgia,serif;border:2px solid #3399cc}
.tpl-b .fold{border-top:2px dashed #3399cc;flex-shrink:0}
.tpl-b .tail{height:22px;flex-shrink:0}
.tpl-b .half-top{flex:1;display:flex;flex-direction:column;justify-content:center;padding:6px 10px}
.tpl-b .half-bot{flex:1;display:flex;flex-direction:column;justify-content:center;padding:6px 10px}"""

s = s.replace(old_b, new_b)

open(p, 'w', encoding='utf-8').write(s)
print('css done')
