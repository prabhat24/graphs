import sys
from collections import deque

def time_to_rot(matrix, m, n, visited):
    q = deque()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 2:
                q.append([i, j])

    level = 0
    q.append(None)

    while len(q):
        ele = q.popleft()
        if ele == None:
            if len(q):
                level += 1
                q.append(ele)
            continue
        row, col = ele
        if visited[row][col] == -1:
            visited[row][col] = level
            paths = [
                [-1, 0],
                [0, 1],
                [1, 0],
                [0, -1]
            ]
            for p in paths:
                if not (row + p[0] < 0 or 
                        row + p[0] >= m or
                        col + p[1] < 0 or
                        col + p[1] >= n or
                        visited[row+p[0]][col+p[1]] >= 0 or matrix[row+p[0]][col+p[1]] == 0):
                    q.append([row+p[0], col+p[1]])
    
    # check if 1 exist in the matrix
    for i in range(m):
        for j in range(n):
            if visited[i][j] == -1 and matrix[i][j] == 1:
                return -1
    return level


def main():
    m, n = [int(i) for i in sys.stdin.readline().strip().split()]
    
    matrix = []
    for k in range(m):
        line = [int(i) for i in sys.stdin.readline().strip().split()]
        matrix.append(line)
    visited = [[-1] * n for i in range(m)]
    
    print(time_to_rot(matrix, m, n, visited))
main()
