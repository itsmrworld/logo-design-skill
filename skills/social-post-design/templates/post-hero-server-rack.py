import re
from playwright.sync_api import sync_playwright
Dw=open("../dist/svg/mark-tight_white.svg").read(); DP=re.search(r' d="([^"]+)"',Dw)[1]
MW,MH=[int(x) for x in re.search(r'viewBox="0 0 (\d+) (\d+)"',Dw).groups()]
B="#1A73E8"
def mark(w,c="#fff"): return f'<svg viewBox="0 0 {MW} {MH}" width="{w}" height="{w*MH/MW:.1f}"><path fill="{c}" d="{DP}"/></svg>'
def ic(p,c="#fff",s=24,w=2): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'
PIN='<path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.4"/>'
def unit(i):
    bays="".join('<i class="bay"><b></b></i>' for _ in range(8))
    return f'<div class="unit"><span class="ear"></span><div class="bays">{bays}</div><span class="ear r"></span><span class="led"></span></div>'
UNITS="".join(unit(i) for i in range(9))
def vent(): return '<div class="vents"></div>'
def pill(x,y,t,sub,side):
    return f'<div class="gl" style="position:absolute;left:{x}px;top:{y}px;width:210px;height:62px;display:flex;align-items:center;gap:11px;padding:0 12px 0 8px;border-radius:19px"><span style="width:42px;height:42px;border-radius:13px;background:linear-gradient(150deg,#5aa6ff,{B});display:flex;align-items:center;justify-content:center;box-shadow:0 0 16px rgba(77,163,255,.7)">{ic(PIN,"#fff",23)}</span><span style="flex:1"><b style="display:block;font-size:21px;font-weight:800;letter-spacing:-.4px">{t}</b><i style="font-style:normal;font-size:12.5px;color:#a9c7f5;font-weight:600">{sub}</i></span><span style="width:8px;height:8px;border-radius:50%;background:#2ee59d;box-shadow:0 0 0 3px rgba(46,229,157,.2),0 0 8px #2ee59d"></span></div>'
