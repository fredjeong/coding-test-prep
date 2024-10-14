import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.n = int(input()) # 크레인의 개수
        self.weight_limit = sorted(list(map(int, input().split())), reverse = True) # 각 크레인의 무게 제한
        self.m = int(input()) # 박스의 개수
        self.box = sorted(list(map(int, input().split()))) # 각 박스의 무게
        self.time = 1

    def main(self):
        # 가장 무게 제한이 높은 크레인으로도 현재 박스를 옮길 수 없다면 -1을 출력
        if self.box[-1] > self.weight_limit[0]:
            print(-1)
            return

        while True:
            temp = []
            # 모든 크레인은 동시에 움직인다
            for i in range(self.n):
                while self.box:
                    # 큐에서 박스를 하나 뽑는다
                    box = self.box.pop()

                    # i번째 크레인으로 그 박스를 들 수 있다면 그 박스는 사라진다
                    if box <= self.weight_limit[i]:
                        break
                    # 만약 현재 크레인으로 그 박스를 들 수 없다면 다른 박스를 보자
                    else:
                        temp.append(box)

            self.box = sorted(self.box + temp)

            # 더 이상 옮길 박스가 없다면 모든 과정을 종료하고 시간을 출력한다
            if not self.box and not temp:
                print(self.time)
                return

            self.time += 1

if __name__ == "__main__":
    instance = Problem()
    instance.main()