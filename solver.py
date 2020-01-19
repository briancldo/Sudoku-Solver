from sudoku_obj import *
from sudoku_file_convert import file_to_grid

def solve(filename):
    grid = file_to_grid(filename)
    
    # TODO: implement my (Brian Do) style of sudoku solving.