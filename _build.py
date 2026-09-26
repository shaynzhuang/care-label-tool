# -*- coding: utf-8 -*-
"""生成 水洗标生成器.html

所有排版参数都来自已批复的 Illustrator 模板（矢量 PDF 实测）：
  - SH / ADV / CC（APPROVED DILLARDS ... YS0626.pdf）：25x99mm，折边 10mm，
    成分/洗涤/款号 ArialMT 5.8pt 水平缩放 90%，产地/RN/YS ArialMT 6.5pt
  - EdgeHill（0713111.pdf）：25x99mm，折边 10mm，青色 #00AEEF 边框，
    成分 CataneoBT-Light 8.44pt，Exclusive of Decoration / Made in China
    AGaramondPro-Italic 9pt，洗涤/款号 CataneoBT-Light 6.14pt，RN/YS ArialMT 6.26pt
  - ANDY & EVAN（APPROVED ae ... YS062651.pdf / HOUSE CC .pdf）：两张 28x100mm，
    折边 8mm，品红边框，ArialMT 4.8-6.2pt
追踪码：S27 规则 BATCH & TRACKING CODE = S27品牌代码/工厂代码/YY/MM。
洗护文字、翻译、ISO 符号均来自 S27 HOUSE CARE LABEL RULE Excel（data/ 目录）。
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
EXCEL = json.load(open(os.path.join(HERE, 'data', 'excel_lists.json'), encoding='utf-8'))

# ---------------- 洗护选项（EN 为标签文字；FR/ES 取自 Excel） ----------------
# (符号key, EN, FR, ES)
WASH = [
    ("washX", "Do not wash", "Lavage interdit.", "No lavar."),
    ("washHand", "Hand wash", "Lavage à la main.", "Lavar a mano."),
    ("w30vm", "Machine wash cold with like colors. Gentle cycle.", "Lavage en machine max. 30°C. Laver avec des couleurs similaires. Cycle très délicat.", "Temperatura máxima de lavado 30°C. Lavar con colores similares. Proceso muy suave."),
    ("w30m", "Machine wash max. 30°C, mild process", "Lavage en machine max. 30°C, cycle délicat.", "Temperatura máxima de lavado 30°C. Proceso suave."),
    ("w30n", "Machine wash max. 30°C, normal process", "Lavage en machine max. 30°C, cycle normal.", "Temperatura máxima de lavado 30°C. Proceso normal."),
    ("w40vm", "Machine wash max. 40°C, very mild process", "Lavage en machine max. 40°C, cycle très délicat.", "Temperatura máxima de lavado 40°C. Proceso muy suave."),
    ("w40m", "Machine wash max. 40°C, mild process", "Lavage en machine max. 40°C, cycle délicat.", "Temperatura máxima de lavado 40°C. Proceso suave."),
    ("w40n", "Machine wash max. 40°C, normal process", "Lavage en machine max. 40°C, cycle normal.", "Temperatura máxima de lavado 40°C. Proceso normal."),
    ("w50m", "Machine wash max. 50°C, mild process", "Lavage en machine max. 50°C, cycle délicat.", "Temperatura máxima de lavado 50°C. Proceso suave."),
    ("w50n", "Machine wash max. 50°C, normal process", "Lavage en machine max. 50°C, cycle normal.", "Temperatura máxima de lavado 50°C. Proceso normal."),
    ("w60m", "Machine wash max. 60°C, mild process", "Lavage en machine max. 60°C, cycle délicat.", "Temperatura máxima de lavado 60°C. Proceso suave."),
    ("w60n", "Machine wash max. 60°C, normal process", "Lavage en machine max. 60°C, cycle normal.", "Temperatura máxima de lavado 60°C. Proceso normal."),
    ("w70n", "Machine wash max. 70°C, normal process", "Lavage en machine max. 70°C, cycle normal.", "Temperatura máxima de lavado 70°C. Proceso normal."),
    ("w95n", "Machine wash max. 95°C, normal process", "Lavage en machine max. 95°C, cycle normal.", "Temperatura máxima de lavado 95°C. Proceso normal."),
]
BLEACH = [
    ("bleachX", "Do not bleach.", "Pas de blanchiment.", "No usar lejía."),
    ("bleachNC", "Only non-chlorine bleach when needed.", "Produits de blanchiment oxygénés uniquement.", "Solo blanqueador oxigenado / sin cloro permitido."),
    ("bleachNC", "Only oxygen / non-chlorine bleach allowed", "Produits de blanchiment oxygénés uniquement.", "Solo blanqueador oxigenado / sin cloro permitido."),
    ("bleachAny", "Any bleaching agent allowed", "Tous types de blanchiment autorisés.", "Cualquier agente blanqueador permitido."),
]
TUMBLE = [
    ("dryX", "Do not tumble dry", "Pas de séchage en tambour.", "No usar secadora."),
    ("dry1", "Tumble dry low temperature", "Séchage en tambour autorisé, température modérée 60°C.", "Posible uso de secadora a temperatura baja, máxima temperatura de escape 60°C."),
    ("dry2", "Tumble dry normal temperature", "Séchage en tambour autorisé, température normale 80°C.", "Posible uso de secadora a temperatura normal, máxima temperatura de escape 80°C."),
]
NATURAL = [
    ("", "(none)", "", ""),
    ("line", "Line drying", "Séchage sur fil.", "Secar tendido."),
    ("dripLine", "Drip line drying", "Séchage sur fil sans essorage.", "Secar colgado por goteo."),
    ("flat", "Flat drying", "Séchage à plat.", "Secar extendido."),
    ("dripFlat", "Drip flat drying", "Séchage à plat sans essorage.", "Secado plano por goteo."),
    ("lineShade", "Line drying in shade", "Séchage sur fil à l'ombre.", "Secar colgado a la sombra."),
    ("dripLineShade", "Drip line drying in shade", "Séchage sur fil sans essorage à l'ombre.", "Secado línea de goteo en la sombra."),
    ("flatShade", "Flat drying in the shade", "Séchage à plat à l'ombre.", "Secar extendido a la sombra."),
    ("dripFlatShade", "Drip flat drying in the shade", "Séchage à plat sans essorage à l'ombre.", "Secado plano por goteo a la sombra."),
]
IRON = [
    ("ironX", "Do not iron", "Ne pas repasser.", "No planchar."),
    ("iron1", "Cool iron from inside if needed", "Repasser au froid de l’intérieur si nécessaire.", "Hierro frío desde el interior si es necesario."),
    ("iron1", "Iron at low temperature (maximum 110°C)", "Repasser à une température maximale de 110°C.", "Planchar máximo a temperatura de 110°C."),
    ("iron2", "Iron at medium temperature (maximum 150°C)", "Repasser à une température maximale de 150°C.", "Planchar máximo a temperatura de 150°C."),
    ("iron3", "Iron at high temperature (maximum 200°C)", "Repasser à une température maximale de 200°C.", "Planchar máximo a temperatura de 200°C."),
]
DRYCLEAN = [
    ("dcX", "Do not dry clean", "Pas d'entretien professionnel à sec.", "No limpiar en seco."),
    ("dcP1", "Professional dry cleaning mild process", "Entretien professionnel à sec cycle modéré.", "Limpieza profesional en seco en tetracloroetileno y todos los solventes listados para el símbolo F. Proceso suave."),
    ("dcP", "Professional dry cleaning normal process", "Entretien professionnel à sec cycle normal.", "Limpieza profesional en seco en tetracloroetileno y todos los solventes listados para el símbolo F. Proceso normal."),
    ("dcF1", "Professional dry cleaning mild process", "Entretien professionnel à sec cycle modéré.", "Limpieza profesional en seco en hidrocarburos (temperatura de destilación entre 150°C y 210°C, punto de inflamación entre 38°C y 70°C). Proceso suave."),
    ("dcF", "Professional dry cleaning normal process", "Entretien professionnel à sec cycle normal.", "Limpieza profesional en seco en hidrocarburos (temperatura de destilación entre 150°C y 210°C, punto de inflamación entre 38°C y 70°C). Proceso normal."),
]
WET = [
    ("", "(none)", "", ""),
    ("wetX", "Do not wet clean", "Pas d'entretien professionnel à l'eau.", "No limpieza profesional mojado."),
    ("wet2", "Professional wet cleaning gentle process", "Entretien professionnel à l'eau cycle très modéré.", "Limpieza profesional mojado. Proceso muy suave."),
    ("wet1", "Professional wet cleaning mild process", "Entretien professionnel à l'eau cycle modéré.", "Limpieza profesional en mojado. Proceso suave."),
    ("wet", "Professional wet cleaning normal process", "Entretien professionnel à l'eau cycle normal.", "Limpieza profesional en mojado. Proceso normal."),
]
EXTRAS = [  # Excel 中无符号 (N/A) 的附加语句
    ("", "Wash with like colors", "Laver avec des couleurs similaires.", "Lavar con colores similares."),
    ("", "Do not use fabric softener", "Ne pas utiliser d'assouplissant.", "No usar suavizante."),
    ("", "Wash before first use", "Laver avant la première utilisation.", "Lavar antes del primer uso."),
    ("", "Turn the clothes inside out", "Retourner les vêtements à l'envers.", "Voltear la ropa del revés."),
]
# 下拉框里区分同名选项
DC_LABEL = {"dcP1": " (P)", "dcP": " (P)", "dcF1": " (F)", "dcF": " (F)"}

# ---------------- 成分翻译（Excel + 已批复 ANDY & EVAN 模板用词） ----------------
FABRIC_EXTRA = [
    ["Nylon", "Nylon", "Nailon"], ["Lurex", "Lurex", "Lúrex"], ["Mesh", "Maille", "Malla"],
    ["Upper", "Partie supérieure", "Parte superior"], ["Skirt Shell", "Coquille de jupe", "Forro exterior de falda"],
    ["Skirt Lining", "Doublure de jupe", "Forro interior de falda"],
]
def clean(s):
    for junk in ('钩针织品英语', '法语', '西班牙语', '西语', '薄纱', '蕾丝英语', '(网状的，花边， 蕾丝）'):
        s = s.replace(junk, '')
    return ' '.join(s.split())
FABRIC = []
seen = set()
for en, fr, es in FABRIC_EXTRA + EXCEL['fabric']:
    en, fr, es = clean(en), clean(fr), clean(es)
    fixes = {'POLYIAMIDE': 'Polyamide', 'LINNING': 'Lining', 'KNIT RRIM': 'Knit trim'}
    en = fixes.get(en.upper(), en)
    if fr.lower() == 'polyamide or nylon':
        fr = 'Polyamide'
    if en.upper() in seen or not fr or '/' in en:
        continue
    seen.add(en.upper())
    FABRIC.append([en, fr, es])
FABRIC += [["Vest", "Gilet", "Chaleco"], ["Bowtie", "Nœud papillon", "Corbata de moño"]]

COUNTRY = [[clean(a), clean(b), clean(c)] for a, b, c in EXCEL['country']]

SYMBOL_CHART = [
    ("1) Washing", [(k, en) for k, en, *_ in WASH]),
    ("2) Bleaching", [("bleachX", "Do not bleach"), ("bleachNC", "Only oxygen / non-chlorine bleach"), ("bleachAny", "Any bleaching agent allowed")]),
    ("3.1) Tumble drying", [(k, en) for k, en, *_ in TUMBLE]),
    ("3.2) Natural drying", [(k, en) for k, en, *_ in NATURAL if k]),
    ("4) Ironing", [("ironX", "Do not iron"), ("iron1", "Low (max 110°C) / cool iron"), ("iron2", "Medium (max 150°C)"), ("iron3", "High (max 200°C)")]),
    ("5.1) Professional dry care", [("dcX", "Do not dry clean"), ("dcP1", "Dry clean P, mild"), ("dcP", "Dry clean P, normal"), ("dcF1", "Dry clean F, mild"), ("dcF", "Dry clean F, normal")]),
    ("5.2) Professional wet care", [(k, en) for k, en, *_ in WET if k]),
]

def options(rows, selected, labels=None):
    out = []
    for i, (k, en, *_r) in enumerate(rows):
        lab = en + ((labels or {}).get(k, ''))
        out.append('<option value="%d"%s>%s</option>' % (i, ' selected' if i == selected else '', lab.replace('&', '&amp;')))
    return '\n        '.join(out)

CARE_DATA = {'wash': WASH, 'bleach': BLEACH, 'tumble': TUMBLE, 'natural': NATURAL, 'iron': IRON, 'dryclean': DRYCLEAN, 'wet': WET, 'extras': EXTRAS}

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='10' fill='%23165dff'/%3E%3Cpath d='M18 26 L21 48 L43 48 L46 26 Z' fill='none' stroke='white' stroke-width='3'/%3E%3C/svg%3E">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital@1&display=swap">
<title>Care Label Generator</title>
<style>
/* 模板字体：优先用本机安装的原字体（与 Illustrator 模板一致），缺失时回退 */
@font-face{font-family:TplCataneo;font-style:italic;src:local("Cataneo BT Light"),local("CataneoBT-Light"),local("Cataneo Lt BT"),local("Cataneo BT")}
@font-face{font-family:TplGaramond;font-style:italic;src:local("Adobe Garamond Pro Italic"),local("AGaramondPro-Italic"),local("Garamond Italic"),local("Garamond-Italic")}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,"Segoe UI","Microsoft YaHei",sans-serif;background:#f0f2f5;color:#1f2329}
.topbar{background:#fff;border-bottom:1px solid #e5e6eb;padding:12px 24px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:10}
.topbar h1{font-size:17px;font-weight:600}
.topbar .sub{font-size:12px;color:#86909c;font-weight:400}
.btn{background:#165dff;color:#fff;border:none;padding:8px 18px;border-radius:6px;font-size:13px;cursor:pointer}
.btn.ghost{background:#fff;color:#165dff;border:1px solid #165dff;margin-right:8px}
.main{display:grid;grid-template-columns:400px 1fr;gap:20px;padding:20px 24px;max-width:1500px;margin:0 auto}
.panel{background:#fff;border-radius:8px;padding:18px;max-height:calc(100vh - 110px);overflow-y:auto}
.group{margin-bottom:16px}
.group-title{font-size:12px;font-weight:600;color:#86909c;text-transform:uppercase;letter-spacing:.5px;margin-bottom:8px;padding-bottom:4px;border-bottom:1px solid #f0f2f5}
label.field{display:block;font-size:12px;color:#4e5969;margin:8px 0 3px}
input[type=text],select,textarea{width:100%;padding:7px 9px;font-size:13px;border:1px solid #e5e6eb;border-radius:5px;font-family:inherit;background:#fff}
textarea{resize:vertical;min-height:50px}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.row3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px}
.check{display:flex;align-items:center;gap:6px;font-size:12px;color:#4e5969;margin-top:6px}
.hint{font-size:11px;color:#86909c;margin-top:3px}
.brand-badge{display:inline-block;background:#e8f3ff;color:#165dff;padding:3px 10px;border-radius:4px;font-size:12px;font-weight:600;margin-top:6px}
.warn{color:#e63946;font-size:12px;margin-top:6px;white-space:pre-line}
.preview-area{display:flex;justify-content:center;align-items:flex-start;padding:10px;min-width:0}
.label-sheet{background:#fff;padding:20px;border-radius:4px;box-shadow:0 2px 12px rgba(0,0,0,.08);display:flex;gap:4mm;flex-wrap:wrap;justify-content:center;align-items:flex-start}

/* ===== 标签通用：按 mm 绘制；--k 为自动缩放系数（内容放不下时 <1） ===== */
.label-wrap{display:flex;flex-direction:column;align-items:center;gap:2.7mm;break-inside:avoid;page-break-inside:avoid}
.care-label{background:#fff;color:#231f20;text-align:center;display:flex;flex-direction:column;overflow:hidden;flex-shrink:0}
.care-label .tail{flex:0 0 auto;display:flex;align-items:center;justify-content:center}
.care-label .sec{flex:0 0 var(--sec);height:var(--sec);min-height:0;overflow:hidden;display:flex;flex-direction:column;align-items:center;padding:0 1mm;--k:1}
.care-label .sec>*{flex-shrink:0;max-width:100%}
.care-label .sp{flex:1 1 0;min-height:0}
/* 模板中的固定间距；内容多时先压缩间距（最小 1mm），再考虑缩小字号 */
.care-label .gap{flex:0 1 auto;min-height:1mm}
.care-label [class=dash-line]{margin-bottom:-.25pt!important}
.care-label.over{outline:2px solid #e63946;outline-offset:2px}
.nw{white-space:nowrap}
.symbols{display:flex;justify-content:center;align-items:center;gap:.7mm}
.symbols svg{width:3.5mm;height:3.5mm;flex-shrink:0;overflow:visible}
.qty{color:#e60012;font-family:SimSun,"Songti SC",serif;font-size:12pt;white-space:nowrap}
.qty-below{text-align:center}
.qty-below .styles{font-family:Arial,sans-serif;font-size:6pt;color:#231f20;line-height:1.2;margin-bottom:1mm}

/* ===== 模板A：SH / ADV / CC（Dillards）25x99mm ===== */
.tpl-a{font-family:Arial,"Liberation Sans",Helvetica,sans-serif;border:.25pt solid #231f20}
.tpl-a .dash-line{height:0;border-top:.25pt dashed #231f20;margin:0 .9mm 0 1.2mm;flex-shrink:0}
.tpl-a .sx{font-size:calc(5.8pt * var(--k));line-height:1.383;width:111.111%;margin:0 -5.556%;max-width:none;transform:scaleX(.9);white-space:pre-line}
.tpl-a .sx.nw{white-space:nowrap}
.tpl-a .meta{font-size:calc(6.5pt * var(--k));line-height:1.352}
.tpl-a .meta .origin{margin-bottom:2.3mm}
.tpl-a .sec{padding-left:.8mm;padding-right:.8mm}
.tpl-a .top{padding-top:8.75mm;padding-bottom:3.33mm}
.tpl-a .bot{padding-top:1.26mm;padding-bottom:4.21mm}

/* ===== 模板B：EdgeHill 25x99mm ===== */
.tpl-b{font-family:TplCataneo,TplGaramond,"EB Garamond",Georgia,serif;font-style:italic;border:1pt solid #00aeef}
.tpl-b .dash-line{height:0;border-top:.5pt dashed #00aeef;margin:0 .9mm 0 1.2mm;flex-shrink:0}
.tpl-b .top{padding-top:6.3mm;padding-bottom:1.4mm}
.tpl-b .comp-b{font-size:calc(8.44pt * var(--k));line-height:1.18;white-space:pre-line}
.tpl-b .decor-b,.tpl-b .origin-b{font-family:TplGaramond,"EB Garamond",Georgia,serif;font-size:calc(9pt * var(--k));line-height:1.0}
.tpl-b .origin-b{line-height:1.1}
.tpl-b .bot{padding-top:2.7mm;padding-bottom:1mm}
.tpl-b .care-b{font-size:calc(6.14pt * var(--k));line-height:1.186;text-transform:uppercase;white-space:pre-line}
.tpl-b .style-b{font-size:calc(6.14pt * var(--k));line-height:1.186}
.tpl-b .rn-ys{font-family:Arial,"Liberation Sans",Helvetica,sans-serif;font-style:normal;font-size:calc(6.26pt * var(--k));line-height:1.22}

/* ===== 模板C：ANDY & EVAN 两张 28x100mm ===== */
.tpl-c{font-family:Arial,"Liberation Sans",Helvetica,sans-serif;border:.25pt solid #ec008c}
.tpl-c .dash-line{height:0;border-top:.567pt dashed #e73f97;flex-shrink:0}
.tpl-c .sec{padding:0 .6mm}
.tpl-c .logo{font-family:"Times New Roman",Times,serif;font-size:calc(7.6pt * var(--k));letter-spacing:.2em;line-height:1;margin-top:.5mm;white-space:nowrap}
.tpl-c .logo sup{font-size:.5em;letter-spacing:0;vertical-align:.9em}
.tpl-c .c-comp{font-size:calc(6.18pt * var(--k));line-height:1.15;white-space:pre-line}
.tpl-c .c-comp-es{font-size:calc(4.85pt * var(--k));line-height:1.2;white-space:pre-line}
.tpl-c .c-care-en{font-size:calc(4.95pt * var(--k));line-height:1.117;text-transform:capitalize}
.tpl-c .c-care-fr{font-size:calc(5.06pt * var(--k));line-height:1.01}
.tpl-c .c-care-es{font-size:calc(5.24pt * var(--k));line-height:1.146}
.tpl-c .c-meta{font-size:calc(4.95pt * var(--k));line-height:1.15}
.tpl-c .c-addr{font-size:calc(4.79pt * var(--k));line-height:1.065;letter-spacing:.02em}
.tpl-c .c-imp{font-size:calc(4.95pt * var(--k));line-height:1.61}
.tpl-c .symbols{margin:.8mm 0 .7mm}
.tpl-c .symbols svg{width:3mm;height:3mm}
.tpl-c .s1{padding-bottom:3.4mm}
.tpl-c .s2{padding-top:1.7mm;padding-bottom:.8mm}
.tpl-c .s3{padding-top:4.1mm;padding-bottom:2.8mm}
.tpl-c .s4{padding-top:5.1mm}
.tpl-c .gap1{flex:0 0 1.9mm}
.tpl-c .gap2{flex:0 0 2.2mm}

.query-panel{max-width:1500px;margin:0 auto 20px;padding:0 24px}
.query-panel .panel{max-height:none}
.query-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.qbox{background:#f7f8fa;padding:10px;border-radius:5px;min-height:40px;font-size:13px;line-height:1.8;margin-top:6px}
.qbox svg{width:40px;height:40px}
.chart-cat{font-size:12px;font-weight:600;color:#165dff;margin:12px 0 4px}
.chart{display:flex;flex-wrap:wrap;gap:10px}
.chart-item{text-align:center;width:92px}
.chart-item svg{width:40px;height:40px}
.chart-item span{font-size:10px;color:#4e5969;display:block;margin-top:2px;line-height:1.3}
@media (max-width:900px){.main{grid-template-columns:1fr}.query-grid{grid-template-columns:1fr}.panel{max-height:none}}
@media print{body{background:#fff}.topbar,.panel,.query-panel{display:none!important}.main{display:block;padding:0}.preview-area{padding:0}.label-sheet{box-shadow:none;padding:0;justify-content:flex-start}.care-label.over{outline:none}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}@page{size:A4 landscape;margin:8mm}}
</style>
</head>
<body>
<div class="topbar">
  <div><h1>Care Label Generator <span class="sub">Layout per approved templates · rules per S27 HOUSE CARE LABEL RULE</span></h1></div>
  <div><button class="btn ghost" onclick="resetForm()">Clear</button><button class="btn" onclick="window.print()">Print / Save PDF</button></div>
</div>
<div class="main">
  <div class="panel">
    <div class="group">
      <div class="group-title">Style Number (auto brand)</div>
      <label class="field">STYLE #</label>
      <input type="text" id="styleNo" value="F64SW840B/J">
      <div id="brandBadge"></div>
      <label class="field">Override Template</label>
      <select id="templateOverride">
        <option value="auto">Auto detect</option>
        <option value="a_adv">ADV / CC (no symbols)</option>
        <option value="a_sym">Scene &amp; Heard (with symbols)</option>
        <option value="b">EdgeHill</option>
        <option value="c">ANDY &amp; EVAN (EN/FR + ES)</option>
      </select>
    </div>
    <div class="group">
      <div class="group-title">Composition &amp; Origin</div>
      <label class="field">Composition (English, one part per line)</label>
      <textarea id="composition">100% Cotton</textarea>
      <label class="field">Country of origin</label>
      <select id="country"></select>
      <label class="check"><input type="checkbox" id="decor" checked> "Exclusive of Decoration" (EdgeHill)</label>
    </div>
    <div class="group">
      <div class="group-title">RN &amp; Tracking</div>
      <div class="row2">
        <div><label class="field">RN #</label><input type="text" id="rn" value="58909"></div>
        <div><label class="field">Factory code</label><input type="text" id="fty" value="YS"></div>
      </div>
      <label class="field">Date (YY/MM)</label><input type="text" id="ys" value="">
      <div class="hint">Batch &amp; tracking code = S27 brand code / factory code / YY / MM</div>
      <label class="field">Tracking line (blank = auto)</label>
      <input type="text" id="trackOverride" placeholder="">
    </div>
    <div class="group">
      <div class="group-title">Care Instructions (S27 rule)</div>
      <label class="field">1) Washing</label>
      <select id="wash">
        ''' + options(WASH, 2) + '''
      </select>
      <label class="field">2) Bleaching</label>
      <select id="bleach">
        ''' + options(BLEACH, 0) + '''
      </select>
      <label class="field">3.1) Tumble drying</label>
      <select id="tumble">
        ''' + options(TUMBLE, 1) + '''
      </select>
      <label class="field">3.2) Natural drying</label>
      <select id="natural">
        ''' + options(NATURAL, 0) + '''
      </select>
      <label class="field">4) Ironing</label>
      <select id="iron">
        ''' + options(IRON, 1) + '''
      </select>
      <label class="field">5.1) Professional dry care</label>
      <select id="dryclean">
        ''' + options(DRYCLEAN, 0, DC_LABEL) + '''
      </select>
      <label class="field">5.2) Professional wet care</label>
      <select id="wet">
        ''' + options(WET, 0) + '''
      </select>
      <label class="field">Additional text (no symbol)</label>
      <div id="extras"></div>
    </div>
    <div class="group">
      <div class="group-title">Print Setup</div>
      <div class="row3">
        <div><label class="field">Width (mm)</label><input type="text" id="labelWidth"></div>
        <div><label class="field">Length (mm)</label><input type="text" id="labelLength"></div>
        <div><label class="field">Fold (mm)</label><input type="text" id="foldMm"></div>
      </div>
      <div class="hint">Filled from the template automatically; edit to override.</div>
      <label class="field">Quantity (red, blank = hide)</label>
      <input type="text" id="qty" placeholder="e.g. 4250">
      <label class="field">Copies</label>
      <select id="copies"><option>1</option><option>2</option><option selected>4</option><option>6</option><option>8</option></select>
      <div id="fitWarn" class="warn"></div>
    </div>
  </div>
  <div class="preview-area"><div class="label-sheet" id="sheet"></div></div>
</div>

<div class="query-panel">
  <div class="panel">
    <div class="group-title" style="font-size:14px;color:#1f2329;">Care Label Rule Reference (S27 HOUSE CARE LABEL RULE)</div>
    <div class="query-grid">
      <div>
        <div style="font-size:12px;font-weight:600;color:#86909c;">Fabric Translation EN / FR / ES</div>
        <input type="text" id="qFabric" placeholder="Type fabric, e.g. cotton, spandex..." style="margin-top:6px;">
        <div class="qbox" id="qFabricResult">Type to search...</div>
      </div>
      <div>
        <div style="font-size:12px;font-weight:600;color:#86909c;">Care Instruction EN / FR / ES + ISO Symbol</div>
        <select id="qCare" style="margin-top:6px;"><option value="">-- Select care instruction --</option></select>
        <div class="qbox" id="qCareResult">Select to view...</div>
      </div>
    </div>
    <div style="margin-top:16px;">
      <div style="font-size:12px;font-weight:600;color:#86909c;">ISO 3758 Symbol Chart</div>
      <div id="qSymbolChart"></div>
    </div>
  </div>
</div>

<script>
const CARE = ''' + json.dumps(CARE_DATA, ensure_ascii=False) + ''';
const FABRIC = ''' + json.dumps(FABRIC, ensure_ascii=False) + ''';
const COUNTRY = ''' + json.dumps(COUNTRY, ensure_ascii=False) + ''';
const SYMBOL_CHART = ''' + json.dumps(SYMBOL_CHART, ensure_ascii=False) + r''';

// ---------- 模板参数（实测自批复模板） ----------
const TPL = {
  a_adv:{name:'ADV / CC', w:25, l:99, fold:10, rn:'58909'},
  a_sym:{name:'Scene & Heard (symbols)', w:25, l:99, fold:10, rn:'58909'},
  b:{name:'EdgeHill', w:25, l:99, fold:10, rn:'58909'},
  c:{name:'ANDY & EVAN', w:28, l:100, fold:8, rn:'136762'}
};

// ---------- ISO 3758 符号（按 Excel 图例绘制，viewBox 40x40） ----------
const LINE='fill="none" stroke="#231f20" stroke-width="2.2" stroke-linejoin="miter"';
function svg(inner){return '<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><g '+LINE+'>'+inner+'</g></svg>'}
function dots(n,y,cx,gap){let s='';const x0=cx-(n-1)*gap/2;for(let i=0;i<n;i++)s+='<circle cx="'+(x0+i*gap)+'" cy="'+y+'" r="1.9" fill="#231f20" stroke="none"/>';return s}
function bars(n,y0,x1,x2){let s='';for(let i=0;i<n;i++)s+='<path d="M'+x1+' '+(y0+i*3.4)+' H'+x2+'"/>';return s}
function cross(x1,y1,x2,y2){return '<path d="M'+x1+' '+y1+' L'+x2+' '+y2+' M'+x1+' '+y2+' L'+x2+' '+y1+'"/>'}
const TUB='<path d="M3 8 L8 31 H32 L37 8"/><path d="M5.2 9.2 q2.4 2.6 4.8 0 t4.8 0 t4.8 0 t4.8 0 t4.8 0 t4.8 0"/>';
function tubTxt(t){return '<text x="20" y="21.5" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="10.5" fill="#231f20" stroke="none">'+t+'</text>'}
const TRI='<path d="M20 4 L37 34 H3 Z"/>';
const SQ='<rect x="4" y="4" width="32" height="32"/>';
const DRUM='<circle cx="20" cy="20" r="11.5"/>';
const IRONP='<path d="M3 32 H37 L34.6 9 H12.5 L11 18.5 M3 32 C3.8 24 6.5 18.5 11 18.5 H35.6"/>';
const CIR='<circle cx="20" cy="20" r="12.5"/>';
function pro(letter,nbar){const cy=[20,17.5,15.5][nbar],r=[12.5,11.5,10][nbar];return '<circle cx="20" cy="'+cy+'" r="'+r+'"/>'+(letter?'<text x="20" y="'+(cy+5.8)+'" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="bold" font-size="'+(nbar==2?14:16)+'" fill="#231f20" stroke="none">'+letter+'</text>':'')+bars(nbar,cy+r+3.5,9,31)}
function SYM(k){
  if(!k)return '';
  const m=k.match(/^w(\d+)(vm|m|n)$/);
  if(m){const t=+m[1],nb={vm:2,m:1,n:0}[m[2]],nd={30:1,40:2,50:3,60:4}[t]||0;return svg(TUB+tubTxt(t+'C')+dots(nd,26.3,20,4.4)+bars(nb,34.3,7.5,32.5))}
  switch(k){
    case 'washX':return svg(TUB+cross(2,4,38,35));
    case 'washHand':return svg(TUB+'<path d="M15 21 C14 16 17 12.5 21.5 11 L30.5 3 L33.5 6 L27.5 11.5 L32.5 11 L32.8 14.2 L26 15.6 C25 20.5 19.5 23.5 15 21 Z" fill="#231f20" stroke="none"/>');
    case 'bleachX':return svg('<path d="M20 4 L37 34 H3 Z" fill="#231f20"/>'+cross(1,13,39,31));
    case 'bleachNC':return svg(TRI+'<path d="M12 34 L24.5 11.9 M21 34 L29 19.9"/>');
    case 'bleachAny':return svg(TRI);
    case 'dryX':return svg(SQ+DRUM+cross(1,6,39,34));
    case 'dry1':return svg(SQ+DRUM+dots(1,20,20,0));
    case 'dry2':return svg(SQ+DRUM+dots(2,20,20,6));
    case 'line':return svg(SQ+'<path d="M20 8 V32"/>');
    case 'dripLine':return svg(SQ+'<path d="M16.5 8 V32 M23.5 8 V32"/>');
    case 'flat':return svg(SQ+'<path d="M8 20 H32"/>');
    case 'dripFlat':return svg(SQ+'<path d="M8 16.5 H32 M8 23.5 H32"/>');
    case 'lineShade':return svg(SQ+'<path d="M4 14 L14 4 M22 8 V32"/>');
    case 'dripLineShade':return svg(SQ+'<path d="M4 14 L14 4 M19 8 V32 M26 8 V32"/>');
    case 'flatShade':return svg(SQ+'<path d="M4 14 L14 4 M11 22 H32"/>');
    case 'dripFlatShade':return svg(SQ+'<path d="M4 14 L14 4 M11 19 H32 M11 26 H32"/>');
    case 'ironX':return svg(IRONP+cross(1,6,39,36));
    case 'iron1':return svg(IRONP+dots(1,25.5,21,0));
    case 'iron2':return svg(IRONP+dots(2,25.5,21,6.5));
    case 'iron3':return svg(IRONP+dots(3,25.5,21,6.5));
    case 'dcX':return svg(CIR+cross(1,8,39,32));
    case 'dcP':return svg(pro('P',0));
    case 'dcP1':return svg(pro('P',1));
    case 'dcF':return svg(pro('F',0));
    case 'dcF1':return svg(pro('F',1));
    case 'wetX':return svg(pro('W',0)+cross(1,8,39,32));
    case 'wet':return svg(pro('W',0));
    case 'wet1':return svg(pro('W',1));
    case 'wet2':return svg(pro('W',2));
  }
  return '';
}

// ---------- 工具函数 ----------
function $(id){return document.getElementById(id)}
function esc(t){return String(t).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
function titleCase(s){return s.toLowerCase().replace(/(^|[\s\-/(:,&])([a-zà-ÿ])/g,(m,a,b)=>a+b.toUpperCase())}
function capFirst(s){return s?s.charAt(0).toUpperCase()+s.slice(1):s}
function detectTemplate(s){s=s.toUpperCase().trim();if(/^(F64EH|S74EH)/.test(s))return'b';if(/^F26/.test(s))return'c';if(/^(F64SW|F54SH|S64SM|F64SH|S74SH)/.test(s))return'a_sym';return'a_adv'}
function brandCode(s){s=s.toUpperCase();if(/^F64SL/.test(s))return'S27CC';if(/^(F64SW|F54SH|S64SM|F64SH|S74SH)/.test(s))return'S27SH';if(/^(F64AW|S74AW)/.test(s))return'S27AD';if(/^(F64EH|S74EH)/.test(s))return'S27EC';if(/^F26/.test(s))return'S27AE';return'S27XX'}
function curTpl(){return $('templateOverride').value==='auto'?detectTemplate($('styleNo').value):$('templateOverride').value}
function pick(cat){return CARE[cat][+$(cat).value]}
function careRows(){return ['wash','bleach','tumble','natural','iron','dryclean','wet'].map(pick).filter(x=>x&&x[1]!=='(none)')}
function selectedCare(){const r=careRows();document.querySelectorAll('#extras input:checked').forEach(c=>r.push(CARE.extras[+c.value]));return r}
function careSymbols(){return careRows().filter(x=>x[0]).map(x=>SYM(x[0])).join('')}

// 成分翻译：最长匹配优先，保留百分比与标点
const FAB_SORTED=FABRIC.slice().sort((a,b)=>b[0].length-a[0].length);
const isL=ch=>/[A-Za-zÀ-ÿ]/.test(ch||'');
function translateComp(txt,lang){ // lang 1=FR 2=ES
  const missing=[];
  const text=txt.split('\n').map(line=>{
    let res='',i=0;
    while(i<line.length){
      let hit=null;
      if(isL(line[i])&&!isL(line[i-1])){
        for(const f of FAB_SORTED){const n=f[0].length;if(line.substr(i,n).toLowerCase()===f[0].toLowerCase()&&!isL(line[i+n])){hit=f;break}}
      }
      if(hit){res+=capFirst(hit[lang].toLowerCase());i+=hit[0].length}
      else if(isL(line[i])){let j=i;while(j<line.length&&isL(line[j]))j++;missing.push(line.slice(i,j));res+=line.slice(i,j);i=j}
      else{res+=line[i];i++}
    }
    return res;
  }).join('\n');
  return {text,missing};
}
function countryRow(){return COUNTRY[+$('country').value]||COUNTRY[0]}
function fixAbbr(s){return s.replace(/\bUsa\b/,'USA')}
function originEN(){return 'Made in '+fixAbbr(titleCase(countryRow()[0]))}
function originFR(){const g=countryRow()[1],m=g.match(/^(\S+)\s+(.*)$/);return 'Fabriqué '+(m?m[1].toLowerCase()+' '+titleCase(m[2]):titleCase(g))}
function originES(){return 'Hecho en '+titleCase(countryRow()[2])}

let lastTpl=null;
function applyTemplateDefaults(tpl){const t=TPL[tpl];$('labelWidth').value=t.w;$('labelLength').value=t.l;$('foldMm').value=t.fold;$('rn').value=t.rn}
function trackingLine(tpl){
  const o=$('trackOverride').value.trim();if(o)return o;
  // S27 规则：BATCH & TRACKING CODE = S27CC/SH/AD/EC/AE + / 工厂代码 / YY / MM（五个品牌相同）
  return brandCode($('styleNo').value)+'/'+$('fty').value.trim()+'/'+$('ys').value.trim();
}

function render(){
  const tpl=curTpl();
  if(tpl!==lastTpl){applyTemplateDefaults(tpl);lastTpl=tpl}
  $('brandBadge').innerHTML='<span class="brand-badge">'+esc(TPL[tpl].name)+' · '+brandCode($('styleNo').value)+'</span>';
  const w=parseFloat($('labelWidth').value)||TPL[tpl].w, L=parseFloat($('labelLength').value)||TPL[tpl].l, fm=Math.max(0,parseFloat($('foldMm').value)||0), n=parseInt($('copies').value);
  const compRaw=$('composition').value.replace(/\s+$/,''), styleNo=esc($('styleNo').value.trim()), qty=esc($('qty').value.trim()), rn=esc($('rn').value.trim());
  const care=selectedCare(), track=esc(trackingLine(tpl));
  const box='width:'+w+'mm;height:'+L+'mm;--sec:'+((L-2*fm)/2)+'mm;', tail='<div class="tail" style="height:'+fm+'mm"></div>';
  const warns=[];
  let h='';
  for(let c=0;c<n;c++){
    if(tpl==='b'){
      h+='<div class="label-wrap"><div class="care-label tpl-b" style="'+box+'">'+tail+'<div class="dash-line"></div>';
      h+='<div class="sec top"><div class="comp-b">'+esc(titleCase(compRaw))+'</div><div class="sp"></div>';
      if($('decor').checked)h+='<div class="decor-b">Exclusive<br>of Decoration</div><div class="gap" style="height:4mm"></div>';
      h+='<div class="origin-b nw">'+esc(originEN())+'</div></div><div class="dash-line"></div>';
      h+='<div class="sec bot"><div class="care-b">'+care.map(x=>esc(x[1])).join('\n')+'</div><div class="gap" style="height:1.5mm"></div><div class="style-b nw">Style # '+styleNo+'</div><div class="gap" style="height:2.2mm"></div><div class="rn-ys nw">RN'+rn+'<br>'+track+'</div></div>';
      h+='<div class="dash-line"></div>'+tail+'</div>';
      if(qty)h+='<div class="qty">数量：'+qty+'</div>';
      h+='</div>';
    }else if(tpl==='c'){
      const fr=translateComp(compRaw,1),es=translateComp(compRaw,2);
      if(c===0&&fr.missing.length)warns.push('No FR/ES translation in the S27 rule for: '+[...new Set(fr.missing)].join(', '));
      const en=care.map(x=>esc(x[1].replace(/\./g,''))).join('<br>'), frc=care.map(x=>esc(x[2])).filter(Boolean).join('<br>'), esc_=care.map(x=>esc(x[3])).filter(Boolean).join('<br>');
      h+='<div class="label-wrap">';
      // 第一张：EN + FR
      h+='<div class="care-label tpl-c" style="'+box+'">'+tail+'<div class="dash-line"></div>';
      h+='<div class="sec s1"><div class="logo">ANDY &amp; EVAN<sup>®</sup></div><div class="sp"></div><div class="c-comp">'+esc(compRaw)+'</div><div class="sp"></div>';
      h+='<div class="c-care-en">'+en+'</div><div class="symbols">'+careSymbols()+'</div>';
      h+='<div class="c-meta">'+esc(titleCase(originEN()).replace(/\bUsa\b/,'USA'))+'<br>RN#'+rn+'<br>'+track+'</div></div><div class="dash-line"></div>';
      h+='<div class="sec s2"><div class="c-comp">'+esc(fr.text)+'</div><div class="sp"></div><div class="c-care-fr">'+frc+'</div><div class="gap1"></div>';
      h+='<div class="c-addr">'+esc(originFR())+'<br>WPL 11590<br>David Peyser Sportswear<br>90 Spence Street<br>Bayshore, NY 11706<br>USA</div><div class="sp"></div></div>';
      h+='<div class="dash-line"></div>'+tail+'</div>';
      // 第二张：ES + 进口商
      h+='<div class="care-label tpl-c" style="'+box+'">'+tail+'<div class="dash-line"></div>';
      h+='<div class="sec s3"><div class="c-comp-es">'+esc(es.text)+'</div><div class="sp"></div><div class="c-care-es">'+esc_+'</div><div class="gap2"></div><div class="c-care-es">'+esc(originES())+'</div><div class="sp"></div></div><div class="dash-line"></div>';
      h+='<div class="sec s4"><div class="c-imp">IMPORTADO POR:<br>IMPORTADORA PRIMEX<br>S.A. DE C.V.<br>BLVD. MAGNOCENTRO<br>NO. 4 SAN FERNANDO<br>LA HERRADURA<br>HUIXQUILUCAN,<br>ESTADO DE MEXICO<br>C.P. 52765<br>RFC: IPR-903907-S70</div></div>';
      h+='<div class="dash-line"></div>'+tail+'</div>';
      if(qty)h+='<div class="qty-below"><div class="styles">'+styleNo+'</div><div class="qty">数量：'+qty+'</div></div>';
      h+='</div>';
    }else{
      // SH / ADV / CC
      h+='<div class="label-wrap"><div class="care-label tpl-a" style="'+box+'">'+tail+'<div class="dash-line"></div>';
      h+='<div class="sec top"><div class="sx">'+esc(compRaw.toUpperCase())+'</div><div class="sp"></div><div class="meta nw"><div class="origin">'+esc(originEN().toUpperCase())+'</div><div>RN#'+rn+'</div><div>'+track+'</div></div></div><div class="dash-line"></div>';
      h+='<div class="sec bot"><div class="sx">'+care.map(x=>esc(x[1].toUpperCase())).join('\n')+'</div><div class="sp"></div>';
      if(tpl==='a_sym')h+='<div class="symbols">'+careSymbols()+'</div><div class="gap" style="height:3.55mm"></div>';
      h+='<div class="sx nw">STYLE '+styleNo+'</div></div><div class="dash-line"></div>';
      h+='<div class="tail" style="height:'+fm+'mm">'+(qty?'<div class="qty">数量：'+qty+'</div>':'')+'</div></div></div>';
    }
  }
  $('sheet').innerHTML=h;
  fitLabels(warns);
}

// 各区块内容超出时整体按比例缩小字号（--k），最小 70%；仍超出则标红
function overflowing(el){return el.scrollHeight>el.clientHeight+0.5||el.scrollWidth>el.clientWidth+0.5}
function fitLabels(warns){
  let bad=0,shrunk=false;
  document.querySelectorAll('#sheet .care-label').forEach(lab=>{
    let ok=true;
    lab.querySelectorAll('.sec').forEach(el=>{
      let k=1;el.style.setProperty('--k',k);
      while(overflowing(el)&&k>0.7){k=Math.round((k-0.02)*100)/100;el.style.setProperty('--k',k)}
      if(overflowing(el))ok=false;
      if(k<1)shrunk=true;
    });
    lab.classList.toggle('over',!ok);if(!ok)bad++;
  });
  if(bad)warns.push('Content does not fit the label: shorten the text or change width/length.');
  else if(shrunk)warns.push('Note: font reduced below the template size so the content fits.');
  $('fitWarn').textContent=warns.join('\n');
}

function resetForm(){$('composition').value='';$('styleNo').value='';$('qty').value='';$('trackOverride').value='';render()}

// ---------- 初始化 ----------
(function init(){
  const d=new Date();$('ys').value=String(d.getFullYear()).slice(2)+'/'+String(d.getMonth()+1).padStart(2,'0');
  $('country').innerHTML=COUNTRY.map((c,i)=>'<option value="'+i+'"'+(c[0]==='CHINA'?' selected':'')+'>'+esc(fixAbbr(titleCase(c[0])))+'</option>').join('');
  $('extras').innerHTML=CARE.extras.map((x,i)=>'<label class="check"><input type="checkbox" value="'+i+'"> '+esc(x[1])+'</label>').join('');
  // 参考区
  $('qFabric').addEventListener('input',function(){
    const q=this.value.trim().toUpperCase();
    if(!q){$('qFabricResult').innerHTML='Type to search...';return}
    const f=FABRIC.filter(r=>r[0].toUpperCase().includes(q));
    if(!f.length){$('qFabricResult').innerHTML='<span style="color:#86909c;">Not found in the S27 rule.</span>';return}
    $('qFabricResult').innerHTML=f.map(r=>'<b>'+esc(r[0])+'</b><br>FR: '+esc(r[1])+'<br>ES: '+esc(r[2])).join('<hr style="border:none;border-top:1px solid #e5e6eb;margin:6px 0">');
  });
  const DCL={dcP1:' (P)',dcP:' (P)',dcF1:' (F)',dcF:' (F)'};
  [['wash','1) Washing'],['bleach','2) Bleaching'],['tumble','3.1) Tumble drying'],['natural','3.2) Natural drying'],['iron','4) Ironing'],['dryclean','5.1) Professional dry care'],['wet','5.2) Professional wet care'],['extras','Additional (no symbol)']].forEach(([cat,lab])=>{
    const og=document.createElement('optgroup');og.label=lab;
    CARE[cat].forEach((r,i)=>{if(r[1]==='(none)')return;const o=document.createElement('option');o.value=cat+':'+i;o.textContent=r[1]+(DCL[r[0]]||'');og.appendChild(o)});
    $('qCare').appendChild(og);
  });
  $('qCare').addEventListener('change',function(){
    if(!this.value){$('qCareResult').innerHTML='Select to view...';return}
    const [cat,i]=this.value.split(':'),f=CARE[cat][+i];
    $('qCareResult').innerHTML=(f[0]?'<div style="margin-bottom:6px;">'+SYM(f[0])+'</div>':'<div style="color:#86909c">No symbol (text only)</div>')+'<b>EN:</b> '+esc(f[1])+'<br><b>FR:</b> '+esc(f[2])+'<br><b>ES:</b> '+esc(f[3]);
  });
  $('qSymbolChart').innerHTML=SYMBOL_CHART.map(([cat,items])=>'<div class="chart-cat">'+esc(cat)+'</div><div class="chart">'+items.map(([k,l])=>'<div class="chart-item">'+SYM(k)+'<span>'+esc(l)+'</span></div>').join('')+'</div>').join('');
  document.querySelectorAll('.main .panel input,.main .panel select,.main .panel textarea').forEach(e=>{e.addEventListener('input',render);e.addEventListener('change',render)});
  if(document.fonts&&document.fonts.ready)document.fonts.ready.then(render);
  render();
})();
</script>
</body>
</html>'''

with open(os.path.join(HERE, '水洗标生成器.html'), 'w', encoding='utf-8') as f:
    f.write(html)
print('OK', len(html))
