def file_to_grid(filename):
    puzzle_file = open(filename)
    grid = []
    
    for file_line in puzzle_file:
        if file_line[0] != '#':
            grid_line = []
            for char in file_line:
                if char != '\n':
                    grid_line.append(0 if char == '.' else int(char))
            
            grid.append(grid_line)
    
    return grid