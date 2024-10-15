import sys
input = sys.stdin.readline

from collections import deque

class Problem():
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.board = [list(map(int, input().split())) for _ in range(self.n)]
        self.visited = [[False for _ in range(self.m)] for _ in range(self.n)]
        self.dx = [1, -1, 0, 0, 1, 1, -1, -1]
        self.dy = [0, 0, 1, -1, 1, -1, 1, -1]
        self.count = 0

    def run(self):
        for i in range(self.n):
            for j in range(self.m):
                if self.visited[i][j]:
                    continue
                s = set()

                height = self.board[i][j]

                q = deque()
                q.append([i, j])

                while q:
                    x, y = q.popleft()
                    if self.visited[x][y]:
                        continue
                    self.visited[x][y] = True
                    s.add((x, y))

                    for k in range(len(self.dx)):
                        nx = x + self.dx[k]
                        ny = y + self.dy[k]

                        if nx < 0 or nx >= self.n or ny < 0 or ny >= self.m:
                            continue
                        if self.visited[nx][ny]:
                            continue
                        if self.board[nx][ny] == height:
                            q.append([nx, ny])

                if self.can_add_check(s, height):
                    self.count += 1

    def can_add_check(self, s, height):
        for x, y in s:
            for k in range(len(self.dx)):
                nx = x + self.dx[k]
                ny = y + self.dy[k]

                if nx < 0 or nx >= self.n or ny < 0 or ny >= self.m:
                    continue
                if self.board[nx][ny] == height:
                    continue
                if self.board[nx][ny] > height:
                    return False
        return True


def main():
    instance = Problem()
    instance.run()
    print(instance.count)

if __name__ == "__main__":
    main()