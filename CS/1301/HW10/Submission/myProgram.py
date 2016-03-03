#Sagar Laud
#I worked on this assignment alone using only this semester's course materials
#slaud3@gatech.edu

#IMPORTANT: This program will only function properly on windows.

#The idea is simply to create another version of windows explorer: entirely text based with the general concept of a game
#I got the idea itself mainly because I wondered if there was a way to make opening files less boring
#The logic is simple: the program will open up any directory it is given (the C directory by default) and will then display the options to the user.
#The user will then choose what they want to do...and the program responds accordingly with conditionals and a while loop
#The only time there will be an error in this program is if the folder one tries to open has restricted access and access is denied.


#This beginning portion of code does nothing other than set some conditions.  It will open the directory for the path it is given.
#If an error occurs such that a file or folder that one is looking for does not exist, it will handle the exception and close the program.
import os
import sys
def main(path):
    print path
    try:
            os.chdir(path)
    except WindowsError:
            print "I can't find that folder.  Goodbye..."
            return
    items = os.listdir(path)
    files, folders = separateItems(items)
    printItems(files, folders)
    choice = listOptions()
    #If choice 1 is chosen, it will ask the user which file they wish to open...and will repeatedly do so.
    #Once you choose a directory and ask to open a file, you are locked in...there is no way to exit the directory unless you type 'quit' to close.
    while choice != '3':
        if choice == '1':
            while '1':
                fileToOpen = raw_input('What would you like to open? Type quit to exit the program ')
                newPath = os.path.abspath('.').split('\\')
                newPath.append(fileToOpen)
                newpath = "\\".join(newPath)
                if os.path.isfile(fileToOpen):
                    os.startfile(newpath)
                    #return
                elif os.path.isdir(fileToOpen):
                    main(newpath)
                    return
                elif fileToOpen == 'quit':
                    return
                    print "returned"
                else:
                    print "I can't find that file or folder, please try again or 'quit'"
            return
        #If one chooses choice 2, it will open up the root directory
        elif choice == '2':
            if len(os.path.abspath('.'))>3: #Cause it will be C:\\ and one is escaped
                parentpathList = os.path.abspath(path).split('\\')[:-1]
                main('\\'.join(parentpathList))
                return
            else:
                print "You are already at the root directory"
        #Choice 4 will reprint the files and folders in the directory
        elif choice == '4':
            printItems(files, folders)
        #Choice 5 will will print these options for the user again.
        elif choice == '5':
            pass
        else:
            print 'That is not an option.'
        choice = listOptions()
    #If choice 3 is chosen, the program simply exits.
    if choice == '3':
        print "Bye Bye!  Hope you enjoyed the program!"
        return
        
#This program separates the items in a given directory based upon the criteria of files or folders.  The items in a directory are classified and a tuple is returned with the items organized.
def separateItems(items):
    files = []
    folders = []
    for item in items:
        if os.path.isfile(item):
            files.append(item)
        if os.path.isdir(item):
            folders.append(item)
    return (files, folders)

#This function simply takes the items in the tuple from the program above and prints these items.  It prints the files and lets the user know they are files...and does the same with folders.
def printItems(files, folders):
    if files == [] and folders == []:
        print 'This is an empty folder...please run the function with a different path'
    else:
        print "Here are the files in your directory:"
        for file in files:
            print file
        print "Here are the folders in your directory:"
        for folder in folders:
            print folder

#This function lists the options for the user.
def listOptions():
    print "Here are your options:"
    print "1: Open a file or folder"
    print "2: Drop back a folder"
    print "3: Close the program"
    print "4: Show me the files and folders again"
    print "5: Reprint these Options"
    return raw_input("What would you like to do? ")

#I chose to call the function using the home directory by default.  One can simply comment this part of the code out and run the code with any regular path.  The code will work fine.
main('C:/')

