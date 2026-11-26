// Pick the PanelPex logo variant with the best contrast for ANY background colour.
// usage: pxLogoVariant('#38bdf8') -> 'black' | 'white' | 'color' | 'reversed'
function pxLum(hex){hex=hex.replace('#','');const c=[0,2,4].map(i=>parseInt(hex.substr(i,2),16)/255).map(v=>v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4));return .2126*c[0]+.7152*c[1]+.0722*c[2];}
function pxContrast(a,b){const x=pxLum(a),y=pxLum(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05);}
function pxLogoVariant(bg){
  const parts={color:['#1e1b4b','#6d28d9','#8b5cf6'],reversed:['#ffffff','#a78bfa']};
  for(const v of ['color','reversed']){ if(Math.min(...parts[v].map(c=>pxContrast(c,bg)))>=3) return v; }
  return pxContrast('#000000',bg)>=pxContrast('#ffffff',bg)?'black':'white';
}
