import main as mp

def test_can_place(test_row, test_col, row, col, grid):
    if mp.out_of_bounds(row, col, grid) or mp.out_of_bounds(test_row, test_col, grid):
        raise Exception("Parameters out of bound")    
    mp.chess_grid[row][col] = 1
    mp.print_grid(grid=mp.chess_grid)
    value = mp.can_place(test_row, test_col, grid=mp.chess_grid)
    mp.chess_grid[row][col] = 0
    print("Can Place!" if value else "Can't Place.")

test_can_place(0, 0, 7, 7, mp.chess_grid)
test_can_place(0, 0, 0, 7, mp.chess_grid)
test_can_place(0, 0, 7, 0, mp.chess_grid)
test_can_place(0, 0, 1, 2, mp.chess_grid)
test_can_place(0, 0, -1, -1, mp.chess_grid)

