p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# 修复法文撇号转义问题
s = s.replace("REPASSER À FROID SUR L'ENVERS SI NÉCESSAIRE.", "REPASSER À FROID SUR L\u2019ENVERS SI NÉCESSAIRE.")

open(p, 'w', encoding='utf-8').write(s)
print('done')
