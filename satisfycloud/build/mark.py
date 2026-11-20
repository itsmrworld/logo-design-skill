import pathops
from pathops import Path, PathOp, LineCap, LineJoin, op
from fontTools.pens.svgPathPen import SVGPathPen
K=0.5522847498
def circle(cx,cy,r):
    p=Path();k=K*r
    p.moveTo(cx+r,cy);p.cubicTo(cx+r,cy+k,cx+k,cy+r,cx,cy+r);p.cubicTo(cx-k,cy+r,cx-r,cy+k,cx-r,cy)
    p.cubicTo(cx-r,cy-k,cx-k,cy-r,cx,cy-r);p.cubicTo(cx+k,cy-r,cx+r,cy-k,cx+r,cy);p.close();return p
def rect(x,y,w,h):
    p=Path();p.moveTo(x,y);p.lineTo(x+w,y);p.lineTo(x+w,y+h);p.lineTo(x,y+h);p.close();return p
def union(*ps):
    r=ps[0]
    for q in ps[1:]: r=op(r,q,PathOp.UNION)
    return r
def stroke_of(path,w):
    q=Path();q.addPath(path);q.stroke(w,LineCap.ROUND_CAP,LineJoin.ROUND_JOIN,4);q.convertConicsToQuads();return q
def soften(shape,r):
    er=op(shape,stroke_of(shape,2*r),PathOp.DIFFERENCE)
    return op(er,stroke_of(er,2*r),PathOp.UNION)
def build(spine,gap,left=(146,231,61),top=(216,212,80),low=(268,237,54),bottom=291,round_r=2.4,flat=None):
    cloud=union(circle(*left),circle(*top),circle(*low),rect(left[0],200,low[0]-left[0],bottom-200))
    cloud=op(cloud,rect(0,0,500,bottom),PathOp.INTERSECTION)
    sp=Path()
    sp.moveTo(*spine[0])
    for i in range(1,len(spine),3): sp.cubicTo(*spine[i],*spine[i+1],*spine[i+2])
    sp.stroke(gap,LineCap.BUTT_CAP,LineJoin.ROUND_JOIN,4);sp.convertConicsToQuads()
    shape=op(cloud,sp,PathOp.DIFFERENCE)
    # softening only on the outer silhouette convex corners
    if round_r: shape=soften(shape,round_r)
    return shape
def to_d(path,tx=0,ty=0,s=1.0):
    p=Path();p.addPath(path);
    from pathops import Path as P
    p.transform(s,0,0,s,tx*s,ty*s) if False else None
    pen=SVGPathPen(None,lambda v:f"{v:.2f}".rstrip('0').rstrip('.'))
    path.draw(pen);return pen.getCommands()
