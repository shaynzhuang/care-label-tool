p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\批复-0921.html'
s = open(p, encoding='utf-8').read()

# SH标：MACHINE WASH COLD SEPARATELY 改为 Machine wash cold with like colors. Gentle cycle.
# 位置 y=279-296, x=199-248
old_sh = '<rect x="193" y="302" width="60" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>'
new_sh = '<rect x="196" y="278" width="52" height="18" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>'
s = s.replace(old_sh, new_sh)

# 更新SH说明
old_note1 = '5. S64SM821B/J：<b>TUMBLE DRY MEDIUM</b> 与符号（1点=低温）不匹配，改为 <b>TUMBLE DRY LOW TEMPERATURE</b>（与1点符号一致）'
new_note1 = '5. S64SM821B/J：<b>MACHINE WASH COLD SEPARATELY</b> 改为 <b>Machine wash cold with like colors. Gentle cycle.</b>，<br>&nbsp;&nbsp;&nbsp;TUMBLE DRY MEDIUM 改为 <b>TUMBLE DRY LOW TEMPERATURE</b>'
s = s.replace(old_note1, new_note1)

# EdgeHill标：洗涤文字也改成表格写法
# EdgeHill洗涤文字在 y=307-323 附近，6个标x起点 114/218/322/426/530/634
old_eh = '''      <rect x="114" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="218" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="322" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="426" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="530" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="634" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>'''
new_eh = '''      <rect x="112" y="306" width="60" height="18" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="216" y="306" width="60" height="18" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="320" y="306" width="60" height="18" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="424" y="306" width="60" height="18" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="528" y="306" width="60" height="18" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="632" y="306" width="60" height="18" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="114" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="218" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="322" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="426" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="530" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="634" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>'''
s = s.replace(old_eh, new_eh)

old_note2 = '全部6个标：<b>TUMBLE DRYLOW</b>（连写）改为 <b>TUMBLE DRY LOW TEMPERATURE</b>'
new_note2 = '全部6个标：洗涤文字改为 <b>Machine wash cold with like colors. Gentle cycle.</b>，<br>&nbsp;&nbsp;&nbsp;TUMBLE DRYLOW（连写）改为 <b>TUMBLE DRY LOW TEMPERATURE</b>'
s = s.replace(old_note2, new_note2)

open(p, 'w', encoding='utf-8').write(s)
print('done')
