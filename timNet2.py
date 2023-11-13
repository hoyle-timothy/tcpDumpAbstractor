#!/usr/bin/env python

from subprocess import Popen, PIPE

#first, grab all of the interface names with 'tcpdump -D' cmd and place them
#inside of an array
i = 0

def grab_interfaces():
    '''this function grabs the name of each available interface on your system and plugs those names into a list for later reference'''
    intList = []
    n = 0
    p = Popen(["tcpdump","-D"], stdout=PIPE)
    while True:
        line = p.stdout.readline()
        if len(line.strip()) == 0: # line.strip() removes any leading or trailing
                                   # whitespace
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
#list their possible options for them

def choice_control(intList):
    option = 1
    n = 0
    i = 0
    for element in intList:
        choice_dict = {option: intList[i]}
        option += 1
        i += 1
    for x in choice_dict:
        print(choice_dict[x])
    print(f"\nHERE ARE YOU AVAILABLE INTERFACES: ")
    p = Popen(["tcpdump","-D"], stdout=PIPE)
    while True:
        line = p.stdout.readline()
        if len(line.strip())==0:
            print("\n")
            break
        else:
            line = line.decode('utf-8')
            print(line.strip()) #adding '.strip() removes any leading or
                                #trailing whitespace
            n += 1
    userChoice = input("PRESS THE NUMBER OF THE INTERFACE YOU WOULD LIKE TO LISTEN ON: ")
intList = grab_interfaces()
choice_control(intList)
