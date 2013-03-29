from read_maze import *

class Die:
	""" Represents the die for the game. """
	def __init__(self, start, goal, board):
		self.board = board
		self.start = start
		self.goal = goal
		self.curLoc = start
		self.value = 1
		self.north = 2
		self.direction = 'X'
		
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
		return self.goal
	
	def Value(self):
		""" Returns the value face up on the die. """
		return self.value
		
	def Direction(self):
		""" Returns the direction the 'one' side is facing 
		as <, >, ^, v or X. """
		return self.direction
	
	def GetMoves(self):
		""" Returns a list of new dice objects that can represent the possible
		states that the dice can be in for the next move. """
		pass
		
	def Move(self, direction):
		""" Moves the die in a direction. 1 is up, 2 is right,
		 3 is down and is 4 left. """
		if direction == 1:
			next = 7 - self.value
			self.north = self.value
			self.value = next
			
		
		
data = read_maze('maze5.txt')
print Die(data[0], data[1], data[2])
	
