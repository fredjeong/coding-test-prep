from collections import deque

def solution(h, w, board):
    visited = [[False for _ in range(w)] for _ in range(h)]

    def bfs(h, w):
        count = 0
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        for row in range(h):
            for col in range(w):
                if board[row][col] == ".":
                    continue
                x, y = row, col
                
                if visited[x][y] == True:
                    continue
                visited[x][y] = True

                q = deque()
                q.append([x, y])

                while q:
                    x, y = q.popleft()

                    for i in range(len(dx)):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if nx < 0 or nx >= h or ny < 0 or ny >= w:
                            continue
                        if board[nx][ny] == ".":
                            continue
                        if visited[nx][ny] == False:
                            visited[nx][ny] = True
                            q.append([nx, ny])
                count += 1

        return count         

    return bfs(h, w)

T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    board = []
    for _ in range(h):
        board.append(input()[:w])
    if __name__ == "__main__":
        result = solution(h, w, board)
        print(result)
    
