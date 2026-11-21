import re, math
from playwright.sync_api import sync_playwright
Dw=open("../dist/svg/mark-tight_white.svg").read(); D=re.search(r' d="([^"]+)"',Dw)[1]
MW,MH=[int(x) for x in re.search(r'viewBox="0 0 (\d+) (\d+)"',Dw).groups()]
def mark(w,c="#0B63F6"): return f'<svg viewBox="0 0 {MW} {MH}" width="{w}" height="{w*MH/MW:.1f}"><path fill="{c}" d="{D}"/></svg>'
def ic(p,c="#fff",s=30,w=2.1): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'
P=dict(
globe='<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/>',
server='<rect x="3" y="4" width="18" height="6.5" rx="2"/><rect x="3" y="13.5" width="18" height="6.5" rx="2"/><path d="M7 7.25h.01M7 16.75h.01M11 7.25h6M11 16.75h6"/>',
shield='<path d="M12 3l7.5 3v5.5c0 4.6-3.1 8.2-7.5 9.5-4.4-1.3-7.5-4.9-7.5-9.5V6z"/><path d="M8.6 12.2l2.5 2.5 4.4-4.9"/>',
cloud='<path d="M7 18a4.5 4.5 0 0 1-.6-8.96A6 6 0 0 1 18 9.5a4.2 4.2 0 0 1-.5 8.5z"/>',
lock='<rect x="4.5" y="10.5" width="15" height="10" rx="2.5"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/>',
search='<circle cx="11" cy="11" r="6.5"/><path d="M20 20l-4.2-4.2"/>',
check='<path d="M5 12.5l4.5 4.5L19 7.5"/>',
db='<ellipse cx="12" cy="6" rx="7.5" ry="3"/><path d="M4.5 6v6c0 1.7 3.4 3 7.5 3s7.5-1.3 7.5-3V6M4.5 12v6c0 1.7 3.4 3 7.5 3s7.5-1.3 7.5-3v-6"/>',
grid='<rect x="3.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="3.5" y="13.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="13.5" width="7" height="7" rx="1.5"/>',
mail='<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3.5 7l8.5 6 8.5-6"/>')
IC=lambda k,c="#fff",s=30,w=2.1: ic(P[k],c,s,w)
CSS="""*{margin:0;box-sizing:border-box}body{font-family:'Inter Display','Inter',Arial,sans-serif;color:#0B1220;background:#fff}
.pill{display:inline-flex;align-items:center;gap:14px;font-weight:700;border-radius:999px}
.fl{position:absolute;background:#fff;border-radius:26px;box-shadow:0 40px 80px -20px rgba(0,10,70,.65),0 10px 24px rgba(0,10,70,.25);}
.ibx{width:62px;height:62px;border-radius:19px;display:flex;align-items:center;justify-content:center;background:linear-gradient(150deg,#3a8bff,#0B63F6);box-shadow:0 10px 22px rgba(11,99,246,.4)}
.ibx.g{background:linear-gradient(150deg,#2fd083,#0e9a55);box-shadow:0 10px 22px rgba(18,160,92,.4)}
.sb{display:flex;align-items:center;gap:12px;padding:12px 16px;border-radius:14px;font-size:19px;font-weight:600;color:#9db0e0}
.sb.on{background:#0B63F6;color:#fff}
.stat{background:#fff;border-radius:20px;padding:18px 18px;box-shadow:0 6px 18px rgba(11,60,160,.08)}
.dot{display:inline-block;width:10px;height:10px;border-radius:50%;background:#12c46f;margin-right:8px}"""
def dashboard():
    chart='<svg viewBox="0 0 360 120" width="100%" height="120"><defs><linearGradient id="ar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0B63F6" stop-opacity=".35"/><stop offset="1" stop-color="#0B63F6" stop-opacity="0"/></linearGradient></defs><path d="M0 95 C40 80 60 90 95 62 S160 70 190 45 S260 55 295 28 S340 30 360 14 V120 H0z" fill="url(#ar)"/><path d="M0 95 C40 80 60 90 95 62 S160 70 190 45 S260 55 295 28 S340 30 360 14" fill="none" stroke="#0B63F6" stroke-width="4" stroke-linecap="round"/><circle cx="295" cy="28" r="7" fill="#fff" stroke="#0B63F6" stroke-width="4"/></svg>'
    return f'''<div style="position:absolute;left:0;top:0;width:760px;height:560px;border-radius:34px;overflow:hidden;background:#eef3ff;display:flex;box-shadow:0 60px 120px -20px rgba(0,5,60,.8),0 0 0 2px rgba(255,255,255,.35)">
 <div style="width:210px;background:linear-gradient(180deg,#0a2166,#06154a);padding:26px 18px;display:flex;flex-direction:column;gap:8px">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:18px;padding-left:6px">{mark(40,"#fff")}<span style="color:#fff;font-weight:800;font-size:21px;letter-spacing:-.5px">Satisfy</span></div>
  <div class="sb on">{IC("grid","#fff",22)}Dashboard</div><div class="sb">{IC("globe","#9db0e0",22)}Domains</div><div class="sb">{IC("cloud","#9db0e0",22)}Hosting</div><div class="sb">{IC("server","#9db0e0",22)}Servers</div><div class="sb">{IC("shield","#9db0e0",22)}Security</div><div class="sb">{IC("mail","#9db0e0",22)}Email</div></div>
 <div style="flex:1;padding:26px 26px">
  <div style="display:flex;justify-content:space-between;align-items:center"><div><div style="font-size:15px;color:#6b7a99;font-weight:600">Welcome back</div><div style="font-size:30px;font-weight:800;letter-spacing:-1px">Your control center</div></div><span style="background:#e7f8ee;color:#0b7a45;font-weight:700;font-size:15px;border-radius:999px;padding:7px 14px"><span class="dot"></span>All systems online</span></div>
  <div style="display:flex;gap:14px;margin-top:20px">
   <div class="stat" style="flex:1">{IC("globe","#0B63F6",30)}<div style="font-size:18px;font-weight:800;margin-top:8px">Domains</div><div style="font-size:14px;color:#0b7a45;font-weight:700;margin-top:3px">● Active</div></div>
   <div class="stat" style="flex:1">{IC("cloud","#0B63F6",30)}<div style="font-size:18px;font-weight:800;margin-top:8px">Hosting</div><div style="font-size:14px;color:#0b7a45;font-weight:700;margin-top:3px">● Online</div></div>
   <div class="stat" style="flex:1">{IC("server","#0B63F6",30)}<div style="font-size:18px;font-weight:800;margin-top:8px">Servers</div><div style="font-size:14px;color:#0b7a45;font-weight:700;margin-top:3px">● Running</div></div></div>
  <div class="stat" style="margin-top:14px;padding:16px 20px"><div style="display:flex;justify-content:space-between;font-size:17px;font-weight:800"><span>Website traffic</span><span style="color:#6b7a99;font-weight:600;font-size:14px">Last 7 days</span></div>{chart}</div>
  <div style="display:flex;gap:14px;margin-top:14px"><div class="stat" style="flex:1;display:flex;align-items:center;gap:12px;padding:14px 16px">{IC("lock","#12a05c",28)}<div><div style="font-size:16px;font-weight:800">SSL</div><div style="font-size:13px;color:#0b7a45;font-weight:700">Active</div></div></div><div class="stat" style="flex:1;display:flex;align-items:center;gap:12px;padding:14px 16px">{IC("shield","#0B63F6",28)}<div><div style="font-size:16px;font-weight:800">Firewall</div><div style="font-size:13px;color:#0b7a45;font-weight:700">On</div></div></div></div>
 </div></div>'''
