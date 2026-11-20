import os, json, shutil, uharfbuzz as hb
from mark import *
from fontTools.ttLib import TTFont
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

BLUE="#0B63F6"; INK="#0B1220"; WHITE="#FFFFFF"; BLACK="#000000"; MIST="#F4F7FF"
def SX(x,k=1.06): return 216+(x-216)*k
_sp=[(166,100),(160,168),(198,196),(240,216),(286,239),(288,272),(252,288),(236,296),(214,298),(190,304)]
SPINE=[(SX(x),y) for x,y in _sp]
CIRC=dict(left=(SX(146),231,61),top=(216,212,80),low=(SX(268),237,54))
MAIN=build(SPINE,24,round_r=2.4,**CIRC)
SMALL=build(SPINE,38,round_r=0,**CIRC)
BX0,BY0,BX1,BY1=MAIN.bounds; MW,MH=BX1-BX0,BY1-BY0
fmt=lambda v:f"{v:.2f}".rstrip('0').rstrip('.')
def mark_d(shape,cx,cy,width):
    x0,y0,x1,y1=shape.bounds; s=width/(x1-x0)
    pen=SVGPathPen(None,fmt); tp=TransformPen(pen,(s,0,0,s,cx-s*(x0+x1)/2,cy-s*(y0+y1)/2)); shape.draw(tp); return pen.getCommands(), s*(y1-y0)
FONT="/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"
def text_d(txt,x,baseline,size,tracking=-0.02,anchor="start",font=FONT):
    tt=TTFont(font); gs=tt.getGlyphSet(); order=tt.getGlyphOrder(); upm=tt['head'].unitsPerEm
    blob=hb.Blob.from_file_path(font);face=hb.Face(blob);f=hb.Font(face)
    buf=hb.Buffer();buf.add_str(txt);buf.guess_segment_properties();hb.shape(f,buf,{"kern":True,"liga":False})
    sc=size/upm;pen=SVGPathPen(None,fmt);cur=0;gl=[]
    for info,pos in zip(buf.glyph_infos,buf.glyph_positions):
        gl.append((order[info.codepoint],cur+pos.x_offset));cur+=pos.x_advance+tracking*upm
    total=(cur-tracking*upm)*sc
    ox=x-(total if anchor=="end" else total/2 if anchor=="middle" else 0)
    for name,gx in gl:
        tp=TransformPen(pen,(sc,0,0,-sc,ox+gx*sc,baseline)); gs[name].draw(tp)
    return pen.getCommands(),total,(tt['OS/2'].sCapHeight*sc)
def svg(w,h,body,bg=None,title="SatisfyCloud"):
    b=f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}"><title>{title}</title>{b}{body}</svg>\n'
def P(d,c): return f'<path fill="{c}" d="{d}"/>'
out="../dist"; shutil.rmtree(out,ignore_errors=True)
for s in ("svg","png","web","pdf","jpg"): os.makedirs(f"{out}/{s}")
files={}
def put(name,content): files[name]=content; open(f"{out}/svg/{name}.svg","w").write(content)
# palettes: (mark, text, bg)
PAL={"color":(BLUE,INK,None),"blue":(BLUE,BLUE,None),"white":(WHITE,WHITE,None),"black":(BLACK,BLACK,None),
     "white-on-blue":(WHITE,WHITE,BLUE),"color-on-white":(BLUE,INK,WHITE),"blue-on-mist":(BLUE,INK,MIST),"white-on-ink":(WHITE,WHITE,INK)}
# ---- mark only (square canvas 1024, mark = 62% width)
for k,(mc,tc,bg) in PAL.items():
    d,_=mark_d(MAIN,512,512,640); put(f"mark_{k}",svg(1024,1024,P(d,mc),bg,"SatisfyCloud icon"))
# tight mark (no padding) for designers
for k in ("color","white","black"):
    mc=PAL[k][0]; d,h=mark_d(MAIN,MW/2*1.0,MH/2,MW)
    d=mark_d(MAIN,0,0,MW)[0]
    put(f"mark-tight_{k}",svg(round(MW),round(MH),P(mark_d(MAIN,MW/2,MH/2,MW)[0],mc),None,"SatisfyCloud icon"))
