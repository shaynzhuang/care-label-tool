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

# ---------------- 洗护选项：文字逐字取自 S27 HOUSE CARE LABEL RULE（data/excel_care.json，键为单元格） ----------------
CELL = json.load(open(os.path.join(HERE, 'data', 'excel_care.json'), encoding='utf-8'))
def X(key, cell, label=None, en=None):
    """(符号key, EN, FR, ES, 下拉框显示名)；label 只用于下拉框区分同名选项，不印在标签上"""
    e, f, sp = CELL[cell]
    sp = sp.split(' (only if')[0].strip()   # U4 西语单元格里给厂家的备注，不印
    if sp == '/': sp = ''
    e = en or e
    return (key, e, f, sp, label or e)

WASH = [
    X("washX", "K3"), X("washHand", "K4"),
    # 0921 批复 / 统一要求：标签印 MACHINE WASH COLD WITH LIKE COLORS GENTLE CYCLE（Excel K5 去掉句号）
    X("w30vm", "K5", en="Machine wash cold with like colors gentle cycle"),
    X("w30m", "K6", "Mild Process (30°C)"), X("w30n", "K7", "Normal Process (30°C)"),
    X("w40vm", "K8", "Very mild process (40°C)"), X("w40m", "K9", "Mild Process (40°C)"), X("w40n", "K10", "Normal Process (40°C)"),
    X("w50m", "K11", "Mild Process (50°C)"), X("w50n", "K12", "Normal Process (50°C)"),
    X("w60m", "K13", "Mild Process (60°C)"), X("w60n", "K14", "Normal Process (60°C)"),
    X("w70n", "K15", "Normal Process (70°C)"), X("w95n", "K16", "Normal Process (95°C)"),
]
BLEACH = [X("bleachX", "P3"), X("bleachNC", "brief!D13"), X("bleachNC", "P4"), X("bleachAny", "P5")]
TUMBLE = [X("dryX", "P7"), X("dry1", "P8"), X("dry2", "P9")]
NONE = ("", "(none)", "", "", "(none)")
NATURAL = [NONE] + [X(k, c) for k, c in (("line", "P11"), ("dripLine", "P12"), ("flat", "P13"), ("dripFlat", "P14"),
                                          ("lineShade", "P15"), ("dripLineShade", "P16"), ("flatShade", "P17"), ("dripFlatShade", "P18"))]
IRON = [X("ironX", "U3"), X("iron1", "U5"), X("iron1", "U4"), X("iron2", "U6"), X("iron3", "U7")]
DRYCLEAN = [X("dcX", "U9"),
            X("dcP1", "U12", "Professional dry cleaning mild process (P)"), X("dcP", "U13", "Professional dry cleaning normal process (P)"),
            X("dcF1", "U10", "Professional dry cleaning mild process (F)"), X("dcF", "U11", "Professional dry cleaning normal process (F)")]
WET = [NONE, X("wetX", "U15"), X("wet2", "U16"), X("wet1", "U17"), X("wet", "U18")]
EXTRAS = [X("", c) for c in ("K17", "K18", "K19", "K20", "K21", "K22", "K23", "K25", "brief!D38")]

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
    ("1) Washing", [(r[0], r[4]) for r in WASH]),
    ("2) Bleaching", [("bleachX", "Do not bleach"), ("bleachNC", "Only oxygen / non-chlorine bleach"), ("bleachAny", "Any bleaching agent allowed")]),
    ("3.1) Tumble drying", [(k, en) for k, en, *_ in TUMBLE]),
    ("3.2) Natural drying", [(r[0], r[4]) for r in NATURAL if r[0]]),
    ("4) Ironing", [("ironX", "Do not iron"), ("iron1", "Low (max 110°C) / cool iron"), ("iron2", "Medium (max 150°C)"), ("iron3", "High (max 200°C)")]),
    ("5.1) Professional dry care", [("dcX", "Do not dry clean"), ("dcP1", "Dry clean P, mild"), ("dcP", "Dry clean P, normal"), ("dcF1", "Dry clean F, mild"), ("dcF", "Dry clean F, normal")]),
    ("5.2) Professional wet care", [(r[0], r[4]) for r in WET if r[0]]),
]

def options(rows, selected):
    out = []
    for i, r in enumerate(rows):
        lab = r[4]
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
<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
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

