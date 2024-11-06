import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.n = int(input())
        self.scores = [float(input()) for _ in range(self.n)]

    def run(self):
        num = 1
        while True:
            if self.check(num):
                print(num)
                return
            num += 1

    def check(self, num):
        for score in self.scores:
            temp = round(num * score, 3)
            temp_2 = int(num * score)

            error = round(temp_2 - temp, 3)

            if error < 0:
                error = round(error + 1, 3)


            if round(error, 3) >= round(0.001 * num, 3):
                return False

        return True

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()