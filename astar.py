import collections

def astar(die, heuristic):
    open_set = collections.deque()
    visited = {}
    open_set.append((die, heuristic(die)))
    visited[start] = 0
    while len(open_set) != 0:
        currentDie, f_cost = reduce(lambda a, b: a if a[1] < b[1] else b, open_set)

        if currentDie.IsGoal():
            return die.getParentsAsList()

        open_set.remove((currentDie, f_cost))
        visited[currentDie] = len(currentDie.GetParentsAsList())

        for newDie in currentDie.GetMoves():
            tentative_g = len(newDie.GetParentsAsList()) + heuristic(newDie)
            if visited.get(newDie, 20000) <= tentative_g
                continue

            if not newDie in open_set:
                open_set.append(newDie, len(newDie.GetParentsAsList()) + heuristic(newDie))

    return None

if __name__ == '__main__':
