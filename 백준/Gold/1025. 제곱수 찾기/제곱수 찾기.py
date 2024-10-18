import sys
input = sys.stdin.readline

from collections import deque

class Problem():
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.board = [input().strip() for _ in range(self.n)]

        self.max_val = -1

    def run(self):
        for i in range(self.n):
            for j in range(self.m):
                # 하나의 좌표 선택
                self.bfs(i, j)

    def bfs(self, row, col):
        # 행 공차와 열 공차를 모두 설정해줘야 한다
        for a_row in range(-8, 9, 1):
            for a_col in range(-8, 9, 1):
                if a_row == 0 and a_col == 0:
                    continue

                q = deque()
                q.append([row, col, self.board[row][col]])

                while q:
                    x, y, stack = q.popleft()

                    # 현재까지 구한 수가 완전제곱수라면 최댓값 업데이트
                    if int(int(stack) ** 0.5) == int(stack) ** 0.5:
                        self.max_val = max(int(stack), self.max_val)

                    nx = x + a_row
                    ny = y + a_col

                    # 다음에 올 수가 격자를 벗어나면 더 이상 검토하지 않는다
                    if nx < 0 or nx >= self.n or ny < 0 or ny >= self.m:
                        continue
                    q.append([nx, ny, stack + self.board[nx][ny]])

def main():
    instance = Problem()
    instance.run()
    print(instance.max_val)

if __name__ == "__main__":
    main()