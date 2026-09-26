p = r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\_build.py'
s = open(p, encoding='utf-8').read()

# 找到当前模板C的render并替换为两个独立label
old = """// ANDY & EVAN trilingual: EN block + FR block + ES block
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

new = """// ANDY & EVAN: label 1 = EN+FR, label 2 = ES+importer
      // Label 1: EN + FR
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
      h+='<div class="lang-block">';
      h+='<div class="comp">100% Coton</div>';
      h+='<div class="care-text">Lavage en machine max. 30°C. Laver avec des couleurs similaires.<br>Cycle doux.<br>Pas de blanchiment.<br>Séchage en tambour autorisé, température modérée 60°C.<br>Repasser au froid de l\u2019intérieur si nécessaire.<br>Pas d\u2019entretien professionnel à sec.</div>';
      h+='<div class="origin">Fabriqué en Chine</div>';
      h+='<div class="rn">WPL 11590<br>David Peyser Sportswear<br>90 Spence Street<br>Bayshore, NY 11706<br>USA</div>';
      h+='</div>';
      h+='</div>';
      // Label 2: ES + importer
      h+='<div class="care-label tpl-c" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;margin-top:6px;">';
      h+='<div class="lang-block">';
      h+='<div class="comp">100% Algodón</div>';
      h+='<div class="care-text">Temperatura máxima de lavado 30°C.<br>Lavar con colores similares.<br>Proceso muy suave.<br>No usar lejía.<br>Posible uso de secadora a temperatura baja, máxima temperatura de escape 60°C.<br>Hierro frío desde el interior si es necesario.<br>No limpiar en seco.</div>';
      h+='<div class="origin">Hecho en China</div>';
      h+='</div>';
      h+='<div class="lang-block">';
      h+='<div class="importer">IMPORTADO POR:<br>IMPORTADORA PRIMEX<br>S.A. DE C.V.<br>BLVD. MAGNOCENTRO<br>NO. 4 SAN FERNANDO<br>LA HERRADURA<br>HUIXQUILUCAN,<br>ESTADO DE MEXICO<br>C.P. 52765<br>RFC: IPR-903070-S70</div>';
      h+='</div>';
      h+='</div>';"""

s = s.replace(old, new)
open(p, 'w', encoding='utf-8').write(s)
print('done')
