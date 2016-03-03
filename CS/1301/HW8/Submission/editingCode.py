#Sagar Laud, Oliver Goldbart
#We worked on this assignment alone using only this semester's course material
#slaud3@gatech.edu

#This was the code used to both take and manipulate the images

def seeingRed():
    aList = []
    for i in range(40):
        p = takePicture()
        for pix in getPixels(p):
            setRed(pix, 200)
        aList.append(p)
        savePicture(aList, 'seeingRed.gif')
        if i < 10:
            turnRight(.5,.2)
        if i >= 10 and i < 20:
            turnLeft(.5, .2)
        if i >= 20 and i < 30:
            turnRight(.5,.2)
        if i >= 30 and i < 40:
            turnLeft(.5, .2)
        
def screenShake():
    aList = []
    
    p = takePicture()
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

def kamehameha(): #we put purple dots on our hands and allowed the program to average the y-values...and put a blue/red circle there
    aList = []
    for i in range(50):
        print i + 1
        aList.append( takePicture() )
    for j in range(20, 50):
        print j + 1
        c = aList[j]
        avX = 0
        avY = 0
        purpNum = 0
        LOC = ( 0, 0 )
        for pix in getPixels( c ):
            if distance( ( getRed( pix ), getGreen( pix ), getBlue( pix ) ), (130, 40, 80) ) < 50:# or distance( ( getRed( pix ), getGreen( pix ), getBlue( pix ) ), (120, 50, 145) ) < 30:
                    #setRed( pix, 0 )
                    #setGreen( pix, 255 )
                    #setBlue( pix, 0 )
                    avX += getX( pix )
                    avY += getY( pix )
                    purpNum += 1
        show( c )
        print purpNum
    
        for pix in getPixels( c ):
            d = distance( ( getX( pix ), getY( pix ) ), (avX / purpNum, avY / purpNum) )
            if d < 30 + j:
                setBlue( pix, getBlue( pix ) - 5 *( 30 + j - int(d ) ))
                setGreen( pix, getGreen( pix ) - 5 *( 30 + j - int( d )) )
                setRed( pix, 225 + 5 * ( int( d ) ) )
        show(c)
        aList[j] = c
    savePicture(aList, 'kamehameha.gif')

def split( ):
    leftList = []
    for k in range( 25):
        leftList.append( makePicture( 'C://Users/Oliver/Desktop/AllDemPics/PAC' + str( k ) + '.png' ) )
    rightList = []
    for j in range( 25):
        rightList.append( makePicture( 'C://Users/Oliver/Desktop/AllDemPics/pic' + str( j ) + '.png' ) )  

    aSplit = []
    for i in range( 25 ):
        p = makePicture( getWidth( leftList[ i ] ), getHeight( leftList[ i ] ) )
        for pix in getPixels( p ):
            if getX( pix ) < 128:
                setColor( pix, getColor( getPixel( leftList[ i ], getX( pix ), getY( pix ) ) ) )
            else:
                setColor( pix, getColor( getPixel( rightList[ i ], getX( pix ), getY( pix ) ) ) )
        #aSplit.append( p )
        #aSplit.append( p )
        #aSplit.append( p )
        savePicture( p, "C://Users/Oliver/Desktop/SplitPics/split" + str( i ) + '.png' )
        
        print k
    savePicture( aSplit, 'C://Users/Oliver/Desktop/Splitter.gif')

def collision():
    p = makePicture( 'C://Users/Oliver/Desktop/battle.png' )
    colList = []
    trigger = 0
    trigger2 = 0
    for i in range( 0, 90, 6 ):
        print i / 6
        c = copyPicture( p )
        for pix in getPixels( c ):
            d = distance( ( getX( pix ), getY( pix ) ), ( i, 95 ) )
            if d < ( i / 3 ) + 20:
                setRed( pix, getBlue( pix ) - ( ( i / 3 ) + 20 - d ) * 3 )
                setGreen( pix, getBlue( pix ) - ( ( i / 3 ) + 20 - d ) * 3 )
                setBlue( pix, getBlue( pix ) + ( ( i / 3 ) + 20 - d ) * 3 )
                trigger += 1
            dRed = distance( ( getX( pix ), getY( pix ) ), ( 255 - i, 95 ) )
            if dRed < ( i / 3 ) + 20:
                setGreen( pix, getBlue( pix ) - ( ( i / 3 ) + 20 - dRed ) * 3 )
                setRed( pix, getBlue( pix ) + ( ( i / 3 ) + 20 - dRed ) * 3 )
                setBlue( pix, getBlue( pix ) - ( ( i / 3 ) + 20 - dRed ) * 3 )
            
        colList.append( c )
        savePicture( c, 'C://Users/Oliver/Desktop/bluefolder/blue' + str( i / 6 ) + '.png' )
    counter = 14
    for l in range( len( colList ) - 1, -1 ,-1 ):
        counter += 1
        savePicture( colList[l], 'C://Users/Oliver/Desktop/bluefolder/blue' + str( counter ) + '.png' )
    savePicture( colList, 'C://Users/Oliver/Desktop/collision.gif' )

