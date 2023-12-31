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
    '''define choice_control here'''
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
        except:
            print("\nYOUR INPUT WAS NOT A NUMBER.")
            continue
        if userChoice in choice_dict:
            break
        else:
            print("\nYOUR SELECTION DOES NOT EXIST - PLEASE MAKE A VALID SELECTION")
    print(f'\nYou\'ve selected: {userChoice} --> Interface: {choice_dict[userChoice]}')
    return choice_dict[userChoice]

def main_menu():
    '''Main menu selection'''
    print("\nNow that you've selected the interface to listen on, what would you like to do?")
    print(f"\n*************************MAIN MENU********************\n  1. Listen NOW\n  2. Select SOURCE IP address to listen for\n  3. Select DESTINATION IP address to listen for\n  4. Select DPORT (destination port)to listen for\n  5. Select SPORT (source port) to listen for\n  6. SHOW me the current payload")
    menu_choice = input("\nPlease make your selection: ")
    return menu_choice

def listen(int_choice):
    p = Popen(["tcpdump","-i","int_choice","-l"], stdout=PIPE) # grabs the results from the 'tcpdump' command and pipes them to a file handle, 'p'
    for row in iter(p.stdout.readline, b''):
        print (row.rstrip())

intList = grab_interfaces()
int_choice = choice_control(intList)
user_menu_selection = main_menu()
mmenu_selection_dict = {'1':'listen(int_choice)','2':'','3':'','4':'','5':'','6':''} # initializes main menu dictionary
choice = mmenu_selection_dict.get(user_menu_selection)
choice
