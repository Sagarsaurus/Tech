#Sagar Laud and Shih An Hsu
#We worked on the homework assignment alone, using only this semester's course materials.
#slaud3@gatech.edu

from myro import *
p = loadPicture('RA_colorswap_source.jpg')
for pix in getPixels(p):
    r = getRed(pix)
    g = getGreen(pix)
    b = getBlue(pix)
    if r > g and r > b:
        setGreen(pix, 255)
        setRed(pix, 0)
        setBlue(pix, 0)
    if g > r and g > b:
        setGreen(pix, 0)
        setRed(pix, 0)
        setBlue(pix, 255)
    if b > r and b > g:
        setGreen(pix, 0)
        setRed(pix, 255)
        setBlue(pix, 0)
show(p)
