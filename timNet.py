#!/usr/bin/env python3

from subprocess import Popen, PIPE

#first, grab all of the interface names with 'tcpdump -D' cmd and place them
#inside of an array

def grab_interfaces():
    '''this function grabs the name of each available interface on your system and plugs those names into a list for later reference'''
    intList = [] # initialize list
    n = 0 # initialize iterator
    p = Popen(["tcpdump","-D"], stdout=PIPE) # grabs the results from the 'tcpdump -D' command and pipes them to a file handle, 'p'
    while True:
        line = p.stdout.readline() # take the result from the line that was read and place the result into a variable called 'line'
        if len(line.strip()) == 0: # tests for the presence of an empty line and breaks out of the loop if it sees an empty line. 
				   # 'Line.strip()' removes any leading or trailing whitespace from the line
            break
        else:
            line = line.decode('utf-8')
            line = line.split(' ')[0]
            line = line.split('.')[1]
            intList.append(line)
            n += 1

        if not line:
            break;
    return intList

#next, query the user for which interface they would like to listen on, and
#list the possible options for them

def choice_control(intList):
    choice_dict = {} #initialize dictionary
    option = 1
    n = 0
    i = 0
    for element in intList:
        choice_dict[option] = intList[i]
        option += 1
        i += 1

    print(f"\nHERE ARE YOUR AVAILABLE INTERFACES: ")
    p = Popen(["tcpdump","-D"], stdout=PIPE)
    while True:
        line = p.stdout.readline()
        if len(line.strip())==0:
            print("\n")
            break
        else:
            line = line.decode('utf-8')
            print(line.strip()) #adding '.strip() removes any leading or trailing whitespace
    while True:
        userChoice = input("PRESS THE NUMBER OF THE INTERFACE YOU WOULD LIKE TO LISTEN ON: ")
        try:
            userChoice = int(userChoice)
            break
        except:
            print("\nYOUR INPUT WAS NOT A NUMBER.")
    while not userChoice in choice_dict:
        userChoice = int(input(f"\nNON-EXISTENT INTERFACE. \nPLEASE SELECT A VALID INTERFACE BY TYPING THE NUMBER NEXT TO IT: "))
    print(f'You\'ve selected: {userChoice} --> {choice_dict[userChoice]}')
intList = grab_interfaces()
choice_control(intList)
