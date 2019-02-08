#!/usr/bin/env python3
"""
Author : gwatts
Date   : 2019-02-05
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]
#    print('file is:', file)

    if len(args) != 1:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = args[0]

# get the file lines into a list then:
    lines = []
    for line in open(file):
        lines.append(line.rstrip('\n'))

# use enumereate on the list:

    for i, listelement in enumerate(lines):
        print(i+1, listelement)
# we increment 1 so we don't start at 0

# print('Arg is "{}"'.format(arg))

# --------------------------------------------------
main()
