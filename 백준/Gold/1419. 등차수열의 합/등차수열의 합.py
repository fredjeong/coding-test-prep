import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.l = int(input())
        self.r = int(input())
        self.k = int(input())

    def run(self):
        if self.k % 2 == 0:
            if self.l * 2 / self.k == int(self.l * 2 / self.k):
                a = int(self.l * 2 / self.k)
            else:
                a = int(self.l * 2 / self.k) + 1
            a = max(a, 2 + self.k - 1)

            b = int(self.r * 2 / self.k)

            if b < a:
                print(0)
                return
            else:
                count = b - a + 1
                if self.k == 4 and a <= 6 <= b:
                    count -= 1
                print(count)
                return
        else:
            if self.l / self.k == int(self.l / self.k):
                a = int(self.l / self.k)
            else:
                a = int(self.l / self.k) + 1
            a = max(a, int(1 + ((self.k - 1)/2)))

            b = int(self.r / self.k)

            if b < a:
                print(0)
                return
            else:
                count = b - a + 1
                print(count)
                return

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()