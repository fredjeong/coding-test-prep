import sys
input = sys.stdin.readline

from collections import deque

class Problem():
    def __init__(self):
        self.board = [list(map(int, input().split())) for _ in range(5)]
        self.pos = list(map(int, input().split()))

        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]

        self.can = False

    def bfs(self):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        q = deque()
        q.append([self.pos, 0, 0, {(self.pos[0], self.pos[1])}])

        while q:
            [x, y], count, apple, visited = q.popleft()

            if self.board[x][y] == 1:
                apple += 1

            if apple == 2:
                print(1)
                return

            for i in range(4):
                nx = x + self.dx[i]
                ny = y + self.dy[i]

                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                    continue
                if self.board[nx][ny] == -1:
                    continue
                if (nx, ny) in visited:
                    continue
                if count < 3:
                    q.append([[nx, ny], count + 1, apple, visited | {(nx, ny)}])

        print(0)
        return

def main():
    instance = Problem()
    instance.bfs()

if __name__ == "__main__":
    main()