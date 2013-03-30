import sys

from astar import *
from die import *
from heuristics import *
from read_maze import *

def main():
    if len(sys.argv) != 2:
        print "usage: python sdmaze.py maze_file"
        return

    print 'Reading in ' + sys.argv[1] + '...\n'
    data = read_maze(sys.argv[1])
    
    if data[0] == None or data[1] == None:
        print "Invalid board configuration. Board must have start and stop goals."
        return;
    
    die = Die(data[0], data[1], data[2], None, 1, 2, 3)
    
    results, manhattan_analysis = astar(die, manhattanDistance)
    _, straight_line_analysis = astar(die, straightLineDistance)

    if results != None:
        for res in results:
            print res

        print '\nIt takes %s moves to solve the puzzle' % len(results)
    else:
        print 'The puzzle is impossible'

    for analysis in \
        [("Manhattan", manhattan_analysis), ("Straight line", straight_line_analysis)]:
        print '---', analysis[0], '---'
        print '\t%s nodes generated' % analysis[1][0]
        print '\t%s nodes visited' % analysis[1][1]
    
    
if __name__ == '__main__':
    main()
    
