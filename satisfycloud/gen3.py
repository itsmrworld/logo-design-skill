CP='<rect x="64" y="290" width="384" height="112" rx="56"/><circle cx="190" cy="268" r="82"/><circle cx="305" cy="232" r="104"/>'
def mk(name,spine,close,light,deep,gap=22,bg=None):
    region=spine+close
    bgr=f'<rect width="512" height="512" fill="{bg}"/>' if bg else ''
    s=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><title>SatisfyCloud mark</title><defs><clipPath id="c">{CP}</clipPath>
<mask id="m"><rect width="512" height="512" fill="#fff"/><path d="{spine}" fill="none" stroke="#000" stroke-width="{gap}"/></mask></defs>{bgr}
<g mask="url(#m)"><g clip-path="url(#c)"><rect width="512" height="512" fill="{deep}"/><path d="{region}" fill="{light}"/></g></g></svg>'''
    open(name,"w").write(s)
H="M490 158 C338 140 196 190 256 262 C316 334 172 384 22 372"
V="M352 90 C226 126 186 212 256 262 C326 312 290 392 170 424"
mk("v1.svg",H," L-100 372 L-100 -100 L490 -100 Z","#5B7CFF","#2A3BFF")
mk("v2.svg",V," L170 424 L-100 600 L-100 -100 L352 -100 Z","#5B7CFF","#2A3BFF")
mk("v3.svg",V," L170 424 L-100 600 L-100 -100 L352 -100 Z","#7C8CFF","#3B4EFF",bg="#15161A")
mk("v4.svg",H," L-100 372 L-100 -100 L490 -100 Z","#7C8CFF","#3B4EFF",bg="#15161A")
cl=" L-100 380 L-100 -100 L490 -100 Z"
mk("w1.svg","M490 150 C340 120 190 170 232 240 C268 300 190 372 20 380",cl,"#6F86FF","#2A3BFF")
mk("w2.svg","M490 140 C330 130 200 160 214 226 C228 290 322 262 330 318 C336 366 200 388 20 384"," L-100 384 L-100 -100 L490 -100 Z","#6F86FF","#2A3BFF")
sp="M490 140 C330 130 200 160 214 226 C228 290 322 262 330 318 C336 372 210 410 60 440"
c2=" L60 440 L-100 440 L-100 -100 L490 -100 Z"
mk("satisfycloud-mark.svg",sp,c2,"#6F86FF","#2A3BFF")
mk("satisfycloud-mark-dark.svg",sp,c2,"#8EA0FF","#4A5CFF",bg="#15161A")
mk("satisfycloud-mark-mono.svg",sp,c2,"#2A3BFF","#2A3BFF")
