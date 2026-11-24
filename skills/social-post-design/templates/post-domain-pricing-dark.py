import re, base64
from playwright.sync_api import sync_playwright
Dw=open("../dist/svg/mark-tight_white.svg").read(); DP=re.search(r' d="([^"]+)"',Dw)[1]
MW,MH=[int(x) for x in re.search(r'viewBox="0 0 (\d+) (\d+)"',Dw).groups()]
B="#1A73E8"
def mark(w,c="#fff"): return f'<svg viewBox="0 0 {MW} {MH}" width="{w}" height="{w*MH/MW:.1f}"><path fill="{c}" d="{DP}"/></svg>'
def ic(p,c="#8cc4ff",s=28,w=1.9): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'
EYE='<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/><path d="M4 4l16 16"/>'
MAIL='<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3.5 7l8.5 6 8.5-6"/>'
DNS='<circle cx="6" cy="12" r="2.6"/><circle cx="18" cy="6" r="2.6"/><circle cx="18" cy="18" r="2.6"/><path d="M8.4 11l7.2-4M8.4 13l7.2 4"/>'
LOCK='<rect x="4.5" y="10.5" width="15" height="10" rx="2.5"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/>'
img=base64.b64encode(open("assets/website-portrait.png","rb").read()).decode()
ROWS=[(".com","$11.26","Popular","blue"),(".net","$14.14","Popular","blue"),(".org","$8.49","Save 41% year one","green"),(".online","$1.46","Save 92% year one","green"),(".xyz","$2.55","Save 85% year one","green"),(".shop","$1.12","Save 97% year one","green")]
def tag(t,k):
    col={"green":("#0c3a2a","#2ee59d"),"blue":("#14275e","#6fa8ff")}[k]
    return f'<span style="background:{col[0]};color:{col[1]};font-size:14.5px;font-weight:700;border-radius:999px;padding:5px 12px;white-space:nowrap">{t}</span>'