# ---- lockups
def horizontal(k,com):
    mc,tc,bg=PAL[k]; pad=90; mw=400; _,mh=mark_d(MAIN,0,0,mw)
    size=mh*0.62; txt="SatisfyCloud"
    cap=0.727*size
    gap=mh*0.30; cy=pad+mh/2
    mcd,_=mark_d(MAIN,pad+mw/2,cy,mw)
    base=cy+cap/2; x=pad+mw+gap
    td,tw,_=text_d(txt,x,base,size)
    body=P(mcd,mc)+P(td,tc); W=x+tw
    if com:
        cd,cw,_=text_d(".com",x+tw+size*0.02,base,size,anchor="start",font="/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf")
        cc=BLUE if k=="color" else tc
        body+=P(cd,cc); W=x+tw+size*0.02+cw
    return svg(round(W+pad),round(mh+2*pad),body,bg)
def stacked(k,com):
    mc,tc,bg=PAL[k]; pad=110; mw=380; _,mh=mark_d(MAIN,0,0,mw)
    size=mw*0.27; txt="SatisfyCloud"
    td,tw,cap=text_d(txt,0,0,size)
    cwid=tw
    ctd=None
    if com:
        _,cw,_=text_d(".com",0,0,size,font="/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf"); cwid=tw+size*0.02+cw
    W=max(mw,cwid)+2*pad; cx=W/2
    mcd,_=mark_d(MAIN,cx,pad+mh/2,mw)
    base=pad+mh+mw*0.17+cap
    if com:
        td,tw,_=text_d(txt,cx-cwid/2,base,size,anchor="start")
        cd,cw,_=text_d(".com",cx-cwid/2+tw+size*0.02,base,size,anchor="start",font="/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf")
        cc=BLUE if k=="color" else tc
        body=P(mcd,mc)+P(td,tc)+P(cd,cc)
    else:
        td,tw,_=text_d(txt,cx,base,size,anchor="middle"); body=P(mcd,mc)+P(td,tc)
    return svg(round(W),round(base+pad*0.8),body,bg)
for k in PAL:
    put(f"lockup-horizontal_{k}",horizontal(k,False)); put(f"lockup-horizontal-com_{k}",horizontal(k,True))
    put(f"lockup-stacked_{k}",stacked(k,False)); put(f"lockup-stacked-com_{k}",stacked(k,True))
# ---- web icons
dsm,_=mark_d(SMALL,0,0,10)
def icon_sq(size,mc,bg,frac,radius=0,small=False):
    shape=SMALL if small else MAIN
    d,_=mark_d(shape,size/2,size/2,size*frac)
    b=f'<rect width="{size}" height="{size}" rx="{radius}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}">{b}<path fill="{mc}" d="{d}"/></svg>\n'
web={
 "favicon.svg":icon_sq(64,BLUE,None,0.94,small=True),
 "favicon-dark.svg":icon_sq(64,WHITE,None,0.94,small=True),
 "app-icon_1024.svg":icon_sq(1024,WHITE,BLUE,0.64),
 "app-icon-rounded_1024.svg":icon_sq(1024,WHITE,BLUE,0.64,radius=230),
 "maskable_512.svg":icon_sq(512,WHITE,BLUE,0.50),
 "safari-pinned-tab.svg":icon_sq(64,BLACK,None,0.94,small=True),
 "avatar-circle_1024.svg":f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024"><circle cx="512" cy="512" r="512" fill="{BLUE}"/><path fill="#fff" d="{mark_d(MAIN,512,512,560)[0]}"/></svg>\n',
}
for n,c in web.items(): open(f"{out}/web/{n}","w").write(c)
# OG image 1200x630
mcd,_=mark_d(MAIN,0,0,1)
og_mark,mh=mark_d(MAIN,330,315,300)
td,tw,cap=text_d("SatisfyCloud",520,315+0.727*110/2,110,anchor="start")
og=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630"><rect width="1200" height="630" fill="{BLUE}"/><path fill="#fff" d="{og_mark}"/><path fill="#fff" d="{td}"/></svg>\n'
open(f"{out}/web/og-image_1200x630.svg","w").write(og)
json.dump({"name":"SatisfyCloud","short_name":"SatisfyCloud","icons":[{"src":"/android-chrome-192.png","sizes":"192x192","type":"image/png"},{"src":"/android-chrome-512.png","sizes":"512x512","type":"image/png"},{"src":"/maskable-512.png","sizes":"512x512","type":"image/png","purpose":"maskable"}],"theme_color":BLUE,"background_color":"#FFFFFF","display":"standalone"},open(f"{out}/web/site.webmanifest","w"),indent=2)
open(f"{out}/web/head-snippet.html","w").write('''<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="mask-icon" href="/safari-pinned-tab.svg" color="#0B63F6">
<meta name="theme-color" content="#0B63F6">
<meta property="og:image" content="/og-image.png">
''')
print("svg done",len(os.listdir(f"{out}/svg")))
