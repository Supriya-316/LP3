# 8 Queens Problem using Backtracking

N = 8
board = [[0] * N for _ in range(N)]

# Step 1: Place the first queen
first_row = 0
first_col = 0
board[first_row][first_col] = 1

# EXTERNAL MODIFICATION:
# If the examiner asks the user to enter the first queen's position,
# replace the above three lines with:
# first_row = int(input("Enter row (1-8): ")) - 1
# first_col = int(input("Enter column (1-8): ")) - 1
# board[first_row][first_col] = 1

# Step 2: Check whether position is safe
def is_safe(row, col):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                if i == row or j == col or abs(row-i) == abs(col-j):
                    return False
    return True

# Step 3: Place remaining queens
def solve(row):
    if row == N: #base case
        return True

    # Skip the row where the first queen is already placed
    if row == first_row:
        return solve(row + 1)

    for col in range(N):
        if is_safe(row, col):
            board[row][col] = 1

            if solve(row + 1): #recursion step
                return True

            board[row][col] = 0 #backtracking step

    return False

# Step 4: Display the solution
if solve(0):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
else:
    print("No solution exists")

#t.c = O(N!)