def phone():
    return f'''<div style="position:absolute;left:0;top:0;width:250px;height:500px;border-radius:44px;background:#0b1535;padding:10px;box-shadow:0 50px 90px -20px rgba(0,5,60,.85),0 0 0 2px rgba(255,255,255,.25)">
<div style="width:100%;height:100%;border-radius:36px;background:#fff;overflow:hidden;position:relative">
 <div style="height:44px;display:flex;justify-content:space-between;align-items:center;padding:0 18px;font-size:12px;font-weight:700;color:#0B1220"><span>9:41</span><span style="width:70px;height:20px;border-radius:12px;background:#0b1535;display:block;margin-top:2px"></span><span>●●●</span></div>
 <div style="padding:6px 16px;display:flex;align-items:center;gap:8px;font-size:15px;font-weight:800">{mark(26)}yourbrand</div>
 <div style="margin:10px 14px;border-radius:22px;height:210px;background:linear-gradient(150deg,#0B63F6,#6fb0ff 60%,#bfe0ff);position:relative;overflow:hidden"><div style="position:absolute;left:16px;top:18px;color:#fff;font-size:22px;font-weight:800;line-height:1.1;letter-spacing:-.5px">Welcome to<br>our website</div><div style="position:absolute;left:16px;bottom:18px;background:#fff;color:#0B63F6;font-weight:800;font-size:13px;padding:9px 16px;border-radius:999px">Shop now</div><div style="position:absolute;right:-30px;bottom:-30px;width:130px;height:130px;border-radius:50%;background:rgba(255,255,255,.3)"></div></div>
 <div style="margin:0 14px;display:flex;gap:10px"><div style="flex:1;height:80px;border-radius:16px;background:#eef3ff"></div><div style="flex:1;height:80px;border-radius:16px;background:#eef3ff"></div></div>
 <div style="margin:14px 18px;font-size:12px;color:#12a05c;font-weight:800"><span class="dot"></span>Live on the cloud</div></div></div>'''
