#!/usr/bin/python

from PIL import Image
from random import *
import sys
import os

def randomize_int (val, range):
    r = (int)(randrange(range) - (int)(range/2))
    if( val + r > 256 ):
        val = 256 - abs( r )
    elif( val + r < 0 ):
        val = abs( r )
    else:
        val = val + r
    return val

def randomize_pixel (pxl,range):
    try:
        ret = list()
        for p in pxl:
            ret.append( randomize_int( p, range ) )
        return tuple(ret)
    except TypeError:
        return randomize_int( pxl, range )

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
        pxl = randomize_pixel( pxl, rng )
        memeImage.putpixel( (x,y), pxl )

memeImage.save(outpath)
