# Heuristic
#
# Authors: Sean Mullen
#
import math


def manhattanDistance(start, end):
    return abs((end[0] - start[0]) + (end[1] - start[1]))

def directionHeuristic(start, end):
    pass

def straightLineDistance(start, end):
    '''We can change this to a different heuristic if we want.'''
    return math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
