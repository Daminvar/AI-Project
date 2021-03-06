# Handles reading in maze files.
#
# Authors: Sean Mullen, Dennis Honeyman


def read_maze(filename):
	'''Returns the maze as a 2D array of booleans, the starting coordinates,
	and the goal coordinates. In the array, True represents walkable.'''
	maze = []
	start = None
	goal = None
	
	# gets file handler
	fileInput = open(filename, 'r')
	
	index = 0
	for line in fileInput:
		maze.append(line.strip())
		
		if (start == None):
			temp = find(line, 'S')
			
			if temp > -1:
				# create start tuple in Y, X
				start = (index, temp)
		
		if (goal == None):
			temp = find(line, 'G')
			
			if temp > -1:
				# create goal tuple in Y, X
				goal = (index, temp)
			
		index += 1
	
	
	return start, goal, maze
	
	
def find(source, search):
	i = 0
	
	while i < len(source):
		if source[i] == search:
			return i
		
		i += 1
	
	return -1
