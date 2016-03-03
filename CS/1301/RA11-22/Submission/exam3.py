#Sagar Laud
#I worked on this assignment alone using only this semester's course material
#slaud3@gatech.edu

from myro import * 

def colorBlind(p):
    p2 = copyPicture(p)
    for pix in getPixels(p2):
        r = getRed(pix)
        g = getGreen(pix)
        setRed(pix, g)
        setGreen(pix, r)
    return p2
    

def bigNumbersOnly(fileName):
    f = open(fileName, 'r')
    lines = f.readlines()
    f.close()
    aList = []
    finalList = []
    for items in lines:
        items = float(items)
        if items > 50:
            if items not in aList:
                aList.append(items)
    return aList

def border(p):
    p2 = copyPicture(p)
    width = getWidth(p2)
    height = getHeight(p2)
    for pix in getPixels(p2):
        x = getX(pix)
        y = getY(pix)
        if x <=5 or x >= width - 5 or y <=5 or y >= height - 5:
            setRed(pix, 0)
            setGreen(pix, 0)
            setBlue(pix, 0)
    return(p2)

p = loadPicture('rca1.gif')
p2 = colorBlind(p)
p3 = border(p2)
show(p, 'original')
show(p2, 'colorBlind')
show(p3, 'withBorder')
bnList = bigNumbersOnly('numbers.txt')
print bnList
