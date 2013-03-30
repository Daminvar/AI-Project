from read_maze import *

# According to the professor's definition, the dice looks
# as such when unrolled:
#   2
# 4 1 3 6
#   5

class Die:
    """ Represents the die for the game. """
    def __init__(self, start, goal, board, parent, value, north, east):
        self.board = board
        self.start = start
        self.goal = goal
        self.parent = parent
        self.value = value
        self.north = north
        self.east = east
        self.direction = 'X'

    def __str__(self):
        """ Returns the representation of the die upon the board. """
        result = "\n"

        for s in range(len(self.board)):
            if s == self.start[0]:
                rowAsString = list(self.board[s])
                rowAsString[self.start[1]] = str(self.value)
                result += ''.join(rowAsString)
            else:
                result += self.board[s]
            result += '\n'

        result += "-- One is facing: " + self.Direction()

        return result

    def __eq__(self, other):
        if other == None:
            return False
        return self.start == other.start and \
            self.value == other.value and \
            self.north == other.north and \
            self.east == other.east

    def __hash__(self):
        return hash(self.start) ^ hash(self.value) ^ hash(self.north) ^ hash(self.east)

    def Board(self):
        return self.board

    def Start(self):
        return self.start

    def Goal(self):
        return self.goal

    def IsGoal(self):
        return self.value == 1 and self.start == self.goal

    def Value(self):
        """ Returns the value face up on the die. """
        return self.value

    def Direction(self):
        """ Returns the direction the 'one' side is facing 
        as <, >, ^, v or X. """
        return self.direction
        
    def GetAbsStart(self):
    	start = None
    	for s in range(len(self.board)):
    		for c in range(len(self.board[s])):
    			if self.board[s][c] == 'S':
    				return (s, c)

    def GetParentsAsList(self):
        if self.parent == None:
            return []
        return self.parent.GetParentsAsList() + [self];

    def GetMoves(self):
        """ Returns a list of new dice objects that can represent the possible
        states that the dice can be in for the next move. """
        moves = []

        possible_directions = [
                (-1, 0),
                (0, 1),
                (1, 0),
                (0, -1),
        ]

        for move, direction in zip(possible_directions, range(1,5)):
            new_pos = (self.start[0] + move[0], self.start[1] + move[1])
            if not (0 <= new_pos[0] < len(self.board) and 0 <= new_pos[1] < len(self.board[0])):
                continue
            if self.board[new_pos[0]][new_pos[1]] == '*':
                continue
            new_die = self.Move(direction)
            if new_die.value == 6:
                continue
            moves.append(new_die)
        return moves


    def Move(self, direction):
        """ Moves the die in a direction. 1 is up, 2 is right, 3 is down and is
        4 left. """

        newStart = ()
        newNorth = self.north
        newValue = self.value
        newEast = self.east

        if direction == 1:
            next = 7 - self.north
            newNorth = self.value
            newValue = next

            newStart = (self.start[0] - 1, self.start[1])
        elif direction == 2:
            next = 7 - self.east
            newEast = self.value
            newValue = next

            newStart = (self.start[0], self.start[1] + 1)
        elif direction == 3:
            next = 7 - self.value
            newValue = self.north
            newNorth = next

            newStart = (self.start[0] + 1, self.start[1])
        elif direction == 4:
            next = 7 - self.value
            newValue = self.east
            newEast = next    

            newStart = (self.start[0], self.start[1] - 1) 

        newDie = Die(newStart, self.goal, self.board,
                self, newValue, newNorth, newEast)
        newDie.updateDirection()
        
        return newDie 

    def updateDirection(self):
        """ This is for updating '1' direction. Just broken out here to keep
        Move more clean. """
        
        if self.value == 1:
            self.direction = 'X'
        elif self.north == 6:
            self.direction = 'v'
        elif self.north == 1:
            self.direction = '^'
        elif self.east == 1:
            self.direction = '>'
        elif self.east == 6:
            self.direction = '<'
        else:
            self.direction = 'O'


if __name__ == '__main__':
    data = read_maze('maze1.txt')
    die = Die(data[0], data[1], data[2], None, 1, 2, 3)
    
    print "#### MAZE 1 ####"
    print die
    moves = [3,2,2,2,2,1]
    
    for i in moves:
        die = die.Move(i)
        print die
        
    data = read_maze('maze2.txt')
    die = Die(data[0], data[1], data[2], None, 1, 2, 3)

    print "#### MAZE 2 ####"
    print die
    moves = [3,2,1,4,3,3,3,2,2,3,4,1,2,2,2,3,4,1,1,2]
    
    for i in moves:
        die = die.Move(i)
        print die
        
    data = read_maze('maze4.txt')
    die = Die(data[0], data[1], data[2], None, 1, 2, 3)

    print "#### MAZE 4 ####"
    print die
    moves = [3,2,1,4,3,3,3,2,3,4,1,1,4,4,3,3,4,1,2,1,1,4,4,1,2]
    
    for i in moves:
        die = die.Move(i)
        print die
    
    data = read_maze('maze5.txt')
    die = Die(data[0], data[1], data[2], None, 1, 2, 3)

    print "#### MAZE 5 ####"
    print die
    moves = [3,4,4,4,4,4,4,4,4,4,4,4,1,2,3,3,3,3,3,3,3,3,3,3,3,4]
    
    for i in moves:
        die = die.Move(i)
        print die
