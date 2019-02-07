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

    if size < 2 or size > 9:
        print("NUM (",size,") must be between 1 and 9",sep="")
        sys.exit(1)

    grid = range(1,((size ** 2)+1))

    for i in grid:
        print("{:3}".format(i), end='')
        if (i % size) == 0:
            print()

# --------------------------------------------------
main()
