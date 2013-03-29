from read_maze import *

class Die:
	""" Represents the die for the game. """
	def __init__(self, start, goal, board):
		self.board = board
		self.start = start
		self.goal = goal
		self.curLoc = start
		
	def __str__(self):
		""" Returns the representation of the die upon the board. """
		result = ""
		
		for s in self.board:
			result += s
		
		result += "\nOne is facing: " + self.Direction()
		
		return result
		
	def Board(self):
		return self.board
	
	def Start(self):
		return self.start
		
	def Goal(self):
		return goal
	
	def Value(self):
		""" Returns the value face up on the die. """
		pass
		
	def Direction(self):
		""" Returns the direction the 'one' side is facing 
		as <, >, ^, v or X. """
		return 'X'
	
	def GetMoves(self):
		""" Returns a list of new dice objects that can represent the possible
		states that the dice can be in for the next move. """
		pass
		
data = read_maze('maze5.txt')
print Die(data[0], data[1], data[2])
	
