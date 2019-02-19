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
def grid(board):

    print('-------------')
    for key in board:
        if re.match(r'[XO]', board[key]):
            print('| {} '.format(board[key]), end='')
        else:
            print('| {} '.format(key), end='')
        if (key % 3) == 0:
            print('|\n-------------')

def main():
    args = get_args()
    state = args.state
    player = args.player
    cell = args.cell

    board = {}
    i = 1
    for mark in state:
        board[i] = mark
        i += 1

    if not re.match(r'^[XO.]{9}$', state):
        print('Invalid state "{}", must be 9 characters of only -, X, O'.format(state))
        sys.exit(1)

    if (player) and (not re.match('[XO]{1}$', player)):
        print('Invalid player "{}", must be X or O'.format(player))
        sys.exit(1)

    if cell is not None and not 1 <= cell <= 9:
        print('Invalid cell "{}", must be 1-9'.format(cell))
        sys.exit(1)
    elif cell is not None and (not re.match('[XO]{1}$', board[cell])):
        board[cell] = player
    elif cell is not None:
        print('Cell {} already taken'.format(cell))
        sys.exit(1)

    if any([player, cell]) and not all([player, cell]):
        print('Must provide both --player and --cell')
        sys.exit(1)
    
    grid(board)

# --------------------------------------------------
if __name__ == '__main__':
    main()

