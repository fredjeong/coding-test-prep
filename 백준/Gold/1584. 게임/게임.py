import sys
input = sys.stdin.readline

from collections import deque

class Problem():
    def __init__(self):
        self.board = [[0 for _ in range(501)] for _ in range(501)]

        self.n = int(input())
        for _ in range(self.n):
            x1, y1, x2, y2 = map(int, input().split())
            x1, x2 = min(x1, x2), max(x1, x2)
            y1, y2 = min(y1, y2), max(y1, y2)
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    self.board[i][j] = 1

        self.m = int(input())
        for _ in range(self.m):
            x1, y1, x2, y2 = map(int, input().split())
            x1, x2 = min(x1, x2), max(x1, x2)
            y1, y2 = min(y1, y2), max(y1, y2)
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    self.board[i][j] = 2

    def bfs(self):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        visited = [[False for _ in range(501)] for _ in range(501)]

        q = deque()
        q.append([0, 0, 0])

        while q:
            x, y, cum_hp = q.popleft()

            if x == 500 and y == 500:
                return cum_hp

            if visited[x][y]:
                continue
            visited[x][y] = True

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= 501 or ny < 0 or ny >= 501:
                    continue

                if visited[nx][ny]:
                    continue

                if self.board[nx][ny] == 2:
                    continue

                if self.board[nx][ny] == 1:
                    q.append([nx, ny, cum_hp + 1])
                else:
                    q.appendleft([nx, ny, cum_hp])

        return -1

def main():
    instance = Problem()
    print(instance.bfs())

if __name__ == "__main__":
    main()