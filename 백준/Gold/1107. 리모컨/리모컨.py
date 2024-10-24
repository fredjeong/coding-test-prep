import sys
input = sys.stdin.readline

from collections import deque

class Problem():
    def __init__(self):
        self.n = int(input())
        self.m = int(input())
        self.broken = [False for _ in range(10)]

        if self.m > 0:
            # 버튼이 + 또는 -인 경우도 생각해야 한다
            arr = list(input().split())
            for button in arr:
                self.broken[int(button)] = True


        self.buttons = set(str(button) for button in range(len(self.broken)) if not self.broken[button])

        self.channel = 100

    def get_channel(self, up):
        # 가장 근접한 수 찾기
        q = deque()
        q.append(self.n)

        while q:
            x = q.popleft()
            s = set(list(str(x)))

            if s & self.buttons == s:
                return x

            if len(str(x)) + len(str(x)) + abs(self.n - x) >= abs(self.n - self.channel):
                break

            if up == True:
                nx = x + 1
                q.append(nx)

            else:
                nx = x - 1
                if nx >= 0:
                    q.append(nx)
        return -1

    def run(self):
        down = self.get_channel(False)
        up = self.get_channel(True)

        if down != -1 and up != -1:
            answer = min(len(str(down)) + abs(self.n - down), len(str(up)) + abs(self.n - up), abs(self.n - self.channel))
        elif down != -1 and up == -1:
            answer = min(len(str(down)) + abs(self.n - down), abs(self.n - self.channel))
        elif down == -1 and up != -1:
            answer = min(len(str(up)) + abs(self.n - up), abs(self.n - self.channel))
        elif down == -1 and up == -1:
            answer = abs(self.n - self.channel)

        return answer

def main():
    instance = Problem()
    print(instance.run())

if __name__ == "__main__":
    main()