import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())


box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 익은 토마토 찾기
rotten = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k]==1:
                rotten.append([i, j, k])

def bfs():
    visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
    
    dz = [0, 0, 0, 0, 1, -1]
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    
    count = 0
    child = []
    while rotten:
        z, x, y = rotten.popleft()
    
        if visited[z][x][y] == True:
            continue
        visited[z][x][y] = True

        for i in range(len(dz)):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if box[nz][nx][ny] == -1:
                continue
            if box[nz][nx][ny] == 1:
                continue
            box[nz][nx][ny] = 1
            if visited[nz][nx][ny] == True:
                continue
            child.append([nz, nx, ny])
        
        if not rotten and child:
            rotten.extend(child)
            count += 1
            child = []
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k]==0:
                    return -1
    return count

result = bfs()
print(result)