#Sagar Laud
#We worked on the homework assignment alone, using only this semester's course materials.
#slaud3@mail.gatech.edu


def countChars(x):
    counter = 0
    for i in x:
        if i == " ":
            pass
        else:
            counter = counter + 1
    return counter

def removeT(y):
    answer = ""
    x = raw_input("Enter a word/sentence you want to process: ")
    while x != "quit":
            if y == False:
                for i in x:
                    if i == "T":
                        answer = answer + " "
                    else:
                        answer = answer + i
            elif y ==True:
                for i in x:
                    if i == "T" or i =="t":
                        answer = answer + " "
                    else:
                        answer = answer + i
            x = raw_input("Enter a word/sentence you want to process: ")
    return answer
            
