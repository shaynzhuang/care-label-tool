import json,zipfile,xml.etree.ElementTree as E,io,base64,re
from PIL import Image
import openpyxl
source=r'C:/Users/shayn/Desktop/S27  HOUSE CARE LABEL RULE - 9.10 (4).xlsx'
w=openpyxl.load_workbook(source,data_only=True);old=json.load(open('data/excel_care.json',encoding='utf8'));diff=[]
norm=lambda v:re.sub(r'\s+',' ',str(v or '')).strip()
for k,v in old.items():
 s=w['brief info'] if k.startswith('brief!') else w['FABRIC CARE GUIDE 7.9'];cell=s[k.split('!')[-1]];got=[s.cell(cell.row,cell.column+i).value or '' for i in range(3)]
 if list(map(norm,v))!=list(map(norm,got)):diff.append(k)
print('SOURCE CARE',len(old),'meaningful text differences',diff)
z=zipfile.ZipFile(source)
mapping={'washX':3,'washHand':38,'w30vm':34,'w30m':39,'w30n':42,'w40vm':4,'w40m':5,'w40n':6,'w50m':8,'w50n':9,'w60m':7,'w60n':10,'w70n':11,'w95n':12,'bleachX':37,'bleachNC':13,'bleachAny':14,'dryX':31,'dry1':35,'dry2':30,'line':25,'dripLine':26,'flat':41,'dripFlat':27,'dripLineShade':28,'flatShade':32,'dripFlatShade':29,'ironX':40,'iron1':33,'iron2':15,'iron3':16,'dcX':36,'dcP1':19,'dcP':20,'dcF1':17,'dcF':18,'wetX':23,'wet2':24,'wet1':22,'wet':21}
# flatShade has no distinct source at row17? image32 is drip-line shade; row15 absent: leave original until source verified.
# P15 lineShade has no anchored original: keep explicitly unverified fallback.
assets={}
for key,n in mapping.items():
 names=[name for name in z.namelist() if name.lower().startswith('xl/media/image'+str(n)+'.')]
 if not names:continue
 a=Image.open(io.BytesIO(z.read(names[0]))).convert('RGBA');bg=Image.new('RGBA',a.size,'white');bg.alpha_composite(a);m=bg.convert('L').point(lambda p:255 if p<150 else 0);box=m.getbbox();a=a.crop(box);stream=io.BytesIO();a.save(stream,format='PNG');assets[key]={'uri':'data:image/png;base64,'+base64.b64encode(stream.getvalue()).decode(),'w':a.width,'h':a.height,'body':a.height,'source':'FABRIC CARE GUIDE 7.9 / '+names[0]}
json.dump(assets,open('data/house_symbol_assets.json','w',encoding='utf8'),ensure_ascii=False,indent=2)
print('SOURCE SYMBOLS',len(assets))
