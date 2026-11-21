import re, math, random
import numpy as np
from global_land_mask import globe
from playwright.sync_api import sync_playwright
random.seed(7)
Dw=open("../dist/svg/mark-tight_white.svg").read(); DP=re.search(r' d="([^"]+)"',Dw)[1]
MW,MH=[int(x) for x in re.search(r'viewBox="0 0 (\d+) (\d+)"',Dw).groups()]
B="#1A73E8";LB="#5aa9ff"
def mark(w,c="#fff"): return f'<svg viewBox="0 0 {MW} {MH}" width="{w}" height="{w*MH/MW:.1f}"><path fill="{c}" d="{DP}"/></svg>'
def ic(p,c="#fff",s=28,w=1.9): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'
PIN='<path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.4"/>'
CPU='<rect x="6" y="6" width="12" height="12" rx="2.5"/><rect x="9.5" y="9.5" width="5" height="5" rx="1"/><path d="M9 2.5v3M15 2.5v3M9 18.5v3M15 18.5v3M2.5 9h3M2.5 15h3M18.5 9h3M18.5 15h3"/>'
SHIELD='<path d="M12 3l7.5 3v5.5c0 4.6-3.1 8.2-7.5 9.5-4.4-1.3-7.5-4.9-7.5-9.5V6z"/><path d="M8.6 12.2l2.5 2.5 4.4-4.9"/>'
WALLET='<rect x="3" y="6" width="18" height="13" rx="3"/><path d="M3 10h18M16 14.5h2"/>'
# ---- projection (tilted-plane trapezoid)
CX,Y0,HM,S0,KX=540,860,520,.6,3.1
LATN,LATS=76,-50
def proj(lon,lat,h=0):
    t=(LATN-lat)/(LATN-LATS); sc=S0+(1-S0)*t
    return CX+(lon-10)*KX*sc, Y0+t*HM-h*sc, sc
# ---- land dots
dots=[]
for lat in np.arange(-52,78,2.0):
    for lon in np.arange(-168,180,2.0):
        if globe.is_land(lat,lon):
            sx,sy,s=proj(lon+random.uniform(-.3,.3),lat+random.uniform(-.3,.3))
            dots.append((sx,sy,s))
dsvg=""
for sx,sy,s in dots:
    a=min(.95,max(.38,(s-.45)*1.4)); r=1.0+s*1.15
    dsvg+=f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{r:.2f}" fill="{"#bfe0ff" if random.random()<.06 else LB}" fill-opacity="{a:.2f}"/>'
# ---- hubs
HUB={"USA":(-112,38),"Canada":(-75,50),"Germany":(13,52),"France":(-1,45),"Singapore":(104,1.3),"Australia":(150,-33)}
LIFT={"USA":70,"Canada":95,"Germany":120,"France":80,"Singapore":90,"Australia":90}
P={k:proj(*v) for k,v in HUB.items()}
def arc(a,b,peak):
    (lo1,la1),(lo2,la2)=HUB[a],HUB[b];pts=[]
    for i in range(41):
        t=i/40;lon=lo1+(lo2-lo1)*t;lat=la1+(la2-la1)*t;h=peak*4*t*(1-t)
        sx,sy,_=proj(lon,lat,h);pts.append((sx,sy))
    return "M"+" L".join(f"{x:.1f} {y:.1f}" for x,y in pts),pts
links=[("USA","Canada",60),("Canada","Germany",170),("USA","France",190),("France","Germany",45),("Germany","Singapore",190),("France","Singapore",150),("Singapore","Australia",90)]
arcs="";packets=""
for a,b,pk in links:
    d,pts=arc(a,b,pk)
    arcs+=f'<path d="{d}" fill="none" stroke="url(#ag)" stroke-width="7" stroke-opacity=".35" filter="url(#gb)"/><path d="{d}" fill="none" stroke="url(#ag)" stroke-width="2.4" stroke-linecap="round"/>'
    for t in (.3,.68):
        x,y=pts[int(t*40)];packets+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="#fff" fill-opacity=".25"/><circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#fff"/>'
mk=""
for k,(sx,sy,s) in P.items():
    ex,ey=sx,sy-LIFT[k]*s
    mk+=f'<ellipse cx="{sx:.1f}" cy="{sy:.1f}" rx="{34*s:.1f}" ry="{9*s:.1f}" fill="none" stroke="#9fd0ff" stroke-opacity=".6" stroke-width="2"/><ellipse cx="{sx:.1f}" cy="{sy:.1f}" rx="{58*s:.1f}" ry="{15*s:.1f}" fill="none" stroke="#9fd0ff" stroke-opacity=".25" stroke-width="2"/><line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="url(#bm)" stroke-width="3"/><circle cx="{sx:.1f}" cy="{sy:.1f}" r="{9*s:.1f}" fill="#fff"/><circle cx="{sx:.1f}" cy="{sy:.1f}" r="{20*s:.1f}" fill="#4da3ff" fill-opacity=".35"/><circle cx="{ex:.1f}" cy="{ey:.1f}" r="7" fill="#fff"/><circle cx="{ex:.1f}" cy="{ey:.1f}" r="15" fill="#7fc0ff" fill-opacity=".4"/>'
