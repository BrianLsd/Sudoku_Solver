board = [
    [6,0,9,0,0,4,0,0,1],
    [8,0,0,0,5,0,0,0,0],
    [0,3,5,1,0,9,0,0,8],
    [0,0,8,0,0,0,0,0,4],
    [0,5,0,0,0,0,0,3,0],
    [4,0,0,0,7,0,0,5,2],
    [0,0,0,0,0,1,0,0,0],
    [0,0,1,0,4,0,0,0,0],
    [7,6,0,9,3,0,0,0,0]
]

def solve(bo): # Backtrack algorithm 
    find = find_empty(bo)
    if not find: # complete
        return True
    else:
        row, col = find # find a empty square

    for i in range(1,10): # put different numbers from 1-9 to the square
        if valid(bo, i, (row, col)): # check if it's valid
            bo[row][col] = i # if it's valid, put the number in the square

            if solve(bo): # recursively backtrack, if it's complete, return True
                return True
            bo[row][col] = 0 # if there is any wrong numbers being put before, reset the square to 0
    return False 

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

def print_board(bo): # Print the whole puzzle
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0: # divide the puzzle into three sections vertically
            print("- - - - - - - - - - -")

        for j in range(len(bo[0])): # divide the puzzle into three sections horizontally
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:  # if it's the last number of a column, do not print '|'
                print(bo[i][j])
            elif j == 2 or j == 5:
                print(bo[i][j],end='')
            else:       
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo): # find any sqaures that contain 0
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col (position)
    return None # if the puzzle is complete, return none

print_board(board)
solve(board)
print()
print()
print_board(board)

