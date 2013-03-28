
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
    	maze.append(line)
    	
    	if (start == None):
    		temp = find(line, 'S')
    		
    		# create start tuple in Y, X
    		start = (temp, index)
    	
		if (goal == None):
    		temp = find(line, 'G')
    		
    		# create goal tuple in Y, X
    		goal = (temp, index)
    		
    	index += 1
    
    
    return start, goal, maze
    
    
def find(source, search):
	i = 0
	
	while i < len(source):
		if source[i] == search:
			return i
		
		i += 1
	
	return -1
			