# ---- callouts (pill centres)
CALL={"Canada":(150,800,"North America"),"USA":(150,915,"North America"),"France":(150,1030,"Europe"),"Germany":(930,800,"Europe"),"Singapore":(930,1000,"Asia-Pacific"),"Australia":(930,1200,"Oceania")}
lead="";pills=""
for k,(px,py,sub) in CALL.items():
    sx,sy,s=P[k];ex,ey=sx,sy-LIFT[k]*s
    edge=px+(105 if px<540 else -105)
    lead+=f'<path d="M{ex:.1f} {ey:.1f} L{(ex+edge)/2:.1f} {py} L{edge} {py}" fill="none" stroke="#8cc4ff" stroke-opacity=".55" stroke-width="1.8" stroke-dasharray="3 6" stroke-linecap="round"/>'
    pills+=f'<div class="glass" style="position:absolute;left:{px-105}px;top:{py-32}px;width:210px;height:64px;display:flex;align-items:center;gap:12px;padding:0 14px 0 9px;border-radius:20px"><span style="width:44px;height:44px;border-radius:14px;background:linear-gradient(150deg,#5aa6ff,{B});display:flex;align-items:center;justify-content:center;box-shadow:0 0 18px rgba(77,163,255,.6)">{ic(PIN,"#fff",24,2)}</span><span style="flex:1"><b style="display:block;font-size:22px;font-weight:800;letter-spacing:-.5px">{k}</b><i style="font-style:normal;font-size:13px;color:#a9c7f5;font-weight:600">{sub}</i></span><span style="width:9px;height:9px;border-radius:50%;background:#2ee59d;box-shadow:0 0 0 4px rgba(46,229,157,.2),0 0 10px #2ee59d"></span></div>'
# ---- stars
stars="".join(f'<circle cx="{random.uniform(0,1080):.0f}" cy="{random.uniform(0,1250):.0f}" r="{random.choice([.7,.9,1.2,1.6,2.2]):.1f}" fill="#fff" fill-opacity="{random.uniform(.25,.95):.2f}"/>' for _ in range(330))
def feat(icon,t,s):
    return f'<div class="glass" style="flex:1;display:flex;align-items:center;gap:13px;border-radius:22px;padding:15px 16px"><span style="width:46px;height:46px;border-radius:14px;background:rgba(77,163,255,.18);border:1px solid rgba(120,185,255,.35);display:flex;align-items:center;justify-content:center;flex:none">{ic(icon,"#8cc4ff",26)}</span><span><b style="display:block;font-size:16.5px;font-weight:800;letter-spacing:-.3px;white-space:nowrap">{t}</b><i style="font-style:normal;font-size:13.5px;color:#a9c7f5;font-weight:600">{s}</i></span></div>'
