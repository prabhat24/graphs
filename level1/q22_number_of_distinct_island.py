import sys


def dfs_island(board, m, n, row, col, hash_set):
    global psf
    
    board[row][col] = 0
    paths = [
        [-1, 0, "u"],
        [0, 1, "r"],
        [1, 0, "d"],
        [0, -1, "l"]
    ]
    for p in paths:
        new_row = row + p[0] 
        new_col = col + p[1]
        if not (new_row<0 or new_row>=m or 
                new_col<0 or new_col>=n or 
                board[new_row][new_col] == 0):
            psf = psf+ str(p[2])
            dfs_island(board, m, n, new_row, new_col, hash_set)
    psf = psf+ "z"

m,n = [int(i) for i in sys.stdin.readline().strip().split()]

psf = ""
board = []
for _ in range(m):
    line = [int(i) for i in sys.stdin.readline().strip().split()]
    board.append(line)

hash_set = set()
for i in range(m):
    for j in range(n):
        psf = "x"
        if board[i][j] == 1:
            dfs_island(board, m, n, i, j, hash_set)
            hash_set.add(psf)
print(hash_set)

