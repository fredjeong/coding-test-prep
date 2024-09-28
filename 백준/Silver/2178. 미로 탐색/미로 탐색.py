import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

def bfs():
    q = deque()
    q.append([0, 0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 1
    child = []
    while q:
        x, y = q.popleft()
        if x==n-1 and y==m-1:
            break
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if visited[nx][ny]==True:
                continue
            visited[nx][ny] = True
            if board[nx][ny]=="0":
                continue
            child.append([nx, ny])
        if not q:
            count += 1
            q.extend(child)
            child = []

    return count

result = bfs()
print(result)