p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# 重写CSS：模板A/B用上下等大对折结构
old_css = """.care-label{background:#fff;border-left:1px solid #333;border-right:1px solid #333;border-top:1px dashed #999;border-bottom:1px dashed #999;padding:14px 10px;font-family:Arial,sans-serif;color:#000;text-align:center;font-size:10.5px;line-height:1.45}
.care-label .comp{font-weight:bold;font-size:11px;margin-bottom:6px;white-space:pre-line}
.care-label .origin{margin:5px 0}.care-label .rn{font-size:10px}.care-label .ys{font-size:10px;margin-bottom:6px}
.care-label .care-text{margin:6px 0;white-space:pre-line}
.care-label .symbols{display:flex;justify-content:center;gap:3px;margin:6px 0}
.care-label .symbols svg{width:20px;height:20px}
.care-label .style{margin-top:6px;font-size:10.5px}
.care-label .qty{color:#e63946;font-size:13px;font-weight:bold;margin-top:8px}
.tpl-b{font-family:Georgia,serif;border:2px solid #3399cc;padding:16px 12px}
.tpl-b .comp-b{font-style:italic;font-size:13px;margin-bottom:16px}
.tpl-b .decor-b{font-style:italic;font-size:12.5px;margin-bottom:16px;line-height:1.3}
.tpl-b .origin-b{font-style:italic;font-size:13px;margin-bottom:14px}
.tpl-b .rule-b{border-top:2px dashed #3399cc;margin:0 -12px 14px}
.tpl-b .care-text-b{font-style:italic;font-size:11.5px;white-space:pre-line;margin-bottom:14px;line-height:1.4}
.tpl-b .style-b{font-style:italic;font-size:12px;margin-bottom:12px}
.tpl-b .rn-b,.tpl-b .ys-b{font-weight:bold;font-size:12px}"""

new_css = """.care-label{background:#fff;font-family:Arial,sans-serif;color:#000;text-align:center;font-size:10.5px;line-height:1.45;display:flex;flex-direction:column}
.care-label .half-top{flex:1;display:flex;flex-direction:column;justify-content:center;padding:10px 8px}
.care-label .half-bot{flex:1;display:flex;flex-direction:column;justify-content:center;padding:10px 8px}
.care-label .fold{border-top:1px dashed #999;flex-shrink:0}
.care-label .edge{border-left:1px solid #333;border-right:1px solid #333}
.care-label .comp{font-weight:bold;font-size:11px;margin-bottom:8px;white-space:pre-line}
.care-label .origin{margin:4px 0}
.care-label .rn{font-size:10px;margin:2px 0}
.care-label .ys{font-size:10px;margin:2px 0}
.care-label .care-text{margin:6px 0;white-space:pre-line}
.care-label .symbols{display:flex;justify-content:center;gap:4px;margin:6px 0}
.care-label .symbols svg{width:20px;height:20px}
.care-label .style{margin-top:6px;font-size:10.5px}
.care-label .qty{color:#e63946;font-size:13px;font-weight:bold;margin:6px 0}
.tpl-b{font-family:Georgia,serif;border:2px solid #3399cc}
.tpl-b .fold{border-top:2px dashed #3399cc}
.tpl-b .comp-b{font-style:italic;font-size:13px;margin-bottom:14px}
.tpl-b .decor-b{font-style:italic;font-size:12.5px;margin-bottom:14px;line-height:1.3}
.tpl-b .origin-b{font-style:italic;font-size:13px;margin-bottom:10px}
.tpl-b .care-text-b{font-style:italic;font-size:11.5px;white-space:pre-line;margin-bottom:10px;line-height:1.4}
.tpl-b .style-b{font-style:italic;font-size:12px;margin-bottom:8px}
.tpl-b .rn-b,.tpl-b .ys-b{font-weight:bold;font-size:12px}"""

s = s.replace(old_css, new_css)

open(p, 'w', encoding='utf-8').write(s)
print('css done')