cover=f"""<html><style>{CSS}
.bg{{position:absolute;inset:0;background:radial-gradient(60% 80% at 72% 45%,rgba(30,110,255,.75) 0%,rgba(10,50,200,0) 70%),radial-gradient(40% 50% at 0% 0%,rgba(40,100,255,.45) 0%,rgba(40,100,255,0) 70%),linear-gradient(120deg,#07123d 0%,#040a28 45%,#06123f 100%)}}
.lines{{position:absolute;inset:0;opacity:.5}}</style>
<body style="width:2000px;height:1125px;position:relative;overflow:hidden;background:#040a28"><div class="bg"></div>
<svg class="lines" width="2000" height="1125" fill="none" stroke="#4d86ff" stroke-opacity=".28" stroke-width="1.6"><path d="M0 130 L520 60 L1120 330"/><path d="M130 420 L470 70"/><path d="M0 760 L1000 300 L1480 120"/><path d="M900 0 L1260 540"/><path d="M1500 1125 L1900 600"/><circle cx="470" cy="70" r="5" fill="#6aa4ff"/><circle cx="1120" cy="330" r="5" fill="#6aa4ff"/></svg>
<div style="position:absolute;left:170px;top:245px;width:820px;color:#fff">
 <div style="display:flex;align-items:center;gap:22px">{mark(98,"#fff")}<span style="font-size:48px;font-weight:700;letter-spacing:-1.5px">SatisfyCloud</span></div>
 <div style="font-size:106px;line-height:1;font-weight:800;letter-spacing:-4.4px;margin-top:34px">More Security.<br><span style="background:linear-gradient(90deg,#7fb8ff,#fff);-webkit-background-clip:text;color:transparent">More Control.</span></div>
 <div style="font-size:30px;line-height:1.45;color:rgba(255,255,255,.8);margin-top:26px;font-weight:500;max-width:690px">Domains, hosting &amp; servers for businesses worldwide — all under one roof.</div>
 <div style="margin-top:36px;display:flex;gap:16px"><span class="pill" style="font-size:27px;padding:18px 36px;background:#fff;color:#0B63F6;box-shadow:0 18px 40px -8px rgba(0,0,0,.5)">Order your domain →</span><span class="pill" style="font-size:27px;padding:16px 30px;border:2px solid rgba(255,255,255,.55);color:#fff">satisfycloud.com</span></div>
</div>
<div style="position:absolute;left:955px;top:182px;width:960px;height:900px;perspective:2600px;transform:scale(.9);transform-origin:0 0">
 <div style="position:absolute;left:150px;top:150px;width:760px;height:560px;transform:rotateY(-16deg) rotateX(7deg) rotateZ(-2.5deg);transform-style:preserve-3d;-webkit-mask-image:linear-gradient(180deg,#000 0%,#000 82%,transparent 100%);mask-image:linear-gradient(180deg,#000 0%,#000 82%,transparent 100%)">{dashboard()}</div>
 <div style="position:absolute;left:10px;top:330px;width:250px;height:500px;transform:rotateY(14deg) rotateZ(4deg) rotateX(4deg)">{phone()}</div>
 <div class="fl" style="left:20px;top:70px;width:560px;height:100px;border-radius:30px;display:flex;align-items:center;padding:0 16px 0 22px;gap:16px;transform:rotate(-4deg)">{IC("globe","#0B63F6",40)}<div style="flex:1;font-size:34px;font-weight:800;letter-spacing:-1px">yourbrand<span style="color:#0B63F6">.com</span></div><span style="background:#0B63F6;color:#fff;font-weight:800;font-size:22px;border-radius:18px;padding:16px 26px">Order</span></div>
 <div class="fl" style="left:600px;top:60px;width:300px;padding:18px 20px;display:flex;gap:14px;align-items:center;transform:rotate(3deg)"><span class="ibx g">{IC("check","#fff",30,3)}</span><div><div style="font-size:24px;font-weight:800;letter-spacing:-.6px">Hosting ready</div><div style="font-size:14px;color:#6b7a99;font-weight:600">Live on the cloud</div></div></div>
 <div class="fl" style="left:430px;top:690px;width:400px;padding:18px 22px;display:flex;gap:16px;align-items:center;transform:rotate(-2deg)"><span class="ibx g" style="width:56px;height:56px">{IC("lock","#fff",28)}</span><div style="flex:1;font-size:25px;font-weight:800;letter-spacing:-.6px">SSL Certificate</div><span style="background:#e7f8ee;color:#0b7a45;font-weight:800;font-size:17px;border-radius:12px;padding:9px 16px">Active</span></div>
 <div class="fl" style="left:690px;top:470px;width:250px;padding:20px 22px;transform:rotate(3deg)"><div style="display:flex;align-items:center;gap:12px">{IC("shield","#0B63F6",34)}<div style="font-size:24px;font-weight:800;letter-spacing:-.6px">Protected</div></div><div style="display:flex;gap:6px;margin-top:14px;align-items:flex-end;height:36px">{"".join(f'<i style="width:14px;border-radius:5px;background:linear-gradient(180deg,#4b9bff,#0B63F6);height:{h}px"></i>' for h in (14,22,18,30,24,36,28))}</div><div style="font-size:14px;color:#6b7a99;font-weight:600;margin-top:8px">Server status · Online</div></div>
</div></body></html>"""
open("cover.html","w").write(cover)
def chip(x,y,icon,t,sub,g=False):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;transform:translate(-50%,-50%);display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.92);border:1.5px solid #fff;border-radius:24px;padding:12px 24px 12px 12px;box-shadow:0 26px 50px -16px rgba(10,50,150,.4),0 6px 14px rgba(10,50,150,.10);white-space:nowrap"><span class="ibx {"g" if g else ""}" style="width:54px;height:54px;border-radius:17px">{IC(icon,"#fff",28)}</span><span><b style="font-size:25px;font-weight:800;letter-spacing:-.6px;display:block">{t}</b><i style="font-style:normal;font-size:15px;color:#5f6f8f;font-weight:600">{sub}</i></span></div>'
cx,cy,cw=540,722,330
chm=[(190,575,"globe","Domains","Register yours"),(160,722,"cloud","Web Hosting","Fast & reliable"),(190,869,"server","Servers","VPS & dedicated"),(890,575,"lock","SSL Secured","Always active"),(920,722,"shield","Firewall On","Protected"),(890,869,"db","Auto Backups","Every day")]
lines="".join(f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="#0B63F6" stroke-opacity=".3" stroke-width="2" stroke-dasharray="2 8" stroke-linecap="round"/><circle cx="{x}" cy="{y}" r="6" fill="#0B63F6"/>' for x,y,*_ in chm)
rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#0B63F6" stroke-opacity="{o}" stroke-width="2" {d}/>' for r,o,d in [(520,.10,'stroke-dasharray="3 10"'),(400,.16,''),(280,.2,'stroke-dasharray="2 9"')])
mh=cw*MH/MW;sc=cw/MW
post=f"""<html><style>{CSS}</style><body style="width:1080px;height:1080px;position:relative;overflow:hidden;background:#fff">
<div style="position:absolute;inset:0;background:radial-gradient(60% 50% at 50% 66%,rgba(110,170,255,.55) 0%,rgba(110,170,255,0) 72%),linear-gradient(180deg,#f2f7ff 0%,#fff 100%)"></div>
<svg width="1080" height="1080" style="position:absolute;inset:0"><defs><radialGradient id="gl"><stop offset="0" stop-color="#5aa0ff" stop-opacity=".6"/><stop offset="1" stop-color="#5aa0ff" stop-opacity="0"/></radialGradient>
<linearGradient id="cg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4b9bff"/><stop offset=".45" stop-color="#0B63F6"/><stop offset="1" stop-color="#0636bf"/></linearGradient>
<linearGradient id="sh" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/></linearGradient>
<filter id="bl" x="-50%" y="-300%" width="200%" height="700%"><feGaussianBlur stdDeviation="22"/></filter></defs>
{rings}<circle cx="{cx}" cy="{cy}" r="250" fill="url(#gl)"/>{lines}
<ellipse cx="{cx}" cy="{cy+mh/2+18}" rx="{cw*.4}" ry="20" fill="#0B3FC0" opacity=".45" filter="url(#bl)"/>
<g transform="translate({cx-cw/2},{cy-mh/2}) scale({sc})"><path d="{D}" fill="url(#cg)"/><path d="{D}" fill="url(#sh)"/></g></svg>
<div style="position:absolute;left:0;right:0;top:58px;display:flex;justify-content:center;align-items:center;gap:16px">{mark(70)}<span style="font-size:34px;font-weight:700;letter-spacing:-1px">SatisfyCloud</span></div>
<div style="position:absolute;left:0;right:0;top:160px;text-align:center"><span style="display:inline-block;background:#fff;color:#0B63F6;font-weight:800;font-size:20px;letter-spacing:1px;border-radius:999px;padding:9px 22px;box-shadow:0 10px 26px rgba(11,99,246,.18)">ALL-IN-ONE CLOUD · WORLDWIDE</span>
<div style="font-size:82px;line-height:1;font-weight:800;letter-spacing:-3.3px;margin-top:20px">Your idea. Your domain.<br><span style="color:#0B63F6">Your cloud.</span></div></div>
{"".join(chip(*c,g=False) for c in chm)}
<div style="position:absolute;left:0;right:0;bottom:44px;display:flex;justify-content:center"><span class="pill" style="font-size:31px;padding:17px 44px;background:linear-gradient(180deg,#2a7bff,#0B63F6);color:#fff;box-shadow:0 18px 36px -6px rgba(11,99,246,.5)">satisfycloud.com →</span></div>
</body></html>"""
open("post.html","w").write(post)
CH='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'
with sync_playwright() as pw:
    br=pw.chromium.launch(executable_path=CH,args=['--no-sandbox'])
    pg=br.new_page(viewport={"width":2000,"height":1125});pg.goto("file:///home/user/logo-design-skill/satisfycloud/social/cover.html");pg.wait_for_timeout(200);pg.screenshot(path="facebook-cover.png");pg.close();pg=br.new_page(viewport={"width":1080,"height":1080},device_scale_factor=2);pg.goto("file:///home/user/logo-design-skill/satisfycloud/social/post.html");pg.wait_for_timeout(200);pg.screenshot(path="facebook-post@2x.png");br.close()
