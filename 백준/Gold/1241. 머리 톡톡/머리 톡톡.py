import sys
input = sys.stdin.readline

from collections import defaultdict

class Problem():
    def __init__(self):
        self.n = int(input())
        self.dic = defaultdict(int)
        self.arr = []
        for _ in range(self.n):
            num = int(input())
            self.dic[num] += 1
            self.arr.append(num)


    def run(self):
        s = set(self.dic.keys())
        new_dic = defaultdict(int)
        for num in self.arr:
            count = 0
            for i in s & self.get_divisors(num):
                count += self.dic[i]
            print(count - 1)

    def get_divisors(self, num):
        arr = set()
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                arr.add(i)
                if (i**2) != num:
                    arr.add(num // i)
        return arr

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()