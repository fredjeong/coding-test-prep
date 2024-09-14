from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def solution(N, M, board):
    def bfs(N, M, board):
        
        dx = [1, -1, 0, 0, 1, 1, -1, -1]
        dy = [0, 0, 1, -1, 1, -1, 1, -1]
        answer = 0
        for i in range(N):
            for j in range(M):
                visited = [[False for _ in range(M)] for _ in range(N)]
                dist = 1
                if board[i][j] == 1 or visited[i][j] == True:
                    continue
                visited[i][j] == True
                q = deque()
                q.append([i,j])
                child = []
                is_break = 0
                dist = 1
                while q:
                    x, y = q.popleft()
                    for k in range(len(dx)):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or nx >= N or ny < 0 or ny >= M:
                            continue
                        if visited[nx][ny] == True:
                            continue
                        if board[nx][ny] == 1:
                            is_break = 1
                            break
                            new_dist = abs(nx-x) + abs(ny-y)
                            dist = max(dist, new_dist)
                            #is_break = 1
                        visited[nx][ny] = True
                        child.append([nx, ny])
                    if is_break == 1:
                        break
                    if len(q) == 0:
                        q.extend(child)
                        dist += 1
                        child = []
                if dist > answer:
                    answer = dist

        return answer
    
    return bfs(N, M, board)

if __name__ == "__main__":
    result = solution(N, M, board)
    print(result)