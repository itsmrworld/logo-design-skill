import sys
B="#0B63F6"
# silhouette in reference coordinates (400 canvas)
CP='<circle cx="155" cy="231" r="61"/><circle cx="214" cy="214" r="78"/><circle cx="256" cy="237" r="54"/><rect x="155" y="200" width="101" height="91"/>'
CLIPBOT='<rect x="0" y="0" width="400" height="291"/>'
GAP="M170 118 C176 168 202 198 236 218 C272 239 272 264 254 280 C244 289 228 296 204 302"
def mk(name,fg,bg=None,scale=1.3,gap=22):
    bgr=f'<rect width="400" height="400" fill="{bg}"/>' if bg else ''
    tf=f'translate(200,200) scale({scale}) translate(-202,-214)'
    open(name,"w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400"><title>SatisfyCloud mark</title><defs><clipPath id="b"><rect x="0" y="0" width="400" height="291"/></clipPath><mask id="m"><rect width="400" height="400" fill="#fff"/><path d="{GAP}" fill="none" stroke="#000" stroke-width="{gap}"/></mask></defs>{bgr}<g transform="{tf}"><g mask="url(#m)" clip-path="url(#b)" fill="{fg}">{CP}</g></g></svg>''')
mk("ref-test.svg",B,"#fff",scale=1)
mk("logo-white-on-brand.svg","#fff",B)
mk("logo-brand-on-white.svg",B,"#fff")
mk("logo-transparent.svg",B)
