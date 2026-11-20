import re
from playwright.sync_api import sync_playwright
Dw=open("../dist/svg/mark-tight_white.svg").read(); D=re.search(r' d="([^"]+)"',Dw)[1]
MW,MH=[int(x) for x in re.search(r'viewBox="0 0 (\d+) (\d+)"',Dw).groups()]
def mark(w,c="#0B63F6"): return f'<svg viewBox="0 0 {MW} {MH}" width="{w}" height="{w*MH/MW:.1f}"><path fill="{c}" d="{D}"/></svg>'
def ic(p,c="#fff",s=40,w=2): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'
GLOBE='<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/>'
SERVER='<rect x="3" y="4" width="18" height="6.5" rx="2"/><rect x="3" y="13.5" width="18" height="6.5" rx="2"/><path d="M7 7.25h.01M7 16.75h.01M11 7.25h6M11 16.75h6"/>'
CPU='<rect x="6" y="6" width="12" height="12" rx="2.5"/><rect x="9.5" y="9.5" width="5" height="5" rx="1"/><path d="M9 2.5v3M15 2.5v3M9 18.5v3M15 18.5v3M2.5 9h3M2.5 15h3M18.5 9h3M18.5 15h3"/>'
SHIELD='<path d="M12 3l7.5 3v5.5c0 4.6-3.1 8.2-7.5 9.5-4.4-1.3-7.5-4.9-7.5-9.5V6z"/><path d="M8.6 12.2l2.5 2.5 4.4-4.9"/>'
CLOUD='<path d="M7 18a4.5 4.5 0 0 1-.6-8.96A6 6 0 0 1 18 9.5a4.2 4.2 0 0 1-.5 8.5z"/>'
SEARCH='<circle cx="11" cy="11" r="6.5"/><path d="M20 20l-4.2-4.2"/>'
CHECK='<path d="M5 12.5l4.5 4.5L19 7.5"/>'
CSS="""*{margin:0;box-sizing:border-box}body{font-family:'Inter Display','Inter',Arial,sans-serif;color:#0B1220;background:#fff}
.pill{display:inline-flex;align-items:center;gap:14px;background:linear-gradient(180deg,#2a7bff,#0B63F6);color:#fff;font-weight:700;border-radius:999px;box-shadow:0 18px 36px -6px rgba(11,99,246,.5),inset 0 1px 0 rgba(255,255,255,.35)}
.ghost{display:inline-flex;align-items:center;background:#fff;border:2px solid #cfe0ff;color:#0B63F6;font-weight:700;border-radius:999px}
.tile{position:absolute;border-radius:38px;padding:34px 36px;overflow:hidden;box-shadow:0 40px 70px -24px rgba(10,50,150,.35),0 8px 20px rgba(10,50,150,.08)}
.tile .ib{width:84px;height:84px;border-radius:26px;display:flex;align-items:center;justify-content:center}
.tile h3{font-size:40px;font-weight:800;letter-spacing:-1.2px;margin-top:22px}.tile p{font-size:22px;line-height:1.35;margin-top:8px;font-weight:500}
.tags{display:flex;gap:10px;margin-top:20px;flex-wrap:wrap}.tags span{font-size:18px;font-weight:700;border-radius:999px;padding:7px 16px}
.w{background:#fff;border:1.5px solid #e3ecff}.w .ib{background:linear-gradient(150deg,#3a8bff,#0B63F6);box-shadow:0 12px 24px rgba(11,99,246,.35)}.w p{color:#5a6a8a}.w .tags span{background:#eaf2ff;color:#0B63F6}
.b{background:linear-gradient(150deg,#0e3fd6,#0B63F6 55%,#3a95ff);color:#fff}.b .ib{background:rgba(255,255,255,.2);box-shadow:inset 0 1px 0 rgba(255,255,255,.4)}.b p{color:rgba(255,255,255,.85)}.b .tags span{background:rgba(255,255,255,.2)}
.n{background:linear-gradient(150deg,#0a1f5c,#0B1B4A);color:#fff}.n .ib{background:rgba(255,255,255,.12);box-shadow:inset 0 1px 0 rgba(255,255,255,.25)}.n p{color:rgba(255,255,255,.75)}.n .tags span{background:rgba(255,255,255,.14)}"""
cover=f"""<html><style>{CSS}
.bg{{position:absolute;inset:0;background:radial-gradient(55% 75% at 80% 45%,rgba(110,170,255,.5) 0%,rgba(110,170,255,0) 72%),radial-gradient(45% 55% at 0% 100%,rgba(190,215,255,.7) 0%,rgba(190,215,255,0) 70%),linear-gradient(180deg,#f2f7ff 0%,#fff 100%)}}
.dots{{position:absolute;inset:0;background-image:radial-gradient(rgba(11,99,246,.16) 1.6px,transparent 1.8px);background-size:36px 36px;-webkit-mask-image:radial-gradient(45% 70% at 80% 45%,#000 0%,transparent 80%);mask-image:radial-gradient(45% 70% at 80% 45%,#000 0%,transparent 80%)}}</style>
<body style="width:2000px;height:1125px;position:relative;overflow:hidden"><div class="bg"></div><div class="dots"></div>
<div style="position:absolute;left:170px;top:245px;width:820px">
 <div style="display:flex;align-items:center;gap:22px">{mark(96)}<span style="font-size:48px;font-weight:700;letter-spacing:-1.5px">SatisfyCloud</span></div>
 <div style="font-size:104px;line-height:1;font-weight:800;letter-spacing:-4.2px;margin-top:34px">More Security.<br><span style="color:#0B63F6">More Control.</span></div>
 <div style="font-size:30px;line-height:1.42;color:#44516d;margin-top:26px;font-weight:500;max-width:700px">Domains, hosting &amp; servers for businesses worldwide — all under one roof.</div>
 <div style="margin-top:34px;display:flex;gap:16px"><span class="pill" style="font-size:27px;padding:18px 36px">Order your domain →</span><span class="ghost" style="font-size:27px;padding:16px 30px">satisfycloud.com</span></div>
</div>
<div class="tile b" style="left:1040px;top:240px;width:390px;height:320px"><div class="ib">{ic(GLOBE,"#fff",44)}</div><h3>Domains</h3><p>Find your perfect name</p><div class="tags"><span>.com</span><span>.net</span><span>.org</span></div></div>
<div class="tile w" style="left:1460px;top:240px;width:390px;height:320px"><div class="ib">{ic(CLOUD,"#fff",46)}</div><h3>Web Hosting</h3><p>Fast, reliable cloud hosting</p><div class="tags"><span>Business-ready</span></div></div>
<div class="tile w" style="left:1040px;top:590px;width:390px;height:320px"><div class="ib">{ic(SERVER,"#fff",44)}</div><h3>Servers</h3><p>VPS &amp; dedicated power</p><div class="tags"><span>Full control</span></div></div>
<div class="tile n" style="left:1460px;top:590px;width:390px;height:320px"><div class="ib">{ic(SHIELD,"#fff",44)}</div><h3>Security</h3><p>SSL &amp; protection, always on</p><div class="tags"><span>● SSL Active</span></div></div>
</body></html>"""
post=f"""<html><style>{CSS}
.bg{{position:absolute;inset:0;background:radial-gradient(70% 55% at 85% 5%,rgba(120,180,255,.55) 0%,rgba(120,180,255,0) 70%),radial-gradient(60% 50% at 0% 100%,rgba(0,20,120,.5) 0%,rgba(0,20,120,0) 70%),linear-gradient(160deg,#1a73ff 0%,#0B63F6 40%,#0536b0 100%)}}
.dots{{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.20) 1.6px,transparent 1.8px);background-size:34px 34px;-webkit-mask-image:radial-gradient(75% 55% at 50% 45%,#000 0%,transparent 85%);mask-image:radial-gradient(75% 55% at 50% 45%,#000 0%,transparent 85%)}}
.svc{{display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.14);border:1.5px solid rgba(255,255,255,.35);border-radius:22px;padding:14px 24px 14px 16px;color:#fff;font-size:26px;font-weight:700;backdrop-filter:blur(6px)}}
.svc .i{{width:52px;height:52px;border-radius:16px;background:rgba(255,255,255,.2);display:flex;align-items:center;justify-content:center}}
@keyframes b{{50%{{opacity:0}}}}</style>
<body style="width:1080px;height:1080px;position:relative;overflow:hidden"><div class="bg"></div><div class="dots"></div>
<div style="position:absolute;left:0;right:0;top:62px;display:flex;justify-content:center;align-items:center;gap:16px">{mark(70,"#fff")}<span style="font-size:34px;font-weight:700;letter-spacing:-1px;color:#fff">SatisfyCloud</span></div>
<div style="position:absolute;left:0;right:0;top:178px;text-align:center;color:#fff"><div style="font-size:84px;line-height:1.02;font-weight:800;letter-spacing:-3.4px">Your brand deserves<br>its own address.</div></div>
<div style="position:absolute;left:90px;right:90px;top:468px;height:150px;background:#fff;border-radius:36px;box-shadow:0 50px 90px -20px rgba(0,20,100,.55),0 0 0 10px rgba(255,255,255,.18);display:flex;align-items:center;padding:0 26px 0 40px;gap:20px">
 {ic(GLOBE,"#0B63F6",54,2)}<span style="font-size:60px;font-weight:700;letter-spacing:-2px;flex:1">yourbrand<span style="color:#0B63F6">.com</span><span style="display:inline-block;width:5px;height:60px;background:#0B63F6;margin-left:6px;vertical-align:-8px;animation:b 1s infinite"></span></span>
 <span style="background:linear-gradient(180deg,#2a7bff,#0B63F6);width:100px;height:100px;border-radius:28px;display:flex;align-items:center;justify-content:center;box-shadow:0 14px 28px rgba(11,99,246,.4)">{ic(SEARCH,"#fff",48,2.4)}</span></div>
<div style="position:absolute;left:90px;top:652px;display:flex;align-items:center;gap:16px"><span style="display:inline-flex;align-items:center;gap:12px;background:#e7f8ee;color:#0b7a45;font-size:28px;font-weight:800;border-radius:999px;padding:12px 26px 12px 14px;box-shadow:0 14px 30px rgba(0,60,20,.25)"><span style="width:36px;height:36px;border-radius:50%;background:#12a05c;display:flex;align-items:center;justify-content:center">{ic(CHECK,"#fff",22,3.6)}</span>It's available!</span>
 <span style="display:flex;gap:10px;color:#fff;font-size:26px;font-weight:700"><span style="border:2px solid rgba(255,255,255,.5);border-radius:999px;padding:8px 20px">.net</span><span style="border:2px solid rgba(255,255,255,.5);border-radius:999px;padding:8px 20px">.org</span><span style="border:2px solid rgba(255,255,255,.5);border-radius:999px;padding:8px 20px">.io</span></span></div>
<div style="position:absolute;left:0;right:0;top:790px;display:flex;justify-content:center;gap:18px">
 <div class="svc"><span class="i">{ic(GLOBE,"#fff",30)}</span>Domains</div><div class="svc"><span class="i">{ic(CLOUD,"#fff",32)}</span>Hosting</div><div class="svc"><span class="i">{ic(SERVER,"#fff",30)}</span>Servers</div></div>
<div style="position:absolute;left:0;right:0;bottom:56px;display:flex;justify-content:center"><span style="display:inline-flex;align-items:center;background:#fff;color:#0B63F6;font-size:32px;font-weight:800;border-radius:999px;padding:18px 46px;box-shadow:0 20px 40px -10px rgba(0,20,100,.5)">satisfycloud.com →</span></div>
</body></html>"""
open("cover.html","w").write(cover);open("post.html","w").write(post)
CH='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'
with sync_playwright() as pw:
    br=pw.chromium.launch(executable_path=CH,args=['--no-sandbox'])
    for n,w,h,sc,out in [("cover",2000,1125,1,"facebook-cover.png"),("post",1080,1080,2,"facebook-post@2x.png")]:
        pg=br.new_page(viewport={"width":w,"height":h},device_scale_factor=sc);pg.goto(f"file:///home/user/logo-design-skill/satisfycloud/social/{n}.html");pg.wait_for_timeout(200);pg.screenshot(path=out);pg.close()
    br.close()
