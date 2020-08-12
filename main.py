'''
Game of Life
Fredrik Jansson
'''

from board import Board


def main():
    in_row = int(input("Enter how many rows: "))
    in_col = int(input("Enter how many columns: "))

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
