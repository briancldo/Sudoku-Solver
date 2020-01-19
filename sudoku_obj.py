class SudokuUnit:
    def __init__(self, val):
        if val != 0:
            self.cand = set()
        else:
            self.cand = set([1,2,3,4,5,6,7,8,9])
        
        self.val = val


class SudokuGrid:
    def __init__(self, grid):
        self.grid = [[SudokuUnit(unit) for unit in row] for row in grid]
    
    def getCandidates(self, x, y):
        return self.grid[x][y].cand
    
    def addCandidates(self, new_cands, x, y):
        self.grid[x][y].cand.update(new_cands)
    
    def removeCandidates(self, rem_cands, x, y):
        for c in rem_cands:
            self.grid[x][y].cand.remove(c)