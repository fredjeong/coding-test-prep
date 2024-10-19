import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.n = int(input())
        # 가장 큰 수는 9876543210이다
        self.count = 0

    def run(self):
        if self.n > 1022:
            return -1
        # 자릿수
        for i in range(1, 11):
            num = ""
            for j in range(i):
                num = str(j) + num

            while len(num) == i:
                do_break = False
                for k in range(i-1):
                    if int(num[k]) <= int(num[k+1]):
                        # 문제가 생긴 k번째 자릿수의 숫자를 하나 증가시키고 나머지 모든 수는 0으로 맞춰준다
                        num = num[:k] + str(int(num[k])+1) + str(0)*(i-1-k)
                        do_break = True
                        break
                if do_break:
                    continue
                else:
                    if self.count == self.n:
                        return num

                    num = str(int(num) + 1)
                    self.count += 1

def main():
    instance = Problem()
    print(instance.run())

if __name__ == "__main__":
    main()