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


# -s|--state: The state of the board (type str, default "........." [9 dots])
# -p|--player: The player to modify the state (type str, valid "X" or "O", no default)
# -c|--cell: The cell to alter (type int, valid 1-9, default None)
# -h|--help: Indication to print "usage" and exit (no error)

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
#   print the state with . replaced by position
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

#   check if we have no args
    if (not player) and (not cell) and (re.match('^[.]{9}$', state)):
        grid(player, cell, state)
        sys.exit(0)

#   check that the state argument contains only -, X, O
    if not re.match(r'^[XO-]{9}$', state):
        print('state "{}" must be 9 characters of only -, X, or O'.format(state))
        sys.exit(1)

#   check that the player argument is X or O
    if not re.match(r'[XO]', player):
        print('--player must be either "X" or "O"')
        sys.exit(1)

#   check that cell is between 1 and 9
    if (cell < 1) or (cell > 9):
        print('cell must be integer between 1 and 9')
        sys.exit(1)

#   check that we have a player and a cell argument
#    if (not player) or (not cell):
#        print('Must provide both --player and --cell')
#        sys.exit(1)


# --------------------------------------------------
if __name__ == '__main__':
    main()
