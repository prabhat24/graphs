import sys

from collections import deque

def manhatern_distance(matrix, m, n, visited):
    q = deque()
    for i in range(0, m):
        for j in range(0, n):
            if matrix[i][j] == 0:
                q.append([i, j,])
    q.append(None)
    level = 0
    while len(q):
        ele = q.popleft()
        if ele == None:
            level += 1
            if len(q):
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
                if not(row + p[0] < 0 or 
                        row + p[0] >= m or
                        col + p[1] < 0 or
                        col + p[1] >= n or
                        visited[row+p[0]][col+p[1]] != -1):
                    q.append([row+p[0],col+p[1]])
    return





def main():
    m, n = [int(i) for i in sys.stdin.readline().strip().split()]
    
    matrix = []
    for k in range(m):
        line = [int(i) for i in sys.stdin.readline().strip().split()]
        matrix.append(line)
    visited = [[-1] * n for i in range(m)]
    
    manhatern_distance(matrix, m, n, visited)
    for i in range(m):
        for j in range(n):
            print(visited[i][j], end=" ")
        print()
    print()
main()



########################################################

import sys

from collections import deque

def manhatern_distance(matrix, m, n):
    q = deque()
    for i in range(0, m):
        for j in range(0, n):
            if matrix[i][j] == 0:
                q.append([i, j,])
    q.append(None)
    level = 0
    while len(q):
        ele = q.popleft()
        if ele == None:
            level += 1
            if len(q):
                q.append(ele)
            continue

        row, col = ele
        if matrix[row][col] >= 0:
            matrix[row][col] = -1 * level
            paths = [
                [-1, 0],
                [0, 1],
                [1, 0],
                [0, -1]
            ]
            for p in paths:
                if not(row + p[0] < 0 or 
                        row + p[0] >= m or
                        col + p[1] < 0 or
                        col + p[1] >= n or
                        matrix[row+p[0]][col+p[1]] <= 0):
                    q.append([row+p[0],col+p[1]])
    return





def main():
    m, n = [int(i) for i in sys.stdin.readline().strip().split()]
    
    matrix = []
    for k in range(m):
        line = [int(i) for i in sys.stdin.readline().strip().split()]
        matrix.append(line)
    # visited = [[-1] * n for i in range(m)]
    
    manhatern_distance(matrix, m, n)
    for i in range(m):
        for j in range(n):
            print((-1) * matrix[i][j], end=" ")
        print()
    print()
main()
