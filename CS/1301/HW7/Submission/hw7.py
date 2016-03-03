#Sagar Laud and Shih An Hsu
#We worked on the homework assignment alone, using only this semester's course materials.
#slaud3@gatech.edu

from myro import *
#initialize()

#robot takes pictures, and changes all r values to 255, makes gif have red tint
def seeingRed(): #15
    aList = []
    for i in range(20):
        p = takePicture()
        for pix in getPixels(p):
            setRed(pix, 255)
        aList.append(p)
        savePicture(aList, 'seeingRed.gif')
        turnRight(1,.2)
        

#takes multiple pictures while moving closer to an object, makes gif zoom
def robotZoom():#15
    aList = []
    for i in range(10):
        p = takePicture()
        aList.append(p)
        forward(.5,.5)
    savePicture(aList, 'robotZoom.gif')

#takes pics while spinning in a circle and adds all pictures to a list, coverts to gif
def threeSixty():#15
    aList = []
    for i in range(17):
        p = takePicture()
        aList.append(p)
        savePicture(aList, 'threeSixty.gif')
        turnRight(1,.2)

#takes multiple pictures in the same axis in order to pan across the scene
def dollyShot():#20
    aList = []
    for i in range(10):
        p = takePicture()
        aList.append(p)
        savePicture(aList, 'dollyShot.gif')
        turnRight(.5, 1.6)
        forward(.5, .5)
        turnLeft(.5, 1.)
        

#takes a picture and gradually lowers the rgb values to 0, causing the picture to fade to black
def fadeBlack():#35
    p = takePicture()
    aList = []
    for i in range(12):
        p2 = copyPicture(p)
        aList.append(p2)
	for pix in getPixels(p):
                setRed(pix, getRed(pix) - 25)
                setGreen(pix, getGreen(pix) - 25)
                setBlue(pix, getBlue(pix) - 25)
    savePicture(aList, 'fadeBlack.gif')

#takes in two images: soccer.jpg and cube.jpg...averages rgb values to give effect of extended exposure(two pictures in one)
def extendedExposure():#50
    p=loadPicture('soccer.jpg')
    pic=loadPicture('cube.jpg')
    M=makePicture(256,192)
    cList=[]
    for x in range(256):
        for y in range(192):   

            p=getPixel(p,x,y)
            p2=getPixel(pic,x,y)
            p3=getPixel(M,x,y)

            r1=getRed(p)
            g1=getGreen(p)
            b1=getBlue(p)

            r2=getRed(p2)
            g2=getGreen(p2)
            b2=getBlue(p2)


            avgRed=(r1+r2)/2
            avgBlue=(b1+b2)/2
            avgGreen=(g1+g2)/2

            setRed(p3,avgRed)
            setBlue(p3,avgBlue)
            setGreen(p3,avgGreen)

        savePicture(M, 'extendedExposure.gif')

#This function loads a picture, copies it, and then alternates between a modified picture and the original in order to give the effect of a shaking picture...a picture can also be taken
def screenShake():#45
    aList = []
    
    p = loadPicture('pic0.gif')
    p2 = copyPicture(p)

    xSize = p2.getWidth()
    ySize = p2.getHeight()
    shake = 8

    for y in range(0, ySize-1):
        for x in range(xSize-1, shake,-1):
            pix = getPixel(p2, x-shake,y)
            g = getGreen(pix)
            b = getBlue(pix)
            r = getRed(pix)
            
            pix2 = getPixel(p2, x,y)
            setBlue(pix2,b)
            setRed(pix2,r)
            setGreen(pix2,g)

    for y in range(0, ySize-1):
        for x in range(0, shake):
            pix3 = getPixel(p2,x,y)
            setGreen(pix3, 255)
            setRed(pix3, 255)
            setBlue(pix3, 255)


    for m in range (0,10):
        if m%2 ==0:
            aList.append(p)
        else:
            aList.append(p2)

    savePicture(aList, "screenShake.gif")

