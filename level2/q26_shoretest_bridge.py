import sys
from collections import deque

def dfs_island(matrix, m, n, visited, srci, srcj, q):
    visited[srci][srcj] = 0
    q.append([srci, srcj])
    paths = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1]
    ]
    for pr, pc in paths:
        destr = srci + pr
        destc = srcj + pc
        if not (destr < 0 or 
                destr >= m or 
                destc < 0 or 
                destc >= n or
                matrix[destr][destc] == 0 or
                visited[destr][destc] == 0):
            dfs_island(matrix, m, n, visited, destr, destc, q)



def solve(matrix, m, n, visited):
    q = deque()
    flag = True
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                dfs_island(matrix, m, n, visited, i, j, q)
                flag = False
                break
        if flag == False:
            break
           
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
        visited[row][col] = level
        paths = [
            [-1, 0],
            [0, 1],
            [1, 0],
            [0, -1]
        ] 
        for r,c in paths:
            if not (row+r < 0 or row+r>=m or
                    col+c < 0 or col+c>=n or
                    visited[row+r][col+c ] != -1):
                if matrix[row+r][col+c] == 0:
                    q.append([row+r, col+c])
                else:
                    return visited[row][col]
    return -1




def main():
    m = int(input())    
    matrix = []
    for k in range(m):
        line = [int(i) for i in sys.stdin.readline().strip().split()]
        matrix.append(line)
    visited = [[-1] * m for i in range(m)]
    
    print(solve(matrix, m, m, visited))
main()
