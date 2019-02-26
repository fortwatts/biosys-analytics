#!/usr/bin/env python3
"""
Author : gwatts
Date   : 2019-01-31
Purpose: first python script exploring strings, lists, and tuples
"""

import os
import sys

# --------------------------------------------------
def main():
    names = sys.argv[1:]
    if not names:
        print('Usage: {} NAME [NAME ...]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    elif len(names) == 1:
        print ('Hello to the 1 of you: {}!'.format(names[0]))
    elif len(names) == 2:
        print ('Hello to the 2 of you: {} and {}!'.format(names[0], names[1]))
    elif len(names) > 2:
        print ('Hello to the {} of you: {}, and {}!'.format(len(names), ", ".join(names[:-1]), names[-1]))

#    print ('Hello to the {} of you : {}, and {}!'.format(len(names), ", ".join(names{:-1}), names[-1]))
# --------------------------------------------------
main()
