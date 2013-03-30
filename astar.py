import collections
from die import *
from read_maze import *
from heuristics import *

def astar(die, heuristic):
    open_set = collections.deque()
    visited = {}
    open_set.append((die, heuristic(die)))
    visited[die] = 0
    while len(open_set) != 0:
        currentDie, f_cost = reduce(lambda a, b: a if a[1] < b[1] else b, open_set)

        if currentDie.IsGoal():
            return currentDie.GetParentsAsList()

        open_set.remove((currentDie, f_cost))
        visited[currentDie] = len(currentDie.GetParentsAsList())

        for newDie in currentDie.GetMoves():
            tentative_g = len(newDie.GetParentsAsList())
            if visited.get(newDie, 20000) <= tentative_g:
                continue

            in_open_set = newDie in map(lambda a: a[0], open_set)
            if not in_open_set or tentative_g < visited.get(newDie, 20000):
                visited[newDie] = tentative_g
                open_set.append((newDie, len(newDie.GetParentsAsList()) + heuristic(newDie)))

    return None

if __name__ == '__main__':
    data = read_maze('maze5.txt')
    die1 = Die(data[0], data[1], data[2], None, 1, 2, 3)
    die2 = Die(data[0], data[1], data[2], None, 1, 2, 3)

    for res in astar(die1, straightLineDistance):
        print res
