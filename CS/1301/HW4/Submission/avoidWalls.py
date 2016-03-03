#Sagar Laud
#I worked on the homework assignment alone, using only this semester's course materials.
#slaud3@mail.gatech.edu

from myro import *
initialize()

def avoidWalls():
    while timeRemaining(60):
        wait(.2)
	while getObstacle(0) < 1000 and getObstacle(2) < 1000:
		forward(1)
		wait(.5)
	if getObstacle(1) > 1000:
		turnRight(1, 1.5)
	if getObstacle(0) > 650:
		turnRight(1,.3)
	if getObstacle(2) > 650:
		turnLeft(1,.3)
    stop()

    wait(1)

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

    
    
