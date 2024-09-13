N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

from collections import deque

def solution(N, board):
    visited = [[False for _ in range(N)] for _ in range(N)]
    
    dx = [0, 1]
    dy = [1, 0]

    def bfs(x, y):
        q = deque()
        q.append([x, y])

        while q:
            x, y = q.popleft()
            step = board[x][y]

            if step == -1:
                return True

            for i in range(len(dx)):
                nx = x + dx[i] * step
                ny = y + dy[i] * step

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue

                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])

    if bfs(0, 0):
        return "HaruHaru"
    else:
        return "Hing"

if __name__ == '__main__':
    result = solution(N, board)
    print(result)