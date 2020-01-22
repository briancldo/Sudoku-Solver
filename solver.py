from sudoku_obj import *
from sudoku_file_convert import file_to_grid

def solve(filename):
    grid = SudokuGrid(file_to_grid(filename))
    num_rows = grid.rows
    num_cols = grid.cols
    
    while grid.num_unknown > 0:
        for row in range(num_rows):
            for col in range(num_cols):
                if grid.getValue(row, col) == 0:
                    # TODO: Implement
                    x = 1