import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.n = int(input())
        self.x = list(map(int, input().split()))
        self.answers = []

    def recursion(self, seq_, idx_1, idx_2, visited_):
        """
        idx_1: 수열 S에서의 자릿수
        idx_2: 집합 X에서의 자릿수
        """
        seq = seq_[:]
        visited = visited_[:]

        num = self.x[idx_2]
        visited[idx_2] = True
        seq[idx_1] = num

        if idx_1 + seq[idx_1] + 1 >= self.n * 2:
            return
        seq[idx_1 + seq[idx_1] + 1] = num

        if -1 not in seq:
            self.answers.append(seq)
            return

        # 아직 채워지지 않은 곳을 보자
        new_idx_1 = seq.index(-1)

        for new_idx_2 in range(self.n):
            if visited[new_idx_2]:
                continue
            else:
                self.recursion(seq, new_idx_1, new_idx_2, visited)

    def run(self):
        seq = [-1 for _ in range(self.n * 2)]
        visited = [False for _ in range(self.n)]
        for idx_2 in range(self.n):
            self.recursion(seq, 0, idx_2, visited)

def main():
    instance = Problem()
    instance.run()

    if not instance.answers:
        print(-1)
        return

    instance.answers.sort()
    answer = instance.answers[0]
    print(" ".join(map(str, answer)))

if __name__ == "__main__":
    main()