html=f"""<html><head><meta charset="utf-8"></head><style>*{{margin:0;box-sizing:border-box}}body{{font-family:'Inter Display','Inter',Arial,sans-serif;width:1080px;height:1920px;position:relative;overflow:hidden;background:#020617;color:#fff}}
.glass{{background:linear-gradient(160deg,rgba(255,255,255,.14),rgba(255,255,255,.05));border:1.5px solid rgba(160,200,255,.28);backdrop-filter:blur(14px);box-shadow:0 20px 50px -18px rgba(0,0,0,.7),inset 0 1px 0 rgba(255,255,255,.25);color:#fff}}</style><body>
<div style="position:absolute;inset:0;background:radial-gradient(90% 40% at 50% 38%,rgba(26,115,232,.55) 0%,rgba(26,115,232,0) 70%),radial-gradient(60% 30% at 15% 8%,rgba(90,60,255,.28) 0%,rgba(90,60,255,0) 70%),radial-gradient(60% 30% at 95% 20%,rgba(0,170,255,.22) 0%,rgba(0,170,255,0) 70%),linear-gradient(180deg,#010412 0%,#041033 38%,#06215f 62%,#030b27 100%)"></div>
<svg width="1080" height="1920" style="position:absolute;inset:0"><defs>
<linearGradient id="ag" x1="0" x2="1"><stop offset="0" stop-color="#4da3ff"/><stop offset=".5" stop-color="#bfe3ff"/><stop offset="1" stop-color="#4da3ff"/></linearGradient>
<linearGradient id="bm" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#7fc0ff" stop-opacity=".9"/><stop offset="1" stop-color="#7fc0ff" stop-opacity=".05"/></linearGradient>
<filter id="gb" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="5"/></filter>
<linearGradient id="st" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient><linearGradient id="pl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2f86ff" stop-opacity=".45"/><stop offset="1" stop-color="#2f86ff" stop-opacity="0"/></linearGradient><radialGradient id="hz"><stop offset="0" stop-color="#6fb4ff" stop-opacity=".75"/><stop offset="1" stop-color="#6fb4ff" stop-opacity="0"/></radialGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#020617" stop-opacity="1"/><stop offset="1" stop-color="#020617" stop-opacity="0"/></linearGradient></defs>
{stars}<g stroke-linecap="round"><path d="M1010 70 L850 200" stroke="url(#st)" stroke-width="3"/><path d="M260 60 L120 200" stroke="url(#st)" stroke-width="2.4"/><path d="M520 90 L440 160" stroke="url(#st)" stroke-width="2"/></g>
<path d="M-200 1980 Q540 1640 1280 1980" fill="none" stroke="#4da3ff" stroke-opacity=".5" stroke-width="3"/><path d="M-200 1980 Q540 1640 1280 1980 V2100 H-200Z" fill="url(#pl)"/>
<ellipse cx="540" cy="1120" rx="700" ry="300" fill="url(#hz)" opacity=".7"/>
<g fill="none" stroke="#6fb4ff" stroke-opacity=".18" stroke-width="1.6"><ellipse cx="540" cy="1130" rx="560" ry="210"/><ellipse cx="540" cy="1130" rx="760" ry="290"/></g>
{dsvg}

{arcs}{mk}{packets}{lead}</svg>
<div style="position:absolute;left:0;right:0;top:250px;display:flex;justify-content:center;align-items:center;gap:14px">{mark(58)}<span style="font-size:34px;font-weight:700;letter-spacing:-1px">SatisfyCloud</span></div>
<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><span class="glass" style="display:inline-flex;align-items:center;gap:10px;font-weight:800;font-size:17px;letter-spacing:1.5px;border-radius:999px;padding:9px 22px;color:#bfe0ff"><i style="width:8px;height:8px;border-radius:50%;background:#2ee59d;box-shadow:0 0 10px #2ee59d;display:block"></i>GLOBAL NVMe VPS NETWORK</span></div>
<div style="position:absolute;left:0;right:0;top:392px;text-align:center"><div style="font-size:84px;line-height:1.02;font-weight:800;letter-spacing:-3.4px;text-shadow:0 10px 40px rgba(26,115,232,.55)">Unmatched Power.<br><span style="background:linear-gradient(90deg,#4da3ff,#b9dcff 55%,#fff);-webkit-background-clip:text;color:transparent">Zero Boundaries.</span></div>
<div style="font-size:25px;line-height:1.4;color:#c3d6f5;font-weight:500;margin:20px auto 0;max-width:820px">Deploy high-frequency cloud VPS across 6 global hubs<br>in under 60 seconds.</div></div>
{pills}
<div style="position:absolute;left:44px;right:44px;top:1470px;display:flex;gap:14px">{feat(CPU,"Dedicated vCPU &amp; NVMe","Pure raw speed")}{feat(SHIELD,"Full Root &amp; DDoS Shield","Enterprise control")}{feat(WALLET,"Crypto, Cards &amp; Local Pay","Instant activation")}</div>
<div style="position:absolute;left:0;right:0;top:1594px;display:flex;justify-content:center"><span style="display:inline-flex;align-items:center;gap:16px;background:linear-gradient(180deg,#3b8bf0,{B});color:#fff;font-size:27px;font-weight:700;border-radius:999px;padding:18px 42px;box-shadow:0 0 50px rgba(26,115,232,.75),0 18px 36px -8px rgba(26,115,232,.6),inset 0 1px 0 rgba(255,255,255,.45)">Deploy Your VPS →<span style="opacity:.55">|</span><span style="font-weight:800">satisfycloud.com</span></span></div>
</body></html>"""
open("story.html","w").write(html)
CH='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'
with sync_playwright() as pw:
    br=pw.chromium.launch(executable_path=CH,args=['--no-sandbox'])
    pg=br.new_page(viewport={"width":1080,"height":1920},device_scale_factor=1.5);pg.goto("file:///home/user/logo-design-skill/satisfycloud/social/story.html");pg.wait_for_timeout(300);pg.screenshot(path="facebook-story-vps-network.png");br.close()
