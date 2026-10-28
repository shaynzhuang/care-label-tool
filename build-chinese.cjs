const fs = require('fs');
const source = fs.readFileSync('水洗标生成器.html', 'utf8');
const words = {
'Care Label Generator':'水洗标生成器','Layout per approved templates · rules per S27 HOUSE CARE LABEL RULE':'版式依据批复模板 · 规则依据 S27 水洗标规范','Clear':'清空','Print / Save PDF':'打印 / 保存 PDF','Batch from Excel 批量生成':'Excel 批量生成','Care Instructions':'洗护说明','Style Number (auto brand)':'款号（自动识别品牌）','Brand (blank = auto from style number)':'品牌（留空则按款号自动识别）','Auto from style number':'按款号自动识别','STYLE #':'款号','Override Template':'指定模板','Auto detect':'自动识别','Composition & Origin':'成分与产地','Composition (English, one part per line)':'成分（填写英文，每个部位一行）','Country of origin':'原产国','RN & Tracking':'RN 注册号与追踪码','RN #':'RN 注册号','Factory code':'供应商代码','Date (YY/MM)':'日期（年后两位/月）','Batch & tracking code = S27 brand code / factory code / YY / MM':'批次与追踪码 = S27 品牌代码 / 供应商代码 / 年后两位 / 月','Tracking line (blank = auto)':'追踪码（留空自动生成）','Care Instructions (S27 rule)':'洗护说明（S27 规则）','1) Washing':'1）水洗','2) Bleaching':'2）漂白','3.1) Tumble drying':'3.1）滚筒烘干','3.2) Natural drying':'3.2）自然晾干','4) Ironing':'4）熨烫','5.1) Professional dry care':'5.1）专业干洗','5.2) Professional wet care':'5.2）专业湿洗','Additional text (no symbol)':'附加说明（无符号）','Print Setup':'打印设置','Width (mm)':'宽度（毫米）','Length (mm)':'长度（毫米）','Fold (mm)':'折边（毫米）','Filled from the template automatically; edit to override.':'自动填入模板尺寸，可手动修改。','Quantity (red, blank = hide)':'数量（红色显示，留空隐藏）','Copies':'打印份数','Care Label Rule Reference (S27 HOUSE CARE LABEL RULE)':'水洗标规则查询（S27 HOUSE CARE LABEL RULE）','Fabric Translation EN / FR / ES':'面料译名：英文 / 法文 / 西班牙文','Care Instruction EN / FR / ES + ISO Symbol':'洗护说明：英 / 法 / 西及 ISO 符号','ISO 3758 Symbol Chart':'ISO 3758 洗护符号表','Type to search...':'输入面料英文名称查询…','Select to view...':'选择洗护说明查看…','-- Select care instruction --':'请选择洗护说明','Not found in the S27 rule.':'S27 规则中未找到该项目。','No symbol (text only)':'无符号（仅文字）','(none)':'（无）','Do not wash':'不可水洗','Hand wash':'手洗','Do not bleach.':'不可漂白','Do not tumble dry':'不可滚筒烘干','Tumble dry low temperature':'低温滚筒烘干','Tumble dry normal temperature':'常温滚筒烘干','Do not iron':'不可熨烫','Do not dry clean':'不可干洗','Do not wet clean':'不可湿洗','Line drying':'悬挂晾干','Drip line drying':'滴水悬挂晾干','Flat drying':'平摊晾干','Drip flat drying':'滴水平摊晾干','Line drying in shade':'阴凉处悬挂晾干','Drip line drying in shade':'阴凉处滴水悬挂晾干','Flat drying in the shade':'阴凉处平摊晾干','Drip flat drying in the shade':'阴凉处滴水平摊晾干','Cool Iron From inside If Needed':'如有需要，从反面低温熨烫','Machine wash cold with like colors gentle cycle':'冷水机洗，同色衣物一起洗，轻柔程序','Only non-chlorine bleach when needed.':'必要时仅使用非氯漂白剂','Only Oxygen / non-chlorine bleach allowed':'仅允许氧系 / 非氯漂白剂','Any bleaching agent allowed':'允许使用各类漂白剂','Exclusive of Decoration':'装饰部分除外','China':'中国'};
function translate(text) {
 let s=text.trim(); if(words[s]) return text.replace(s,words[s]);
 for(const [a,b] of Object.entries(words).sort((a,b)=>b[0].length-a[0].length)) s=s.split(a).join(b);
 const parts={'Very mild process':'非常轻柔程序','Mild Process':'轻柔程序','Normal Process':'正常程序','Professional dry cleaning mild process':'专业干洗，轻柔程序','Professional dry cleaning normal process':'专业干洗，正常程序','Professional wet cleaning gentle process':'专业湿洗，非常轻柔程序','Professional wet cleaning mild process':'专业湿洗，轻柔程序','Professional wet cleaning normal process':'专业湿洗，正常程序','Iron at low temperature':'低温熨烫','Iron at medium temperature':'中温熨烫','Iron at high temperature':'高温熨烫','maximum':'最高','no symbols':'无符号','with symbols':'含符号','EN/FR + ES':'英文/法文 + 西班牙文'};
 for(const [a,b] of Object.entries(parts)) s=s.split(a).join(b);
 return text.replace(text.trim(),s);
}

const runtime = `
(function(){
const words=DICTIONARY;
TRANSLATOR
let language=decodeURIComponent(location.pathname).includes('中文版')?'zh':'en';
const originals=new WeakMap();
const wrap=document.createElement('label');wrap.style.cssText='display:inline-flex;align-items:center;gap:6px;margin-right:12px;font-size:13px';wrap.innerHTML='Language / 语言 <select id="uiLanguage" style="width:auto"><option value="zh">中文</option><option value="en">English</option></select>';
document.querySelector('.topbar>div:last-child').prepend(wrap);const picker=document.getElementById('uiLanguage');picker.value=language;
function apply(){observer.disconnect();document.querySelectorAll('.topbar,.panel').forEach(root=>{const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);let n;while(n=walker.nextNode()){if(n.parentElement.closest('#uiLanguage,script,style,textarea,#qFabricResult,#qCareResult,#presetInfo,#manualList,#manualStatus'))continue;let entry=originals.get(n);if(!entry||n.nodeValue!==entry.shown){entry={base:n.nodeValue,shown:n.nodeValue};originals.set(n,entry)}n.nodeValue=language==='zh'?translate(entry.base):entry.base;entry.shown=n.nodeValue;}});document.documentElement.lang=language==='zh'?'zh-CN':'en';document.title=language==='zh'?'水洗标生成器':'Care Label Generator';observer.observe(document.body,{childList:true,subtree:true,characterData:true});}
const observer=new MutationObserver(apply);picker.addEventListener('change',()=>{language=picker.value;apply()});apply();
})();
`.replace('DICTIONARY',JSON.stringify(words)).replace('TRANSLATOR',translate.toString());
let html=source.replace(/<!-- UI_LANGUAGE_START -->[\s\S]*?<!-- UI_LANGUAGE_END -->/g,'');
html=html.replace('</body>','<!-- UI_LANGUAGE_START --><script>'+runtime+'</script><!-- UI_LANGUAGE_END --></body>');
fs.writeFileSync('水洗标生成器.html',html);
fs.writeFileSync('水洗标生成器-中文版.html',html);
console.log('已生成统一界面，支持中英文切换');
