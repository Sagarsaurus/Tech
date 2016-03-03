#Sagar Laud, Oliver Goldbart
#We worked on this assignment alone using only this semester's course material
#slaud3@gatech.edu

'''There isn't very much acting code because
a) our video didn't have very much robot acting
(we discussed this more in the write-up)
and b) for timing along with voices, we sometimes
used the joyStick() function.'''
def lookAround():
    turnRight( .2, 5)
    turnLeft( .2, 8 )
    turnRight( .2, 10 )
    #This is the code for one of the robots during the conversation scene

def redVideo():
    for i in range( 3 ):
        savePicture( takePicture(), 'redFrame%i.png' % i * 8 )
        turnRight( 1, .2 )
        savePicture( takePicture(), 'redFrame%i.png' % i * 8 + 1 )
        turnRight( 1, .2 )
        savePicture( takePicture(), 'redFrame%i.png' % i * 8 + 2 )
        turnRight( 1, .2 )
        savePicture( takePicture(), 'redFrame%i.png' % i * 8 + 3 )
        turnRight( 1, .2 )
        savePicture( takePicture(), 'redFrame%i.png' % i * 8 + 4)
        turnLeft( 1, .2 )
        savePicture( takePicture(), 'redFrame%i.png' % i * 8 + 5 )
        turnLeft( 1, .2 )
        savePicture( takePicture(), 'redFrame%i.png' % i * 8 + 6 )
        turnLeft( 1, .2 )
        savePicture( takePicture(), 'redFrame%i.png' % i * 8 + 7 )
        turnLeft( 1, .2 )
    
