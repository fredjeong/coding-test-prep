import sys
input = sys.stdin.readline

from collections import deque

class Problem():
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.board = [input().strip() for _ in range(self.n)]
        self.max_dist = 0

    def run(self):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(self.n):
            for j in range(self.m):
                # 바다는 고려하지 않는다
                if self.board[i][j] == "W":
                    continue

                count = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx < 0 or nx >= self.n or ny < 0 or ny >= self.m:
                        continue
                    if self.board[nx][ny] == "W":
                        continue
                    count += 1
                if count > 2:
                    continue

                visited = [[False for _ in range(self.m)] for _ in range(self.n)]

                q = deque()
                q.append([i, j, 0])

                while q:
                    x, y, cum_dist = q.popleft()

                    if visited[x][y]:
                        continue
                    visited[x][y] = True

                    if cum_dist > self.max_dist:
                        self.max_dist = cum_dist

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or nx >= self.n or ny < 0 or ny >= self.m:
                            continue
                        if self.board[nx][ny] == "W":
                            continue
                        if visited[nx][ny]:
                            continue

                        q.append([nx, ny, cum_dist + 1])


def main():
    instance = Problem()
    instance.run()
    print(instance.max_dist)

if __name__ == "__main__":
    main()