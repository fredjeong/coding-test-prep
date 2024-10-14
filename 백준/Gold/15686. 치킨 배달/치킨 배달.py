from collections import deque

class Problem():
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.board = [list(map(int, input().split())) for _ in range(self.n)]

        # 치킨집 후보 좌표
        self.candidates = []
        self.house_pos = []
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 2:
                    self.candidates.append([i, j])
                    #self.board[i][j] = 0
                elif self.board[i][j] == 1:
                    self.house_pos.append([i, j])

        self.chicken_pos = []
        self.combination([], 0)
        self.min_dist = 1e9

    # 조합을 사용해서 배치할 치킨집들을 골라야 한다
    def combination(self, new_arr, c):
        # len(self.candidates)개 중에서 self.m개를 고르는 것
        if len(new_arr) == self.m:
            self.chicken_pos.append(new_arr)
            return

        for idx in range(c, len(self.candidates)):
            self.combination(new_arr + [self.candidates[idx]], idx+1)

    def get_distance(self, pos_1, pos_2):
        return abs(pos_1[0] - pos_2[0]) + abs(pos_1[1] - pos_2[1])

    # chicken_pos 내의 모든 경우에 대해서 치킨 거리의 최솟값을 출력한다
    def run(self):
        for candidate in self.chicken_pos:
            global chicken_dist
            chicken_dist = 0

            for home_pos in self.house_pos:
                min_dist = 1e9
                for shop_pos in candidate:
                    dist = self.get_distance(home_pos, shop_pos)
                    if dist < min_dist:
                        min_dist = dist
                chicken_dist += min_dist

            if chicken_dist < self.min_dist:
                self.min_dist = chicken_dist

def main():
    instance = Problem()
    instance.run()
    print(instance.min_dist)

if __name__ == "__main__":
    main()