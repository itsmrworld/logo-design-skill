import os, glob, re, io
from playwright.sync_api import sync_playwright
from PIL import Image
out="../dist"
def dims(p):
    m=re.search(r'viewBox="0 0 (\d+) (\d+)"',open(p).read());return int(m[1]),int(m[2])
with sync_playwright() as pw:
    br=pw.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox']); 
    def shot(svgpath,w,h,dest,transparent=True):
        pg=br.new_page(viewport={"width":w,"height":h})
        s=open(svgpath).read()
        pg.set_content(f'<html><body style="margin:0;background:transparent">{s.replace("width=\"%d\""%dims(svgpath)[0],"width=\"%d\""%w,1).replace("height=\"%d\""%dims(svgpath)[1],"height=\"%d\""%h,1)}</body></html>')
        pg.screenshot(path=dest,omit_background=transparent,clip={"x":0,"y":0,"width":w,"height":h});pg.close()
    # marks
    for k in ("color","blue","white","black"):
        for s in (1024,512,256,128,64):
            shot(f"{out}/svg/mark_{k}.svg",s,s,f"{out}/png/mark_{k}_{s}.png")
    for k in ("white-on-blue","color-on-white","blue-on-mist","white-on-ink"):
        shot(f"{out}/svg/mark_{k}.svg",1024,1024,f"{out}/png/mark_{k}_1024.png",False)
    # lockups at 2400px wide
    for p in glob.glob(f"{out}/svg/lockup-*.svg"):
        w,h=dims(p);W=2400;H=round(h*W/w);n=os.path.basename(p)[:-4]
        bgd=("on" in n.split("_")[1] or "mist" in n)
        shot(p,W,H,f"{out}/png/{n}.png",not bgd)
        if not bgd and n.split("_")[1] in("color",):
            pg=br.new_page(viewport={"width":W,"height":H});pg.set_content(f'<body style="margin:0;background:#fff">'+open(p).read().replace(f'width="{w}"',f'width="{W}"',1).replace(f'height="{h}"',f'height="{H}"',1)+'</body>');pg.screenshot(path=f"/tmp/x.png");pg.close()
            Image.open("/tmp/x.png").convert("RGB").save(f"{out}/jpg/{n}.jpg",quality=95)
        if n.split("_")[1] in ("color","color-on-white","white-on-blue","black","blue-on-mist","white-on-ink","blue","white"):
            pg=br.new_page();pg.set_content(f'<html><body style="margin:0">'+open(p).read()+'</body></html>')
            pg.pdf(path=f"{out}/pdf/{n}.pdf",width=f"{w}px",height=f"{h}px",print_background=True,page_ranges="1");pg.close()
    # web
    for s in (16,32,48,64,180,192,512):
        pass
    W=f"{out}/web"
    for s in (16,32,48):
        shot(f"{W}/favicon.svg" if False else f"{W}/favicon.svg",s,s,f"{out}/web/favicon-{s}.png")
    shot(f"{W}/favicon.svg",64,64,f"{W}/favicon-64.png")
    shot(f"{W}/app-icon_1024.svg",180,180,f"{W}/apple-touch-icon.png",False)
    shot(f"{W}/app-icon_1024.svg",192,192,f"{W}/android-chrome-192.png",False)
    shot(f"{W}/app-icon_1024.svg",512,512,f"{W}/android-chrome-512.png",False)
    shot(f"{W}/app-icon_1024.svg",1024,1024,f"{W}/app-icon_1024.png",False)
    shot(f"{W}/app-icon-rounded_1024.svg",1024,1024,f"{W}/app-icon-rounded_1024.png")
    shot(f"{W}/maskable_512.svg",512,512,f"{W}/maskable-512.png",False)
    shot(f"{W}/avatar-circle_1024.svg",1024,1024,f"{W}/avatar-circle_1024.png")
    shot(f"{W}/og-image_1200x630.svg",1200,630,f"{W}/og-image.png",False)
    br.close()
ims=[Image.open(f"{W}/favicon-{s}.png").convert("RGBA") for s in (16,32,48)]
ims[2].save(f"{W}/favicon.ico",sizes=[(16,16),(32,32),(48,48)],append_images=ims[:2])
for f in glob.glob(f"{W}/favicon-1*.png")+glob.glob(f"{W}/favicon-4*.png")+glob.glob(f"{W}/favicon-3*.png"):pass
print("exported")
