import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

board_1 = [input().strip() for _ in range(n)]
board_2 = board_1[:]
for i in range(n):
    board_2[i] = board_2[i].replace("G", "R")

def bfs(board):
    visited = [[False for _ in range(n)] for _ in range(n)]

    x_pos = 0
    y_pos = 0
    visited[x_pos][y_pos] = True

    q = deque()
    q.append([x_pos, y_pos])
    
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    count = 1
    child = deque()
    while q:
        x, y = q.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
                
            if visited[nx][ny] == True:
                continue
            if board[nx][ny] == board[x][y]:
                visited[nx][ny] = True
                q.append([nx, ny])
            else:
                child.append([nx, ny])
            
        if not q:
            while child:
                cx, cy = child.popleft()
                if visited[cx][cy]==True:
                    continue
                else:
                    visited[cx][cy] = True
                    q.append([cx, cy])
                    count += 1
                    break
    return count

result_1 = bfs(board_1)
result_2 = bfs(board_2)
print(result_1, result_2)       