#!/usr/bin/env python3
"""
Author : gwatts@email.arizona.edu
Date   : 2019-02-07
Purpose: tictactoe script using commandline gflagged arguments
"""

import argparse
import sys
import re


#-s|--state: The state of the board (type str, default "........." [9 dots])
#-p|--player: The player to modify the state (type str, valid "X" or "O", no default)
#-c|--cell: The cell to alter (type int, valid 1-9, default None)
#-h|--help: Indication to print "usage" and exit (no error)

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

#    parser.add_argument(
#        'positional', metavar='str', help='A positional argument')

    parser.add_argument(
        '-s',
        '--state',
        help='the state of the board (type str, default "........." [9 dots])',
        metavar='str',
        type=str,
        default='.........')

    parser.add_argument(
        '-p',
        '--player',
        help='The player to modify the state (type str, valid "X" or "O", no default)',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-c',
        '--cell',
        help='the cell to alter (type int, valid 1-9, default None)',
        metavar='int',
        type=int,
        default=None)

#    parser.add_argument(
#        '-h', '--help', help='Indication to print "usage" and exit (no error)', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    state = args.state
    player = args.player
    cell = args.cell

    for e in state:
         if not re.match(r'[.XO]', state):
            print ('state "{}" must be 9 characters of only -, X, or O'.format(state))
            sys.exit(1)

    if len(state) != 9:
        print('state "{}" must be 9 characters of only -, X, or O'.format(state))
        sys.exit(1)

    if (not player) or (not cell):
       print('Must provide both --player and --cell')

    if not re.match(r'[XO]', player):
       print('--player must be either "X" or "O"')
       sys.exit(1)

    for index, index_state in enumerate(state, start=1):
#        print('index of index_state is: {}'.format(index))
        if re.match(r'[XO]', index_state):
            print('{}'.format(index_state),end='')
        else:
            print('{}'.format(index),end='')
            #print('success!')
    print('\n')

# --------------------------------------------------
if __name__ == '__main__':
    main()
