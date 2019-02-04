#!/usr/bin/env python3
"""
Author : gwatts
Date   : 2019-02-03
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    size = sys.argv[1:]

    if len(size) != 1:
        print("Usage: {} NUM".format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    size = int(size[0])

    if size < 2 or size > 8:
        print("NUM (",size,") must be between 1 and 9",sep="")
        sys.exit(1)

    grid = list(range(1,((size ** 2)+1)))
    i = 0
    while i < int(grid[-1]):
        # this works        print(*(grid[i:(i+(int(size[0])))]))
        print(*(grid[i:(i+size)]))
        #print('{}'.format(*(grid[i:(i+(int(size[0])))])))
        #print(*(grid[i:(i+(int(size[0])))])).rjust(width)
        #print('{}'.format(grid[i:(i+int(size[0]))]))
        #print('*'.join(str(grid[i:(i+size)])))
        i = i+size
        #print("i is:",i,"and size0 is:", (int(size[0])))

# --------------------------------------------------
main()
