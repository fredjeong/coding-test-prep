import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if 2 not in board[i]:
        continue
    else:
        j = board[i].index(2)
        obj_x = i
        obj_y = j
        break

def bfs(n, m, board, obj_x, obj_y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([obj_x, obj_y])
    visited[obj_x][obj_y] = True
    dist = 0
    child = []
    while q:
        x, y = q.popleft()
        if board[x][y] == 0:
            board[x][y] = "0"
            if len(q) == 0:
                q.extend(child)
                dist += 1
                child = []
            continue
        board[x][y] = str(dist)
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == True:
                continue
            visited[nx][ny] = True
            child.append([nx, ny])
        if len(q) == 0:
            q.extend(child)
            dist += 1
            child = []

bfs(n, m, board, obj_x, obj_y)
for i in range(n):
    print(" ".join(map(lambda x: str(-1) if x==1 else str(x), board[i])))