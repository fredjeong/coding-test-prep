import sys
input = sys.stdin.readline

from collections import defaultdict

class Problem():
    def __init__(self):
        self.m = int(input())
        self.arr = input().strip()

    def run(self):
        length = self.m
        minimum = 1e9

        while length > 0:
            count = 0

            for idx in range(length):
                temp = self.arr[idx::length]

                # 각 원소의 개수
                dic = defaultdict(int)
                for char in temp:
                    dic[char] += 1

                vals = dic.values()
                count += sum(vals) - max(vals)
            minimum = min(minimum, count)

            length -= 1

        print(minimum)

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()