import re, math
from playwright.sync_api import sync_playwright
D=re.search(r' d="([^"]+)"',open("../dist/svg/mark-tight_white.svg").read())[1]
MW,MH=[int(x) for x in re.search(r'viewBox="0 0 (\d+) (\d+)"',open("../dist/svg/mark-tight_white.svg").read()).groups()]
def mark(w,extra=""): return f'<svg viewBox="0 0 {MW} {MH}" width="{w}" height="{w*MH/MW:.1f}" {extra}><path fill="#fff" d="{D}"/></svg>'
def globe(cx,cy,r,op=1):
    s=f'<g fill="none" stroke="#fff" stroke-opacity="{.22*op}" stroke-width="1.6">'
    s+=f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke-opacity="{.4*op}"/>'
    for k in (.25,.5,.75): s+=f'<ellipse cx="{cx}" cy="{cy}" rx="{r*k}" ry="{r}"/>'
    s+=f'<line x1="{cx}" y1="{cy-r}" x2="{cx}" y2="{cy+r}"/>'
    for lat in (-.66,-.33,0,.33,.66):
        y=cy+r*lat;rx=r*math.sqrt(1-lat*lat);s+=f'<ellipse cx="{cx}" cy="{y}" rx="{rx}" ry="{rx*.12}"/>'
    s+='</g>'
    # city dots + arcs
    pts=[(-.55,-.1),(-.1,-.45),(.35,-.2),(.6,.25),(-.3,.4),(.05,.05),(.2,.55)]
    P=[(cx+r*x,cy+r*y) for x,y in pts]
    s+=f'<g fill="none" stroke="#9fc0ff" stroke-opacity="{.8*op}" stroke-width="2.2" stroke-linecap="round">'
    for a,b in [(0,1),(1,2),(2,3),(0,4),(4,5),(5,2),(5,6),(6,3),(1,5)]:
        (x1,y1),(x2,y2)=P[a],P[b];mx,my=(x1+x2)/2,(y1+y2)/2-abs(x2-x1)*.22
        s+=f'<path d="M{x1:.1f} {y1:.1f} Q{mx:.1f} {my:.1f} {x2:.1f} {y2:.1f}" stroke-dasharray="2 7"/>'
    s+='</g>'
    for x,y in P: s+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="15" fill="#fff" fill-opacity="{.18*op}"/><circle cx="{x:.1f}" cy="{y:.1f}" r="6.5" fill="#fff"/>'
    return s
CSS="""*{margin:0;box-sizing:border-box}body{font-family:'Inter Display','Inter',Arial,sans-serif;color:#fff}
.bg{position:absolute;inset:0;background:radial-gradient(120% 140% at 80% 20%,#2f86ff 0%,#0B63F6 38%,#0638b8 100%)}
.pill{display:inline-flex;align-items:center;gap:12px;background:#fff;color:#0B63F6;font-weight:700;border-radius:999px}
.chip{border:2px solid rgba(255,255,255,.55);border-radius:999px;font-weight:600;display:inline-block}"""
cover=f"""<html><style>{CSS}</style><body style="width:1640px;height:856px;position:relative;overflow:hidden">
<div class="bg"></div>
<svg style="position:absolute;left:0;top:0" width="1640" height="856">{globe(1380,470,440)}</svg>
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(8,70,200,.96) 0%,rgba(10,90,235,.9) 40%,rgba(11,99,246,0) 72%)"></div>
<div style="position:absolute;left:300px;top:190px;width:900px">
 <div style="display:flex;align-items:center;gap:26px;margin-bottom:34px">{mark(110)}<div style="font-size:48px;font-weight:700;letter-spacing:-1.2px">SatisfyCloud</div></div>
 <div style="font-size:84px;line-height:1.02;font-weight:800;letter-spacing:-3px">Domains &amp; Hosting<br>Built for the World.</div>
 <div style="font-size:30px;margin-top:28px;opacity:.92;font-weight:500;letter-spacing:-.3px">Launch your website on fast, secure cloud hosting — anywhere.</div>
 <div style="margin-top:36px;display:flex;gap:16px;align-items:center"><span class="pill" style="font-size:30px;padding:12px 30px">satisfycloud.com</span><span class="chip" style="font-size:24px;padding:10px 24px">Domains</span><span class="chip" style="font-size:24px;padding:10px 24px">Web Hosting</span></div>
</div></body></html>"""
post=f"""<html><style>{CSS}</style><body style="width:1080px;height:1080px;position:relative;overflow:hidden">
<div class="bg" style="background:radial-gradient(110% 110% at 85% 8%,#3d8fff 0%,#0B63F6 40%,#0535ab 100%)"></div>
<svg style="position:absolute;left:0;top:0" width="1080" height="1080">{globe(900,820,480,.9)}</svg>
<div style="position:absolute;inset:0;background:linear-gradient(100deg,rgba(7,60,190,.95) 0%,rgba(10,90,235,.88) 45%,rgba(11,99,246,0) 78%)"></div>
<div style="position:absolute;left:84px;top:84px;display:flex;align-items:center;gap:20px">{mark(84)}<div style="font-size:38px;font-weight:700;letter-spacing:-1px">SatisfyCloud</div></div>
<div style="position:absolute;left:84px;top:300px;width:820px">
 <div class="chip" style="font-size:26px;padding:10px 26px;margin-bottom:34px;letter-spacing:.5px">WE'RE LIVE</div>
 <div style="font-size:128px;line-height:.98;font-weight:800;letter-spacing:-5px">Hello,<br>world.</div>
 <div style="font-size:38px;line-height:1.3;margin-top:36px;font-weight:500;opacity:.95;letter-spacing:-.5px">Domains &amp; web hosting<br>for businesses everywhere.</div>
</div>
<div style="position:absolute;left:84px;bottom:84px"><span class="pill" style="font-size:36px;padding:16px 38px">satisfycloud.com</span></div>
</body></html>"""
open("cover.html","w").write(cover);open("post.html","w").write(post)
CH='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'
with sync_playwright() as pw:
    br=pw.chromium.launch(executable_path=CH,args=['--no-sandbox'])
    for n,w,h,sc in [("cover",1640,856,1),("cover",1640,856,2),("post",1080,1080,2)]:
        pg=br.new_page(viewport={"width":w,"height":h},device_scale_factor=sc);pg.goto(f"file:///home/user/logo-design-skill/satisfycloud/social/{n}.html")
        pg.screenshot(path=f"facebook-{n}"+("@2x" if sc==2 else "")+".png");pg.close()
    br.close()
