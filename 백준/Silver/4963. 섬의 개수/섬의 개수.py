import sys
from collections import deque

def solution(w, h, board):
    
    def bfs(w, h, board):
        count = 0
        visited = [[False for _ in range(w)] for _ in range(h)]
        
        land = []
        for i in range(h):
            for j in range(w):
                if board[i][j] == 1:
                    land.append([i,j])
        if len(land) == 0:
            return 0

        dx = [0, 0, 1, -1, 1, 1, -1, -1]
        dy = [1, -1, 0, 0, 1, -1, 1, -1]
        
        for i in land:
            x, y = i[0], i[1]
            if visited[x][y] == True:
                continue
            q = deque()
            q.append([x, y])

            while q:
                x, y = q.popleft()
                
                for i in range(len(dx)):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or nx >= h or ny < 0 or ny >= w:
                        continue

                    if visited[nx][ny] == False and board[nx][ny] == 1:
                        visited[nx][ny] = True
                        
                        q.append([nx, ny])
            count += 1
        
        return count           
            

    return bfs(w, h, board)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = [list(map(int, input().split())) for _ in range(h)]
    
    if __name__ == "__main__":
        result = solution(w, h, board)
        print(result)