from solver import *
from sudoku_file_convert import file_to_grid

grid = SudokuGrid([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

tests = dict()


tests['add_get_remove_candidates'] = lambda: add_get_remove_candidates()
def add_get_remove_candidates():
    assert grid.getCandidates(1, 1) == set()
    grid.addCandidates([1, 2, 3, 4, 5], 1, 1)
    assert grid.getCandidates(1, 1) == {1, 2, 3, 4, 5}
    grid.removeCandidates([2, 3], 1, 1)
    assert grid.getCandidates(1, 1) == {1, 4, 5}
    grid.addCandidates([6], 1, 1)
    assert grid.getCandidates(1, 1) == {1, 4, 5, 6}
    grid.removeCandidates([1], 1, 1)
    assert grid.getCandidates(1, 1) == {4, 5, 6}


tests['grid_convert'] = lambda: grid_convert()
def grid_convert():
    filename = 'test_puzzle.sdk'
    grid_correct = [[2, 0, 0, 1, 0, 5, 0, 0, 3], [0, 5, 4, 0, 0, 0, 7, 1, 0], [0, 1, 0, 2, 0, 3, 0, 8, 0], [6, 0, 2, 8, 0, 7, 3, 0, 4], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 5, 3, 0, 9, 8, 0, 6], [0, 2, 0, 7, 0, 1, 0, 6, 0], [0, 8, 1, 0, 0, 0, 2, 4, 0], [7, 0, 0, 4, 0, 2, 0, 0, 1]]
    grid_eval = file_to_grid(filename)
    
    assert grid_eval == grid_correct



# run and evaluate tests
num_failed = 0
failed_tests = []
for test in tests:
    try:
        tests[test]()
    except:
        num_failed += 1
        failed_tests.append(test)
        
num_tests = len(tests)
print(f'Passed {num_tests - num_failed} out of {num_tests} tests')
if(num_failed > 0):
    print('Failed tests:')
    
    for t in failed_tests:
        print(t)