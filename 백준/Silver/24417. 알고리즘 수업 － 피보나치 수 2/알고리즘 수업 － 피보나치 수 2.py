import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.n = int(input())
        self.dp_count = (self.n - 2) % 1000000007

    def run(self):
        recursion_count = self.dp()
        print(recursion_count, self.dp_count)

    def dp(self):
        a = 1
        b = 1

        for _ in range(2, self.n):
            c = b
            b = (a + b)%1000000007
            a = c

        return b

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()