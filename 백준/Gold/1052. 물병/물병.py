import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.count = 0
        self.sizes = [0 for _ in range(25)]
        self.sizes[0] = self.n

    def run(self):
        while True:
            self.merge()
            if sum(self.sizes) <= self.k:
                print(self.count)
                return

            bonus = 2**(self.sizes.index(1))
            self.sizes[0] += bonus
            self.count += bonus

        print(-1)
        return

    def merge(self):
        for i in range(1, 25):
            self.sizes[i] += self.sizes[i-1]//2
            self.sizes[i-1] = self.sizes[i-1]%2

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()