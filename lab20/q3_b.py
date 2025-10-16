def get_columns(grid):
    num_cols = len(grid[0])
    return [[row[i] for row in grid] for i in range(num_cols)]
def get_diagonals(grid):
    rows = len(grid)
    cols = len(grid[0])
    diagonals = []
        if diag:
            diagonals.append(diag)
    return diagonals