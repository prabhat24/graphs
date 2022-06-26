import sys
from collections import deque

def solve(matrix, m, n, visited):
    q = deque()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
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
                        visited[row+p[0]][col+p[1]] != -1 or matrix[row+p[0]][col+p[1]] == 1):
                    q.append([row+p[0], col+p[1]])
    
    return level


def main():
    m = int(input())
    
    matrix = []
    for k in range(m):
        line = [int(i) for i in sys.stdin.readline().strip().split()]
        matrix.append(line)
    visited = [[-1] * m for i in range(m)]
    
    a = solve(matrix, m, m, visited)
    if a == 0:
        print(-1)
    else:
        print(a)
main()
