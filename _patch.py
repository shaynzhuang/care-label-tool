p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# 1. bleachX: 实心黑三角+X
old_bleach = '<path d="M20 9 L34 32 L6 32 Z"/><line x1="6" y1="6" x2="34" y2="34"/><line x1="34" y1="6" x2="6" y2="34"/></svg>'
new_bleach = '<path d="M20 9 L34 32 L6 32 Z" fill="#000"/><line x1="6" y1="6" x2="34" y2="34"/><line x1="34" y1="6" x2="6" y2="34"/></svg>'
s = s.replace(old_bleach, new_bleach, 1)

# 2. 默认烘干选项改为实物标签写法
s = s.replace('<option selected>Tumble dry low temperature (60°C)</option>', '<option selected>Tumble dry low temperature</option>')
s = s.replace('<option>Tumble dry normal temperature (80°C)</option>', '<option>Tumble dry normal temperature</option>')

# 3. 洗涤默认选项
s = s.replace('<option selected>Machine wash cold with like colors. Gentle cycle.</option>', '<option selected>MACHINE WASH COLD SEPARATELY</option>')

# 4. 熨烫默认
s = s.replace('<option selected>Iron at low temperature (max 110°C)</option>', '<option selected>Cool Iron from inside if needed</option>')

open(p, 'w', encoding='utf-8').write(s)
print('done')
