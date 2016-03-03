#Sagar Laud and Shih An Hsu
#We worked on the homework assignment alone, using only this semester's course materials.
#slaud3@gatech.edu

from myro import *
initialize()

def markYellow(pic):
	for pix in getPixels(pic):
		r = getRed(pix)
		g = getGreen(pix)
		b = getBlue(pix)
		if r > g and r == 255 and b < 100 and g > 100:
			setRed(pix, 255)
			setGreen(pix, 255)
			setBlue(pix, 255)
		else:
			setRed(pix, 0)
			setGreen(pix, 0)
			setBlue(pix, 0)

def pctMarked(pic):
    count = 0
    totalPix = 0
    for pix in getPixels(pic):
        r = getRed(pix)
        totalPix = totalPix + 1
        if r == 255:
            count = count + 1

    pct = 100 * (count / float(totalPix) )
    return pct

def findAvgX(pic):
    pixelCount = 0
    totalXCount = 0
    for pix in getPixels(pic):
        g = getGreen(pix)
        if g == 255:
            pixelCount = pixelCount + 1
            x = getX(pix)
            totalXCount = totalXCount + x

    avgX = totalXCount / float(pixelCount)
    return(avgX)

def celebration():
    turnRight(1, .3)
    wait(.2)
    turnRight(1, .3)
    wait(.2)
    turnRight(1, .3)
    wait(.2)
    turnRight(1, .3)
    wait(.2)
    turnRight(1, .3)
    wait(.2)
    turnLeft(1) ; beep(3, 990, 450)
    turnRight(1, .3)
    wait(.2)
    turnRight(1, .3)
    wait(.2)
    turnRight(1, .3)
    wait(.2)
    turnRight(1, .3)
    wait(.2)
    turnRight(1, .3)
    wait(.2)
    turnLeft(1) ; beep(3, 880)
    turnRight(1, .3)
    wait(.2)
    turnRight(1, .3)
    wait(.2)
    turnRight(1, .3)
    wait(.2)
    turnRight(1, .3)
    wait(.2)
    turnRight(1, .3)
    wait(.2)
    turnLeft(1) ; beep(3, 990, 450)
    backward(1, 1)
    turnRight(1,2)
    backward(1,.5)
    backward(1,.5)
    forward(1,.5)
    turnRight(1,.5)
    turnLeft(1,.5)
    beep(1, 900)
    
def findWall():
    value = (sum(getObstacle())/3)
    while value > 1000:
        backward(1,1)
        value = (sum(getObstacle())/3)
    done = False
    while(not done):
        p = takePicture()
        p2 = copyPicture(p)
        markYellow(p2)
        numYellow = pctMarked(p2)
        if numYellow > 1.0:
            avgX = findAvgX(p2)
            if avgX < 64:
                turnLeft(1,.2)
                findWall()
            if avgX >= 64 and avgX < 100:
                turnLeft(1,.1)
                findWall()
            if avgX >= 150 and avgX < 192:
                turnRight(1,.1)
                findWall()
            if avgX >= 192 and avgX < 256:
                turnRight(1,.2)
                findWall()
            if avgX >= 100 and avgX <= 150:
                g = getObstacle('center')
                total = (sum(getObstacle())/3)
                while total < 950:
                    print total
                    forward(1,1)
                    wait(1)
                    total = (sum(getObstacle())/3)
                done = True
        else:
            turnRight(1, .3)
    wait(1)
    celebration()
    stop()
    return None
findWall()
