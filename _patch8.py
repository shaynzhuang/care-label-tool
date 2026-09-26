p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# 统一下拉选项为句首大写（sentence case）
old = '''        <option selected>MACHINE WASH COLD WITH LIKE COLORS GENTLE CYCLE.</option>
        <option>Mild Process (30-50°C)</option>
        <option>Normal Process (30-60°C)</option>
        <option>Very mild process (40°C)</option>'''
new = '''        <option selected>Machine wash cold with like colors. Gentle cycle.</option>
        <option>Mild process (30-50°C)</option>
        <option>Normal process (30-60°C)</option>
        <option>Very mild process (40°C)</option>'''
s = s.replace(old, new)

old = '''        <option selected>Do not bleach.</option>
        <option>Only Oxygen / non-chlorine bleach allowed</option>
        <option>Any bleaching agent allowed</option>'''
new = '''        <option selected>Do not bleach.</option>
        <option>Only non-chlorine bleach when needed.</option>
        <option>Any bleaching agent allowed</option>'''
s = s.replace(old, new)

old = '''        <option selected>Tumble dry low temperature</option>
        <option>Tumble dry normal temperature</option>
        <option>Do not tumble dry</option>
        <option>Line drying</option>
        <option>Flat drying</option>'''
new = '''        <option selected>Tumble dry low temperature</option>
        <option>Tumble dry normal temperature</option>
        <option>Do not tumble dry</option>
        <option>Line drying</option>
        <option>Flat drying</option>'''
s = s.replace(old, new)

old = '''        <option selected>Cool Iron from inside if needed</option>
        <option>Cool Iron from inside if needed</option>
        <option>Iron at medium temperature (max 150°C)</option>
        <option>Iron at high temperature (max 200°C)</option>
        <option>Do not iron</option>'''
new = '''        <option selected>Cool iron from inside if needed.</option>
        <option>Iron at medium temperature (max 150°C)</option>
        <option>Iron at high temperature (max 200°C)</option>
        <option>Do not iron</option>'''
s = s.replace(old, new)

old = '''        <option selected>Do not dry clean</option>
        <option>Professional dry cleaning mild process</option>
        <option>Professional dry cleaning normal process</option>
        <option>Do not wet clean</option>'''
new = '''        <option selected>Do not dry clean.</option>
        <option>Professional dry cleaning mild process</option>
        <option>Professional dry cleaning normal process</option>
        <option>Do not wet clean.</option>'''
s = s.replace(old, new)

open(p, 'w', encoding='utf-8').write(s)
print('done')
