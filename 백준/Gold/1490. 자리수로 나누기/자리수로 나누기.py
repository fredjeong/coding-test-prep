import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.n = input().strip()
        self.s = set(map(int, list(self.n)))
        self.s.discard(0)

    def check(self, num):
        num = int(num)
        for i in self.s:
            if num % i != 0:
                return False
        return True

    def run(self):
        if self.check(self.n):
            print(self.n)
            return

        add_on = str(0)
        length = 1
        while True:
            num = self.n + add_on

            if self.check(num):
                print(num)
                return

            if set(list(add_on)) == {'9'}:
                length += 1
                add_on = "0" * length
            else:
                temp = str(int(add_on) + 1)
                add_on = "0" * (length - len(temp)) + temp

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()