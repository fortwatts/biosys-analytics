#!/usr/bin/env python3
"""
Author : gwatts@email.arizona.edu
Date   : 2019-02-07
Purpose: tictactoe script using commandline gflagged arguments
Made with Visual studio
"""

import argparse
import sys
import re

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe board',
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
def grid(player, cell, state):
    print('-------------')
    for index, index_state in enumerate(state, start=1):
        if re.match(r'[XO]', index_state):
            print('| {} '.format(index_state), end='')
        else:
            print('| {} '.format(index), end='')
        if (index) % 3 == 0:
            print('|\n-------------')

def main():
    """Make a jazz noise here"""
    args = get_args()
    state = args.state
    player = args.player
    cell = args.cell

    if (not player) and (not cell) and (re.match('^[.]{9}$', state)):
        #print('printing no arg grid')
        grid(player, cell, state)
        sys.exit(0)
#    print('passed no args test')

    if not re.match(r'^[XO.]{9}$', state):
        print('Invalid state "{}", must be 9 characters of only -, X, O'.format(state))
        sys.exit(1)
#    print('passed no state test')

    if (player) and (not re.match('[XO]{1}$', player)):
        print('Invalid player "{}", must be X or O'.format(player))
        sys.exit(1)
#    print('passed player test')

    if (cell):
        if (cell < 1 or cell > 9):
            print('Invalid cell "{}", must be 1-9'.format(cell))
            sys.exit(1)
#    print('passed cell test')

    if not all([player, cell]):
        print('Must provide both --player and --cell')
        sys.exit(1)
#    print('passed both cell and player test')

        grid(player, cell, state)

# --------------------------------------------------
if __name__ == '__main__':
    main()

