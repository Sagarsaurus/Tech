#Sagar Laud and Alex O'Connor
#slaud3@mail.gatech.edu
#We worked on the homework assignment alone, using only this semester's course materials.

import math

def mass(ounces):
    solutionlbs = 0.0625*ounces
    print solutionlbs,"lbs"


def volume(liters):
    float(liters)
    solutionCups = 4.227*liters
    float(solutionCups)
    print"There are "+str(("%.3f" % solutionCups)),"US cups in "+str(("%.3f" % liters)), "liters"

def puppy(puppies,digits):
    boxesofcuteness = puppies*1093.236234
    print("There are " +("%." + str(digits) + "f")%boxesofcuteness + " boxes of cuteness in " + ("%."+str(digits)+"f")%(puppies) + " puppies")

    
    
def tipCalculator(waffles,hashbrowns):
    solutionPrice = waffles*3.35 + hashbrowns*1.45
    print "Calculated bill before tip $"+str(solutionPrice)
    percentTip = raw_input("What percent tip do you want to leave? ")
    percentTip = int(percentTip)
    tip = percentTip
    tip = float(tip)
    solutionPrice = round(solutionPrice,2)
    solutionTip = (tip/100) * solutionPrice
    solutionTip = round(solutionTip,2)
    solutionBill = solutionPrice + solutionTip
    roundedBill = math.ceil(solutionBill)
    roundedBill = int(roundedBill)
    print"A", str(percentTip)+ "% Tip is $"+str(solutionTip)+","
    print "Total bill is $"+str(solutionBill)+", rounded up to $"+str(roundedBill)
    

