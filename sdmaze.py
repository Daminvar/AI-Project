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
    
    manhattan_results, manhattan_analysis = astar(die, manhattanDistance)
    straight_line_results, straight_line_analysis = astar(die, straightLineDistance)
    direction_results, direction_analysis = astar(die, directionHeuristic)

    for results in \
        [("Manhattan", manhattan_results), ("Straight line", straight_line_results), ("Direction", direction_results)]:

        print '---', results[0], '---'
        if results[1] != None:
            for res in results[1]:
                print res

            print '\nIt takes %s moves to solve the puzzle' % len(results[1])
        else:
            print 'The puzzle is impossible'

    print ''

    for analysis in \
        [("Manhattan", manhattan_analysis), ("Straight line", straight_line_analysis), ("Direction", direction_analysis)]:
        print '---', analysis[0], '---'
        print '\t%s nodes generated' % analysis[1][0]
        print '\t%s nodes visited' % analysis[1][1]
    
    
if __name__ == '__main__':
    main()
    
