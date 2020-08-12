class Cell:
    def __init__(self):
        '''
        Initializes all cells as 'Dead'.
        Can set the state with accompanying functions.
        '''
        self.status = 'Dead'

    def set_dead(self):
        '''
        Sets <i>this</i> cell as dead.
        '''
        self.status = 'Dead'

    def set_alive(self):
        '''
        Sets <i>this</i> cell as alive.
        '''
        self.status = 'Alive'

    def is_alive(self):
        '''
        Helper function for getting cell state.
        '''
        return self.status == 'Alive'

    def get_character(self):
        '''
        Get the character used to print on the board.
        Depends on if the cell is alive or not.
        '''
        return '#' if self.is_alive() else '.'
