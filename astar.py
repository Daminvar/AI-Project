import collections
from die import *
from read_maze import *
from heuristics import *

def astar(die, heuristic):
    # analysis: [generated, visted]
    analysis = [0, 0]
    open_set = collections.deque()
    visited = {}
    open_set.append((die, heuristic(die)))
    visited[die] = 0
    while len(open_set) != 0:
        currentDie, f_cost = reduce(lambda a, b: a if a[1] < b[1] else b, open_set)

        if currentDie.IsGoal():
            return currentDie.GetParentsAsList(), analysis

        open_set.remove((currentDie, f_cost))
        analysis[1] += 1
        visited[currentDie] = len(currentDie.GetParentsAsList())

        for newDie in currentDie.GetMoves():
            tentative_g = len(newDie.GetParentsAsList())
            if visited.get(newDie, 20000) <= tentative_g:
                continue

            in_open_set = newDie in map(lambda a: a[0], open_set)
            if not in_open_set or tentative_g < visited.get(newDie, 20000):
                visited[newDie] = tentative_g
                analysis[0] += 1
                open_set.append((newDie, len(newDie.GetParentsAsList()) + heuristic(newDie)))

    return None, analysis

if __name__ == '__main__':
    data = read_maze('maze5.txt')
    die1 = Die(data[0], data[1], data[2], None, 1, 2, 3)
    die2 = Die(data[0], data[1], data[2], None, 1, 2, 3)

    results, analysis = astar(die1, manhattanDistance)

    if results != None:
        for res in results:
            print res

        print '\nIt takes %s moves to solve the puzzle' % len(results)
    else:
        print 'The puzzle is impossible'
    print '%s nodes generated' % analysis[0]
    print '%s nodes visited' % analysis[1]
