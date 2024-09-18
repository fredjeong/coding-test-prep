import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

def bfs(N, M, board, start, start_colour):
    count = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[start[0]][start[1]] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = deque()
    q.append(start)
    
    while q:
        x, y = q.popleft()
        if start_colour == "white":
            if (x+y)%2 == 0 and board[x][y] == "B":
                count += 1
            elif (x+y)%2 == 1 and board[x][y] == "W":
                count += 1
        elif start_colour == "black":
            if (x+y)%2 == 0 and board[x][y] == "W":
                count += 1
            elif (x+y)%2 == 1 and board[x][y] == "B":
                count += 1
        
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < start[0] or nx >= start[0]+8 or ny < start[1] or ny >= start[1]+8:
                continue
            if visited[nx][ny] == True:
                continue
            visited[nx][ny] = True
            q.append([nx, ny])
    
    return count

count = 1e9
for i in range(N-7):
    for j in range(M-7):
        # 시작점 선정
        start = [i,j]
        # 맨 왼쪽 위를 검은색으로 칠하는 경우
        result_1 = bfs(N, M, board, start, "white")
        # 맨 아래를 검은색으로 칠하는 경우
        result_2 = bfs(N, M, board, start, "black")
        if min(result_1, result_2) < count:
            count = min(result_1, result_2)

print(count)