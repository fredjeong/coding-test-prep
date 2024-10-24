import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.n = int(input())
        self.arr = list(map(int, input().split()))

        a, b, c, d, e, f = self.arr
        self.one_side_score = min(self.arr)
        self.two_sides_score = min(d+a, d+b, d+f, d+e, a+b, b+f, f+e, e+a, a+c, b+c, f+c, e+c)
        self.three_sides_score = min(b+a+c, a+e+c, e+f+c, f+b+c, b+a+d, a+e+d, e+f+d, f+b+d)

    def run(self):
        one_side = (self.n - 2)**2 * 5 + (self.n - 2)*4
        two_sides = 4 + (self.n - 2) * 4 + (self.n - 2) * 4
        three_sides = 4
        return one_side * self.one_side_score + two_sides * self.two_sides_score + three_sides * self.three_sides_score

def main():
    instance = Problem()
    if instance.n == 1:
        print(sum(instance.arr) - max(instance.arr))
        return
    print(instance.run())

if __name__ == "__main__":
    main()