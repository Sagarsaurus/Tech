#Sagar Laud, Oliver Goldbart
#We worked on this assignment alone using only this semester's course material
#slaud3@gatech.edu

#The pictures themselves were taken as a part of the FX functions.  Please refer to the editing code to see how the functions were actually implemented


def takeKamehameha():#this code was used to take 50 pictures which were then modified with the kamehameha code
    aList = []
    for i in range(50):
        p = takePicture
        aList.append(p)
        savePicture(aList, 'takeKamehameha.gif')

def conversation():#this code was used to film two robots separately and then we used the split function to merge them into a split screen
    aList = []
    for i in range(25):
        p = takePicture
        aList.append(p)
        savePicture(aList, 'conversation.gif')

def powerLevels():#this code allowed the robot to turn left and right, scanning the power levels of the warriors.  The seeingRed function was used to modify it
    aList = []
    for i in range(40):
        p = takePicture()
        aList.append(p)
        savePicture(aList, 'powerLevels.gif')
        if i < 10:
            turnRight(.5,.2)
        if i >= 10 and i < 20:
            turnLeft(.5, .2)
        if i >= 20 and i < 30:
            turnRight(.5,.2)
        if i >= 30 and i < 40:
            turnLeft(.5, .2)

def pic(): #this code was used to take one picture that could later be modified as necessary(the collision scene and the screen shake)
    p = takePicture()
    savePicture(p, 'default.jpg')



        
