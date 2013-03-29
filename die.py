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
        result = ""

        for s in range(len(self.board)):
            if s == self.start[0]:
                rowAsString = list(self.board[s])
                rowAsString[self.start[1]] = str(self.value)
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

    def GetParentsAsList(self):
        if parent == None:
            return []
        return parent.GetParentsAsList() + self;

    def GetMoves(self):
        """ Returns a list of new dice objects that can represent the possible
        states that the dice can be in for the next move. """
        moves = []

        possible_directions = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0),
        ]

        for move, direction in zip(possible_directions, range(1,5)):
            new_pos = (self.start[0] + move[0], self.start[1] + move[1])
            if not (0 <= new_pos[0] < len(self.board) and 0 <= new_pos[1] < len(self.board[0])):
                continue
            if self.board[new_pos[0]][new_pos[1]] == '*':
                continue
            new_die = self.Move(direction)
            moves.append(new_die)
        return moves

    def Move(self, direction):
        """ Moves the die in a direction. 1 is up, 2 is right,
         3 is down and is 4 left. """
        if direction == 1:
            next = 7 - self.value
            self.north = self.value
            self.value = next



if __name__ == '__main__':
    data = read_maze('maze5.txt')
    die = Die(data[0], data[1], data[2])
    for newDie in die.GetMoves():
        print newDie
