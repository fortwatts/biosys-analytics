#!/usr/bin/env python3
"""
Author : gwatts
Date   : 2019-02-07
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    items = []

    while(True):
        item = input('What are you bringing? ["quit" to quit]')
        if item == 'quit':
            break
        items.append(item)
        print('You are bringing {}'.format(', '.join(items)))

    print('Done.')
# --------------------------------------------------
main()
