import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.x, self.y = map(int, input().split())

    def run(self):
        obj = self.y - self.x

        if obj == 0:
            print(0)
            return

        num = int(obj**0.5)

        if obj == num**2:
            print(2 * num - 1)
        elif num**2 < obj <= num**2 + num:
            print(2 * num)
        elif num**2 + num < obj < (num+1)**2:
            print(2 * num + 1)

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()