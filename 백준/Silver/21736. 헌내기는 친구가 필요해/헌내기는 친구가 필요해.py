import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j]=="I":
            pos_x = i
            pos_y = j
            break

def bfs():
    q = deque()
    q.append([pos_x, pos_y])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[pos_x][pos_y] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    count=0

    while q:
        x, y = q.popleft()
        if board[x][y]=="P":
            count += 1
        
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]==True:
                continue
            visited[nx][ny] = True
            if board[nx][ny]=="X":
                continue
            q.append([nx, ny])
    
    if count:
        return count
    else:
        return "TT"
        
result = bfs()
print(result)