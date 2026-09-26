p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# 修改模板C：加三语（EN/FR/ES）
old = "h+='<div class=\"care-label tpl-c\" style=\"width:'+w+'mm;font-size:'+(10.5*sc)+'px;\"><div class=\"brand-logo\">ANDY & EVAN&reg;</div><div class=\"lang-block\"><div class=\"comp\">'+comp+'</div><div class=\"care-text\">'+care+'</div></div><div class=\"origin\">'+$('origin').value+'</div><div class=\"rn\">RN#'+$('rn').value+'</div><div class=\"ys\">'+trackingLine()+'</div></div>';"

new = """const careEn=careArr;
  const frMap={'MACHINE WASH COLD WITH LIKE COLORS GENTLE CYCLE.':'LAVER A FROID AVEC COULEURS SEMBLABLES. CYCLE DOUX.','DO NOT BLEACH.':'NE PAS JAVELLISER.','TUMBLE DRY LOW TEMPERATURE':'SÉCHAGE EN TAMBOUR BASSE TEMPÉRATURE','COOL IRON FROM INSIDE IF NEEDED.':'REPASSER À FROID SUR L'ENVERS SI NÉCESSAIRE.','DO NOT DRY CLEAN.':'NE PAS NETTOYER À SEC.'};
  const esMap={'MACHINE WASH COLD WITH LIKE COLORS GENTLE CYCLE.':'LAVAR A MAQUINA FRIO CON COLORES SIMILARES. CICLO SUAVE.','DO NOT BLEACH.':'NO USAR CLORO.','TUMBLE DRY LOW TEMPERATURE':'SECADORA A TEMPERATURA BAJA','COOL IRON FROM INSIDE IF NEEDED.':'PLANCHAR FRIO POR DENTRO SI ES NECESARIO.','DO NOT DRY CLEAN.':'NO LIMPIAR EN SECO.'};
  const careFr=careEn.map(x=>frMap[x]||x);
  const careEs=careEn.map(x=>esMap[x]||x);
  const careTrilingual=careEn.join('<br>')+'<br><span style="font-style:italic">'+careFr.join('<br>')+'</span><br><span style="font-style:italic">'+careEs.join('<br>')+'</span>';
      h+='<div class="care-label tpl-c" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;"><div class="brand-logo">ANDY & EVAN&reg;</div><div class="lang-block"><div class="comp">'+comp+'</div><div class="care-text">'+careTrilingual+'</div></div><div class="origin">'+$('origin').value+'</div><div class="rn">RN#'+$('rn').value+'</div><div class="ys">'+trackingLine()+'</div></div>';"""

s = s.replace(old, new)

open(p, 'w', encoding='utf-8').write(s)
print('done')
