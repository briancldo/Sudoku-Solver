class SudokuUnit:
    def __init__(self, val):
        if val != 0:
            self.cand = set()
        else:
            self.cand = set([1,2,3,4,5,6,7,8,9])
        
        self.val = val


class SudokuGrid:
    def __init__(self, grid):
        self.num_unknown = 0
        self.grid = []
        self.rows = 9
        self.cols = 9
    
        for row in grid:
            converted_row = []
            for val in row:
                converted_row.append(SudokuUnit(val))
                if val == 0:
                    self.num_unknown += 1
                    
            self.grid.append(converted_row)
    
    def getCandidates(self, x, y):
        return self.grid[x][y].cand
    
    def addCandidates(self, new_cands, x, y):
        self.grid[x][y].cand.update(new_cands)
    
    def removeCandidates(self, rem_cands, x, y):
        for c in rem_cands:
            self.grid[x][y].cand.remove(c)
            
    def setValue(self, val, x, y):
        self.grid[x][y] = val
    
    def getValue(self, x, y):
        return self.grid[x][y]