SPECS=["DEDICATED vCPU","NVMe STORAGE","FULL ROOT ACCESS","DDoS SHIELD","6 GLOBAL HUBS","60-SEC DEPLOY","CRYPTO &amp; CARDS","LOCAL PAY"]
spec="".join(f'<div class="sp">{t}</div>' for t in SPECS)
html=f"""<html><head><meta charset="utf-8"></head><style>
*{{margin:0;box-sizing:border-box}}body{{font-family:'Inter Display','Inter',Arial,sans-serif;width:1080px;height:1080px;position:relative;overflow:hidden;background:#01040c;color:#fff}}
.gl{{background:linear-gradient(160deg,rgba(255,255,255,.16),rgba(255,255,255,.05));border:1.5px solid rgba(150,195,255,.32);backdrop-filter:blur(12px);box-shadow:0 20px 44px -16px rgba(0,0,0,.8),inset 0 1px 0 rgba(255,255,255,.28)}}
.sp{{height:40px;display:flex;align-items:center;justify-content:center;border-radius:999px;border:1.5px solid rgba(190,215,255,.75);background:rgba(8,20,55,.55);font-size:15.5px;font-weight:700;letter-spacing:.4px;box-shadow:0 0 14px rgba(77,163,255,.35),inset 0 0 12px rgba(77,163,255,.18)}}
.scene{{position:absolute;left:0;top:0;width:1080px;height:1080px;perspective:1900px}}
.cube{{position:absolute;left:316px;top:316px;width:380px;height:440px;transform-style:preserve-3d;transform:rotateX(-4deg) rotateY(-34deg)}}
.f{{position:absolute;backface-visibility:hidden}}
.front{{left:0;top:0;width:380px;height:440px;transform:translateZ(130px);background:linear-gradient(180deg,#121a2c,#070b16);border:2px solid #2a3550;border-radius:8px;padding:11px 12px;display:flex;flex-direction:column;gap:5px;box-shadow:inset 0 0 0 2px #05080f}}
.back{{left:0;top:0;width:380px;height:440px;transform:translateZ(-130px) rotateY(180deg);background:#070b16}}
.lside{{left:60px;top:0;width:260px;height:440px;transform:translateX(-190px) rotateY(-90deg);background:linear-gradient(90deg,#070c19,#111b33);border:2px solid #222c44;border-radius:8px}}
.rside{{left:60px;top:0;width:260px;height:440px;transform:translateX(190px) rotateY(90deg);background:linear-gradient(90deg,#111b33,#070c19);border:2px solid #222c44;border-radius:8px}}
.top{{left:0;top:90px;width:380px;height:260px;transform:translateY(-220px) rotateX(90deg);background:linear-gradient(180deg,#26334f,#0e172b);border:2px solid #3a4a72}}
.vents{{position:absolute;inset:22px;background:repeating-linear-gradient(0deg,#02040a 0 5px,#0f1830 5px 10px);border-radius:6px;opacity:.9;box-shadow:inset 0 0 20px #000}}
.unit{{position:relative;flex:1;border-radius:5px;background:linear-gradient(180deg,#1b2540,#0a1020 70%);border-top:1.5px solid #3b4b75;border-bottom:1.5px solid #020408;display:flex;align-items:center;padding:0 10px;gap:8px}}
.bays{{flex:1;display:flex;gap:5px;height:76%}}.bay{{flex:1;border-radius:3px;background:linear-gradient(180deg,#050912,#0d1426);border:1px solid #27324f;position:relative}}.bay b{{position:absolute;right:4px;bottom:4px;width:5px;height:5px;border-radius:50%;background:#4da3ff;box-shadow:0 0 7px #4da3ff}}
.ear{{width:7px;height:60%;border-radius:3px;background:linear-gradient(180deg,#5b6b95,#222b45)}}.led{{width:9px;height:9px;border-radius:50%;background:#2ee59d;box-shadow:0 0 10px #2ee59d}}
</style><body>
<div style="position:absolute;inset:0;background:radial-gradient(60% 55% at 28% 62%,rgba(26,115,232,.65) 0%,rgba(26,115,232,0) 70%),radial-gradient(45% 40% at 80% 70%,rgba(26,115,232,.35) 0%,rgba(26,115,232,0) 70%),linear-gradient(180deg,#010512 0%,#03103a 55%,#02081f 100%)"></div>
<div style="position:absolute;left:-100px;top:-40px;width:900px;height:1000px;background:linear-gradient(115deg,rgba(120,180,255,.34) 0%,rgba(120,180,255,0) 45%);transform:skewX(-14deg);filter:blur(30px)"></div>
<div style="position:absolute;left:0;right:0;top:140px;text-align:center;font-size:430px;line-height:.8;font-weight:900;letter-spacing:-16px;background:linear-gradient(180deg,#fff 15%,rgba(255,255,255,.95) 45%,rgba(255,255,255,0) 82%);-webkit-background-clip:text;color:transparent">VPS</div>
<div style="position:absolute;left:46px;top:36px;display:flex;align-items:center;gap:12px">{mark(52)}<span style="font-size:30px;font-weight:700;letter-spacing:-1px">SatisfyCloud</span></div>
<div style="position:absolute;left:0;right:0;top:48px;text-align:center"><div style="font-size:28px;font-style:italic;font-weight:500;color:#dbe8ff;margin-top:62px;letter-spacing:-.3px">Unmatched Power.</div>
<span style="display:inline-block;margin-top:10px;background:linear-gradient(180deg,#2f86f5,{B});border:1.5px solid #8cc4ff;border-radius:14px;padding:8px 36px;font-size:40px;font-weight:800;letter-spacing:-.8px;box-shadow:0 0 36px rgba(26,115,232,.8)">ZERO BOUNDARIES.</span></div>
<div style="position:absolute;left:200px;right:300px;top:742px;height:44px;border-radius:50%;background:radial-gradient(closest-side,rgba(77,163,255,.7),rgba(77,163,255,0));filter:blur(10px)"></div>
<div class="scene"><div class="cube"><div class="f lside">{vent()}</div><div class="f rside">{vent()}</div><div class="f top"></div><div class="f back"></div><div class="f front">{UNITS}</div></div></div>
<div style="position:absolute;left:0;right:0;top:770px;height:160px;background:linear-gradient(180deg,rgba(77,163,255,0),rgba(77,163,255,.2) 45%,rgba(2,8,31,0))"></div>
{pill(48,448,"Canada","North America",0)}{pill(34,540,"USA","North America",0)}{pill(48,632,"France","Europe",0)}
{pill(822,448,"Germany","Europe",1)}{pill(836,540,"Singapore","Asia-Pacific",1)}{pill(822,632,"Australia","Oceania",1)}
<div style="position:absolute;left:0;right:0;top:812px;text-align:center;font-size:19px;color:#cfe0ff;font-weight:600;letter-spacing:.2px">Deploy high-frequency cloud VPS across <b style="color:#fff">6 global hubs</b> in under 60 seconds.</div>
<div style="position:absolute;left:46px;right:46px;top:848px;display:grid;grid-template-columns:repeat(4,1fr);gap:12px 14px">{spec}</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:104px;background:linear-gradient(180deg,#1a6fe0,#0d4fc0);display:flex;align-items:center;justify-content:space-between;padding:0 46px;box-shadow:0 -20px 50px rgba(26,115,232,.45)">
 <div><div style="font-size:17px;font-weight:600;opacity:.9">Visit now ↘</div><div style="font-size:30px;font-weight:800;letter-spacing:-.6px">www.satisfycloud.com</div></div>
 <span style="background:#fff;color:#0d4fc0;font-size:25px;font-weight:800;border-radius:999px;padding:16px 34px;box-shadow:0 12px 28px rgba(0,20,100,.45)">Deploy Your VPS →</span></div>
</body></html>"""
open("vps2.html","w").write(html)
CH='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'
with sync_playwright() as pw:
    br=pw.chromium.launch(executable_path=CH,args=['--no-sandbox'])
    pg=br.new_page(viewport={"width":1080,"height":1080},device_scale_factor=2);pg.goto("file:///home/user/logo-design-skill/satisfycloud/social/vps2.html");pg.wait_for_timeout(300);pg.screenshot(path="facebook-vps-network-post@2x.png");br.close()
