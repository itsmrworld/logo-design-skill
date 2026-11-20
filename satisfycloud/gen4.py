B="#2447FF"
CP='<rect x="76" y="300" width="360" height="100" rx="50"/><circle cx="182" cy="288" r="76"/><circle cx="292" cy="248" r="108"/>'
GAP="M262 112 C212 186 254 238 316 264 C382 292 362 356 292 428"
def mk(name,fg,bg=None,pad=0):
    bgr=f'<rect width="512" height="512" fill="{bg}"/>' if bg else ''
    open(name,"w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><title>SatisfyCloud mark</title><defs><mask id="m"><rect width="512" height="512" fill="#fff"/><path d="{GAP}" fill="none" stroke="#000" stroke-width="26"/></mask></defs>{bgr}<g transform="translate(0,-14)"><g mask="url(#m)" fill="{fg}">{CP}</g></g></svg>''')
mk("v-a.svg",B)
mk("logo-white-on-brand.svg","#FFFFFF",B)
mk("logo-brand-on-white.svg",B,"#FFFFFF")
mk("logo-transparent.svg",B)
