import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.n = int(input())
        self.arr = list(map(int, input().split()))

    def run(self):
        d = 0
        max_d = 0

        while d < max(abs(max(self.arr)), abs(min(self.arr))):
            d += 1
            if self.check(d):
                max_d = max(max_d, d)

        print(max_d)

    def check(self, d):
        remainder = self.arr[0] % d
        for i in range(1, self.n):
            if self.arr[i] % d != remainder:
                return False
        return True

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()