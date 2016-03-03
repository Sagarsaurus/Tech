#Sagar Laud
#I worked on the homework assignment alone, using only this semester's course materials.
#slaud3@mail.gatech.edu

from myro import *
initialize()


def boogie():
    forward(1,.2)
    backward(1,.2)
    forward(1,.2)
    backward(1,.2)
    turnLeft(1, 1)
    forward(1,.2)
    backward(1,.2)
    forward(1,.2)
    backward(1,.2)
    turnRight(1,1)
    forward(1,.2)
    backward(1,.2)
    forward(1,.2)
    backward(1,.2)
    turnLeft(1, 1)
    forward(1,.2)
    backward(1,.2)
    forward(1,.2)
    backward(1,.2)

def sprinkler():
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
    turnLeft(1, 1.5)
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
    turnLeft(1, 1.5)
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
    turnLeft(1, 1.5)
    
    


def Freestyle():
    forward(1,1)
    translate(1)
    wait(.5)
    rotate(1)
    backward(1,3)
    turnRight(1,4)
    translate(2)
    turnLeft(1,3)
    

def dance():
    turnRight(1)
    beep(.5, 600)
    beep(.5, 660)
    beep(.5, 720)
    beep(.5, 660)
    beep(.5, 600)
    beep(.5, 660)
    beep(.5, 720)
    turnLeft(1)
    beep(.5, 660)
    beep(.5, 660)
    beep(.5, 800)
    beep(.5, 720)
    beep(.5, 660)
    beep(1, 600)
    beep(1, 600)
    boogie()
    turnRight(1, 3)
    turnLeft(1,3)
    sprinkler()
    backward(1,2)
    turnRight(1, 3)
    Freestyle()




def menu():
    print "1. Freestyle"
    print "2. The Boogie"
    print "3. The Sprinkler"
    print "0. Exit"
    x = raw_input("Which dance step would you like? ")
    while x != "0":
        if x == "1":
            Freestyle()
        elif x == "2":
            boogie()
        elif x == "3":
            sprinkler()
        else:
            print "I'm sorry, I don't know that one."
        print "1. Freestyle"
        print "2. The Boogie"
        print "3. The Sprinkler"
        print "0. Exit"
        x = raw_input("Which dance step would you like? ")
    if x == "0":
        print "Have a good day!"
