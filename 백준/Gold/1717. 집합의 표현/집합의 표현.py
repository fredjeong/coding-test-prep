import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.n, self.m = map(int, input().split())
        # 집합이 아니라 문자열로 관리하는게 나을 수도 있다
        self.graph = [i for i in range(self.n + 1)]

    def run(self):
        for _ in range(self.m):
            order, a, b = map(int, input().split())
            # 합집합 연산
            if order == 0:
                self.union(a, b)
            else:
                if self.find(a) == self.find(b):
                    print("YES")
                else:
                    print("NO")
        print(self.graph)


    def find(self, x):
        while self.graph[x] != x:
            x = self.graph[x]
        return x

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx > ry:
            self.graph[ry] = rx
        else:
            self.graph[rx] = ry


def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()