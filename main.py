# Creating chess board
chess_grid = [[0 for j in range(8)] for i in range(8)]

queens = 8

row, column = 0, 0

'''
queen - can attack any direction
Have to check left, right, up, down, left diagonal, right diagonal
1 - indcates queen has been places
0 - empty
'''

def print_grid(grid):
    for row in range(len(grid)):
        for j in grid[row]:
            print(str(j), end=' ')
        print()

def out_of_bounds(row, col, grid):
    return row < 0 or row >= len(grid) or col < 0 or col >= len(grid)

def can_place(row, col, grid):
    '''
    check all elements in row
    check all elements in col
    check all elements in diag-right-up
    check all elements in diag-right-down
    check all elements in diag-left-up
    check all elements in diag-left-down
    '''
    if out_of_bounds(row, col, grid):
        return False
    
    # row check
    for spaces in grid[row]:
        if spaces == 1:
            return False
    
    # column check
    for rows in range(len(grid)):
        if grid[rows][col] == 1:
            return False
    
    # diag-right-up check
    cur_row, cur_col = row, col
    while not out_of_bounds(cur_row, cur_col, grid):
        if grid[cur_row][cur_col] == 1:
            return False
        cur_row -= 1
        cur_col += 1 
    
    # diag-right-down check
    cur_row, cur_col = row, col
    while not out_of_bounds(cur_row, cur_col, grid):
        if grid[cur_row][cur_col] == 1:
            return False
        cur_row += 1
        cur_col += 1 
    
    # diag-left-up check
    cur_row, cur_col = row, col
    while not out_of_bounds(cur_row, cur_col, grid):
        if grid[cur_row][cur_col] == 1:
            return False
        cur_row -= 1
        cur_col -= 1 
    
    # diag-left-down check
    cur_row, cur_col = row, col
    while not out_of_bounds(cur_row, cur_col, grid):
        if grid[cur_row][cur_col] == 1:
            return False
        cur_row += 1
        cur_col -= 1

    return True


def emulate(grid, row, col, queens):
    if queens == 0:
        return grid
    
    if out_of_bounds(row, col, grid):
        return grid
    
    if can_place(row, col, grid):
        grid[row][col] = 1
        print_grid(grid)
        print()
        emulate(grid, row, col + 1, queens - 1)
        grid[row][col] = 0
    
    return emulate(grid, row + 1, col, queens)

print_grid(emulate(chess_grid, 0, 0, 8))



    
