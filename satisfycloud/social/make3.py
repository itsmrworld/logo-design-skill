import re
from playwright.sync_api import sync_playwright
Dw=open("../dist/svg/mark-tight_white.svg").read(); D=re.search(r' d="([^"]+)"',Dw)[1]
MW,MH=[int(x) for x in re.search(r'viewBox="0 0 (\d+) (\d+)"',Dw).groups()]
def mark(w,c="#0B63F6"): return f'<svg viewBox="0 0 {MW} {MH}" width="{w}" height="{w*MH/MW:.1f}"><path fill="{c}" d="{D}"/></svg>'
def ic(p,c="#0B63F6",s=28,w=2.2): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'
GLOBE=ic('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/>')
LOCK=lambda c="#12a05c",s=28:ic('<rect x="4.5" y="10.5" width="15" height="10" rx="2.5"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/>',c,s)
SHIELD=ic('<path d="M12 3l7.5 3v5.5c0 4.6-3.1 8.2-7.5 9.5-4.4-1.3-7.5-4.9-7.5-9.5V6z"/><path d="M8.6 12.2l2.5 2.5 4.4-4.9"/>',"#fff",46,2)
CHK=lambda c="#fff",s=22:ic('<path d="M5 12.5l4.5 4.5L19 7.5"/>',c,s,3.6)
SEARCH=ic('<circle cx="11" cy="11" r="6.5"/><path d="M20 20l-4.2-4.2"/>',"#fff",26,2.6)
CSS="""*{margin:0;box-sizing:border-box}body{font-family:'Inter Display','Inter',Arial,sans-serif;color:#0B1220;background:#fff}
.bg{position:absolute;inset:0;background:
 radial-gradient(60% 70% at 88% 12%,rgba(120,175,255,.55) 0%,rgba(120,175,255,0) 70%),
 radial-gradient(50% 60% at 8% 100%,rgba(170,205,255,.55) 0%,rgba(170,205,255,0) 70%),
 linear-gradient(180deg,#f3f8ff 0%,#ffffff 100%)}
.dots{position:absolute;inset:0;background-image:radial-gradient(rgba(11,99,246,.16) 1.6px,transparent 1.8px);background-size:36px 36px;-webkit-mask-image:radial-gradient(70% 80% at 80% 40%,#000 0%,transparent 75%);mask-image:radial-gradient(70% 80% at 80% 40%,#000 0%,transparent 75%)}
.card{position:absolute;background:rgba(255,255,255,.96);border-radius:32px;border:1.5px solid rgba(255,255,255,.9);outline:1px solid rgba(11,99,246,.08);box-shadow:0 50px 90px -20px rgba(10,50,150,.28),0 12px 28px rgba(10,50,150,.10),inset 0 1px 0 #fff;overflow:hidden}
.pill{display:inline-flex;align-items:center;gap:14px;background:linear-gradient(180deg,#2a7bff,#0B63F6);color:#fff;font-weight:700;border-radius:999px;box-shadow:0 18px 36px -6px rgba(11,99,246,.5),inset 0 1px 0 rgba(255,255,255,.35)}
.ghost{display:inline-flex;align-items:center;background:#fff;border:2px solid #cfe0ff;color:#0B63F6;font-weight:700;border-radius:999px}
.tag{display:inline-flex;align-items:center;gap:8px;background:#e7f8ee;color:#0b7a45;font-weight:700;border-radius:999px}
.row{display:flex;align-items:center;justify-content:space-between;padding:15px 18px;border-radius:18px;background:#f5f8ff}
.btn{background:#0B63F6;color:#fff;font-weight:700;border-radius:12px;padding:10px 22px}
.tg{width:64px;height:36px;border-radius:20px;background:#0B63F6;position:relative;box-shadow:inset 0 2px 4px rgba(0,0,40,.25)}.tg:after{content:'';position:absolute;right:4px;top:4px;width:28px;height:28px;border-radius:50%;background:#fff;box-shadow:0 2px 5px rgba(0,0,0,.3)}"""
def cluster():
    return f'''
<div class="card" style="left:0;top:0;width:570px;transform:rotate(-2.2deg)">
 <div style="background:linear-gradient(120deg,#0B63F6,#3a8bff);padding:22px 28px;display:flex;align-items:center;gap:14px;color:#fff">{mark(46,"#fff")}<div><div style="font-size:26px;font-weight:800;letter-spacing:-.5px">Claim your domain</div><div style="font-size:16px;opacity:.85;font-weight:500">Search · Order · Go live</div></div></div>
 <div style="padding:24px 26px 26px">
  <div style="display:flex;gap:12px"><div style="flex:1;display:flex;align-items:center;gap:12px;border:2px solid #0B63F6;border-radius:16px;padding:13px 18px;box-shadow:0 0 0 6px rgba(11,99,246,.10)">{GLOBE}<span style="font-size:27px;font-weight:700;letter-spacing:-.5px">yourbrand<span style="color:#9aa8c4;font-weight:600">.com</span></span></div><div style="background:#0B63F6;border-radius:16px;width:64px;display:flex;align-items:center;justify-content:center">{SEARCH}</div></div>
  <div style="display:flex;flex-direction:column;gap:10px;margin-top:18px">
   <div class="row" style="background:#ecf9f1;border:1.5px solid #bfe9d0"><div style="display:flex;align-items:center;gap:12px"><span style="width:26px;height:26px;border-radius:50%;background:#12a05c;display:flex;align-items:center;justify-content:center">{CHK("#fff",15)}</span><span style="font-size:23px;font-weight:700">yourbrand.com</span></div><div style="display:flex;align-items:center;gap:14px"><span style="color:#0b7a45;font-weight:700;font-size:17px">Available</span><span class="btn" style="font-size:17px">Order</span></div></div>
   <div class="row"><span style="font-size:22px;font-weight:600;color:#44516d">yourbrand.net</span><span style="color:#0b7a45;font-weight:700;font-size:17px">Available</span></div>
   <div class="row" style="opacity:.6"><span style="font-size:22px;font-weight:600;color:#44516d">yourbrand.io</span><span style="color:#8793ad;font-weight:600;font-size:17px">Taken</span></div>
  </div></div>
</div>
<div class="card" style="left:595px;top:250px;width:415px;padding:26px 28px;transform:rotate(2deg)">
 <div style="display:flex;align-items:center;gap:16px"><span style="width:56px;height:56px;border-radius:50%;background:linear-gradient(160deg,#27c47a,#0e9a55);display:flex;align-items:center;justify-content:center;box-shadow:0 10px 22px rgba(18,160,92,.4)">{CHK("#fff",28)}</span><div><div style="font-size:29px;font-weight:800;letter-spacing:-.8px">Hosting is ready</div><div style="font-size:16px;color:#6b7a99;font-weight:500">Your website is live on the cloud</div></div></div>
 <div style="margin-top:20px;display:flex;flex-direction:column;gap:11px;font-size:19px;font-weight:600;color:#33415c">
  <div style="display:flex;gap:12px;align-items:center"><span class="tag" style="width:26px;height:26px;justify-content:center;padding:0">{CHK("#0b7a45",14)}</span>Domain registered</div>
  <div style="display:flex;gap:12px;align-items:center"><span class="tag" style="width:26px;height:26px;justify-content:center;padding:0">{CHK("#0b7a45",14)}</span>Cloud hosting created</div>
  <div style="display:flex;gap:12px;align-items:center"><span class="tag" style="width:26px;height:26px;justify-content:center;padding:0">{CHK("#0b7a45",14)}</span>SSL certificate installed</div></div>
</div>
<div class="card" style="left:-10px;top:468px;width:390px;padding:26px 28px;background:linear-gradient(150deg,#0e3fd6,#0B63F6 55%,#3a95ff);transform:rotate(-1.6deg);color:#fff;border:none">
 <div style="position:absolute;right:-60px;top:-60px;width:220px;height:220px;border-radius:50%;border:2px solid rgba(255,255,255,.18)"></div><div style="position:absolute;right:-20px;top:-20px;width:140px;height:140px;border-radius:50%;border:2px solid rgba(255,255,255,.25)"></div>
 <div style="width:72px;height:72px;border-radius:22px;background:rgba(255,255,255,.18);display:flex;align-items:center;justify-content:center;box-shadow:inset 0 1px 0 rgba(255,255,255,.4)">{SHIELD}</div>
 <div style="font-size:32px;font-weight:800;letter-spacing:-1px;margin-top:18px">Protected</div>
 <div style="display:flex;gap:10px;margin-top:12px"><span style="background:rgba(255,255,255,.2);border-radius:999px;padding:7px 16px;font-size:16px;font-weight:700">● SSL Active</span><span style="background:rgba(255,255,255,.2);border-radius:999px;padding:7px 16px;font-size:16px;font-weight:700">Firewall On</span></div>
</div>
<div class="card" style="left:545px;top:560px;width:465px;padding:24px 26px;transform:rotate(1.4deg)">
 <div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:27px;font-weight:800;letter-spacing:-.6px">Your control</div><span style="font-size:15px;color:#6b7a99;font-weight:600">Control panel</span></div>
 <div style="display:flex;flex-direction:column;gap:10px;margin-top:16px;font-size:20px;font-weight:600">
  <div class="row" style="padding:11px 16px">Auto backups<span class="tg"></span></div>
  <div class="row" style="padding:11px 16px">Firewall<span class="tg"></span></div>
  <div class="row" style="padding:11px 16px">Auto-renew domain<span class="tg"></span></div></div>
</div>'''
cover=f"""<html><style>{CSS}</style><body style="width:2000px;height:1125px;position:relative;overflow:hidden">
<div class="bg"></div><div class="dots"></div>
<div style="position:absolute;right:-180px;top:60px;opacity:.5">{mark(1250,"#e3edff")}</div>
<div style="position:absolute;left:190px;top:262px;width:880px">
 <div style="display:flex;align-items:center;gap:24px">{mark(112)}<span style="font-size:52px;font-weight:700;letter-spacing:-1.5px">SatisfyCloud</span></div>
 <div style="font-size:112px;line-height:1;font-weight:800;letter-spacing:-4.5px;margin-top:38px">More Security.<br><span style="color:#0B63F6">More Control.</span></div>
 <div style="font-size:32px;line-height:1.42;color:#44516d;margin-top:30px;font-weight:500;max-width:760px">Domains &amp; cloud hosting for businesses worldwide — protected, simple and fully in your hands.</div>
 <div style="margin-top:40px;display:flex;gap:16px"><span class="pill" style="font-size:29px;padding:19px 40px">Order your domain →</span><span class="ghost" style="font-size:29px;padding:17px 34px">satisfycloud.com</span></div>
</div>
<div style="position:absolute;left:1000px;top:215px;width:1010px;height:760px;transform:scale(.93);transform-origin:left top">{cluster()}</div>
</body></html>"""
post=f"""<html><style>{CSS}</style><body style="width:1080px;height:1080px;position:relative;overflow:hidden">
<div class="bg"></div><div class="dots"></div>
<div style="position:absolute;right:-140px;top:-40px;opacity:.5">{mark(760,"#e3edff")}</div>
<div style="position:absolute;left:80px;top:72px;display:flex;align-items:center;gap:18px">{mark(78)}<span style="font-size:36px;font-weight:700;letter-spacing:-1px">SatisfyCloud</span></div>
<div style="position:absolute;right:80px;top:84px"><span class="pill" style="font-size:24px;padius:0;padding:13px 30px">satisfycloud.com</span></div>
<div style="position:absolute;left:80px;top:196px">
 <span class="tag" style="font-size:20px;padding:9px 20px;background:#fff;color:#0B63F6;box-shadow:0 10px 26px rgba(11,99,246,.18);letter-spacing:.4px">● NOW LIVE · WORLDWIDE</span>
 <div style="font-size:82px;line-height:1;font-weight:800;letter-spacing:-3.2px;margin-top:22px">Your idea.<br>Your domain.<br><span style="color:#0B63F6">Your cloud.</span></div>
</div>
<div style="position:absolute;left:300px;top:528px;width:1010px;height:760px;transform:scale(.62);transform-origin:left top">{cluster()}</div>
</body></html>"""
open("cover.html","w").write(cover);open("post.html","w").write(post)
CH='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'
with sync_playwright() as pw:
    br=pw.chromium.launch(executable_path=CH,args=['--no-sandbox'])
    for n,w,h,sc,out in [("cover",2000,1125,1,"facebook-cover.png"),("post",1080,1080,2,"facebook-post@2x.png")]:
        pg=br.new_page(viewport={"width":w,"height":h},device_scale_factor=sc);pg.goto(f"file:///home/user/logo-design-skill/satisfycloud/social/{n}.html");pg.screenshot(path=out);pg.close()
    br.close()
from PIL import Image
c=Image.open("facebook-cover.png").convert("RGB")
web=c.crop((0,190,2000,930)).resize((923,342)); desk=c.crop((0,225,2000,225+760)).resize((820,312)); app=c.resize((640,360))
S=Image.new("RGB",(1000,1000),"#cfd6e4");S.paste(web,(38,30));S.paste(desk,(90,410));S.paste(app,(180,570+0))
S=S.crop((0,0,1000,950));S.save("preview-desktop-mobile.png")
