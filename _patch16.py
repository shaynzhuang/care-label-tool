p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# 重写render函数中模板A和B的部分
old = """    if(tpl==='b'){
      h+='<div class="care-label tpl-b" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;"><div class="rule-b"></div><div class="comp-b">'+comp+'</div>';
      if(dec)h+='<div class="decor-b">Exclusive<br>of Decoration</div>';
      h+='<div class="origin-b">'+$('origin').value+'</div><div class="rule-b"></div><div class="care-text-b">'+care+'</div><div class="style-b">Style # '+styleNo+'</div><div class="rn-b">RN'+$('rn').value+'</div><div class="ys-b">'+trackingLine()+'</div><div class="rule-b"></div></div>';
    }else if(tpl==='c'){
      const careEn=careArr;
  const frMap={'MACHINE WASH COLD WITH LIKE COLORS GENTLE CYCLE.':'LAVER A FROID AVEC COULEURS SEMBLABLES. CYCLE DOUX.','DO NOT BLEACH.':'NE PAS JAVELLISER.','TUMBLE DRY LOW TEMPERATURE':'SÉCHAGE EN TAMBOUR BASSE TEMPÉRATURE','COOL IRON FROM INSIDE IF NEEDED.':'REPASSER À FROID SUR L\u2019ENVERS SI NÉCESSAIRE.','DO NOT DRY CLEAN.':'NE PAS NETTOYER À SEC.'};
  const esMap={'MACHINE WASH COLD WITH LIKE COLORS GENTLE CYCLE.':'LAVAR A MAQUINA FRIO CON COLORES SIMILARES. CICLO SUAVE.','DO NOT BLEACH.':'NO USAR CLORO.','TUMBLE DRY LOW TEMPERATURE':'SECADORA A TEMPERATURA BAJA','COOL IRON FROM INSIDE IF NEEDED.':'PLANCHAR FRIO POR DENTRO SI ES NECESARIO.','DO NOT DRY CLEAN.':'NO LIMPIAR EN SECO.'};
  const careFr=careEn.map(x=>frMap[x]||x);
  const careEs=careEn.map(x=>esMap[x]||x);
  const careTrilingual=careEn.join('<br>')+'<br><span style="font-style:italic">'+careFr.join('<br>')+'</span><br><span style="font-style:italic">'+careEs.join('<br>')+'</span>';
      h+='<div class="care-label tpl-c" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;"><div class="brand-logo">ANDY & EVAN&reg;</div><div class="lang-block"><div class="comp">'+comp+'</div><div class="care-text">'+careTrilingual+'</div></div><div class="origin">'+$('origin').value+'</div><div class="rn">RN#'+$('rn').value+'</div><div class="ys">'+trackingLine()+'</div></div>';
    }else{
      h+='<div class="care-label" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;"><div class="comp">'+comp+'</div><div class="origin">'+$('origin').value+'</div><div class="rn">RN#'+$('rn').value+'</div><div class="ys">'+trackingLine()+'</div><div class="care-text">'+care+'</div>';
      if(tpl==='a_sym')h+='<div class="symbols">'+symbolsFor()+'</div>';
      h+='<div class="style">STYLE '+styleNo+'</div>';
      if(qty)h+='<div class="qty">'+qty+'</div>';
      h+='</div>';
    }"""

new = """    if(tpl==='b'){
      // EdgeHill: top half = comp+decor+origin, bottom half = care+style+rn+ys
      h+='<div class="care-label tpl-b" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;">';
      h+='<div class="half-top"><div class="comp-b">'+comp+'</div>';
      if(dec)h+='<div class="decor-b">Exclusive<br>of Decoration</div>';
      h+='<div class="origin-b">'+$('origin').value+'</div></div>';
      h+='<div class="fold"></div>';
      h+='<div class="half-bot"><div class="care-text-b">'+care+'</div><div class="style-b">Style # '+styleNo+'</div><div class="rn-b">RN'+$('rn').value+'</div><div class="ys-b">'+trackingLine()+'</div></div>';
      h+='<div class="fold"></div>';
      h+='</div>';
    }else if(tpl==='c'){
      // ANDY & EVAN: label1 = EN+FR, label2 = ES+importer
      h+='<div class="care-label tpl-c" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;">';
      h+='<div class="brand-logo">ANDY & EVAN&reg;</div>';
      h+='<div class="lang-block"><div class="comp">'+comp+'</div><div class="care-text">'+careArr.join('<br>')+'</div><div class="sym-row">&#x2647; &#x25B3; &#9673; &#9735; &#9672;</div><div class="origin">'+$('origin').value+'</div><div class="rn">RN#'+$('rn').value+'</div><div class="ys">'+trackingLine()+'</div></div>';
      h+='<div class="lang-block"><div class="comp">100% Coton</div><div class="care-text">Lavage en machine max. 30°C. Laver avec des couleurs similaires.<br>Cycle doux.<br>Pas de blanchiment.<br>Séchage en tambour autorisé, température modérée 60°C.<br>Repasser au froid de l\u2019intérieur si nécessaire.<br>Pas d\u2019entretien professionnel à sec.</div><div class="origin">Fabriqué en Chine</div><div class="rn">WPL 11590<br>David Peyser Sportswear<br>90 Spence Street<br>Bayshore, NY 11706<br>USA</div></div>';
      h+='</div>';
      h+='<div class="care-label tpl-c" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;margin-top:6px;">';
      h+='<div class="lang-block"><div class="comp">100% Algodón</div><div class="care-text">Temperatura máxima de lavado 30°C.<br>Lavar con colores similares.<br>Proceso muy suave.<br>No usar lejía.<br>Posible uso de secadora a temperatura baja, máxima temperatura de escape 60°C.<br>Hierro frío desde el interior si es necesario.<br>No limpiar en seco.</div><div class="origin">Hecho en China</div></div>';
      h+='<div class="lang-block"><div class="importer">IMPORTADO POR:<br>IMPORTADORA PRIMEX<br>S.A. DE C.V.<br>BLVD. MAGNOCENTRO<br>NO. 4 SAN FERNANDO<br>LA HERRADURA<br>HUIXQUILUCAN,<br>ESTADO DE MEXICO<br>C.P. 52765<br>RFC: IPR-903070-S70</div></div>';
      h+='</div>';
    }else{
      // ADV/CC/SH: top half = comp+origin+rn+ys, bottom half = care+[symbols]+style
      h+='<div class="care-label edge" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;">';
      h+='<div class="half-top"><div class="comp">'+comp+'</div><div class="origin">'+$('origin').value+'</div><div class="rn">RN#'+$('rn').value+'</div><div class="ys">'+trackingLine()+'</div></div>';
      h+='<div class="fold"></div>';
      h+='<div class="half-bot"><div class="care-text">'+care+'</div>';
      if(tpl==='a_sym')h+='<div class="symbols">'+symbolsFor()+'</div>';
      h+='<div class="style">STYLE '+styleNo+'</div></div>';
      h+='<div class="fold"></div>';
      if(qty)h+='<div class="qty">'+qty+'</div>';
      h+='</div>';
    }"""

s = s.replace(old, new)
open(p, 'w', encoding='utf-8').write(s)
print('render done')
