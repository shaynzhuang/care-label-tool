# -*- coding: utf-8 -*-
html = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='10' fill='%23165dff'/%3E%3Cpath d='M18 26 L21 48 L43 48 L46 26 Z' fill='none' stroke='white' stroke-width='3'/%3E%3C/svg%3E">
<title>水洗标生成器 Care Label Generator</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: -apple-system, "Segoe UI", "Microsoft YaHei", sans-serif; background: #f0f2f5; color: #1f2329; }
  .topbar { background: #fff; border-bottom: 1px solid #e5e6eb; padding: 12px 24px; display: flex; align-items: center; justify-content: space-between; position: sticky; top: 0; z-index: 10; }
  .topbar h1 { font-size: 17px; font-weight: 600; }
  .topbar .sub { font-size: 12px; color: #86909c; font-weight: 400; }
  .btn { background: #165dff; color: #fff; border: none; padding: 8px 18px; border-radius: 6px; font-size: 13px; cursor: pointer; }
  .btn.ghost { background: #fff; color: #165dff; border: 1px solid #165dff; margin-right: 8px; }
  .main { display: grid; grid-template-columns: 400px 1fr; gap: 20px; padding: 20px 24px; max-width: 1500px; margin: 0 auto; }
  .panel { background: #fff; border-radius: 8px; padding: 18px; max-height: calc(100vh - 110px); overflow-y: auto; }
  .group { margin-bottom: 16px; }
  .group-title { font-size: 12px; font-weight: 600; color: #86909c; text-transform: uppercase; letter-spacing: .5px; margin-bottom: 8px; padding-bottom: 4px; border-bottom: 1px solid #f0f2f5; }
  label.field { display: block; font-size: 12px; color: #4e5969; margin: 8px 0 3px; }
  input[type=text], select, textarea { width: 100%; padding: 7px 9px; font-size: 13px; border: 1px solid #e5e6eb; border-radius: 5px; }
  textarea { resize: vertical; min-height: 50px; }
  .row2 { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
  .check { display: flex; align-items: center; gap: 6px; font-size: 12px; color: #4e5969; margin-top: 6px; }
  .brand-badge { display: inline-block; background: #e8f3ff; color: #165dff; padding: 3px 10px; border-radius: 4px; font-size: 12px; font-weight: 600; margin-top: 6px; }
  .preview-area { display: flex; justify-content: center; padding: 10px; }
  .label-sheet { background: #fff; padding: 20px; border-radius: 4px; box-shadow: 0 2px 12px rgba(0,0,0,.08); display: flex; gap: 20px; flex-wrap: wrap; justify-content: center; }
  .care-label { background: #fff; border-left: 1px solid #333; border-right: 1px solid #333; border-top: 1px dashed #999; border-bottom: 1px dashed #999; padding: 14px 10px; font-family: Arial, sans-serif; color: #000; text-align: center; font-size: 10.5px; line-height: 1.45; }
  .care-label .comp { font-weight: bold; font-size: 11px; margin-bottom: 6px; white-space: pre-line; }
  .care-label .origin { margin: 5px 0; }
  .care-label .rn { font-size: 10px; }
  .care-label .ys { font-size: 10px; margin-bottom: 6px; }
  .care-label .care-text { margin: 6px 0; white-space: pre-line; }
  .care-label .symbols { display: flex; justify-content: center; gap: 3px; margin: 6px 0; }
  .care-label .symbols svg { width: 20px; height: 20px; }
  .care-label .style { margin-top: 6px; font-size: 10.5px; }
  .care-label .qty { color: #e63946; font-size: 13px; font-weight: bold; margin-top: 8px; }
  .tpl-b { font-family: Georgia, serif; border: 2px solid #3399cc; padding: 16px 12px; }
  .tpl-b .comp-b { font-style: italic; font-size: 13px; margin-bottom: 16px; }
  .tpl-b .decor-b { font-style: italic; font-size: 12.5px; margin-bottom: 16px; line-height: 1.3; }
  .tpl-b .origin-b { font-style: italic; font-size: 13px; margin-bottom: 14px; }
  .tpl-b .rule-b { border-top: 2px dashed #3399cc; margin: 0 -12px 14px; }
  .tpl-b .care-text-b { font-style: italic; font-size: 11.5px; white-space: pre-line; margin-bottom: 14px; line-height: 1.4; }
  .tpl-b .style-b { font-style: italic; font-size: 12px; margin-bottom: 12px; }
  .tpl-b .rn-b, .tpl-b .ys-b { font-weight: bold; font-size: 12px; }
  .tpl-c .brand-logo { font-family: Georgia, serif; font-size: 10px; font-weight: bold; margin-bottom: 5px; }
  .tpl-c .lang-block { margin-bottom: 6px; padding-bottom: 5px; border-bottom: 1px dashed #e88ba8; }
  .tpl-c .comp { font-size: 9px !important; }
  .tpl-c .care-text { font-size: 8.5px !important; line-height: 1.35; }
  .query-panel { max-width: 1500px; margin: 0 auto 20px; padding: 0 24px; }
  .query-panel .panel { max-height: none; }
  .query-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
  .qbox { background: #f7f8fa; padding: 10px; border-radius: 5px; min-height: 40px; font-size: 13px; line-height: 1.8; margin-top: 6px; }
  .chart { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 8px; }
  .chart-item { text-align: center; width: 70px; }
  .chart-item svg { width: 36px; height: 36px; }
  .chart-item span { font-size: 10px; color: #4e5969; }
  @media print { .topbar, .panel, .query-panel { display: none !important; } .main { display: block; padding: 0; } .label-sheet { box-shadow: none; padding: 0; } .care-label { border: none; } @page { size: A4; margin: 8mm; } }
</style>
</head>
<body>
<div class="topbar">
  <div><h1>水洗标生成器 <span class="sub">输入款号自动识别品牌、自动套模板</span></h1></div>
  <div><button class="btn ghost" onclick="resetForm()">清空</button><button class="btn" onclick="window.print()">打印 / 存 PDF</button></div>
</div>
<div class="main">
  <div class="panel">
    <div class="group">
      <div class="group-title">款号（自动识别品牌）</div>
      <label class="field">STYLE 款号</label>
      <input type="text" id="styleNo" value="F64SW840B/J">
      <div id="brandBadge"></div>
      <label class="field">手动覆盖模板</label>
      <select id="templateOverride">
        <option value="auto">自动识别</option>
        <option value="a_adv">模板A：ADV/CC（无符号行）</option>
        <option value="a_sym">模板A-SH：Scene&amp;Heard（有符号行）</option>
        <option value="b">模板B：EdgeHill（衬线斜体蓝框）</option>
        <option value="c">模板C：ANDY &amp; EVAN 三语</option>
      </select>
    </div>
    <div class="group">
      <div class="group-title">成分与产地</div>
      <label class="field">成分（英文，多部位分行写）</label>
      <textarea id="composition">100% COTTON</textarea>
      <button type="button" class="btn ghost" style="margin-top:6px;font-size:12px;padding:5px 12px;" onclick="recommendCare()">根据成分推荐洗护</button>
      <label class="field">产地</label>
      <input type="text" id="origin" value="MADE IN CHINA">
      <div class="row2">
        <div><label class="field">RN #</label><input type="text" id="rn" value="58909"></div>
        <div><label class="field">追踪码日期（月/年）</label><input type="text" id="ys" value="04/2026"></div>
      </div>
      <label class="check"><input type="checkbox" id="decor"> 显示 "EXCLUSIVE OF DECORATION"（EdgeHill）</label>
    </div>
    <div class="group">
      <div class="group-title">洗护指令</div>
      <label class="field">洗涤 Washing</label>
      <select id="wash">
        <option>MACHINE WASH COLD SEPARATELY</option>
        <option>MACHINE WASH COLD WITH LIKE COLORS GENTLE CYCLE</option>
        <option>MACHINE WASH COLD</option>
        <option>HAND WASH COLD</option>
        <option>DO NOT WASH</option>
      </select>
      <label class="field">漂白 Bleaching</label>
      <select id="bleach">
        <option>DO NOT BLEACH</option>
        <option>ONLY NON-CHLORINE BLEACH WHEN NEEDED.</option>
        <option>ANY BLEACHING AGENT ALLOWED</option>
      </select>
      <label class="field">烘干 Drying</label>
      <select id="dry">
        <option>TUMBLE DRY MEDIUM</option>
        <option>TUMBLE DRYLOW</option>
        <option>TUMBLE DRY LOW</option>
        <option>DO NOT TUMBLE DRY</option>
      </select>
      <label class="field">熨烫 Ironing</label>
      <select id="iron">
        <option>COOL IRON FROM INSIDE IF NEEDED.</option>
        <option>COOLIRON IF NEEDED</option>
        <option>DO NOT IRON</option>
      </select>
      <label class="field">干洗 Professional Care</label>
      <select id="dryclean">
        <option>DO NOT DRY CLEAN</option>
        <option>DRY CLEAN</option>
      </select>
    </div>
    <div class="group">
      <div class="group-title">打印设置</div>
      <label class="field">水洗标宽度（mm）</label>
      <input type="text" id="labelWidth" value="35">
      <label class="field">数量（红色标注，留空不显示）</label>
      <input type="text" id="qty" placeholder="如 4250">
      <label class="field">并排条数</label>
      <select id="copies"><option>1</option><option>2</option><option selected>4</option><option>6</option></select>
    </div>
  </div>
  <div class="preview-area"><div class="label-sheet" id="sheet"></div></div>
</div>
<div class="query-panel">
  <div class="panel">
    <div class="group-title" style="font-size:14px;color:#1f2329;">洗护规则查询（来自 S27 HOUSE CARE LABEL RULE）</div>
    <div class="query-grid">
      <div>
        <div style="font-size:12px;font-weight:600;color:#86909c;">成分翻译 EN / FR / ES</div>
        <input type="text" id="qFabric" placeholder="输入英文成分，如 cotton, spandex..." style="margin-top:6px;">
        <div class="qbox" id="qFabricResult">输入后自动显示...</div>
      </div>
      <div>
        <div style="font-size:12px;font-weight:600;color:#86909c;">洗护指令对照 EN / FR / ES + 符号</div>
        <select id="qCare" style="margin-top:6px;"><option value="">-- 选择洗护指令 --</option></select>
        <div class="qbox" id="qCareResult">选择后显示...</div>
      </div>
    </div>
    <div style="margin-top:16px;">
      <div style="font-size:12px;font-weight:600;color:#86909c;">ISO 3758 符号图鉴</div>
      <div class="chart" id="qSymbolChart"></div>
    </div>
  </div>
</div>
<script>
const SYM = {
  wash30: '<svg viewBox="0 0 40 40" fill="none" stroke="#000" stroke-width="2"><path d="M6 13 L9 31 L31 31 L34 13 Z"/><text x="20" y="27" text-anchor="middle" font-size="11" font-family="Arial" stroke="none" fill="#000">30</text></svg>',
  washHand: '<svg viewBox="0 0 40 40" fill="none" stroke="#000" stroke-width="2"><path d="M6 13 L9 31 L31 31 L34 13 Z"/><path d="M10 34 L30 34" stroke-width="1.5"/></svg>',
  washX: '<svg viewBox="0 0 40 40" fill="none" stroke="#000" stroke-width="2"><path d="M6 13 L9 31 L31 31 L34 13 Z"/><line x1="6" y1="6" x2="34" y2="34"/><line x1="34" y1="6" x2="6" y2="34"/></svg>',
  bleachX: '<svg viewBox="0 0 40 40" fill="none" stroke="#000" stroke-width="2"><path d="M20 9 L34 32 L6 32 Z"/><line x1="6" y1="6" x2="34" y2="34"/><line x1="34" y1="6" x2="6" y2="34"/></svg>',
  bleachOxygen: '<svg viewBox="0 0 40 40" fill="none" stroke="#000" stroke-width="2"><path d="M20 9 L34 32 L6 32 Z"/><line x1="12" y1="20" x2="26" y2="30"/><line x1="16" y1="16" x2="30" y2="26"/></svg>',
  bleachAny: '<svg viewBox="0 0 40 40" fill="none" stroke="#000" stroke-width="2"><path d="M20 9 L34 32 L6 32 Z"/></svg>',
  dryLow: '<svg viewBox="0 0 40 40" fill="none" stroke="#000" stroke-width="2"><rect x="6" y="6" width="28" height="28"/><circle cx="20" cy="20" r="7"/><circle cx="20" cy="20" r="2" fill="#000" stroke="none"/></svg>',
  dryMed: '<svg viewBox="0 0 40 40" fill="none" stroke="#000" stroke-width="2"><rect x="6" y="6" width="28" height="28"/><circle cx="20" cy="20" r="7"/><circle cx="17" cy="20" r="1.8" fill="#000"/><circle cx="23" cy="20" r="1.8" fill="#000"/></svg>',
  dryX: '<svg viewBox="0 0 40 40" fill="none" stroke="#000" stroke-width="2"><rect x="6" y="6" width="28" height="28"/><circle cx="20" cy="20" r="7"/><line x1="6" y1="6" x2="34" y2="34"/><line x1="34" y1="6" x2="6" y2="34"/></svg>',
  iron1: '<svg viewBox="0 0 40 40" fill="none" stroke="#000" stroke-width="2"><path d="M7 30 L7 20 Q7 11 16 11 L27 11 L34 21 L34 30 Z"/><circle cx="20" cy="24" r="2" fill="#000" stroke="none"/></svg>',
  ironX: '<svg viewBox="0 0 40 40" fill="none" stroke="#000" stroke-width="2"><path d="M7 30 L7 20 Q7 11 16 11 L27 11 L34 21 L34 30 Z"/><line x1="6" y1="6" x2="34" y2="34"/><line x1="34" y1="6" x2="6" y2="34"/></svg>',
  dc: '<svg viewBox="0 0 40 40" fill="none" stroke="#000" stroke-width="2"><circle cx="20" cy="20" r="13"/></svg>',
  dcX: '<svg viewBox="0 0 40 40" fill="none" stroke="#000" stroke-width="2"><circle cx="20" cy="20" r="13"/><line x1="6" y1="6" x2="34" y2="34"/><line x1="34" y1="6" x2="6" y2="34"/></svg>'
};
function $(id){return document.getElementById(id);}
function detectTemplate(s){s=s.toUpperCase();if(s.startsWith('F64EH')||s.startsWith('S74EH'))return'b';if(s.startsWith('F26'))return'c';if(s.startsWith('F64AW')||s.startsWith('F64SL')||s.startsWith('S74AW'))return'a_adv';if(s.startsWith('F64SW')||s.startsWith('F54SH')||s.startsWith('S64SM'))return'a_sym';return'a_adv';}
function getBrandCode(){const s=$('styleNo').value.toUpperCase();if(s.startsWith('F64SL'))return'S27CC';if(s.startsWith('F64SW')||s.startsWith('S64SM'))return'S27SH';if(s.startsWith('F64AW')||s.startsWith('S74AW'))return'S27AD';if(s.startsWith('F64EH')||s.startsWith('S74EH'))return'S27EC';if(s.startsWith('F26'))return'S27AE';return'S27XX';}
function trackingLine(){return getBrandCode()+'/YS/'+$('ys').value;}
function symbolsFor(){const w=$('wash').value,b=$('bleach').value,d=$('dry').value,i=$('iron').value,dc=$('dryclean').value;let o=[];if(w.includes('DO NOT WASH'))o.push('washX');else if(w.includes('HAND'))o.push('washHand');else o.push('wash30');if(b.includes('DO NOT'))o.push('bleachX');else if(b.includes('NON-CHLORINE'))o.push('bleachOxygen');else o.push('bleachAny');if(d.includes('DO NOT'))o.push('dryX');else if(d.includes('LOW'))o.push('dryLow');else o.push('dryMed');if(i.includes('DO NOT'))o.push('ironX');else o.push('iron1');if(dc.includes('DO NOT'))o.push('dcX');else o.push('dc');return o.map(k=>SYM[k]).join('');}
function render(){
  const tpl=$('templateOverride').value==='auto'?detectTemplate($('styleNo').value):$('templateOverride').value;
  const w=parseFloat($('labelWidth').value)||35,sc=w/35,n=parseInt($('copies').value);
  const comp=$('composition').value,care=[$('wash').value,$('bleach').value,$('dry').value,$('iron').value,$('dryclean').value].join('<br>');
  const styleNo=$('styleNo').value,qty=$('qty').value,dec=$('decor').checked;
  $('brandBadge').innerHTML='<span class="brand-badge">'+({a_adv:'ADV/CC',a_sym:'SH有符号行',b:'EdgeHill',c:'ANDY&EVAN三语'}[tpl])+'</span>';
  let h='';
  for(let c=0;c<n;c++){
    if(tpl==='b'){
      h+='<div class="care-label tpl-b" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;"><div class="rule-b"></div><div class="comp-b">'+comp+'</div>';
      if(dec)h+='<div class="decor-b">Exclusive<br>of Decoration</div>';
      h+='<div class="origin-b">'+$('origin').value+'</div><div class="rule-b"></div><div class="care-text-b">'+care+'</div><div class="style-b">Style # '+styleNo+'</div><div class="rn-b">RN'+$('rn').value+'</div><div class="ys-b">'+trackingLine()+'</div><div class="rule-b"></div></div>';
    }else if(tpl==='c'){
      h+='<div class="care-label tpl-c" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;"><div class="brand-logo">ANDY & EVAN&reg;</div><div class="lang-block"><div class="comp">'+comp+'</div><div class="care-text">'+care+'</div></div><div class="origin">'+$('origin').value+'</div><div class="rn">RN#'+$('rn').value+'</div><div class="ys">'+trackingLine()+'</div></div>';
    }else{
      h+='<div class="care-label" style="width:'+w+'mm;font-size:'+(10.5*sc)+'px;"><div class="comp">'+comp+'</div><div class="origin">'+$('origin').value+'</div><div class="rn">RN#'+$('rn').value+'</div><div class="ys">'+trackingLine()+'</div><div class="care-text">'+care+'</div>';
      if(tpl==='a_sym')h+='<div class="symbols">'+symbolsFor()+'</div>';
      h+='<div class="style">STYLE '+styleNo+'</div>';
      if(qty)h+='<div class="qty">'+qty+'</div>';
      h+='</div>';
    }
  }
  $('sheet').innerHTML=h;
}
function recommendCare(){const c=$('composition').value.toUpperCase();if(c.includes('WOOL')||c.includes('SILK')){$('wash').value='HAND WASH COLD';$('dry').value='DO NOT TUMBLE DRY';}render();}
function resetForm(){document.querySelectorAll('input[type=text],textarea').forEach(e=>e.value='');$('decor').checked=false;render();}
const FABRIC_LOOKUP=[['COTTON','coton','ALGODÓN'],['ELASTANE / SPANDEX','élasthanne','ELASTANO'],['ACRYLIC','acrylique','ACRÍLICO'],['MODAL','modal','MODAL'],['MODACRYLIC','modacrylique','MODACRÍLICO'],['RAYON / VISCOSE','viscose','VISCOSA'],['NYLON / POLYAMIDE','polyamide (nylon)','POLIAMIDA / NAILON'],['POLYESTER','polyester','poliéster'],['POLYURETHANE','polyuréthane','POLIURETANO'],['CASHMERE','cachemire','CACHEMIRA'],['DOWN','duvet','PLUMÓN'],['FEATHER','plumes','PLUMAS'],['LINEN','lin','LINO'],['MOHAIR','mohair','MOHAIR'],['ORGANIC COTTON','coton bio','ALGODÓN ORGÁNICO'],['SILK','soie','SEDA'],['WOOL','laine','LANA']];
const CARE_LOOKUP=[['MACHINE WASH COLD SEPARATELY','Laver à l\'eau froide séparément','30°C por separado','wash30'],['MACHINE WASH COLD WITH LIKE COLORS GENTLE CYCLE','Lavage 30°C couleurs similaires','30°C colores similares','wash30'],['DO NOT WASH','Lavage interdit','No lavar','washX'],['HAND WASH','Lavage à la main','Lavar a mano','washHand'],['DO NOT BLEACH','Pas de blanchiment','No usar lejía','bleachX'],['ONLY NON-CHLORINE BLEACH WHEN NEEDED','Produits oxygénés uniquement','Solo blanqueador sin cloro','bleachOxygen'],['ANY BLEACHING AGENT ALLOWED','Tout agent de blanchiment','Cualquier blanqueador','bleachAny'],['TUMBLE DRY LOW (60°C)','Séchage tambour 60°C','Secadora baja 60°C','dryLow'],['TUMBLE DRY MEDIUM','Séchage température modérée','Secadora media','dryMed'],['DO NOT TUMBLE DRY','Pas de séchage tambour','No secadora','dryX'],['COOL IRON (110°C)','Repasser 110°C','Planchar 110°C','iron1'],['DO NOT IRON','Ne pas repasser','No planchar','ironX'],['DO NOT DRY CLEAN','Pas de nettoyage à sec','No limpiar en seco','dcX'],['DRY CLEAN','Nettoyage à sec','Limpieza en seco','dc']];
$('qFabric').addEventListener('input',function(){const q=this.value.trim().toUpperCase();if(!q){$('qFabricResult').innerHTML='输入后自动显示...';return;}const f=FABRIC_LOOKUP.filter(r=>r[0].includes(q));if(!f.length){$('qFabricResult').innerHTML='<span style="color:#86909c;">未找到，试试 COTTON, SPANDEX, POLYESTER, NYLON, RAYON, WOOL, SILK...</span>';return;}$('qFabricResult').innerHTML=f.map(r=>'<b>'+r[0]+'</b> → FR: '+r[1]+' / ES: '+r[2]).join('<br>');});
CARE_LOOKUP.forEach(r=>{const o=document.createElement('option');o.value=r[0];o.textContent=r[0];$('qCare').appendChild(o);});
$('qCare').addEventListener('change',function(){const f=CARE_LOOKUP.find(r=>r[0]===this.value);if(!f){$('qCareResult').innerHTML='选择后显示...';return;}$('qCareResult').innerHTML='<div style="margin-bottom:6px;width:36px;">'+SYM[f[3]]+'</div><b>EN:</b> '+f[0]+'<br><b>FR:</b> '+f[1]+'<br><b>ES:</b> '+f[2];});
const CHART=[['wash30','30°C 水洗'],['washHand','手洗'],['washX','不可水洗'],['bleachX','不可漂白'],['bleachOxygen','仅非氯漂白'],['bleachAny','可漂白'],['dryLow','低温烘干'],['dryMed','中温烘干'],['dryX','不可烘干'],['iron1','低温熨烫'],['ironX','不可熨烫'],['dc','可干洗'],['dcX','不可干洗']];
$('qSymbolChart').innerHTML=CHART.map(([k,l])=>'<div class="chart-item">'+SYM[k]+'<br><span>'+l+'</span></div>').join('');
document.querySelectorAll('input,select,textarea').forEach(e=>{e.addEventListener('input',render);e.addEventListener('change',render);});
render();
</script>
</body>
</html>
'''
with open(r'C:\Users\shayn\Doubao\chats\2026-09-24\new-chat\care-label-tool\水洗标生成器.html','w',encoding='utf-8') as f:
    f.write(html)
print('OK', len(html))
