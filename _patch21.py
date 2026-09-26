p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# 给ADV/CC/SH加顶部空白折痕区
old = """      h+='<div class="care-label edge" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;">';
      h+='<div class="half-top"><div class="comp">'+comp+'</div><div class="origin">'+$('origin').value+'</div><div class="rn">RN#'+$('rn').value+'</div><div class="ys">'+trackingLine()+'</div></div>';
      h+='<div class="fold"></div>';
      h+='<div class="half-bot"><div class="care-text">'+care+'</div>';
      if(tpl==='a_sym')h+='<div class="symbols">'+symbolsFor()+'</div>';
      h+='<div class="style">STYLE '+styleNo+'</div></div>';
      h+='<div class="fold"></div>';
      if(qty)h+='<div class="qty">'+qty+'</div>';
      h+='</div>';"""

new = """      h+='<div class="care-label edge" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;">';
      h+='<div class="tail" style="height:24px"></div><div class="fold"></div>';
      h+='<div class="half-top"><div class="comp">'+comp+'</div><div class="origin">'+$('origin').value+'</div><div class="rn">RN#'+$('rn').value+'</div><div class="ys">'+trackingLine()+'</div></div>';
      h+='<div class="fold"></div>';
      h+='<div class="half-bot"><div class="care-text">'+care+'</div>';
      if(tpl==='a_sym')h+='<div class="symbols">'+symbolsFor()+'</div>';
      h+='<div class="style">STYLE '+styleNo+'</div></div>';
      h+='<div class="fold"></div>';
      if(qty)h+='<div class="qty">'+qty+'</div>';
      h+='</div>';"""

s = s.replace(old, new)

# EdgeHill也加顶部和底部空白
old_b = """      h+='<div class="care-label tpl-b" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;">';
      h+='<div class="half-top"><div class="comp-b">'+comp+'</div>';
      if(dec)h+='<div class="decor-b">Exclusive<br>of Decoration</div>';
      h+='<div class="origin-b">'+$('origin').value+'</div></div>';
      h+='<div class="fold"></div>';
      h+='<div class="half-bot"><div class="care-text-b">'+care+'</div><div class="style-b">Style # '+styleNo+'</div><div class="rn-b">RN'+$('rn').value+'</div><div class="ys-b">'+trackingLine()+'</div></div>';
      h+='<div class="fold"></div>';
      h+='</div>';"""

new_b = """      h+='<div class="care-label tpl-b" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;">';
      h+='<div class="tail" style="height:20px"></div><div class="fold"></div>';
      h+='<div class="half-top"><div class="comp-b">'+comp+'</div>';
      if(dec)h+='<div class="decor-b">Exclusive<br>of Decoration</div>';
      h+='<div class="origin-b">'+$('origin').value+'</div></div>';
      h+='<div class="fold"></div>';
      h+='<div class="half-bot"><div class="care-text-b">'+care+'</div><div class="style-b">Style # '+styleNo+'</div><div class="rn-b">RN'+$('rn').value+'</div><div class="ys-b">'+trackingLine()+'</div></div>';
      h+='<div class="fold"></div><div class="tail" style="height:20px"></div>';
      h+='</div>';"""

s = s.replace(old_b, new_b)

open(p, 'w', encoding='utf-8').write(s)
print('done')
