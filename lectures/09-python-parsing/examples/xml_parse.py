#!/usr/bin/env python3
"""
Author : gwatts
Date   : 2019-03-14
Purpose: Rock the Casbah
"""

import os
import sys
from xml.etree.ElementTree import ElementTree

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = args[0]

    print('File is "{}"'.format(file))
    tree = ElementTree()
    root = tree.parse(file)
    for key, value in root.attrib.items():
     print('{:13}: {}'.format(key, value))

    for id_ in root.find('IDENTIFIERS'):
        print('{:13}: {}'.format(id_.tag, id_.tag))

    for attr in root.findall('SAMPLE_ATTRIBUTES/SAMPLE_ATTRIBUTE'):
        print('attr.' + attr.find('TAG').text, attr.find('VALUE').text)        
        
# --------------------------------------------------
main()
