import sys

input = sys.stdin.readline

class Solution():
    def __init__(self):
        self.visited = [[False for _ in range(5)] for _ in range(5)]
        self.board = []
        for _ in range(5):
            self.board.append(list(map(int, input().split())))

        self.call = []
        for _ in range(5):
            self.call += list(map(int, input().split()))

    def check(self):
        count = 0
        # 가로 줄
        for row in self.visited:
            if False not in row:
                count += 1

        # 세로 줄
        for col in range(5):
            if False not in [self.visited[i][col] for i in range(5)]:
                count += 1

        # 대각 두 줄
        if False not in [self.visited[row][row] for row in range(5)]:
            count += 1
        if False not in [self.visited[row][4 - row] for row in range(5)]:
            count += 1

        if count >= 3:
            return True

        return False

    def run(self):
        for count in range(25):
            num = self.call[count]
            for row in range(5):
                if num in self.board[row]:
                    col = self.board[row].index(num)
                    self.visited[row][col] = True
            if self.check():
                print(count+1)
                return

if __name__ == "__main__":
    instance = Solution()
    instance.run()