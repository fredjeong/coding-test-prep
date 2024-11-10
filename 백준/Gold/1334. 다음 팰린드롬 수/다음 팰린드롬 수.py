import sys
input = sys.stdin.readline

"""
가장 작은 팰린드롬 수를 구하는 것이므로 while문을 쓸 필요가 없다
예외처리만 잘 해주면 됨

고려해야 할 것:
    1) 홀수에서 짝수로 바뀌는 경우
    2) 짝수에서 홀수로 바뀌는 경우
"""

class Problem():
    def __init__(self):
        self.n = input().strip()

    def run(self):
        self.num = self.n
        if len(self.num) % 2 == 1:
            self.odd()
        else:
            self.even()

    def odd(self):
        if len(self.num) == 1:
            if self.num == "9":
                print("11")
                return
            else:
                print(str(int(self.num) + 1))
                return

        # 왼쪽을 뒤집은 수
        length = len(self.num)
        left = self.num[:length//2]
        middle = self.num[length//2]
        right = self.num[length//2 + 1:]
        left_reversed = left[::-1]
        if int(left_reversed) > int(right):
            self.num = left + middle + left_reversed
        else:
            # 가운데 수를 증가시킨다
            for i in range(length//2, -1, -1):
                if self.num[i] != "9":
                    self.num = self.num[:i] + str(int(self.num[i]) + 1) + self.num[i+1:]
                    left = self.num[:length // 2]
                    middle = self.num[length // 2]
                    left_reversed = left[::-1]
                    self.num = left + middle + left_reversed
                    break
                else:
                    if i == 0:
                        self.num = "1" + "0"*length
                    else:
                        if self.num[i-1] == "9":
                            continue
                        else:
                            self.num = self.num[:i - 1] + str(int(self.num[i - 1]) + 1) + "0" * (len(self.num) - i)
                            left = self.num[:length // 2]
                            middle = self.num[length // 2]
                            left_reversed = left[::-1]
                            self.num = left + middle + left_reversed
                            break
        if len(self.num)%2 == 0:
            self.even()
        else:
            print(self.num)

    def even(self):
        # 왼쪽을 뒤집은 수
        length = len(self.num)
        left = self.num[:length//2]
        right = self.num[length//2:]
        left_reversed = left[::-1]
        if int(left_reversed) > int(right):
            self.num = left + left_reversed
        else:
            # 가운데 수를 증가시킨다
            for i in range(length//2-1, -1, -1):
                if self.num[i] != "9":
                    self.num = self.num[:i] + str(int(self.num[i]) + 1) + self.num[i+1:]
                    left = self.num[:length // 2]
                    left_reversed = left[::-1]
                    self.num = left + left_reversed
                    break
                else:
                    if i == 0:
                        self.num = "1" + "0"*length
                    else:
                        if self.num[i-1] == "9":
                            continue
                        else:
                            self.num = self.num[:i - 1] + str(int(self.num[i - 1]) + 1) + "0" * (len(self.num) - i)
                            left = self.num[:length // 2]
                            left_reversed = left[::-1]
                            self.num = left + left_reversed
                            break
        if len(self.num)%2 == 1:
            self.odd()
        else:
            print(self.num)

    def check(self, num):
        if int(num) <= int(self.n):
            return False

        # 문자열을 삽입하면 팰린드롬 수인지 확인
        for i in range(len(num)//2):
            if num[i] != num[len(num) - 1 - i]:
                return False

        return True

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()