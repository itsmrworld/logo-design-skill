import math
def pt(cx,cy,r,deg): a=math.radians(deg); return cx+r*math.cos(a), cy+r*math.sin(a)
def f(p): return f"{p[0]:.1f} {p[1]:.1f}"
CLOUD_PARTS='<rect x="64" y="290" width="384" height="112" rx="56"/><circle cx="190" cy="268" r="82"/><circle cx="305" cy="232" r="104"/>'
def S(cx,cy,r,tail=0,a0=-35,a1=145):
    # two stacked circles; top ccw from a0, bottom cw to a1; optional straight tangent tails
    t=(cx,cy-r); b=(cx,cy+r); tc=(cx,cy-r); bc=(cx,cy+r)  # top circle centre (cx,cy-r), bottom (cx,cy+r)
    s=pt(cx,cy-r,r,a0); e=pt(cx,cy+r,r,a1)
    d=""
    if tail:
        # tangent at a0 for ccw motion (decreasing angle? we go ccw on screen = increasing sweep 0 => angle decreasing)
        ta=math.radians(a0-90)  # direction of travel backwards
        s0=(s[0]-tail*math.cos(ta)*-1, s[1]-tail*math.sin(ta)*-1)
        # moving along path at start: direction = derivative for decreasing angle = (sin a, -cos a)
        da=math.radians(a0); dirv=(math.sin(da),-math.cos(da))
        s0=(s[0]-dirv[0]*tail, s[1]-dirv[1]*tail)
        d+=f"M{f(s0)} L{f(s)} "
    else: d+=f"M{f(s)} "
    d+=f"A{r} {r} 0 1 0 {f((cx,cy))} A{r} {r} 0 1 1 {f(e)}"
    if tail:
        da=math.radians(a1); dirv=(-math.sin(da),math.cos(da))  # cw travel direction
        e2=(e[0]+dirv[0]*tail,e[1]+dirv[1]*tail); d+=f" L{f(e2)}"
    return d
BLUE="#0A5CF5"; LIGHT="#38B6FF"; DEEP="#0638C9"
def svg(body,defs=""): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><defs>{defs}</defs>{body}</svg>'
# A: two-tone split cloud, S-shaped gap through whole cloud
sa=S(256,258,50,tail=170,a0=-50,a1=130)
cl=f'<clipPath id="c">{CLOUD_PARTS}</clipPath>'
mask=f'<mask id="m"><rect width="512" height="512" fill="#fff"/><path d="{sa}" fill="none" stroke="#000" stroke-width="24"/></mask>'
# left region: spine closed to far left
spine=sa
left=spine+" L-200 700 L-200 -200 Z"
# need closing from last point: path ends at bottom tail end; start at top tail start; close via left side
body=f'<g mask="url(#m)"><g clip-path="url(#c)"><rect width="512" height="512" fill="{DEEP}"/><path d="{left}" fill="{LIGHT}"/></g></g>'
open("a-split.svg","w").write(svg(body,cl+mask))
# C: solid cloud, S carved (negative space)
sc=S(262,262,40,a0=-35,a1=145)
mask=f'<mask id="m"><rect width="512" height="512" fill="#fff"/><path d="{sc}" fill="none" stroke="#000" stroke-width="30" stroke-linecap="round"/></mask>'
open("c-negative.svg","w").write(svg(f'<g fill="{BLUE}" mask="url(#m)">{CLOUD_PARTS}</g>',mask))
# B: outline cloud (stroke via mask ring) + solid S
cl2=f'<clipPath id="c">{CLOUD_PARTS}</clipPath>'
ring=f'<mask id="r"><g fill="#fff" stroke="#fff" stroke-width="0">{CLOUD_PARTS}</g><g fill="#000">{CLOUD_PARTS.replace("x=\"64\" y=\"290\" width=\"384\" height=\"112\" rx=\"56\"","x=\"90\" y=\"316\" width=\"332\" height=\"60\" rx=\"30\"").replace("cx=\"190\" cy=\"268\" r=\"82\"","cx=\"190\" cy=\"268\" r=\"56\"").replace("cx=\"305\" cy=\"232\" r=\"104\"","cx=\"305\" cy=\"232\" r=\"78\"")}</g></mask>'
sb=S(256,272,36,a0=-35,a1=145)
body=f'<g fill="{BLUE}" mask="url(#r)">{CLOUD_PARTS}</g><path d="{sb}" fill="none" stroke="{BLUE}" stroke-width="28" stroke-linecap="round"/>'
open("b-outline.svg","w").write(svg(body,ring))
