# Heuristic
#
# Authors: Sean Mullen
#
import math


def manhattanDistance(die):
    return abs((die.goal[0] - die.start[0]) + (die.goal[1] - die.start[1]))

"""
def directionHeuristic(start, end):
    pass

def straightLineDistance(start, end):
    '''We can change this to a different heuristic if we want.'''
    return math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
"""
