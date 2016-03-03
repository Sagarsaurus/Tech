#Sagar Laud
#I worked on this assignment alone using only this semester's course material
#slaud3@gatech.edu

from myro import *
#initialize()

import os
import math

def avgLightValues(n):
    left = []
    middle = []
    right = []
    counter = 0
    while timeRemaining(n):
        values = getLight()
        left.append(values[0])
        middle.append(values[1])
        right.append(values[2])
        x = random.random()
        print x
        forward(x, 1)
        counter = counter + 1
    stop()
    leftValue = reduce(lambda x, y: float(x + y), left)
    middleValue = reduce(lambda x, y: float(x + y), middle)
    rightValue = reduce(lambda x, y: float(x + y), right)
    finalLeft = leftValue / counter
    finalMiddle = middleValue / counter
    finalRight = rightValue / counter
    return (finalLeft, finalMiddle, finalRight)

def hypCalculator(inFile, outFile):
    f = open(inFile, 'r')
    o = open(outFile, 'w')
    lines = f.readlines()
    f.close()
    aList = []
    bList = []
    for items in lines:
        final = items.split(' ')
        aList.append(int(final[0]))
        bList.append(int(final[1]))
    print aList
    print bList
    answer = map(lambda x, y: math.sqrt(x*x+y*y), aList, bList)
    print answer
    for items in answer:
        o.write(str(items))
        o.write('\n')
    o.close()

def pics(a):
    if a[-4:] == '.jpg' or a[-4:] == '.gif' or a[-4:] == '.bmp' or a[-4:] == '.png':
        return a
    
def findImages(directory):
    x = os.listdir(directory)
    answer = filter(pics, x)
    return answer


def imagesWithSubdirectories(path):
    aDict={}
    aList=[]
    for item in os.listdir(path):
        if item[-3:]=='jpg'or item[-3:]=='png' or item[-3:]=='bmp' or item[-3:]=='gif':
            aList.append(item)
    for root, dirs, files in os.walk(path,topdown=True):
        List=[]
        for name in files:
            if name[-3:]=='jpg'or name[-3:]=='png' or name[-3:]=='bmp' or name[-3:]=='gif':
                List.append(name)
                aDict[root]=List
    aDict[path]=aList
    print aDict
