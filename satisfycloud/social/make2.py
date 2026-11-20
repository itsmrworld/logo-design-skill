import re
from playwright.sync_api import sync_playwright
Dw=open("../dist/svg/mark-tight_white.svg").read(); D=re.search(r' d="([^"]+)"',Dw)[1]
MW,MH=[int(x) for x in re.search(r'viewBox="0 0 (\d+) (\d+)"',Dw).groups()]
def mark(w,c="#0B63F6",extra=""): return f'<svg {extra} viewBox="0 0 {MW} {MH}" width="{w}" height="{w*MH/MW:.1f}"><path fill="{c}" d="{D}"/></svg>'
CHECK='<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
LOCK='<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#12a05c" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><rect x="4.5" y="10.5" width="15" height="10" rx="2.5"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/></svg>'
SHIELD='<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#0B63F6" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7.5 3v5.5c0 4.6-3.1 8.2-7.5 9.5-4.4-1.3-7.5-4.9-7.5-9.5V6z"/><path d="M8.6 12.2l2.5 2.5 4.4-4.9"/></svg>'
GLOBE='<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#0B63F6" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/></svg>'
CSS="""*{margin:0;box-sizing:border-box}body{font-family:'Inter Display','Inter',Arial,sans-serif;color:#0B1220;background:#fff}
.sky{position:absolute;inset:0;background:radial-gradient(90% 120% at 85% 0%,#d9e8ff 0%,#eef5ff 45%,#fff 100%)}
.blob{position:absolute;border-radius:50%;background:#fff;filter:blur(2px);box-shadow:0 30px 80px rgba(11,99,246,.10)}
.card{position:absolute;background:#fff;border-radius:26px;box-shadow:0 30px 70px rgba(11,60,160,.16),0 4px 14px rgba(11,60,160,.07);border:1px solid rgba(11,99,246,.07)}
.btn{background:#0B63F6;color:#fff;font-weight:700;border-radius:14px;display:inline-flex;align-items:center}
.ok{display:inline-flex;align-items:center;justify-content:center;background:#12a05c;border-radius:50%}
.tag{display:inline-flex;align-items:center;gap:8px;background:#e8f8ef;color:#0b7a45;font-weight:700;border-radius:999px}
.pill{display:inline-flex;align-items:center;background:#0B63F6;color:#fff;font-weight:700;border-radius:999px;box-shadow:0 14px 30px rgba(11,99,246,.35)}
.ghost{display:inline-flex;align-items:center;border:2px solid #cfe0ff;color:#0B63F6;font-weight:700;border-radius:999px;background:#fff}"""
def cards(s=1.0):
    return f'''
<div class="card" style="left:0;top:40px;width:560px;padding:26px 28px;transform:rotate(-2.5deg)">
 <div style="font-size:17px;color:#6b7a99;font-weight:600;margin-bottom:12px">Find your perfect domain</div>
 <div style="display:flex;gap:12px;align-items:center"><div style="flex:1;border:2px solid #dbe7ff;border-radius:14px;padding:14px 16px;display:flex;align-items:center;gap:12px;background:#f6f9ff">{GLOBE}<span style="font-size:24px;font-weight:700">yourbrand<span style="color:#0B63F6">.com</span></span></div><div class="btn" style="font-size:20px;padding:16px 24px">Order</div></div>
 <div class="tag" style="font-size:16px;padding:7px 14px;margin-top:14px"><span class="ok" style="width:22px;height:22px"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span>Available — claim it now</div>
</div>
<div class="card" style="left:150px;top:290px;width:470px;padding:24px 28px;transform:rotate(1.8deg)">
 <div style="display:flex;align-items:center;gap:16px"><span class="ok" style="width:50px;height:50px">{CHECK}</span><div><div style="font-size:26px;font-weight:800;letter-spacing:-.5px">Your hosting is ready</div><div style="font-size:16px;color:#6b7a99;font-weight:500;margin-top:2px">Your website is live on the cloud</div></div></div>
 <div style="height:10px;border-radius:9px;background:#e6efff;margin-top:20px;overflow:hidden"><div style="width:100%;height:100%;background:linear-gradient(90deg,#0B63F6,#38b6ff)"></div></div>
</div>
<div class="card" style="left:-20px;top:500px;width:330px;padding:22px 24px;transform:rotate(-1.5deg)">
 <div style="display:flex;align-items:center;gap:14px">{LOCK}<div style="font-size:22px;font-weight:800">SSL Certificate</div></div><div class="tag" style="font-size:15px;padding:6px 14px;margin-top:12px">● Active</div>
</div>
<div class="card" style="left:340px;top:520px;width:290px;padding:22px 24px;transform:rotate(2.2deg)">
 <div style="display:flex;align-items:center;gap:14px">{SHIELD}<div style="font-size:22px;font-weight:800">Protected</div></div>
 <div style="font-size:15px;color:#6b7a99;margin-top:8px;font-weight:500">You stay in control</div>
 <div style="display:flex;gap:8px;margin-top:12px"><span style="width:46px;height:26px;border-radius:14px;background:#0B63F6;position:relative"><i style="position:absolute;right:3px;top:3px;width:20px;height:20px;border-radius:50%;background:#fff"></i></span><span style="width:46px;height:26px;border-radius:14px;background:#0B63F6;position:relative"><i style="position:absolute;right:3px;top:3px;width:20px;height:20px;border-radius:50%;background:#fff"></i></span></div>
</div>'''
cover=f"""<html><style>{CSS}</style><body style="width:1640px;height:856px;position:relative;overflow:hidden">
<div class="sky"></div>
<div style="position:absolute;right:-120px;top:70px;opacity:.55">{mark(980,"#dfeaff")}</div>
<div class="blob" style="width:420px;height:200px;left:-120px;bottom:-60px"></div><div class="blob" style="width:520px;height:230px;left:260px;bottom:-110px"></div>
<div style="position:absolute;left:130px;top:150px;width:780px">
 <div style="display:flex;align-items:center;gap:20px">{mark(96)}<span style="font-size:44px;font-weight:700;letter-spacing:-1.2px">SatisfyCloud</span></div>
 <div style="font-size:92px;line-height:1;font-weight:800;letter-spacing:-3.5px;margin-top:30px">More Security.<br><span style="color:#0B63F6">More Control.</span></div>
 <div style="font-size:27px;line-height:1.4;color:#44516d;margin-top:26px;font-weight:500;max-width:640px">Domains &amp; cloud hosting for businesses worldwide — protected, simple and fully in your hands.</div>
 <div style="margin-top:34px;display:flex;gap:14px"><span class="pill" style="font-size:25px;padding:15px 32px">Order your domain →</span><span class="ghost" style="font-size:25px;padding:13px 28px">satisfycloud.com</span></div>
</div>
<div style="position:absolute;left:930px;top:130px;width:640px;height:640px">{cards()}</div>
</body></html>"""
post=f"""<html><style>{CSS}</style><body style="width:1080px;height:1080px;position:relative;overflow:hidden">
<div class="sky" style="background:radial-gradient(100% 90% at 50% 0%,#cfe2ff 0%,#eaf3ff 45%,#fff 80%)"></div>
<div class="blob" style="width:520px;height:230px;left:-140px;bottom:90px;opacity:.9"></div><div class="blob" style="width:640px;height:260px;right:-170px;bottom:-40px"></div><div class="blob" style="width:420px;height:180px;left:300px;bottom:-60px"></div>
<div style="position:absolute;left:0;right:0;top:70px;display:flex;justify-content:center;align-items:center;gap:18px">{mark(82)}<span style="font-size:38px;font-weight:700;letter-spacing:-1px">SatisfyCloud</span></div>
<div style="position:absolute;left:0;right:0;top:190px;text-align:center">
 <div class="tag" style="font-size:22px;padding:9px 22px;letter-spacing:.4px;background:#fff;color:#0B63F6;box-shadow:0 8px 24px rgba(11,99,246,.15)">☁ NOW LIVE · WORLDWIDE</div>
 <div style="font-size:104px;line-height:1;font-weight:800;letter-spacing:-4px;margin-top:30px">Your idea.<br>Your domain.<br><span style="color:#0B63F6">Your cloud.</span></div>
</div>
<div style="position:absolute;left:210px;top:655px;width:660px;height:330px;transform:scale(.88);transform-origin:left top">
 <div class="card" style="left:0;top:0;width:560px;padding:26px 28px;transform:rotate(-2deg)">
  <div style="display:flex;gap:12px;align-items:center"><div style="flex:1;border:2px solid #dbe7ff;border-radius:14px;padding:14px 16px;display:flex;align-items:center;gap:12px;background:#f6f9ff">{GLOBE}<span style="font-size:26px;font-weight:700">yourbrand<span style="color:#0B63F6">.com</span></span></div><div class="btn" style="font-size:22px;padding:17px 26px">Order</div></div>
  <div class="tag" style="font-size:17px;padding:7px 14px;margin-top:14px"><span class="ok" style="width:22px;height:22px"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span>Available — claim it now</div>
 </div>
 <div class="card" style="left:260px;top:170px;width:470px;padding:22px 26px;transform:rotate(2deg)"><div style="display:flex;align-items:center;gap:16px"><span class="ok" style="width:48px;height:48px">{CHECK}</span><div><div style="font-size:25px;font-weight:800;letter-spacing:-.5px">Your hosting is ready</div><div style="font-size:15px;color:#6b7a99;font-weight:500">Secure · SSL active</div></div></div></div>
</div>
<div style="position:absolute;left:0;right:0;bottom:56px;display:flex;justify-content:center"><span class="pill" style="font-size:32px;padding:18px 44px">satisfycloud.com</span></div>
</body></html>"""
open("cover.html","w").write(cover);open("post.html","w").write(post)
CH='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'
with sync_playwright() as pw:
    br=pw.chromium.launch(executable_path=CH,args=['--no-sandbox'])
    for n,w,h,sc,out in [("cover",1640,856,1,"facebook-cover.png"),("cover",1640,856,2,"facebook-cover@2x.png"),("post",1080,1080,2,"facebook-post@2x.png")]:
        pg=br.new_page(viewport={"width":w,"height":h},device_scale_factor=sc);pg.goto(f"file:///home/user/logo-design-skill/satisfycloud/social/{n}.html");pg.screenshot(path=out);pg.close()
    br.close()
from PIL import Image
c=Image.open("facebook-cover.png").convert("RGB")
desk=c.crop((0,116,1640,740)).resize((820,312)); mob=c.crop((58,0,1582,856)).resize((640,360))
sheet=Image.new("RGB",(1560,420),"#cfd6e4");sheet.paste(desk,(20,50));sheet.paste(mob,(880,30));sheet.save("preview-desktop-mobile.png")