.btn.small{padding:5px 10px;font-size:12px;margin:6px 6px 0 0}
.btn-row{display:flex;flex-wrap:wrap}
.batch-box{background:#f7f8fa;border-radius:6px;padding:10px}
.small-box{font-size:11px;line-height:1.5;padding:6px 8px;min-height:0}
.batch-only{display:none}
.preview-area{flex-direction:column;align-items:center}
#batch{display:none;width:100%}
body.batch-mode #sheet{display:none}
body.batch-mode #batch{display:block}
body.batch-mode .batch-only{display:inline-block}
.batch-summary{background:#fff;border-radius:6px;padding:10px 14px;font-size:13px;margin-bottom:10px}
.batch-table{background:#fff;border-radius:6px;padding:6px;overflow-x:auto;margin-bottom:14px}
.batch-table table{border-collapse:collapse;width:100%;font-size:12px}
.batch-table th,.batch-table td{border:1px solid #e5e6eb;padding:4px 6px;text-align:left;vertical-align:top}
.batch-table th{background:#f7f8fa;white-space:nowrap}
.batch-table tr.warnrow td{background:#fff1f0}
.batch-table .pre{white-space:pre-line}
.brand-sec{margin-bottom:14px}
.brand-head{font-size:13px;font-weight:600;margin:6px 0}
.batch-sheet{justify-content:flex-start}
.batch-item{display:flex;flex-direction:column;align-items:center}
.batch-tag{font-size:9pt;color:#86909c;margin-bottom:1mm;font-family:Arial,sans-serif}
.qty-below .styles{max-width:60mm;overflow-wrap:anywhere}
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
@media print{body{background:#fff}.topbar,.panel,.query-panel{display:none!important}.main{display:block;padding:0}.preview-area{padding:0}.label-sheet{box-shadow:none;padding:0;justify-content:flex-start}.batch-summary,.batch-table{display:none!important}.brand-sec+.brand-sec{break-before:page;page-break-before:always}.brand-head{margin:0 0 2mm}.care-label.over{outline:none}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}@page{size:A4 landscape;margin:8mm}@page ae{size:A4 portrait;margin:8mm}.page-ae{page:ae}.batch-item{break-inside:avoid;page-break-inside:avoid}}
</style>
</head>
<body>
<div class="topbar">
  <div><h1>Care Label Generator <span class="sub">Layout per approved templates · rules per S27 HOUSE CARE LABEL RULE</span></h1></div>
  <div><button class="btn ghost" onclick="resetForm()">Clear</button><button class="btn" onclick="window.print()">Print / Save PDF</button></div>
</div>
<div class="main">
  <div class="panel">
    <div class="group batch-box">
      <div class="group-title">Batch from Excel 批量生成</div>
      <input type="file" id="batchFile" accept=".xlsx,.xls,.csv">
      <div class="hint">第一张工作表需有「款号」「成分」「数量」列；可选「品牌」「性别」「产地」和各洗护列。</div>
      <label class="check"><input type="checkbox" id="mergeAll"> 印款号的品牌（SH / ADV / CC / EdgeHill）也合并</label>
      <div class="btn-row">
        <button type="button" class="btn ghost small" id="btnTemplate">下载下单模板</button>
        <button type="button" class="btn small batch-only" id="btnExport">导出结果 Excel</button>
        <button type="button" class="btn ghost small batch-only" id="btnExit">返回单个标签</button>
      </div>
      <label class="field">品牌默认洗护（表中洗护留空时使用）</label>
      <select id="presetBrand"></select>
      <div class="qbox small-box" id="presetInfo"></div>
      <div class="btn-row">
        <button type="button" class="btn ghost small" id="presetSave">用下方「Care Instructions」设为此品牌默认</button>
        <button type="button" class="btn ghost small" id="presetReset">恢复模板默认</button>
      </div>
    </div>
    <div id="single">
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
        ''' + options(DRYCLEAN, 0) + '''
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
  </div>
  <div class="preview-area">
    <div class="label-sheet" id="sheet"></div>
    <div id="batch">
      <div id="batchSummary" class="batch-summary"></div>
      <div id="batchTable" class="batch-table"></div>
      <div id="batchLabels"></div>
    </div>
  </div>
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
  if(m){const t=+m[1],nb={vm:2,m:1,n:0}[m[2]],nd={30:1,40:2,50:3,60:4}[t]||0;return svg(TUB+tubTxt(t>=70?String(t):t+'C')+dots(nd,26.3,20,4.4)+bars(nb,34.3,7.5,32.5))}
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
const BRANDS={S27CC:{name:'CLASS CLUB',tpl:'a_adv'},S27SH:{name:'SCENE & HEARD',tpl:'a_sym'},S27AD:{name:'ADVENTUREWEAR',tpl:'a_adv'},S27EC:{name:'EDGEHILL',tpl:'b'},S27AE:{name:'ANDY & EVAN',tpl:'c'}};
const CATS=['wash','bleach','tumble','natural','iron','dryclean','wet'];
function curTpl(){return $('templateOverride').value==='auto'?detectTemplate($('styleNo').value):$('templateOverride').value}

// 洗护选择 sel = {wash:i, bleach:i, ..., extras:[i]}
function formSel(){const o={};CATS.forEach(c=>o[c]=+$(c).value);o.extras=[...document.querySelectorAll('#extras input:checked')].map(c=>+c.value);return o}
function careOf(sel){const r=CATS.map(c=>CARE[c][sel[c]]).filter(x=>x&&x[1]!=='(none)');(sel.extras||[]).forEach(i=>r.push(CARE.extras[i]));return r}
const enL=x=>x[1].replace(/\.\s*$/,'');
// ANDY & EVAN 需要法语/西语；Excel 中缺译文的条目需提示
function missingFrEs(care){return care.filter(x=>!x[2]||!x[3]).map(x=>x[1])}
function symsOf(sel){return CATS.map(c=>CARE[c][sel[c]]).filter(x=>x&&x[0]).map(x=>SYM(x[0])).join('')}

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
function fixAbbr(s){return s.replace(/\bUsa\b/,'USA')}
function originEN(c){return 'Made in '+fixAbbr(titleCase(c[0]))}
function originFR(c){const g=c[1],m=g.match(/^(\S+)\s+(.*)$/);return 'Fabriqué '+(m?m[1].toLowerCase()+' '+titleCase(m[2]):titleCase(g))}
function originES(c){return 'Hecho en '+titleCase(c[2])}
// S27 规则：BATCH & TRACKING CODE = S27CC/SH/AD/EC/AE + / 工厂代码 / YY / MM（五个品牌相同）
function trackCode(brand){return brand+'/'+$('fty').value.trim()+'/'+$('ys').value.trim()}

/* 生成一个标签（ANDY & EVAN 为两张）。d 字段：
   tpl, w, L, fm, comp, care(rows), syms(html), country(row), rn, track, decor,
   styleLine(已转义, 印在标签上), qtyText(已转义), below(已转义, 标签下方的款号列表) */
function labelHTML(d){
  const box='width:'+d.w+'mm;height:'+d.L+'mm;--sec:'+((d.L-2*d.fm)/2)+'mm;', tail='<div class="tail" style="height:'+d.fm+'mm"></div>';
  const rn=esc(d.rn), track=esc(d.track), care=d.care;
  const qtyDiv=d.qtyText?'<div class="qty">'+d.qtyText+'</div>':'';
  const belowDiv=(d.below||d.qtyText)?'<div class="qty-below">'+(d.below?'<div class="styles">'+d.below+'</div>':'')+qtyDiv+'</div>':'';
  let h='';
  if(d.tpl==='b'){
    h+='<div class="label-wrap"><div class="care-label tpl-b" style="'+box+'">'+tail+'<div class="dash-line"></div>';
    h+='<div class="sec top"><div class="comp-b">'+esc(titleCase(d.comp))+'</div><div class="sp"></div>';
    if(d.decor)h+='<div class="decor-b">Exclusive<br>of Decoration</div><div class="gap" style="height:4mm"></div>';
    h+='<div class="origin-b nw">'+esc(originEN(d.country))+'</div></div><div class="dash-line"></div>';
    h+='<div class="sec bot"><div class="care-b">'+care.map(x=>esc(enL(x))).join('\n')+'</div><div class="gap" style="height:1.5mm"></div><div class="style-b'+(d.styleLine.includes('<br>')?'':' nw')+'">Style # '+d.styleLine+'</div><div class="gap" style="height:2.2mm"></div><div class="rn-ys nw">RN'+rn+'<br>'+track+'</div></div>';
    h+='<div class="dash-line"></div>'+tail+'</div>'+belowDiv+'</div>';
  }else if(d.tpl==='c'){
    const fr=translateComp(d.comp,1),es=translateComp(d.comp,2);
    const en=care.map(x=>esc(x[1].replace(/\./g,''))).join('<br>'), frc=care.map(x=>esc(x[2])).filter(Boolean).join('<br>'), esc_=care.map(x=>esc(x[3])).filter(Boolean).join('<br>');
    h+='<div class="label-wrap">';
    // 第一张：EN + FR
    h+='<div class="care-label tpl-c" style="'+box+'">'+tail+'<div class="dash-line"></div>';
    h+='<div class="sec s1"><div class="logo">ANDY &amp; EVAN<sup>®</sup></div><div class="sp"></div><div class="c-comp">'+esc(d.comp)+'</div><div class="sp"></div>';
    h+='<div class="c-care-en">'+en+'</div><div class="symbols">'+d.syms+'</div>';
    h+='<div class="c-meta">'+esc(fixAbbr(titleCase(originEN(d.country))))+'<br>RN#'+rn+'<br>'+track+'</div></div><div class="dash-line"></div>';
    h+='<div class="sec s2"><div class="c-comp">'+esc(fr.text)+'</div><div class="sp"></div><div class="c-care-fr">'+frc+'</div><div class="gap1"></div>';
    h+='<div class="c-addr">'+esc(originFR(d.country))+'<br>WPL 11590<br>David Peyser Sportswear<br>90 Spence Street<br>Bayshore, NY 11706<br>USA</div><div class="sp"></div></div>';
    h+='<div class="dash-line"></div>'+tail+'</div>';
    // 第二张：ES + 进口商
    h+='<div class="care-label tpl-c" style="'+box+'">'+tail+'<div class="dash-line"></div>';
    h+='<div class="sec s3"><div class="c-comp-es">'+esc(es.text)+'</div><div class="sp"></div><div class="c-care-es">'+esc_+'</div><div class="gap2"></div><div class="c-care-es">'+esc(originES(d.country))+'</div><div class="sp"></div></div><div class="dash-line"></div>';
    h+='<div class="sec s4"><div class="c-imp">IMPORTADO POR:<br>IMPORTADORA PRIMEX<br>S.A. DE C.V.<br>BLVD. MAGNOCENTRO<br>NO. 4 SAN FERNANDO<br>LA HERRADURA<br>HUIXQUILUCAN,<br>ESTADO DE MEXICO<br>C.P. 52765<br>RFC: IPR-903907-S70</div></div>';
    h+='<div class="dash-line"></div>'+tail+'</div>'+belowDiv+'</div>';
  }else{
    // SH / ADV / CC：数量印在下折边内（与 Dillards 模板一致）；合并时款号列表放在标签下方
    h+='<div class="label-wrap"><div class="care-label tpl-a" style="'+box+'">'+tail+'<div class="dash-line"></div>';
    h+='<div class="sec top"><div class="sx">'+esc(d.comp.toUpperCase())+'</div><div class="sp"></div><div class="meta nw"><div class="origin">'+esc(originEN(d.country).toUpperCase())+'</div><div>RN#'+rn+'</div><div>'+track+'</div></div></div><div class="dash-line"></div>';
    h+='<div class="sec bot"><div class="sx">'+care.map(x=>esc(enL(x).toUpperCase())).join('\n')+'</div><div class="sp"></div>';
    if(d.tpl==='a_sym')h+='<div class="symbols">'+d.syms+'</div><div class="gap" style="height:3.55mm"></div>';
    h+='<div class="sx'+(d.styleLine.includes('<br>')?'':' nw')+'">STYLE '+d.styleLine+'</div></div><div class="dash-line"></div>';
    h+='<div class="tail" style="height:'+d.fm+'mm">'+(d.below?'':qtyDiv)+'</div></div>'+(d.below?belowDiv:'')+'</div>';
  }
  return h;
}

let lastTpl=null;
function applyTemplateDefaults(tpl){const t=TPL[tpl];$('labelWidth').value=t.w;$('labelLength').value=t.l;$('foldMm').value=t.fold;$('rn').value=t.rn}
function render(){
  const tpl=curTpl(), brand=brandCode($('styleNo').value);
  if(tpl!==lastTpl){applyTemplateDefaults(tpl);lastTpl=tpl}
  $('brandBadge').innerHTML='<span class="brand-badge">'+esc(TPL[tpl].name)+' · '+brand+'</span>';
  const sel=formSel(), comp=$('composition').value.replace(/\s+$/,''), qty=$('qty').value.trim();
  const d={tpl, w:parseFloat($('labelWidth').value)||TPL[tpl].w, L:parseFloat($('labelLength').value)||TPL[tpl].l, fm:Math.max(0,parseFloat($('foldMm').value)||0),
    comp, care:careOf(sel), syms:symsOf(sel), country:COUNTRY[+$('country').value]||COUNTRY[0], rn:$('rn').value.trim(),
    track:$('trackOverride').value.trim()||trackCode(brand), decor:$('decor').checked, styleLine:esc($('styleNo').value.trim()),
    qtyText:qty?'数量：'+esc(qty):'', below:tpl==='c'&&qty?esc($('styleNo').value.trim()):''};
  const warns=[];
  if(tpl==='c'){const m=translateComp(comp,1).missing;if(m.length)warns.push('No FR/ES translation in the S27 rule for: '+[...new Set(m)].join(', '));const mc=missingFrEs(d.care);if(mc.length)warns.push('S27 rule has no FR/ES text for: '+mc.join(', '))}
  $('sheet').innerHTML=labelHTML(d).repeat(parseInt($('copies').value));
  $('sheet').classList.toggle('page-ae',tpl==='c');
  const r=fitAll($('sheet'));
  if(r.bad)warns.push('Content does not fit the label: shorten the text or change width/length.');
  else if(r.shrunk)warns.push('Note: font reduced below the template size so the content fits.');
  $('fitWarn').textContent=warns.join('\n');
}

// 各区块内容超出时整体按比例缩小字号（--k），最小 70%；仍超出则标红
function overflowing(el){return el.scrollHeight>el.clientHeight+0.5||el.scrollWidth>el.clientWidth+0.5}
function fitLabel(lab){
  let ok=true,shrunk=false;
  lab.querySelectorAll('.sec').forEach(el=>{
    let k=1;el.style.setProperty('--k',k);
    while(overflowing(el)&&k>0.7){k=Math.round((k-0.02)*100)/100;el.style.setProperty('--k',k)}
    if(overflowing(el))ok=false;
    if(k<1)shrunk=true;
  });
  lab.classList.toggle('over',!ok);
  return {ok,shrunk};
}
function fitAll(root){let bad=0,shrunk=false;root.querySelectorAll('.care-label').forEach(l=>{const r=fitLabel(l);if(!r.ok)bad++;if(r.shrunk)shrunk=true});return {bad,shrunk}}

function resetForm(){$('composition').value='';$('styleNo').value='';$('qty').value='';$('trackOverride').value='';render()}

// =====================================================================
// 批量：上传 Excel → 按「品牌 + 性别 + 成分 + 洗护 + 产地」合并 → 结果表 + 标签
// =====================================================================
// 品牌默认洗护：全部统一为 MACHINE WASH COLD WITH LIKE COLORS GENTLE CYCLE + TUMBLE DRY LOW TEMPERATURE（EdgeHill 漂白按其模板），可在页面上用当前设置覆盖（保存在本机浏览器）
const PRESET_BUILTIN={
  S27CC:{wash:2,bleach:0,tumble:1,natural:0,iron:1,dryclean:0,wet:0,extras:[]},
  S27SH:{wash:2,bleach:0,tumble:1,natural:0,iron:1,dryclean:0,wet:0,extras:[]},
  S27AD:{wash:2,bleach:0,tumble:1,natural:0,iron:1,dryclean:0,wet:0,extras:[]},
  S27EC:{wash:2,bleach:1,tumble:1,natural:0,iron:1,dryclean:0,wet:0,extras:[]},
  S27AE:{wash:2,bleach:0,tumble:1,natural:0,iron:1,dryclean:0,wet:0,extras:[]}
};
function loadPresets(){let p={};try{p=JSON.parse(localStorage.getItem('careLabelPresets')||'{}')}catch(e){}return Object.assign({},PRESET_BUILTIN,p)}
function savePreset(brand,sel){let p={};try{p=JSON.parse(localStorage.getItem('careLabelPresets')||'{}')}catch(e){}p[brand]=sel;try{localStorage.setItem('careLabelPresets',JSON.stringify(p))}catch(e){}}
function resetPresets(){try{localStorage.removeItem('careLabelPresets')}catch(e){}}

const HEAD={
  style:['款号','款式','款式号','style','styleno','style#','stylenumber','styleno.'],
  comp:['成分','成份','composition','fabric','fabriccontent','content'],
  qty:['数量','qty','quantity','pcs','labelqty'],
  qtyLoss:['含损耗','含损耗数量','qtywithloss'],
  qtyOrder:['订单数','订单数量','orderqty','order'],
  gender:['性别','男女','男女童','男童/女童','gender','boys/girls','sex'],
  brand:['品牌','brand','label','brand(label)','品牌(label)'],
  origin:['产地','原产地','origin','countryoforigin','country'],
  wash:['水洗','washing','wash'], bleach:['漂白','bleaching','bleach'], tumble:['烘干','滚筒烘干','tumbledrying','tumbledry','drying'],
  natural:['晾干','自然晾干','naturaldrying'], iron:['熨烫','ironing','iron'], dryclean:['干洗','drycleaning','professionaldrycare','professionalcare'], wet:['湿洗','wetcleaning','professionalwetcare']
};
const nk=s=>String(s==null?'':s).toLowerCase().replace(/[\s:：_\-（）()]/g,'');
function findHeader(rows){
  for(let r=0;r<Math.min(rows.length,15);r++){
    const cols={};
    rows[r].forEach((v,i)=>{const k=nk(v);for(const [f,names] of Object.entries(HEAD)){if(cols[f]==null&&names.some(n=>nk(n)===k))cols[f]=i}});
    if(cols.style!=null&&cols.comp!=null)return {row:r,cols};
  }
  return null;
}
function normGender(v){v=String(v||'').trim().toLowerCase();if(!v)return '';if(/男|boy|^b$|^m$|male/.test(v)&&!/female/.test(v))return '男童';if(/女|girl|^g$|^f$|female/.test(v))return '女童';return String(v)}
function brandFromText(v){
  const s=String(v||'').toUpperCase().replace(/[^A-Z0-9]/g,'');if(!s)return '';
  const m={CLASSCLUB:'S27CC',CC:'S27CC',S27CC:'S27CC',SCENEHEARD:'S27SH',SCENEANDHEARD:'S27SH',SH:'S27SH',S27SH:'S27SH',ADVENTUREWEAR:'S27AD',AD:'S27AD',ADV:'S27AD',S27AD:'S27AD',EDGEHILL:'S27EC',EC:'S27EC',EH:'S27EC',S27EC:'S27EC',ANDYEVAN:'S27AE',ANDYANDEVAN:'S27AE',AE:'S27AE',S27AE:'S27AE'};
  return m[s]||'';
}
const nopt=s=>String(s||'').toLowerCase().replace(/[^a-z0-9°]/g,'');
// 先按下拉框名称（含温度 / P、F 区分）匹配，再按 Excel 原文匹配；原文对应多个选项时返回 -2
function matchCare(cat,text){const t=nopt(text);if(!t)return -1;const L=CARE[cat].findIndex(r=>nopt(r[4])===t);if(L>=0)return L;const hits=CARE[cat].map((r,i)=>nopt(r[1])===t?i:-1).filter(i=>i>=0);return hits.length===1?hits[0]:(hits.length?-2:-1)}
function matchCountry(text){const t=nopt(String(text||'').replace(/made\s*in/i,''));if(!t)return -1;return COUNTRY.findIndex(c=>nopt(c[0])===t)}
function normCompKey(s){return String(s).toLowerCase().replace(/[\s,，;；.]/g,'')}
// 百分比检查：按部位（Shell: / Lining: …）分段，每段合计应为 100%；没有部位名时整个成分合计 100%
function checkPct(comp){
  const segs=comp.split(/(?<![A-Za-z])(?=[A-Za-z][A-Za-z &\/\d]*\s*[:：])/).map(x=>x.trim()).filter(Boolean);
  const bad=[];segs.forEach(seg=>{const nums=[...seg.matchAll(/(\d+(?:\.\d+)?)\s*%/g)].map(m=>+m[1]);if(!nums.length)return;const sum=Math.round(nums.reduce((a,b)=>a+b,0)*100)/100;if(sum!==100)bad.push(seg.replace(/\s+/g,' ')+' = '+sum+'%')});return bad}
const fmtQ=n=>String(n);

let BATCH=null; // {groups, rows, file}
function parseWorkbook(wb,fileName){
  const ws=wb.Sheets[wb.SheetNames[0]];
  const rows=XLSX.utils.sheet_to_json(ws,{header:1,defval:'',raw:false});
  const hd=findHeader(rows);
  if(!hd)throw new Error('找不到表头：第一张工作表需要有「款号」和「成分」两列。');
  const c=hd.cols, qCol=c.qty!=null?c.qty:(c.qtyLoss!=null?c.qtyLoss:c.qtyOrder);
  const presets=loadPresets(), defCountry=+$('country').value, mergeAll=$('mergeAll').checked;
  const items=[];
  for(let r=hd.row+1;r<rows.length;r++){
    const row=rows[r], style=String(row[c.style]||'').trim(), comp=String(row[c.comp]||'').replace(/\r/g,'').trim();
    if(!style&&!comp)continue;
    if(/^(合计|总计|total)$/i.test(style))continue;
    const notes=[];
    const brand=brandFromText(c.brand!=null?row[c.brand]:'')||brandCode(style);
    if(!BRANDS[brand])notes.push('无法识别品牌');
    const tpl=(BRANDS[brand]||{tpl:'a_adv'}).tpl;
    const qtyRaw=qCol!=null?String(row[qCol]).replace(/[,，\s]/g,''):'';
    const qty=qtyRaw===''?0:Number(qtyRaw);
    if(qCol==null||qtyRaw===''||isNaN(qty))notes.push('数量为空或不是数字');
    if(!comp)notes.push('成分为空');
    const sel=Object.assign({},presets[brand]||PRESET_BUILTIN.S27SH);sel.extras=(sel.extras||[]).slice();
    CATS.forEach(cat=>{if(c[cat]==null)return;const v=String(row[c[cat]]||'').trim();if(!v)return;const i=matchCare(cat,v);if(i===-2)notes.push('洗护「'+v+'」对应多个选项，请按「Care options」页写明（如温度或 P/F），已用品牌默认');else if(i<0)notes.push('洗护「'+v+'」不在 S27 规则中，已用品牌默认');else sel[cat]=i});
    let country=defCountry;if(c.origin!=null&&String(row[c.origin]).trim()){const i=matchCountry(row[c.origin]);if(i<0)notes.push('产地「'+row[c.origin]+'」不在 S27 国家表中，已用默认');else country=i}
    checkPct(comp).forEach(x=>notes.push('成分百分比不等于 100%：'+x));
    if(tpl==='c'){const m=translateComp(comp,1).missing;if(m.length)notes.push('无 FR/ES 翻译：'+[...new Set(m)].join(', '));const mc=missingFrEs(careOf(sel));if(mc.length)notes.push('S27 规则中缺少法语/西语：'+mc.join(', '))}
    items.push({row:r+1,style,comp,qty:isNaN(qty)?0:qty,gender:normGender(c.gender!=null?row[c.gender]:''),brand,tpl,sel,country,notes});
  }
  // 合并：同品牌 + 同性别 + 同成分 + 同洗护 + 同产地；标签上印款号的模板（SH/ADV/CC/EdgeHill）默认按款分开
  const groups=[],map=new Map();
  items.forEach(it=>{
    const key=[it.brand,it.gender,normCompKey(it.comp),JSON.stringify(it.sel),it.country,(it.tpl!=='c'&&!mergeAll)?it.style:''].join('|');
    let g=map.get(key);
    if(!g){g={brand:it.brand,tpl:it.tpl,gender:it.gender,comp:it.comp,sel:it.sel,country:it.country,items:[],notes:[]};map.set(key,g);groups.push(g)}
    g.items.push(it);it.notes.forEach(n=>{if(!g.notes.includes(n))g.notes.push(n)});
  });
  const order=Object.keys(BRANDS);
  groups.sort((a,b)=>(order.indexOf(a.brand)+100*(order.indexOf(a.brand)<0))-(order.indexOf(b.brand)+100*(order.indexOf(b.brand)<0))||a.gender.localeCompare(b.gender));
  groups.forEach((g,i)=>{g.no=i+1;g.total=g.items.reduce((s,x)=>s+x.qty,0);g.styles=g.items.map(x=>x.style);g.qtys=g.items.map(x=>x.qty);g.track=trackCode(g.brand)});
  BATCH={groups,items,file:fileName,qtyHeader:qCol!=null?rows[hd.row][qCol]:''};
  renderBatch();
}
function brandName(b){return (BRANDS[b]||{name:b}).name}
function renderBatch(){
  const B=BATCH;if(!B)return;
  document.body.classList.add('batch-mode');
  let h='';let lastBrand=null;
  B.groups.forEach(g=>{
    const t=TPL[g.tpl], merged=g.items.length>1;
    const styleLine=merged&&g.tpl!=='c'?g.styles.map(esc).join('<br>'):esc(g.styles[0]);
    const qtyText='数量：'+(merged?g.qtys.map(fmtQ).join(' + ')+' = '+g.total:g.total);
    const d={tpl:g.tpl,w:t.w,L:t.l,fm:t.fold,comp:g.comp,care:careOf(g.sel),syms:symsOf(g.sel),country:COUNTRY[g.country],rn:t.rn,track:g.track,decor:$('decor').checked,
      styleLine,qtyText,below:(merged||g.tpl==='c')?g.styles.map(esc).join(' + '):''};
    if(g.brand!==lastBrand){if(lastBrand!==null)h+='</div></div>';h+='<div class="brand-sec'+(g.tpl==='c'?' page-ae':'')+'"><div class="brand-head">'+esc(brandName(g.brand))+' ('+esc(g.brand)+')</div><div class="label-sheet batch-sheet">';lastBrand=g.brand}
    h+='<div class="batch-item" data-no="'+g.no+'"><div class="batch-tag">#'+g.no+(g.gender?' · '+esc(g.gender):'')+'</div>'+labelHTML(d)+'</div>';
  });
  if(lastBrand!==null)h+='</div></div>';
  $('batchLabels').innerHTML=h;
  // 自动适配并把放不下/缩小的情况记入备注
  B.groups.forEach(g=>{
    const el=document.querySelector('.batch-item[data-no="'+g.no+'"]');let bad=false,shr=false;
    el.querySelectorAll('.care-label').forEach(l=>{const r=fitLabel(l);if(!r.ok)bad=true;if(r.shrunk)shr=true});
    g.fit=bad?'放不下，需缩短文字':(shr?'已自动缩小字号':'');
  });
  const totalQty=B.groups.reduce((s,g)=>s+g.total,0), nNotes=B.groups.filter(g=>g.notes.length||g.fit.startsWith('放不下')).length;
  $('batchSummary').innerHTML='<b>'+esc(B.file)+'</b>：'+B.items.length+' 行 → '+B.groups.length+' 个标签，合计数量 '+totalQty+(B.qtyHeader?'（数量取自「'+esc(B.qtyHeader)+'」列）':'')+(nNotes?' · <span style="color:#e63946">'+nNotes+' 个需要检查</span>':'');
  $('batchTable').innerHTML='<table><thead><tr><th>#</th><th>品牌</th><th>性别</th><th>成分</th><th>洗护</th><th>款号</th><th>数量</th><th>合计</th><th>追踪码</th><th>备注</th></tr></thead><tbody>'+
    B.groups.map(g=>'<tr'+((g.notes.length||g.fit.startsWith('放不下'))?' class="warnrow"':'')+'><td>'+g.no+'</td><td>'+esc(brandName(g.brand))+'</td><td>'+esc(g.gender||'-')+'</td><td class="pre">'+esc(g.comp)+'</td><td>'+careOf(g.sel).map(x=>esc(x[1])).join('<br>')+'</td><td>'+g.styles.map(esc).join(' + ')+'</td><td>'+g.qtys.join(' + ')+'</td><td><b>'+g.total+'</b></td><td>'+esc(g.track)+'</td><td>'+[...g.notes,g.fit].filter(Boolean).map(esc).join('<br>')+'</td></tr>').join('')+'</tbody></table>';
}
function exportBatch(){
  if(!BATCH)return;
  const g1=[['#','品牌 Brand','品牌代码','性别','成分 Composition','洗护 Care (EN)','款号 Styles','数量 Qty','合计 Total','追踪码 Tracking','模板','备注']];
  BATCH.groups.forEach(g=>g1.push([g.no,brandName(g.brand),g.brand,g.gender,g.comp,careOf(g.sel).map(x=>x[1]).join(' / '),g.styles.join(' + '),g.qtys.join(' + '),g.total,g.track,TPL[g.tpl].name,[...g.notes,g.fit].filter(Boolean).join('; ')]));
  const g2=[['原表行号','款号','品牌','性别','成分','数量','合并到标签 #']];
  BATCH.groups.forEach(g=>g.items.forEach(it=>g2.push([it.row,it.style,brandName(it.brand),it.gender,it.comp,it.qty,g.no])));
  g2.sort((a,b)=>typeof a[0]==='number'&&typeof b[0]==='number'?a[0]-b[0]:0);
  const wb=XLSX.utils.book_new();
  const s1=XLSX.utils.aoa_to_sheet(g1);s1['!cols']=[{wch:4},{wch:16},{wch:8},{wch:6},{wch:28},{wch:40},{wch:36},{wch:20},{wch:8},{wch:16},{wch:14},{wch:40}];
  const s2=XLSX.utils.aoa_to_sheet(g2);s2['!cols']=[{wch:8},{wch:20},{wch:16},{wch:6},{wch:30},{wch:8},{wch:12}];
  XLSX.utils.book_append_sheet(wb,s1,'Labels 标签');XLSX.utils.book_append_sheet(wb,s2,'Styles 明细');
  XLSX.writeFile(wb,'care-labels-'+BATCH.file.replace(/\.[^.]+$/,'')+'.xlsx');
}
function downloadInputTemplate(){
  const head=['品牌 Brand','款号 Style','成分 Composition','性别 Gender','数量 Qty','产地 Origin','水洗 Washing','漂白 Bleaching','烘干 Tumble drying','自然晾干 Natural drying','熨烫 Ironing','干洗 Dry care','湿洗 Wet care'];
  const ex=[['','F26G21683B-LBA','95% Cotton 5% Elastane','女童',400],['','F26G21684B-WHA','95% Cotton 5% Elastane','女童',1250],['','F26G31323A-WHA','95% Cotton 5% Elastane','男童',720],['','F64SW840B/J','100% Cotton','男童',3400],['','F64EH44024','30% Wool\n25% Nylon\n45% Acrylic','女童',2200,'','','Only non-chlorine bleach when needed']];
  const opts=[['分类 Category','可填写的内容（英文，与 S27 规则一致）']];
  [['水洗 Washing','wash'],['漂白 Bleaching','bleach'],['烘干 Tumble drying','tumble'],['自然晾干 Natural drying','natural'],['熨烫 Ironing','iron'],['干洗 Dry care','dryclean'],['湿洗 Wet care','wet']].forEach(([l,c])=>CARE[c].forEach(r=>{if(r[1]!=='(none)')opts.push([l,r[4]])}));
  const note=[['说明'],['必填：款号、成分、数量。品牌可留空（按款号开头自动识别）。'],['性别填 男童 / 女童（或 Boys / Girls）。'],['洗护各列留空 = 使用该品牌的默认洗护；填写时请从「Care options」页复制原文。'],['合并规则：同品牌 + 同性别 + 同成分 + 同洗护 + 同产地 → 合并为一个标签，数量相加。']];
  const wb=XLSX.utils.book_new();const s=XLSX.utils.aoa_to_sheet([head,...ex]);s['!cols']=head.map((h,i)=>({wch:[14,18,30,10,8,10,34,34,26,26,32,30,30][i]}));
  XLSX.utils.book_append_sheet(wb,s,'Order 下单');XLSX.utils.book_append_sheet(wb,XLSX.utils.aoa_to_sheet(opts),'Care options');XLSX.utils.book_append_sheet(wb,XLSX.utils.aoa_to_sheet(note),'说明');
  XLSX.writeFile(wb,'care-label-order-template.xlsx');
}
function needXLSX(){if(typeof XLSX==='undefined'){alert('读取/导出 Excel 需要联网加载组件（cdnjs），请检查网络后刷新页面。');return false}return true}
function exitBatch(){BATCH=null;document.body.classList.remove('batch-mode');$('batchFile').value='';$('batchLabels').innerHTML='';$('batchTable').innerHTML='';$('batchSummary').innerHTML='';render()}
function renderPresetInfo(){const p=loadPresets(),b=$('presetBrand').value;$('presetInfo').innerHTML=careOf(p[b]).map(x=>esc(x[1])).join('<br>')}

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
  [['wash','1) Washing'],['bleach','2) Bleaching'],['tumble','3.1) Tumble drying'],['natural','3.2) Natural drying'],['iron','4) Ironing'],['dryclean','5.1) Professional dry care'],['wet','5.2) Professional wet care'],['extras','Additional (no symbol)']].forEach(([cat,lab])=>{
    const og=document.createElement('optgroup');og.label=lab;
    CARE[cat].forEach((r,i)=>{if(r[1]==='(none)')return;const o=document.createElement('option');o.value=cat+':'+i;o.textContent=r[4];og.appendChild(o)});
    $('qCare').appendChild(og);
  });
  $('qCare').addEventListener('change',function(){
    if(!this.value){$('qCareResult').innerHTML='Select to view...';return}
    const [cat,i]=this.value.split(':'),f=CARE[cat][+i];
    $('qCareResult').innerHTML=(f[0]?'<div style="margin-bottom:6px;">'+SYM(f[0])+'</div>':'<div style="color:#86909c">No symbol (text only)</div>')+'<b>EN:</b> '+esc(f[1])+'<br><b>FR:</b> '+esc(f[2])+'<br><b>ES:</b> '+esc(f[3]);
  });
  $('qSymbolChart').innerHTML=SYMBOL_CHART.map(([cat,items])=>'<div class="chart-cat">'+esc(cat)+'</div><div class="chart">'+items.map(([k,l])=>'<div class="chart-item">'+SYM(k)+'<span>'+esc(l)+'</span></div>').join('')+'</div>').join('');
  document.querySelectorAll('#single input,#single select,#single textarea').forEach(e=>{e.addEventListener('input',render);e.addEventListener('change',render)});
  // 批量
  $('presetBrand').innerHTML=Object.entries(BRANDS).map(([k,v])=>'<option value="'+k+'">'+esc(v.name)+'</option>').join('');
  $('presetBrand').addEventListener('change',renderPresetInfo);renderPresetInfo();
  $('presetSave').addEventListener('click',()=>{savePreset($('presetBrand').value,formSel());renderPresetInfo();if(BATCH)$('batchFile').dispatchEvent(new Event('change'))});
  $('presetReset').addEventListener('click',()=>{resetPresets();renderPresetInfo();if(BATCH)$('batchFile').dispatchEvent(new Event('change'))});
  $('batchFile').addEventListener('change',function(){
    const f=this.files[0];if(!f||!needXLSX())return;
    const rd=new FileReader();
    rd.onload=e=>{try{parseWorkbook(XLSX.read(new Uint8Array(e.target.result),{type:'array'}),f.name)}catch(err){alert(err.message||String(err))}};
    rd.readAsArrayBuffer(f);
  });
  $('mergeAll').addEventListener('change',()=>{if(BATCH)$('batchFile').dispatchEvent(new Event('change'))});
  $('btnTemplate').addEventListener('click',()=>{if(needXLSX())downloadInputTemplate()});
  $('btnExport').addEventListener('click',()=>{if(needXLSX())exportBatch()});
  $('btnExit').addEventListener('click',exitBatch);
  if(document.fonts&&document.fonts.ready)document.fonts.ready.then(render);
  render();
})();
</script>
</body>
</html>'''

with open(os.path.join(HERE, '水洗标生成器.html'), 'w', encoding='utf-8') as f:
    f.write(html)
print('OK', len(html))
