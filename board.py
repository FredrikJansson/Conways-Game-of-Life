from cell import Cell
from random import randint


class Board:
    def __init__(self, rows, columns):
        '''
        Initiate the board with given number
        of rows and columns. Create a grid
        and generate the board.
        '''
        self.rows = rows
        self.cols = columns
        self.grid = [[Cell() for row_cell in range(self.rows)]
                     for col_cell in range(self.cols)]
        self.gen_board()

    def draw_board(self):
        '''
        Draws board, prints new lines to "clear" the terminal.
        '''
        print('\n' * 10)
        for row in self.grid:
            for col in row:
                print(col.get_character(), end='')
            print()

    def gen_board(self):
        '''
        Generate the board and using
        the probability of 1/3 to decide if a cell
        starts off alive.

        If should_live becomes 0, the cell will be
        alive, "if not should_live" is true if it's 0.
        '''
        for row in self.grid:
            for col in row:
                should_live = randint(0, 2)
                if not should_live:
                    col.set_alive()

    def check_neighbourhood(self, check_row, check_col):
        '''
        Checks the surrounding neighbourhood of given
        cell coordinates. It will check a 3x3 and return
        all cells given it's a valid neighbour, i.e. not
        outside of the map or itself...
        '''
        min_search = -1
        max_search = 1

        '''
        Considering range() goes from [inclusive] to [exlusive]
        we need to add a one since we want it to be a 3x3.
        '''
        neighbourhood = []
        for row in range(min_search, max_search + 1):
            for col in range(min_search, max_search + 1):
                neighbour_row = check_row + row
                neighbour_col = check_col + col

                is_valid_neighbour = True

                if neighbour_row == check_row and neighbour_col == check_col:
                    is_valid_neighbour = False

                if neighbour_row < 0 or neighbour_row >= self.rows:
                    is_valid_neighbour = False

                if neighbour_col < 0 or neighbour_col >= self.cols:
                    is_valid_neighbour = False

                if is_valid_neighbour:
                    neighbourhood.append(
                        self.grid[neighbour_row][neighbour_col]
                    )
        return neighbourhood

    def update_board(self):
        '''
        Update the board, given the rules of the game.
        '''
        will_die = []
        will_revive = []

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                checked_neighbours = self.check_neighbourhood(row, col)
                living_neighbours = []
                for neighbour_cell in checked_neighbours:
                    if neighbour_cell.is_alive():
                        living_neighbours.append(neighbour_cell)

                cell_obj = self.grid[row][col]
                main_cell_state = cell_obj.is_alive()

                if main_cell_state:
                    if len(living_neighbours) < 2 or len(living_neighbours) > 3:
                        will_die.append(cell_obj)
                    else:
                        will_revive.append(cell_obj)
                else:
                    if len(living_neighbours) == 3:
                        will_revive.append(cell_obj)

        '''
        Update cell states.
        '''
        for cell in will_die:
            cell.set_dead()
        for cell in will_revive:
            cell.set_alive()

    def advance_board(self):
        '''
        Simple helper function for advancing
        instead of having to call both
        functions in main class.
        '''
        self.update_board()
        self.draw_board()
