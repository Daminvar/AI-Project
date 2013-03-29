from read_maze import *
from die import *
from heuristics import *
import sys

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
    
    print 'Initial board state is: '
    print die
    
    
if __name__ == '__main__':
    main()
    
