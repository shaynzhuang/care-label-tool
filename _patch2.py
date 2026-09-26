p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\批复-0921.html'
s = open(p, encoding='utf-8').read()

old = '''      <rect x="641" y="382" width="36" height="13" fill="#1a73e8" fill-opacity="0.3" stroke="#1a73e8" stroke-width="1.5" rx="2"/>
    </svg>
  </div>
  <div class="notes">
    全部6个标：<b>YS14/2026</b>（缺月份）改为 <b>S27EC/YS/07/2026</b>
  </div>'''

new = '''      <rect x="641" y="382" width="36" height="13" fill="#1a73e8" fill-opacity="0.3" stroke="#1a73e8" stroke-width="1.5" rx="2"/>
      <rect x="114" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="218" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="322" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="426" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="530" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
      <rect x="634" y="335" width="50" height="11" fill="#e63946" fill-opacity="0.25" stroke="#e63946" stroke-width="1.5" rx="2"/>
    </svg>
  </div>
  <div class="notes">
    全部6个标：<b>YS14/2026</b>（缺月份）改为 <b>S27EC/YS/07/2026</b><br>
    <span style="color:#e63946;">全部6个标：<b>TUMBLE DRYLOW</b>（连写）改为 <b>TUMBLE DRY LOW TEMPERATURE</b></span>
  </div>'''

s = s.replace(old, new)
open(p, 'w', encoding='utf-8').write(s)
print('done')
