exec(open("gen.py").read().split("# A:")[0])
CP=CLOUD_PARTS
def svg(body,defs=""): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><defs>{defs}</defs>{body}</svg>'
# A: two-tone cloud split by a flowing S ribbon-gap
spine="M478 146 C330 146 196 196 256 262 C316 328 182 378 34 378"
region=spine+" L-100 378 L-100 -100 L478 -100 Z"
defs=f'<clipPath id="c">{CP}</clipPath><mask id="m"><rect width="512" height="512" fill="#fff"/><path d="{spine}" fill="none" stroke="#000" stroke-width="24"/></mask>'
body=f'<g mask="url(#m)"><g clip-path="url(#c)"><rect width="512" height="512" fill="{DEEP}"/><path d="{region}" fill="{LIGHT}"/></g></g>'
open("a-split.svg","w").write(svg(body,defs))
# B: outline cloud + solid S
strokes=CP.replace('/>',' stroke="#fff" stroke-width="56"/>')
fills=f'<g fill="#000">{CP}</g>'
defs=f'<mask id="r"><rect width="512" height="512" fill="#000"/><g fill="#fff">{strokes}</g>{fills}</mask>'
sb=S(256,270,34,a0=-35,a1=145)
body=f'<rect width="512" height="512" fill="{BLUE}" mask="url(#r)"/><path d="{sb}" fill="none" stroke="{BLUE}" stroke-width="28" stroke-linecap="round"/>'
open("b-outline.svg","w").write(svg(body,defs))
# C: solid, negative S
sc=S(260,268,42,a0=-35,a1=145)
mask=f'<mask id="m"><rect width="512" height="512" fill="#fff"/><path d="{sc}" fill="none" stroke="#000" stroke-width="30" stroke-linecap="round"/></mask>'
open("c-negative.svg","w").write(svg(f'<g fill="{BLUE}" mask="url(#m)">{CP}</g>',mask))
