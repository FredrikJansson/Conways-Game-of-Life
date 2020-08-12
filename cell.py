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
