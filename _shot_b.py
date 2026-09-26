import subprocess, os
# 用URL参数自动选EdgeHill模板，截图
html = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\水洗标生成器.html'
# 临时改：页面加载后自动选EdgeHill
s = open(html, encoding='utf-8').read()
# 在render前加自动选择
inject = """
window.addEventListener('load',function(){
  var sel=document.getElementById('tpl');
  if(sel){sel.value='b';render();}
});
"""
if inject not in s:
    s = s.replace('</script>', inject + '</script>')
    open(html, 'w', encoding='utf-8').write(s)
print('injected')
