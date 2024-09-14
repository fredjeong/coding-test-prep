from collections import deque

M, N = map(int, input().split())
board = [str(input().strip()) for _ in range(M)]

def solution(M, N, board):
    def bfs(M, N, board):
        visited = [[False for _ in range(N)] for _ in range(M)]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(len(board[0])):
            if visited[0][i] == True or board[0][i] != "0":
                continue
            visited[0][i] = True
            q = deque()
            q.append([0,i])

            while q:
                x, y = q.popleft()
                if x == M-1:
                    return True
                
                for j in range(len(dx)):
                    nx = x + dx[j]
                    ny = y + dy[j]

                    if nx < 0 or nx >= M or ny < 0 or ny >= N:
                        continue
                    if board[nx][ny] != "0":
                        continue
                    if visited[nx][ny] == True:
                        continue
                    visited[nx][ny] = True
                    q.append([nx, ny])
                
    if bfs(M, N, board):
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    result = solution(M, N, board)
    print(result)