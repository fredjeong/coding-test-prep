import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ripen = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            ripen.append([i,j])

def bfs(M, N, board):
    count = 0
    q = deque()
    q.append(ripen)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    child = []
    while q:
        temp = q.popleft()
        temp = deque(temp)

        while temp:
            arr = temp.popleft()
            x = arr[0]
            y = arr[1]
            
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue

                if board[nx][ny] == 1:
                    continue
                
                if board[nx][ny] == -1:
                    continue
                board[nx][ny] = 1
            
                child.append([nx, ny])
        
        if len(q) == 0 and child != []:
            q.append(child)
            count += 1
            child = []
    return count

result = bfs(M, N, board)

is_break = False
for i in range(N):
    if 0 in board[i]:
        print(-1)
        is_break = True
        break
if is_break == False:
    print(result)