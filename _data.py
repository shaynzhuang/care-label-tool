# -*- coding: utf-8 -*-
# 按 S27 HOUSE CARE LABEL RULE Excel 实际内容重建查询面板数据

# 成分 EN/FR/ES（来自 Excel 列2-4）
FABRIC = [
    ("ELASTANE / SPANDEX", "Élasthanne", "Elastano"),
    ("ACRYLIC", "Acrylique", "Acrílico"),
    ("MODAL", "modal", "MODAL"),
    ("MODACRYLIC", "modacrylique", "MODACRÍLICO"),
    ("RAYON / VISCOSE", "viscose", "VISCOSA"),
    ("NYLON / POLYAMIDE", "polyamide (nylon)", "POLIAMIDA / NAILON"),
    ("POLYESTER", "polyester", "poliéster"),
    ("POLYURETHANE", "polyuréthane", "POLIURETANO"),
    ("COTTON", "coton", "ALGODÓN"),
    ("CASHMERE", "cachemire", "CACHEMIRA"),
    ("DOWN", "duvet", "PLUMÓN"),
    ("FEATHER", "plumes", "PLUMAS"),
    ("WATERFOWL FEATHERS", "plumes d'oiseaux aquatiques", "PLUMAS DE AVES ACUÁTICAS"),
    ("LINEN", "lin", "LINO"),
    ("MOHAIR", "mohair", "MOHAIR"),
    ("ORGANIC COTTON", "coton bio", "ALGODÓN ORGÁNICO"),
    ("SILK", "soie", "SEDA"),
    ("WOOL", "laine", "LANA"),
    ("SHELL", "Matière principale", "Cuerpo"),
    ("LINING", "Doublure", "Forro"),
    ("FILLING", "Garnissage", "Relleno"),
    ("EXCLUSIVE OF DECORATION", "Sauf garnitures", "Excepto adornos"),
    ("CROCHET", "Articles pour crochet", "Artículos de ganchillo"),
    ("CONTRAST FABRIC", "Tissu de contraste", "Tejido de contraste"),
    ("TULLE", "Tulle", "Tul"),
    ("LACE", "Dentelle", "Encaje"),
    ("BODY", "Corps", "Cuerpo"),
]

# 洗护指令（来自 Excel 列11-13 Washing, 16-18 Bleaching/Drying, 21-23 Ironing/Pro Care）
# 格式: (分类, EN, FR, ES, 符号key)
CARE = [
    # Washing
    ("1) Washing", "Do not wash", "Lavage interdit.", "No lavar", "washX"),
    ("1) Washing", "Hand wash", "Lavage à la main.", "Lavar a mano", "washHand"),
    ("1) Washing", "Machine wash cold with like colors. Gentle cycle.",
     "Lavage en machine max. 30°C. Laver avec des couleurs similaires. Cycle très délicat.",
     "30°C. Lavar con colores similares. Proceso muy suave.", "wash30"),
    ("1) Washing", "Mild Process (30-50°C)",
     "Lavage en machine max. 30-50°C, cycle délicat.",
     "Temp. máx. 30-50°C. Proceso suave.", "wash30"),
    ("1) Washing", "Normal Process (30-60°C)",
     "Lavage en machine max. 30-60°C, cycle normal.",
     "Temp. máx. 30-60°C. Proceso normal.", "wash40"),
    ("1) Washing", "Very mild process (40°C)",
     "Lavage en machine max. 40°C, cycle très délicat.",
     "40°C. Proceso muy suave.", "wash40"),
    ("1) Washing", "Wash with like colors", "Laver avec des couleurs similaires.", "Lavar con colores similares", "wash30"),
    ("1) Washing", "Do not use fabric softener", "Ne pas utiliser d'assouplissant.", "No usar suavizante", ""),
    ("1) Washing", "Wash before first use", "Laver avant la première utilisation.", "Lavar antes del primer uso", ""),
    # Bleaching
    ("2) Bleaching", "Do not bleach.", "Pas de blanchiment.", "No usar lejía", "bleachX"),
    ("2) Bleaching", "Only Oxygen / non-chlorine bleach allowed",
     "Produits de blanchiment oxygénés uniquement.",
     "Solo blanqueador oxigenado / sin cloro permitido", "bleachOxygen"),
    ("2) Bleaching", "Any bleaching agent allowed",
     "Tous types de blanchiment autorisés.",
     "Cualquier agente blanqueador permitido", "bleachAny"),
    # Drying
    ("3) Drying", "Do not tumble dry", "Pas de séchage en tambour.", "No usar secadora", "dryX"),
    ("3) Drying", "Tumble dry low temperature (60°C)",
     "Séchage en tambour 60°C.",
     "Secadora baja, máx. 60°C", "dryLow"),
    ("3) Drying", "Tumble dry normal temperature (80°C)",
     "Séchage en tambour 80°C.",
     "Secadora normal, máx. 80°C", "dryMed"),
    ("3) Drying", "Line drying", "Séchage sur fil.", "Secar tendido", "lineDry"),
    ("3) Drying", "Drip line drying", "Séchage sur fil sans essorage.", "Secar colgado por goteo", "dripLine"),
    ("3) Drying", "Flat drying", "Séchage à plat.", "Secar extendido", "flatDry"),
    ("3) Drying", "Drip flat drying", "Séchage à plat sans essorage.", "Secado plano por goteo", "dripFlat"),
    ("3) Drying", "Line drying in shade", "Séchage sur fil à l'ombre.", "Secar colgado a la sombra", "lineShade"),
    ("3) Drying", "Flat drying in the shade", "Séchage à plat à l'ombre.", "Secar extendido a la sombra", "flatShade"),
    # Ironing
    ("4) Ironing", "Do not iron", "Ne pas repasser.", "No planchar", "ironX"),
    ("4) Ironing", "Iron at low temperature (max 110°C)",
     "Repasser max. 110°C.", "Planchar max. 110°C", "iron1"),
    ("4) Ironing", "Cool Iron from inside if needed",
     "Repasser au froid de l'intérieur si nécessaire.",
     "Planchar frío desde el interior si es necesario", "iron1"),
    ("4) Ironing", "Iron at medium temperature (max 150°C)",
     "Repasser max. 150°C.", "Planchar max. 150°C", "iron2"),
    ("4) Ironing", "Iron at high temperature (max 200°C)",
     "Repasser max. 200°C.", "Planchar max. 200°C", "iron3"),
    # Professional care
    ("5) Professional Care", "Do not dry clean", "Pas d'entretien professionnel à sec.", "No limpiar en seco", "dcX"),
    ("5) Professional Care", "Professional dry cleaning mild process",
     "Entretien professionnel à sec cycle modéré.",
     "Limpieza en seco, proceso suave", "dc"),
    ("5) Professional Care", "Professional dry cleaning normal process",
     "Entretien professionnel à sec cycle normal.",
     "Limpieza en seco, proceso normal", "dc"),
    ("5) Professional Care", "Do not wet clean", "Pas d'entretien professionnel à l'eau.", "No limpieza profesional mojado", "wetX"),
]

import json
print("FABRIC_JSON=" + json.dumps(FABRIC, ensure_ascii=False))
print("CARE_JSON=" + json.dumps(CARE, ensure_ascii=False))
