p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\批复-0921.html'
s = open(p, encoding='utf-8').read()
s = s.replace('Machine wash cold with like colors. Gentle cycle.', 'MACHINE WASH COLD WITH LIKE COLORS GENTLE CYCLE.')
open(p, 'w', encoding='utf-8').write(s)
print('done')
