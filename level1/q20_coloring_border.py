import sys


def dfs(matrix, row, column, color, ini_color, dp):

    M, N = len(matrix), len(matrix[0])
    matrix[row][column] = -1 * abs(matrix[row][column])
    paths = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1],
    ]
    count = 0
    for p in paths:
        new_row, new_col = row + p[0], column + p[1]
        if not (new_row < 0 or new_row >= M or 
                new_col < 0 or new_col >= N or abs(matrix[new_row][new_col]) != ini_color):
            if matrix[new_row][new_col] == ini_color:
                dfs(matrix, new_row, new_col, color, ini_color, dp)
            count += 1
    if count != 4:
        dp[row][column] = 1

def coloring(matrix, m, n, color, ini_color, dp):
    for i in range(m):
        for j in range(n):
            if dp[i][j] == 1:
                matrix[i][j] = color
            elif matrix[i][j] < 0:
                matrix[i][j] = abs(matrix[i][j])


def main():
    m, n = sys.stdin.readline().strip().split(" ")
    m, n = int(m), int(n)
    matrix = []
    for l in range(0, m):
        line = [int(i) for i in sys.stdin.readline().strip().split(" ")]
        matrix.append(line)

    row, column, color = [int(i) for i in sys.stdin.readline().strip().split(" ")]
    ini_color = matrix[row][column]
    dp = [[-1] * n for _ in range(m)] 
    dfs(matrix, row, column, color, ini_color, dp)
    coloring(matrix, m, n, color, ini_color, dp)
    
    for i in range(0, m):
        for j in range(0, n):
            print( matrix[i][j], end="\t")
        print()

main()
