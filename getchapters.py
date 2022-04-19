'''
This script turns an exported edl with markers from Davinci Resolve into Youtube chapters. It prints them to the terminal.
Tested with Davinci Resolve 17.4

Usage:
> python3 getchapters [name of edl file]
'''

import argparse

def readMarkers(s):
    arr = []
    with open(s, 'rt') as f:
        for i in f:
            arr.append(i)
    return arr

def printChapters():
    markers = readMarkers(args.edl_file)[3:]

    index = 0
    while index < len(markers):
        timecode = markers[index].split()[4][:-3]
        nameList = markers[index + 1].split()[1:-1]
        name = ''
        for i in nameList:
            name += i + ' '
        name = name[3:]
        index += 3
        print(timecode + ' - ' + name)

        
if __name__ == '__main__':
    # arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument("edl_file", help = "The edl file with markers exported from Davinci Resolve.", type = str)
    args = parser.parse_args()

    printChapters()
