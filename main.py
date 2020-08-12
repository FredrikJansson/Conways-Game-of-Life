'''
Game of Life
Fredrik Jansson
'''

from board import Board

import sys


def get_input_values():
    in_row = int(input("Enter how many rows: "))
    in_col = int(input("Enter how many columns: "))
    return in_row, in_col


def main():
    in_row = 0
    in_col = 0

    if len(sys.argv) > 1:
        in_row = sys.argv[1]
        in_col = sys.argv[2]
    else:
        in_row, in_col = get_input_values()

    try:
        in_row = int(in_row)
        in_col = int(in_col)
    except Exception:
        print('Invalid arguments.')
        in_row, in_col = get_input_values()

    gol_board = Board(in_row, in_col)

    gol_board.draw_board()

    print('Press Q to exit or press enter to add a new generation.')
    user_input = ''
    while user_input != 'q':
        user_input = input()
        if user_input == '':
            gol_board.advance_board()


if __name__ == '__main__':
    main()
