import sys

def dfs(board, m, n, row, col):
    board[row][col] = 0
    paths = [
        [-1,0],
        [0,1],
        [+1, 0],
        [0,-1]
    ]
    for p in paths:
        new_row=row+p[0]
        new_col=col+p[1]
        if not( new_row<0 or new_row >= m or 
            new_col<0 or new_col>=n  or board[new_row][new_col]!=1):
            dfs(board, m, n, new_row, new_col)

def calc_enclave(board, m, n):
    for i in range(0, n):
        col = i
        row = 0
        if board[row][col] == 1:
            dfs(board, m, n, row, col)

    for i in range(0, n):
        col = i
        row = m-1
        if board[row][col] == 1:
            dfs(board, m, n, row, col)
    
    for j in range(0, m):
        col = 0
        row = j
        if board[row][col] == 1:
            dfs(board, m, n, row, col)

    for j in range(0, m):
        col = n-1
        row = j
        if board[row][col] == 1:
            dfs(board, m, n, row, col)
    count = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                count += 1
    print(count)

m, n= [int(i) for i in sys.stdin.readline().strip().split()]

board = []
for k in range(m):
    line = [int(i) for i in sys.stdin.readline().strip().split()]
    board.append(line)

calc_enclave(board, m,n)

