# -*- coding: utf-8 -*-
__author__ = 'Edward'
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
def rand_chr():
    f=[(65,90),(97,122),(48,57)]
    t=random.choice(f)
    return chr(random.randint(t[0],t[1]))
def rand_color1():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def rand_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
def rand_color2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
width=60*4
height=60
im=Image.new('RGB',(width,height),(255,255,255))
font=ImageFont.truetype(r'C:\Windows\Fonts\ITCBLKAD.ttf',40)
draw=ImageDraw.Draw(im)
for x in range(width):
    for y in range(height):
        draw.point((x,y),rand_color1())
im2=im.filter(ImageFilter.BLUR)
draw2=ImageDraw.Draw(im2)
for t in range(4):
    draw2.text((t*60+10,10),rand_chr(),rand_color2(),font)
#image=im.filter(ImageFilter.BLUR)
im2.save(r'd:\code.jpg','jpeg')
