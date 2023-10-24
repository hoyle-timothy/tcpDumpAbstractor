#!/usr/bin/env python

from subprocess import Popen, PIPE

#first, grab all of the interface names with 'tcpdump -D' cmd and place them
#inside of an array

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
        #print(intList[n])
        n += 1

    if not line:
        break;

#next, query the user for which interface they would like to listen on, and
#list their possible options for them

def choice_control():
    range = 1
    i = 0
    print(f'Please make a choice from the following options: ')
    for item in intList:
        print(f'{range}. {intList[i]} interface')
        range += 1
        i += 1
    choice = input('\nPlease input the number next to your choice: ').lower()
choice_control()
