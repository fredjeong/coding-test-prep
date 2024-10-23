import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.n = int(input())
        self.board = [list(map(int, input().split())) for _ in range(self.n)]
        self.results = [0, 0, 0]

    def recursion(self, start_x, start_y, size):
        # 종이가 모두 같은 수로 채워졌는지 확인
        s = set()
        for row in range(start_x, start_x + size):
            s = s | set(self.board[row][start_y:start_y+size])
            if len(s) > 1:
                for i in range(start_x, start_x + size, size // 3):
                    for j in range(start_y, start_y + size, size // 3):
                        self.recursion(i, j, size // 3)
                return
        num = s.pop()
        self.results[num+1] += 1
        return

def main():
    instance = Problem()
    instance.recursion(0, 0, instance.n)
    for result in instance.results:
        print(result)

if __name__ == "__main__":
    main()