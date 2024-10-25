import sys
input = sys.stdin.readline


class Problem():
    def __init__(self):
        self.w, self.h, self.f, self.c, self.x1, self.y1, self.x2, self.y2 = map(int, input().split())
        self.x1 += self.f
        self.x2 += self.f

    def run(self):
        if self.f <= self.w//2:
            # 페인트를 칠한 구역이 x=f 왼쪽 부분과 겹치지 않는 경우
            if self.x1 >= self.f * 2:
                area_1 = self.f * (self.h // (self.c+1))
                area_2 = (self.w - self.f*2) * (self.h // (self.c+1)) - (self.x2 - self.x1)*(self.y2 - self.y1)
            else:
                # 페인트를 칠한 구역이 x=f 왼쪽 부분과 모두 겹치는 경우
                if self.x2 <= self.f * 2:
                    area_1 = self.f * (self.h // (self.c+1)) - (self.x2 - self.x1)*(self.y2 - self.y1)
                    area_2 = (self.w - self.f*2) * (self.h // (self.c+1))
                # 페인트를 칠한 구역이 x=f 왼쪽 부분과 일부만 겹치는 경우
                else:
                    area_1 = self.f * (self.h // (self.c+1)) - (self.f*2 - self.x1)*(self.y2 - self.y1)
                    area_2 = (self.w - self.f*2) * (self.h // (self.c+1)) - (self.x2 - self.f*2)*(self.y2 - self.y1)
            total_area = (area_1 * 2 + area_2) * (self.c + 1)
        else:
            # 페인트를 칠한 구역이 라인 밖의 부분과 겹치지 않는 경우
            if self.x2 <= self.w:
                area_0 = (self.f*2 - self.w)*(self.h // (self.c+1))
                area_1 = (self.w - self.f) * (self.h // (self.c+1)) - (self.x2 - self.x1)*(self.y2 - self.y1)
            else:
                # 페인트를 칠한 구역이 라인 밖의 부분과 모두 겹치는 경우
                if self.x1 >= self.w:
                    area_0 = (self.f*2 - self.w)*(self.h // (self.c+1)) - (self.x2 - self.x1)*(self.y2 - self.y1)
                    area_1 = (self.w - self.f)*(self.h // (self.c+1))
                # 페인트를 칠한 구역이 라인 밖의 부분과 일부만 겹치는 경우
                else:
                    area_0 = (self.f*2 - self.w)*(self.h // (self.c+1)) - (self.x2 - self.w)*(self.y2 - self.y1)
                    area_1 = (self.w - self.f)*(self.h // (self.c+1)) - (self.w - self.x1)*(self.y2 - self.y1)

            total_area = (area_0 + area_1*2) * (self.c+1)

        print(total_area)

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()