rows="".join(f'<div style="display:flex;align-items:center;justify-content:space-between;height:54px;padding:0 20px;border-top:1px solid rgba(255,255,255,.08)"><div style="display:flex;align-items:center;gap:12px"><b style="font-size:28px;font-weight:800;letter-spacing:-.8px;width:96px">{e}</b>{tag(t,k)}</div><div><b style="font-size:27px;font-weight:800;letter-spacing:-.8px">{p}</b><span style="font-size:14px;color:#8fa3c9;font-weight:600"> /yr</span></div></div>' for e,p,t,k in ROWS)
FEATS=[(EYE,"Domain privacy","Your details stay protected"),(MAIL,"Free email forwarding","Any inbox, your domain"),(DNS,"DNS management","Full control of your records"),(LOCK,"Registrar lock","Guards against unwanted transfers")]
feats="".join(f'<div class="gl" style="display:flex;align-items:center;gap:14px;border-radius:20px;padding:13px 16px"><span style="width:46px;height:46px;border-radius:14px;background:rgba(77,163,255,.18);border:1px solid rgba(120,185,255,.35);display:flex;align-items:center;justify-content:center;flex:none">{ic(p)}</span><span><b style="display:block;font-size:19px;font-weight:800;letter-spacing:-.4px">{t}</b><i style="font-style:normal;font-size:13px;color:#a9c7f5;font-weight:600">{s}</i></span></div>' for p,t,s in FEATS)
html=f"""<html><head><meta charset="utf-8"></head><style>*{{margin:0;box-sizing:border-box}}body{{font-family:'Inter Display','Inter',Arial,sans-serif;width:1080px;height:1080px;position:relative;overflow:hidden;background:#05070d;color:#fff}}
.gl{{background:linear-gradient(160deg,rgba(255,255,255,.13),rgba(255,255,255,.05));border:1.5px solid rgba(150,195,255,.28);backdrop-filter:blur(14px);box-shadow:0 30px 60px -20px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.2)}}</style><body>
<div style="position:absolute;inset:0;background:radial-gradient(55% 45% at 80% 30%,rgba(26,115,232,.55) 0%,rgba(26,115,232,0) 70%),radial-gradient(40% 35% at 0% 100%,rgba(26,115,232,.3) 0%,rgba(26,115,232,0) 70%),linear-gradient(180deg,#04060c 0%,#070b17 60%,#05070d 100%)"></div>
<div style="position:absolute;right:-90px;top:20px;width:560px;height:700px;opacity:.95;-webkit-mask-image:radial-gradient(closest-side,#000 50%,transparent 100%);mask-image:radial-gradient(closest-side,#000 50%,transparent 100%)"><img src="data:image/png;base64,{img}" style="width:100%;height:100%;object-fit:cover;mix-blend-mode:screen;filter:saturate(1.25) brightness(1.15)"></div>
<div style="position:absolute;left:46px;top:40px;display:flex;align-items:center;gap:12px">{mark(52)}<span style="font-size:30px;font-weight:700;letter-spacing:-1px">SatisfyCloud</span></div>
<div style="position:absolute;right:46px;top:50px"><span class="gl" style="display:inline-flex;align-items:center;gap:10px;font-weight:800;font-size:16px;letter-spacing:1.4px;border-radius:999px;padding:9px 20px;color:#bfe0ff"><i style="width:8px;height:8px;border-radius:50%;background:#2ee59d;box-shadow:0 0 10px #2ee59d;display:block"></i>POPULAR DOMAINS</span></div>
<div style="position:absolute;left:46px;top:140px;width:760px"><div style="font-size:24px;font-style:italic;color:#cfe0ff;font-weight:500">Secure by default. Fully yours.</div>
<div style="font-size:92px;line-height:1;font-weight:800;letter-spacing:-4px;margin-top:14px;text-shadow:0 10px 40px rgba(26,115,232,.5)">Popular domains.<br><span style="background:linear-gradient(90deg,#4da3ff,#b9dcff 60%,#fff);-webkit-background-clip:text;color:transparent">Full control.</span></div>
<div style="font-size:24px;line-height:1.4;color:#c3d6f5;font-weight:500;margin-top:18px;max-width:640px">Register <b style="color:#fff">.com, .net, .org</b> and more, from <b style="color:#fff">$1.12</b>/yr in year one, with everything you need included.</div></div>
<div class="gl" style="position:absolute;left:46px;top:482px;width:560px;border-radius:26px;overflow:hidden"><div style="display:flex;justify-content:space-between;padding:12px 20px;font-size:12.5px;font-weight:800;letter-spacing:1.6px;color:#8fa3c9"><span>EXTENSION</span><span>REGISTER</span></div>{rows}</div>
<div style="position:absolute;left:634px;top:482px;width:400px"><div style="font-size:14px;font-weight:800;letter-spacing:1.6px;color:#2ee59d;margin:0 0 10px 4px">INCLUDED WITH EVERY DOMAIN</div><div style="display:flex;flex-direction:column;gap:10px">{feats}</div></div>
<div style="position:absolute;left:46px;right:46px;top:880px;font-size:13px;color:#8190b3;font-weight:500;line-height:1.45">Prices in USD per year for first-year registration. Register, renew and transfer prices are shown before you pay; renewal rates apply from year two. See all extensions on satisfycloud.com/domain.</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:98px;background:linear-gradient(180deg,#1a6fe0,#0d4fc0);display:flex;align-items:center;justify-content:space-between;padding:0 46px;box-shadow:0 -20px 50px rgba(26,115,232,.45)">
 <div><div style="font-size:16px;font-weight:600;opacity:.9">Visit now ↘</div><div style="font-size:28px;font-weight:800;letter-spacing:-.6px">satisfycloud.com/domain</div></div>
 <span style="background:#fff;color:#0d4fc0;font-size:25px;font-weight:800;border-radius:999px;padding:16px 34px;box-shadow:0 12px 28px rgba(0,20,100,.45)">Search your name →</span></div>
</body></html>"""
open("domain2.html","w").write(html)
CH='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'
with sync_playwright() as pw:
    br=pw.chromium.launch(executable_path=CH,args=['--no-sandbox'])
    pg=br.new_page(viewport={"width":1080,"height":1080},device_scale_factor=2);pg.goto("file:///home/user/logo-design-skill/satisfycloud/social/domain2.html");pg.wait_for_timeout(300);pg.screenshot(path="facebook-domain-pricing-post@2x.png");br.close()
