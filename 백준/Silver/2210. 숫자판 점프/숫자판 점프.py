import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.board = [list(map(int, input().split())) for _ in range(5)]
        self.result = set()

        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]

    def dfs(self, x, y, string):
        if len(string) == 6:
            self.result.add(string)
            return

        for i in range(4):
            nx = x + self.dx[i]
            ny = y + self.dy[i]

            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            self.dfs(nx, ny, string + str(self.board[nx][ny]))

def main():
    instance = Problem()
    for i in range(5):
        for j in range(5):
            instance.dfs(i, j, str(instance.board[i][j]))
    print(len(instance.result))

if __name__ == "__main__":
    main()