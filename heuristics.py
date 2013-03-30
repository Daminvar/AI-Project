import math

# Heuristic
#
# Authors: Sean Mullen, Dennis Honeyman
#


def manhattanDistance(die):
    # distance along from the non-hypontenuse sides of the triangle
    return abs(die.goal[0] - die.start[0]) + abs(die.goal[1] - die.start[1])

def straightLineDistance(die):
    '''We can change this to a different heuristic if we want.'''
    return math.sqrt((die.goal[0] - die.start[0])**2 + (die.goal[1] - die.start[1])**2)


def directionHeuristic(die):
    
    absStart = die.GetAbsStart()
    absLength = abs(die.goal[0] - absStart[0]) + abs(die.goal[1] - absStart[1])
    
    # expontential decay/growth penalties
    dieUpPenalty = .01
    dieTowardPenalty = .08
    dieAwayPenalty = -.08

    # get the manhattanDistance to goal from current state
    dist = manhattanDistance(die)
    
    # get distance scale from goal based off of starting position
    distScale = dist / absLength
    
    # gets the penalty multiplier based off distance scale
    inc = [0.0, .15, .30, .45, .60, .75, .80, 1.0]
    mult = len(inc) - 1
    for i in inc:
        if distScale <= i:
             break;
        
        mult -= 1
             
    """
        Closer values will have a higher mult. on the exponential decay/growth
        penalty, which is applied to the real distance away from goal.    
    """
    penalty = 0
    if (die.Direction() == 'X'):
        penalty = dist * (1.0 + (dieUpPenalty * mult))
    elif (die.Direction() == '<'):
        if (die.Start()[1] > die.Goal()[1]):
            penalty = dist * (1.0 + (dieTowardPenalty * mult))
        else:
            penalty = dist * (1.0 + (dieAwayPenalty * mult))
    elif (die.Direction() == '>'):
        if (die.Start()[1] < die.Goal()[1]):
            penalty = dist * (1.0 + (dieTowardPenalty * mult))
        else:
            penalty = dist * (1.0 + (dieAwayPenalty * mult))
    elif (die.Direction() == '^'):
        if (die.Start()[0] > die.Goal()[0]):
            penalty = dist * (1.0 + (dieTowardPenalty * mult))
        else:
            penalty = dist * (1.0 + (dieAwayPenalty * mult))
    elif (die.Direction() == 'V'):
        if (die.Start()[0] < die.Goal()[0]):
            penalty = dist * (1.0 + (dieTowardPenalty * mult))
        else:
            penalty = dist * (1.0 + (dieAwayPenalty * mult))
            
    return penalty

