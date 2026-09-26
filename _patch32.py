p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# 确保模板三所有元素居中对齐
s = s.replace('.tpl-c .care-text{font-size:8.5px!important;line-height:1.4}', '.tpl-c .care-text{font-size:8.5px!important;line-height:1.4;text-align:center}')
s = s.replace('.tpl-c .importer{font-size:8px!important;line-height:1.3;margin-top:4px}', '.tpl-c .importer{font-size:8px!important;line-height:1.3;margin-top:4px;text-align:center}')

open(p, 'w', encoding='utf-8').write(s)
print('done')
