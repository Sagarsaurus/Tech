#Sagar Laud
#slaud3@mail.gatech.edu
#I worked on the homework assignment alone, using only this semester's course materials.



import math

def celsiustoFahrenheit():
    celsius = raw_input("Enter your temperature in Celsius.")
    celsius = float(celsius)
    Fahrenheit = 9 * celsius/5 + 32
    print str(Fahrenheit)+" degrees Fahrenheit" 




def cylinderVolume():
    inches = raw_input("What is the radius in inches?")
    inches = float(inches)
    height = raw_input("What is the height in inches?")
    height = float(height)
    Volume = math.pi * inches**2 * height
    print str(Volume)+" inches cubed is your volume."
    



def timeCleanUp():
    seconds = raw_input("What is the number of seconds?")
    seconds = int(seconds)
    minutes = seconds/60
    hours = minutes/60
    days = hours/24
    weeks = days/7
    S = seconds%60
    M = minutes%60
    H = hours%24
    D = days%7
    print weeks, " weeks,", D, " days,", H, " hours,", M, " minutes,", S, " seconds."


def rohrerIndex():
    Weight = raw_input("Enter your weight in pounds.")
    Weight = float(Weight)
    Height = raw_input("Enter your height in inches.")
    Height = float(Height)                   
    RI = (Weight / Height**3) * 2768
    print "Your RI is "+str(("%.1f" % RI))


