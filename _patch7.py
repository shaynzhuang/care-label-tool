p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\批复-0921.html'
s = open(p, encoding='utf-8').read()
s = s.replace('S27EC/YS/07/26', 'S27EC/YS/26/07')
s = s.replace('S27SH/YS/07/26', 'S27SH/YS/26/07')
s = s.replace('S27AD/YS/08/26', 'S27AD/YS/26/08')
open(p, 'w', encoding='utf-8').write(s)
print('done')
