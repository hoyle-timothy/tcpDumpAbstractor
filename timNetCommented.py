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
    for element in intList: # for each item in 'intList'
        choice_dict[option] = intList[i] # load a numeric key and its associated interface value
        option += 1 # move to next number in the number line i.e. 'increment'
        i += 1 # move to next position in interface list 'intList'

    print(f"\nHERE ARE YOUR AVAILABLE INTERFACES: ") # display available interfaces
    p = Popen(["tcpdump","-D"], stdout=PIPE) # open the process 'tcpdump -D' and direct the stdout to a pipe
    while True: # loop while available lines
        line = p.stdout.readline() # take the contents of the pipe (the stdout above) and place it into a variable called 'line'
        if len(line.strip())==0: # if the length of 'line' is equal to '0' AFTER stripping off leading or trailing whitespace
            print("\n") # print a 'newline' character, creating a blankline
            break # break out of the 'while True:' loop
        else: # if the length of line is greater than '0' after stripping off leading and trailing whitespace, perform the following
            line = line.decode('utf-8') # convert the bytestring to utf-8 encoding 
            print(line.strip()) # <instantiatedMethod>.strip() removes any leading or trailing whitespace
    while True: # this while loop tests whether or not the user input was of type 'integer'
        userChoice = input("PRESS THE NUMBER OF THE INTERFACE YOU WOULD LIKE TO LISTEN ON: ") # takes the user input and plugs it into a variable called 'userChoice'
        try: # attempt to perform what is below
            userChoice = int(userChoice) # take the value of the variable 'userChoice' and attempt to force it to become data type integer
        except: # if the attempt to convert the value of the variable 'userChoice' to data type integer was unsuccessful, run the code below
            print("\nYOUR INPUT WAS NOT A NUMBER.") # print this message to the screen and re-enter the 'while True:' loop
	    continue
	if userChoice in choice_dict:
	    break
	else:
	    print("\nYOUR SELECTION DOES NOT EXIST - PLEASE MAKE A VALID SELECTION")	
        print(f'You\'ve selected: {userChoice} --> {choice_dict[userChoice]}')
intList = grab_interfaces()
choice_control(intList)
