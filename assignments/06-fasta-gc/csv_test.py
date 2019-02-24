#!/usr/bin/env python3
"""
Author : gwatts
Date   : enter here
Purpose: Rock the Casbah
"""

import csv
import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    filename = args[0]

    print('filename is "{}"'.format(filename))
    with open(filename) as myfile:
        reader = csv.DictReader(myfile, delimiter=',') # use , or \t for csv or tab-delimited
        for row in reader:
            print(row)

# --------------------------------------------------
main()
