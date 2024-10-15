import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.r, self.c = map(int, input().split())
        self.board = [input().strip() for _ in range(self.r)]
        self.max_dist = 1

    def bfs(self):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        q = set()
        q.add((0, 0, self.board[0][0]))

        while q:
            x, y, path = q.pop()

            self.max_dist = max(self.max_dist, len(path))

            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= self.r or ny < 0 or ny >= self.c:
                    continue
                if self.board[nx][ny] in path:
                    continue
                q.add((nx, ny, path + self.board[nx][ny]))

        return self.max_dist

def main():
    instance = Problem()
    print(instance.bfs())

if __name__ == "__main__":
    main()