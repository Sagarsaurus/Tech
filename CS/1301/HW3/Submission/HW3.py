#Sagar Laud
#slaud3@mail.gatech.edu
#I worked on this homework with Karan Pahawa and Hans Louis and referred only tothis semester's CS 1301 course materials.

def checkHeight(height):
    x = height
    if x <132:
        return 'Sorry. You must be at least 1 meter 32 cm to ride.'
    else:
        return 'Have a great ride!'

def multiplicationTables(number, limit):
    x = -1
    while x < limit:
        x = x + 1
        print str(number)+"*"+str(x), "=", number * x

def xmassTree(x):
    y = 1
    while y < x + 1:
        print " "*((x-y)/2) +  "*" * y
        y = y + 2
    print " " * ((x-1)/2) + "*"
    print " " * ((x-1)/2) + "*"
    print " " * ((x-1)/2) + "*"
        

def countDownByThrees(start):
    x = start
    while x > 0:
       print x
       x = x-3
    print "Blast Off!"


def complimentMaker(answer1, answer2, answer3, answer4):
    if answer1 == True:
        w = " super"
    elif answer1 == False:
        w = ""

    if answer2 == True:
        x = " nice"
    elif answer2 == False:
        x = ""
    
    if answer3 == True:
        y = " smart"
    elif answer3 == False:
        y = ""
    
    if answer4 == True:
        z = " cool"
    elif answer4 == False:
        z = ""
    if answer1 or answer2 or answer3 or answer4 == True:
        return "You are"+str(w)+str(x)+str(y)+str(z)
    else:
        return "No Comment."

    


def comboLock(num1, num2, num3, num4, num5):
        if num1 > 10:
            return "You are locked out."
        elif num2 > 10:
            return "You are locked out."
        elif num3 > 10:
            return "You are locked out."
        elif num4 > 10:
            return "You are locked out."
        elif num5 > 10:
            return "You are locked out."
        elif num1%2 == 0:
            return "You are locked out."
        elif num2%2 == 1:
            return "You are locked out."
        elif num3%2 == 0:
            return "You are locked out."
        elif num4%2 == 1:
            return "You are locked out."
        elif num5%2 == 0:
            return "You are locked out."
        else:
            return "You opened the lock."
           	

import string
def badRecord(sentence):
    capital = ""
    for letter in sentence:
        if letter in string.ascii_uppercase:
            capital = capital + letter
    return capital


def printTimestable():
    print 'Times:',
    print 1,
    for x in range(1, 9):
	print '%6s'%((x+1)),
    print ''
    for x in range(9):
        print '%s' %(x+1),
        for y in range(9):
	    print '%6s'%((x+1)*(y+1)),
	print ''

def printTimes(n):
    print 'Times:',
    print 1,
    for x in range(1, n):
	print '%6s'%((x+1)),
    print ''
    for x in range(n):
        print '%s' %(x+1),
        for y in range(n):
	    print '%6s'%((x+1)*(y+1)),
	print ''



