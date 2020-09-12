#!/usr/bin/python

from PIL import Image
from random import *
import sys
import os

def randomize_color (pxl,range):
    ret = list()
    for p in pxl:
        r = (int)(randrange(range) - (int)(range/2))
        if( p + r > 256 ):
            p = 256 - abs( r )
        elif( p + r < 0 ):
            p = abs( r )
        else:
            p = p + r
        ret.append(p)
    return tuple(ret)

inpath = sys.argv[1]
f, e = os.path.splitext(inpath)
outpath = f + "_mw" + e

rng = 4
if( len(sys.argv) == 3 ):
    rng = int(sys.argv[2])
    if( rng == 0 ):
        rng = 4

memeImage = Image.open(inpath)

print(memeImage)

# Get the size of the image
width, height = memeImage.size

# Process every pixel
for x in range(width):
    for y in range(height):
        pxl = memeImage.getpixel( (x,y) )
        pxl = randomize_color( pxl, rng )
        memeImage.putpixel( (x,y), pxl )

memeImage.save(outpath)
