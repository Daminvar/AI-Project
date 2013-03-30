# Heuristic
#
# Authors: Sean Mullen
#
import math


def manhattanDistance(die):
    return abs(die.goal[0] - die.start[0]) + abs(die.goal[1] - die.start[1])

def straightLineDistance(die):
    '''We can change this to a different heuristic if we want.'''
    return math.sqrt((die.goal[0] - die.start[0])**2 + (die.goal[1] - die.start[1])**2)


def directionHeuristic(die):
    """
    up has no penalty, towards has 1.25 penalty and away has .75 penalty 
    based on scaled distance to goal
    """
    
    absLength = die.GetAbsLength()
    
    dieUpPenalty = .01
    dieTowardPenalty = .08
    dieAwayPenalty = -.08

    dist = manhattanDistance(die)
    
    # get percentage of distance away from goal and every 25% 
    # we add more penalty
    distScale = dist / absLength
    
    # get the penalty multiplier
    inc = [0.0, .25, .50, .75, 1.0]
    mult = len(inc) - 1
    for i in inc
        if distScale <= i:
             break;
        
        mult -= 1
             
    # get direction relative to goal
    penalty = 0
    if (die.Direction() == 'X') 
        penalty = dist * (1.0 + (dieUpPenalty * mult))
    elif (die.Direction() == '<'):
        if (die.Start[1] > die.Goal[1]):
            penalty = dist * (1.0 + (dieTowardPenalty * mult))
        else:
            penalty = dist * (1.0 + (dieAwayPenalty * mult))
    elif (die.Direction() == '>'):
        if (die.Start[1] < die.Goal[1]):
            penalty = dist * (1.0 + (dieTowardPenalty * mult))
        else:
            penalty = dist * (1.0 + (dieAwayPenalty * mult))
    elif (die.Direction() == '^'):
        if (die.Start[0] > die.Goal[0]):
            penalty = dist * (1.0 + (dieTowardPenalty * mult))
        else:
            penalty = dist * (1.0 + (dieAwayPenalty * mult))
    elif (die.Direction() == 'V'):
        if (die.Start[0] < die.Goal[0]):
            penalty = dist * (1.0 + (dieTowardPenalty * mult))
        else:
            penalty = dist * (1.0 + (dieAwayPenalty * mult))
            
    return penalty

