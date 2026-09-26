p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# 1. 更新CSS
old_css = """.tpl-c .brand-logo{font-family:Georgia,serif;font-size:10px;font-weight:bold;margin-bottom:5px}
.tpl-c .lang-block{margin-bottom:6px;padding-bottom:5px;border-bottom:1px dashed #e88ba8}
.tpl-c .comp{font-size:9px!important}
.tpl-c .care-text{font-size:8.5px!important;line-height:1.35}"""

new_css = """.tpl-c{font-family:Georgia,serif!important;border:1.5px solid #e88ba8;padding:6px 8px!important;text-align:center}
.tpl-c .brand-logo{font-family:Georgia,serif;font-size:11px;font-weight:bold;margin-bottom:6px;letter-spacing:0.5px}
.tpl-c .lang-block{margin-bottom:6px;padding-bottom:6px;border-bottom:1.5px dashed #e88ba8}
.tpl-c .lang-block:last-of-type{border-bottom:none;margin-bottom:0;padding-bottom:0}
.tpl-c .comp{font-size:9px!important;margin-bottom:4px}
.tpl-c .care-text{font-size:8.5px!important;line-height:1.4}
.tpl-c .sym-row{font-size:9px;margin:4px 0;line-height:1}
.tpl-c .origin{font-size:8.5px!important;margin:3px 0}
.tpl-c .rn{font-size:8.5px!important;margin:2px 0}
.tpl-c .ys{font-size:8px!important;margin:2px 0 4px}
.tpl-c .importer{font-size:8px!important;line-height:1.3;margin-top:4px}"""

s = s.replace(old_css, new_css)

# 2. 重写render逻辑
old_render = """const careEn=careArr;
  const frMap={'MACHINE WASH COLD WITH LIKE COLORS GENTLE CYCLE.':'LAVER A FROID AVEC COULEURS SEMBLABLES. CYCLE DOUX.','DO NOT BLEACH.':'NE PAS JAVELLISER.','TUMBLE DRY LOW TEMPERATURE':'SÉCHAGE EN TAMBOUR BASSE TEMPÉRATURE','COOL IRON FROM INSIDE IF NÉCESSAIRE.':'REPASSER À FROID SUR L\u2019ENVERS SI NÉCESSAIRE.','DO NOT DRY CLEAN.':'NE PAS NETTOYER À SEC.'};
  const esMap={'MACHINE WASH COLD WITH LIKE COLORS GENTLE CYCLE.':'LAVAR A MAQUINA FRIO CON COLORES SIMILARES. CICLO SUAVE.','DO NOT BLEACH.':'NO USAR CLORO.','TUMBLE DRY LOW TEMPERATURE':'SECADORA A TEMPERATURA BAJA','COOL IRON FROM INSIDE IF NEEDED.':'PLANCHAR FRIO POR DENTRO SI ES NECESARIO.','DO NOT DRY CLEAN.':'NO LIMPIAR EN SECO.'};
  const careFr=careEn.map(x=>frMap[x]||x);
  const careEs=careEn.map(x=>esMap[x]||x);
  const careTrilingual=careEn.join('<br>')+'<br><span style="font-style:italic">'+careFr.join('<br>')+'</span><br><span style="font-style:italic">'+careEs.join('<br>')+'</span>';
      h+='<div class="care-label tpl-c" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;"><div class="brand-logo">ANDY & EVAN&reg;</div><div class="lang-block"><div class="comp">'+comp+'</div><div class="care-text">'+careTrilingual+'</div></div><div class="origin">'+$('origin').value+'</div><div class="rn">RN#'+$('rn').value+'</div><div class="ys">'+trackingLine()+'</div></div>';"""

new_render = """// ANDY & EVAN trilingual: EN block + FR block + ES block
      const symIcons={wash:'&#x2647;',bleach:'&#x25B3;',dry:'&#9673;',iron:'&#9735;',dryclean:'&#9672;'};
      // EN block
      h+='<div class="care-label tpl-c" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;">';
      h+='<div class="brand-logo">ANDY & EVAN&reg;</div>';
      h+='<div class="lang-block">';
      h+='<div class="comp">'+comp+'</div>';
      h+='<div class="care-text">'+careArr.join('<br>')+'</div>';
      h+='<div class="sym-row">&#x2647; &#x25B3; &#9673; &#9735; &#9672;</div>';
      h+='<div class="origin">'+$('origin').value+'</div>';
      h+='<div class="rn">RN#'+$('rn').value+'</div>';
      h+='<div class="ys">'+trackingLine()+'</div>';
      h+='</div>';
      // FR block
      h+='<div class="lang-block">';
      h+='<div class="comp">100% Coton</div>';
      h+='<div class="care-text">Lavage en machine max. 30°C. Laver avec des couleurs similaires.<br>Cycle doux.<br>Pas de blanchiment.<br>Séchage en tambour autorisé, température modérée 60°C.<br>Repasser au froid de l\u2019intérieur si nécessaire.<br>Pas d\u2019entretien professionnel à sec.</div>';
      h+='<div class="origin">Fabriqué en Chine</div>';
      h+='<div class="rn">WPL 11590</div>';
      h+='</div>';
      // ES block
      h+='<div class="lang-block">';
      h+='<div class="comp">100% Algodón</div>';
      h+='<div class="care-text">Temperatura máxima de lavado 30°C.<br>Lavar con colores similares.<br>Proceso muy suave.<br>No usar lejía.<br>Posible uso de secadora a temperatura baja, máxima temperatura de escape 60°C.<br>Hierro frío desde el interior si es necesario.<br>No limpiar en seco.</div>';
      h+='<div class="origin">Hecho en China</div>';
      h+='<div class="importer">IMPORTADO POR:<br>IMPORTADORA PRIMEX<br>S.A. DE C.V.<br>BLVD. MAGNOCENTRO<br>NO. 4 SAN FERNANDO<br>LA HERRADURA<br>HUIXQUILUCAN,<br>ESTADO DE MEXICO<br>C.P. 52765<br>RFC: IPR-903070-S70</div>';
      h+='</div>';
      h+='</div>';"""

s = s.replace(old_render, new_render)

open(p, 'w', encoding='utf-8').write(s)
print('done')
