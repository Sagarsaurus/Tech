#Sagar Laud and Alex O'Conner
#We worked on the homework assignment alone, using only this semester's course materials.
#slaud3@mail.gatech.edu

import string
def wordCounter(filename):
    myfile = file(filename, 'r')
    x = myfile.read()
    x = x.split()
    return len(x)
    
    
