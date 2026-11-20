import re, math
from playwright.sync_api import sync_playwright
Dw=open("../dist/svg/mark-tight_white.svg").read(); D=re.search(r' d="([^"]+)"',Dw)[1]
MW,MH=[int(x) for x in re.search(r'viewBox="0 0 (\d+) (\d+)"',Dw).groups()]
def mark(w,c="#0B63F6"): return f'<svg viewBox="0 0 {MW} {MH}" width="{w}" height="{w*MH/MW:.1f}"><path fill="{c}" d="{D}"/></svg>'
def ic(p,c="#fff",s=30,w=2.2): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'
I={"globe":ic('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/>'),
"lock":ic('<rect x="4.5" y="10.5" width="15" height="10" rx="2.5"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/>'),
"shield":ic('<path d="M12 3l7.5 3v5.5c0 4.6-3.1 8.2-7.5 9.5-4.4-1.3-7.5-4.9-7.5-9.5V6z"/><path d="M8.6 12.2l2.5 2.5 4.4-4.9"/>'),
"db":ic('<ellipse cx="12" cy="6" rx="7.5" ry="3"/><path d="M4.5 6v6c0 1.7 3.4 3 7.5 3s7.5-1.3 7.5-3V6M4.5 12v6c0 1.7 3.4 3 7.5 3s7.5-1.3 7.5-3v-6"/>'),
"check":ic('<path d="M5 12.5l4.5 4.5L19 7.5"/>',"#fff",30,3.2),
"bolt":ic('<path d="M13 2L4.5 13.5H11L10 22l8.5-11.5H12z"/>')}
CSS="""*{margin:0;box-sizing:border-box}body{font-family:'Inter Display','Inter',Arial,sans-serif;color:#0B1220;background:#fff}
.bg{position:absolute;inset:0;background:radial-gradient(55% 70% at 74% 48%,rgba(110,170,255,.55) 0%,rgba(110,170,255,0) 72%),radial-gradient(45% 55% at 0% 100%,rgba(190,215,255,.7) 0%,rgba(190,215,255,0) 70%),linear-gradient(180deg,#f2f7ff 0%,#fff 100%)}
.pill{display:inline-flex;align-items:center;gap:14px;background:linear-gradient(180deg,#2a7bff,#0B63F6);color:#fff;font-weight:700;border-radius:999px;box-shadow:0 18px 36px -6px rgba(11,99,246,.5),inset 0 1px 0 rgba(255,255,255,.35)}
.ghost{display:inline-flex;align-items:center;background:#fff;border:2px solid #cfe0ff;color:#0B63F6;font-weight:700;border-radius:999px}
.chip{position:absolute;display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.88);backdrop-filter:blur(8px);border:1.5px solid #fff;border-radius:24px;padding:14px 26px 14px 14px;box-shadow:0 30px 60px -18px rgba(10,50,150,.35),0 6px 16px rgba(10,50,150,.10);white-space:nowrap}
.chip b{font-size:27px;font-weight:800;letter-spacing:-.6px;display:block}.chip i{font-style:normal;font-size:16px;color:#5f6f8f;font-weight:600;display:block;margin-top:1px}
.ib{width:58px;height:58px;border-radius:18px;background:linear-gradient(150deg,#3a8bff,#0B63F6);display:flex;align-items:center;justify-content:center;box-shadow:0 10px 20px rgba(11,99,246,.35),inset 0 1px 0 rgba(255,255,255,.4)}
.ib.g{background:linear-gradient(150deg,#2fd083,#0e9a55);box-shadow:0 10px 20px rgba(18,160,92,.35),inset 0 1px 0 rgba(255,255,255,.4)}"""
def hero(chips,S=900,cloud=520):
    c=S/2; mh=cloud*MH/MW; sc=cloud/MW
    rings="".join(f'<circle cx="{c}" cy="{c}" r="{r}" fill="none" stroke="#0B63F6" stroke-opacity="{o}" stroke-width="{w}" {d}/>' for r,o,w,d in [(c*.98,.12,2,'stroke-dasharray="3 10"'),(c*.80,.16,2,''),(c*.60,.20,2.5,'stroke-dasharray="2 9"'),(c*.42,.12,2,'')])
    lines="";cs=""
    for ang,rad,icon,t,sub,g in chips:
        a=math.radians(ang);x=c+math.cos(a)*c*rad;y=c+math.sin(a)*c*rad
        lines+=f'<line x1="{c}" y1="{c}" x2="{x:.0f}" y2="{y:.0f}" stroke="#0B63F6" stroke-opacity=".28" stroke-width="2" stroke-dasharray="2 8" stroke-linecap="round"/><circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="#0B63F6"/>'
        cs+=f'<div class="chip" style="left:{x:.0f}px;top:{y:.0f}px;transform:translate(-50%,-50%)"><span class="ib {"g" if g else ""}">{I[icon]}</span><span><b>{t}</b><i>{sub}</i></span></div>'
    return f'''<div style="position:relative;width:{S}px;height:{S}px">
<svg width="{S}" height="{S}" style="position:absolute;inset:0" viewBox="0 0 {S} {S}"><defs>
<radialGradient id="gl"><stop offset="0" stop-color="#5aa0ff" stop-opacity=".55"/><stop offset="1" stop-color="#5aa0ff" stop-opacity="0"/></radialGradient>
<linearGradient id="cg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4b9bff"/><stop offset=".45" stop-color="#0B63F6"/><stop offset="1" stop-color="#0636bf"/></linearGradient>
<linearGradient id="sh" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/></linearGradient>
<filter id="bl" x="-50%" y="-300%" width="200%" height="700%"><feGaussianBlur stdDeviation="26"/></filter></defs>
{rings}<circle cx="{c}" cy="{c}" r="{c*.62}" fill="url(#gl)"/>
<ellipse cx="{c}" cy="{c+mh/2+22}" rx="{cloud*.40}" ry="26" fill="#0B3FC0" opacity=".45" filter="url(#bl)"/>
{lines}
<g transform="translate({c-cloud/2},{c-mh/2}) scale({sc})"><path d="{D}" fill="url(#cg)"/><path d="{D}" fill="url(#sh)"/></g>
</svg>{cs}</div>'''
def head(sz): return ""
cover_chips=[(-62,.84,"globe",".com Domain","Available now",0),(14,.78,"lock","SSL Secured","Active",0),(78,.80,"shield","Firewall On","Protected",0),(150,.80,"db","Auto Backups","Every day",0),(-135,.80,"check","Hosting Ready","Live on the cloud",1)]
cover=f"""<html><style>{CSS}</style><body style="width:2000px;height:1125px;position:relative;overflow:hidden">
<div class="bg"></div>
<div style="position:absolute;left:190px;top:196px;width:900px">
 <div style="display:flex;align-items:center;gap:22px">{mark(104)}<span style="font-size:50px;font-weight:700;letter-spacing:-1.5px">SatisfyCloud</span></div>
 <div style="font-size:116px;line-height:.99;font-weight:800;letter-spacing:-4.8px;margin-top:34px">More Security.<br><span style="color:#0B63F6">More Control.</span></div>
 <div style="font-size:31px;line-height:1.42;color:#44516d;margin-top:26px;font-weight:500;max-width:720px">Domains &amp; cloud hosting for businesses worldwide — protected, simple and fully in your hands.</div>
 <div style="margin-top:34px;display:flex;gap:16px"><span class="pill" style="font-size:28px;padding:19px 38px">Order your domain →</span><span class="ghost" style="font-size:28px;padding:17px 32px">satisfycloud.com</span></div>
</div>
<div style="position:absolute;left:940px;top:105px">{hero(cover_chips,S=960,cloud=560)}</div>
</body></html>"""
post_chips=[(-152,.70,"globe",".com Domain","Available now",0),(-28,.70,"lock","SSL Secured","Active",0),(168,.72,"db","Auto Backups","Every day",0),(12,.72,"shield","Firewall On","Protected",0)]
post=f"""<html><style>{CSS}</style><body style="width:1080px;height:1080px;position:relative;overflow:hidden">
<div class="bg" style="background:radial-gradient(70% 55% at 50% 72%,rgba(110,170,255,.55) 0%,rgba(110,170,255,0) 72%),linear-gradient(180deg,#f2f7ff 0%,#fff 100%)"></div>
<div style="position:absolute;left:0;right:0;top:64px;display:flex;justify-content:center;align-items:center;gap:16px">{mark(72)}<span style="font-size:34px;font-weight:700;letter-spacing:-1px">SatisfyCloud</span></div>
<div style="position:absolute;left:0;right:0;top:180px;text-align:center;font-size:88px;line-height:1;font-weight:800;letter-spacing:-3.6px">Your idea. Your domain.<br><span style="color:#0B63F6">Your cloud.</span></div>
<div style="position:absolute;left:50%;top:322px;margin-left:-480px;transform:scale(1);transform-origin:center top">{hero(post_chips,S=960,cloud=370).replace('class="chip"','class="chip" data-p="1"')}</div>
<div style="position:absolute;left:0;right:0;bottom:46px;display:flex;justify-content:center"><span class="pill" style="font-size:32px;padding:18px 44px">satisfycloud.com →</span></div>
</body></html>"""
open("cover.html","w").write(cover);open("post.html","w").write(post)
CH='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'
with sync_playwright() as pw:
    br=pw.chromium.launch(executable_path=CH,args=['--no-sandbox'])
    for n,w,h,sc,out in [("cover",2000,1125,1,"facebook-cover.png"),("post",1080,1080,2,"facebook-post@2x.png")]:
        pg=br.new_page(viewport={"width":w,"height":h},device_scale_factor=sc);pg.goto(f"file:///home/user/logo-design-skill/satisfycloud/social/{n}.html");pg.screenshot(path=out);pg.close()
    br.close()
