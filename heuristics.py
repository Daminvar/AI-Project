# Heuristic
#
# Authors: Sean Mullen
#
import math


def manhattanDistance(die):
    return abs((die.goal[0] - die.start[0]) + (die.goal[1] - die.start[1]))

def straightLineDistance(die):
    '''We can change this to a different heuristic if we want.'''
    return math.sqrt((die.goal[0] - die.start[0])**2 + (die.goal[1] - die.start[1])**2)

"""
def directionHeuristic(start, end):
    pass

"""
