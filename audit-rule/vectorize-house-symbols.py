import json,base64,io,math
from PIL import Image
p='data/house_symbol_assets.json';assets=json.load(open(p,encoding='utf8'))
def simplify(points,eps=.45):
 if len(points)<3:return points
 a,b=points[0],points[-1];dx=b[0]-a[0];dy=b[1]-a[1];den=math.hypot(dx,dy)
 distances=[abs(dy*(q[0]-a[0])-dx*(q[1]-a[1]))/den if den else math.dist(q,a) for q in points];m=max(distances);i=distances.index(m)
 return simplify(points[:i+1],eps)[:-1]+simplify(points[i:],eps) if m>eps else [a,b]
for k,a in assets.items():
 if not a['uri'].startswith('data:image/png'):continue
 im=Image.open(io.BytesIO(base64.b64decode(a['uri'].split(',')[1]))).convert('RGBA');bg=Image.new('RGBA',im.size,'white');bg.alpha_composite(im);g=bg.convert('L');W,H=g.size;black={(x,y) for y in range(H) for x in range(W) if g.getpixel((x,y))<150};edges={}
 for x,y in black:
  for neighbor,start,end in [((x,y-1),(x,y),(x+1,y)),((x+1,y),(x+1,y),(x+1,y+1)),((x,y+1),(x+1,y+1),(x,y+1)),((x-1,y),(x,y+1),(x,y))]:
   if neighbor not in black:edges.setdefault(start,[]).append(end)
 paths=[]
 while edges:
  start=next(iter(edges));v=start;points=[v]
  while True:
   end=edges[v].pop()
   if not edges[v]:del edges[v]
   points.append(end);v=end
   if v==start or v not in edges:break
  if len(points)<4:continue
  points=simplify(points)
  paths.append('M'+' L'.join(str(x)+','+str(y) for x,y in points)+' Z')
 svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 '+str(W)+' '+str(H)+'"><path fill="#231f20" fill-rule="evenodd" d="'+' '.join(paths)+'"/></svg>'
 a['rasterReference']=a['uri'];a['uri']='data:image/svg+xml;base64,'+base64.b64encode(svg.encode()).decode();a['vectorMethod']='Contour trace of HOUSE original, binary threshold150; simplification0.45 source pixel, no semantic redrawing.'
json.dump(assets,open(p,'w',encoding='utf8'),ensure_ascii=False,indent=2)
