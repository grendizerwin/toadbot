#!/usr/bin/env python3
import sys, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
# Paper Pulse caption composer (from batch 001). Usage:
#   python3 compose.py <photo> <out.jpg> "<HEADLINE>" "<caveat note>" "<LEFT LABEL>" "<RIGHT LABEL>"
# Fonts load straight from the brand kit in ../kit/assets/fonts/ (Pillow reads .woff2).
import os
_B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','kit','assets','fonts')+os.sep
FONTS={'Anton.ttf':_B+'anton-latin-400-normal-Byf51wtH.woff2',
       'PlexMono.ttf':_B+'ibm-plex-mono-latin-400-normal-DMJ8VG8y.woff2',
       'Caveat.ttf':_B+'caveat-latin-700-normal-D8_1Nw6V.woff2',
       'DMSans.ttf':_B+'dm-sans-latin-wght-normal-Xz1IZZA0.woff2'}
class _F(str):
    def __add__(self,name): return FONTS[name]
F=_F('')
CREAM=(0xF9,0xF1,0xD7); FOREST=(0x14,0x41,0x37); YELLOW=(0xF6,0xBE,0x2D); RED=(0xE0,0x2B,0x2F)
def compose(photo, out, headline, note, label_l, label_r):
    W,H=1080,1600; M=56
    img=Image.new('RGB',(W,H),CREAM)
    # subtle paper grain
    random.seed(7)
    g=Image.effect_noise((W,H),18).convert('L')
    grain=Image.new('RGB',(W,H),FOREST)
    img=Image.composite(grain,img,g.point(lambda v: max(0,v-118)//6))
    d=ImageDraw.Draw(img)
    mono=ImageFont.truetype(F+'PlexMono.ttf',22)
    d.text((M,M),label_l,font=mono,fill=FOREST)
    tw=d.textlength(label_r,font=mono); d.text((W-M-tw,M),label_r,font=mono,fill=FOREST)
    d.line([(M,M+40),(W-M,M+40)],fill=FOREST,width=1)
    # headline (Anton), auto-size to width
    size=150
    while True:
        anton=ImageFont.truetype(F+'Anton.ttf',size)
        if d.textlength(headline,font=anton)<=W-2*M or size<60: break
        size-=4
    y=M+80
    bb=d.textbbox((M,y),headline,font=anton)
    # yellow brush underline (behind text bottom)
    bw=int(min(bb[2]-M, (W-2*M))*0.62); by=bb[3]+6
    brush=Image.new('RGBA',(bw+40,60),(0,0,0,0)); bd=ImageDraw.Draw(brush)
    bd.rounded_rectangle([10,18,bw+20,40],radius=14,fill=YELLOW+(255,))
    brush=brush.rotate(0.9,expand=True,resample=Image.BICUBIC).filter(ImageFilter.GaussianBlur(0.6))
    img.paste(brush,(M-10,by-22),brush)
    d=ImageDraw.Draw(img)
    d.text((M,y),headline,font=anton,fill=FOREST)
    # photo
    ph=Image.open(photo).convert('RGB')
    pw=W-2*M; phh=int(ph.height*pw/ph.width)
    maxh=820
    if phh>maxh:
        # crop top/bottom equally
        scale=pw/ph.width; need=maxh/scale; top=(ph.height-need)/2
        ph=ph.crop((0,int(top),ph.width,int(top+need))); phh=maxh
    ph=ph.resize((pw,phh),Image.LANCZOS)
    py=by+60
    mask=Image.new('L',(pw,phh),0); ImageDraw.Draw(mask).rounded_rectangle([0,0,pw-1,phh-1],radius=8,fill=255)
    img.paste(ph,(M,py),mask)
    d.rounded_rectangle([M,py,M+pw-1,py+phh-1],radius=8,outline=FOREST,width=2)
    # caveat note
    cav=ImageFont.truetype(F+'Caveat.ttf',64)
    ny=py+phh+34
    nw=d.textlength(note,font=cav)
    nx=W-M-nw-50
    d.text((nx,ny),note,font=cav,fill=FOREST)
    # little red heart
    hx,hy,s=W-M-30,ny+30,15
    d.ellipse([hx-s,hy-s,hx,hy],fill=RED); d.ellipse([hx,hy-s,hx+s,hy],fill=RED)
    d.polygon([(hx-s+1,hy-s//2+3),(hx+s-1,hy-s//2+3),(hx,hy+s+2)],fill=RED)
    H=ny+64+120
    img=img.crop((0,0,W,H)); d=ImageDraw.Draw(img)
    # footer
    d.line([(M,H-M-40),(W-M,H-M-40)],fill=FOREST,width=1)
    d.text((M,H-M-24),'SAME TOAD. DIFFERENT DAYS.',font=mono,fill=FOREST)
    t='FROM THE POND'; tw=d.textlength(t,font=mono); d.text((W-M-tw,H-M-24),t,font=mono,fill=FOREST)
    img.save(out,quality=95)
USAGE='usage: python3 compose.py <photo> <out.jpg> "<HEADLINE>" "<caveat note>" "<LEFT LABEL>" "<RIGHT LABEL>"'
if __name__=='__main__':
    if len(sys.argv)!=7 or sys.argv[1] in ('-h','--help'):
        print(USAGE); print('Renders a 1080px-wide Paper Pulse card (JPEG). Needs Pillow; fonts from ../kit/assets/fonts/.')
        sys.exit(0 if len(sys.argv)>1 and sys.argv[1] in ('-h','--help') else 2)
    os.makedirs(os.path.dirname(os.path.abspath(sys.argv[2])),exist_ok=True)
    compose(*sys.argv[1:7])
