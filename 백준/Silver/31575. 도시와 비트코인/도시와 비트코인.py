M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

from collections import deque

def solution(M, N, board):
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    def bfs(x, y):
        q = deque()
        q.append([x, y])
        
        dx = [0, 1]
        dy = [1, 0]

        while q:
            x, y = q.popleft()
            if x == N-1 and y == M-1:
                return True
            
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if board[nx][ny] == 0:
                    continue
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append([nx, ny])           
            
    if bfs(0,0):
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    result = solution(M, N, board)
    print(result)