from read_maze import *

# According to the professor's definition, the dice looks
# as such when unrolled:
#   2
# 4 1 3 6
#   5
#
# Authors: Sean Mullen

class Die:
	""" Represents the die for the game. """
	def __init__(self, start, goal, board):
		# start, goal and current location are in (y, x)
		self.board = board
		self.start = start
		self.goal = goal
		self.curLoc = start
		self.value = 1
		self.north = 2
		self.east = 3
		self.direction = 'X'

	def __str__(self):
		""" Returns the representation of the die upon the board. """
		result = ""

		for s in range(len(self.board)):
			if s == self.curLoc[1]:
				rowAsString = list(self.board[s])
				rowAsString[self.curLoc[0]] = str(self.value)
				result += ''.join(rowAsString)
			else:
				result += self.board[s]

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
			next = 7 - self.north
			self.north = self.value
			self.value = next
			
			self.curLoc = (self.curLoc[0], self.curLoc[1] - 1)	
		elif direction == 2:
			next = 7 - self.east
			self.east = self.value
			self.value = next
						
			self.curLoc = (self.curLoc[0] + 1, self.curLoc[1])
		elif direction == 3:
			next = 7 - self.value
			self.value = self.north
			self.north = next
						
			self.curLoc = (self.curLoc[0], self.curLoc[1] + 1)
		elif direction == 4:
			next = 7 - self.value
			self.value = self.east
			self.east = next	
						
			self.curLoc = (self.curLoc[0] - 1, self.curLoc[1])		
			
		self.updateDirection(direction)

	def updateDirection(self, direction):
		""" This is for updating '1' direction. Just broken out here to keep
		Move more clean. """
		if direction == 1:
			if self.direction == 'X':
				self.direction = '^'
			elif self.direction == 'V':
				self.direction = 'X'	
		elif direction == 2:
			if self.direction == 'X':
				self.direction = '>'
			elif self.direction == '<':
				self.direction == 'X'
		elif direction == 3:
			if self.direction == 'X':
				self.direction = 'v'
			elif self.direction == '^':
				self.direction == 'X'
		elif direction == 4:
			if self.direction == 'X':
				self.direction = '<'
			elif self.direction == '>':
				self.direction == 'X'

if __name__ == '__main__':
	data = read_maze('maze5.txt')
	die = Die(data[0], data[1], data[2])
	print die
	
	die.Move(3)
	
	print die
	
	for i in range(11):
		die.Move(4)
	
	print die
