import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [list(map(int, list(input().strip()))) for _ in range(n)]

def bfs():
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append([0, 0])
    visited[0][0] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    island = []
    temp = 0
    while q:
        is_break = False
        x, y = q.popleft()
        if board[x][y]==1:
            temp += 1
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == True:
                continue
            visited[nx][ny] = True
            
            if board[nx][ny] == 1:
                q.append([nx, ny])
        if not q:
            if temp != 0:
                island.append(temp)
                temp = 0
            for i in range(n):
                for j in range(n):
                    if visited[i][j]==True:
                        continue
                    visited[i][j] = True
                    if board[i][j]==1:
                        q.append([i,j])
                        is_break = True
                        break
                if is_break == True:
                    break
    
    return island

result = bfs()
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])