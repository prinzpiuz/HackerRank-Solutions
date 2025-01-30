# dominant cell in matrix


def numCells(grid):
    dom_cell = 0
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            print(f"r{r}c{c}")
            if c - 1 < 0:
                left = 0
            else:
                left = grid[r][c - 1]
            if c + 1 >= len(grid[0]):
                right = 0
            else:
                right = grid[r][c + 1]
            if r - 1 < 0:
                top = 0
            else:
                top = grid[r - 1][c]
            if r + 1 >= len(grid):
                under = 0
            else:
                under = grid[r + 1][c]
            if (
                (grid[r][c] > left)
                and (grid[r][c] > under)
                and (grid[r][c] > right)
                and (grid[r][c] > top)
            ):
                dom_cell += 1
    return dom_cell


print(numCells([[1, 1, 0, 1]]))
