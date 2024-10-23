import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.n = int(input())
        alphabets = "ABCDEFGHI"
        self.board = []
        for _ in range(self.n):
            arr = list(input().strip())
            for i in range(self.n):
                if arr[i].isdigit():
                    arr[i] = int(arr[i])
                else:
                    arr[i] = -1 * (alphabets.index(arr[i]) + 1)
            self.board.append(arr)

        self.min_score = 1e9
        self.max_score = -1e9

        self.visited = [[False for _ in range(self.n)] for _ in range(self.n)]

    def choose(self, x, y, count, history, visited_):
        visited = [visited_[row][:] for row in range(self.n)]

        if x == self.n - 1:
            # 사이클 그룹 구하기
            self.cycle_group = []
            for idx in range(len(history)):
                self.get_cycle(history, [], idx, [False for _ in range(len(history))])

            # 점수 계산
            if len(self.cycle_group) % 2 == 0:
                score = -1
            else:
                score = 1

            for i, j in history:
                score *= self.board[i][j]

            if score < self.min_score:
                self.min_score = score
            if score > self.max_score:
                self.max_score = score
            return

        for row in range(self.n):
            for col in range(self.n):
                if row == x or col == y:
                    visited[row][col] = True

        # 다음 행(x+1)에서 하나 고르기
        for j in range(self.n):
            if visited[x+1][j]:
                continue
            self.choose(x+1, j, count + 1, history + [[x+1, j]], visited)

    def get_cycle(self, history, cycle, idx, visited_):
        """
        history: 사이클을 만들 좌표들의 모임
        cycle_group: 완성된 사이클 그룹의 집합
        idx: 현재 보고 있는 history의 원소의 인덱스
        visited_: 방문한 인덱스
        """
        visited = visited_[:]
        visited[idx] = True

        if cycle:
            # A의 열과 B의 행이 같으면 추가
            if cycle[-1][1] == history[idx][0]:
                cycle.append(tuple(history[idx]))
        else:
            cycle.append(tuple(history[idx]))

        # 사이클을 이루는 첫 번째 도미노의 행과 마지막 도미노의 열이 같아야 한다
        if cycle[0][0] == cycle[-1][1]:
            if set(cycle) not in self.cycle_group:
                self.cycle_group.append(set(cycle))

        for i in range(len(history)):
            if visited[i]:
                continue
            self.get_cycle(history, cycle, i, visited)

def main():
    instance = Problem()
    for j in range(instance.n):
        instance.choose(0, j, 1, [[0, j]], instance.visited)

    print(instance.min_score)
    print(instance.max_score)

if __name__ == "__main__":
    main()