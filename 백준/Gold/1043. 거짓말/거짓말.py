import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.n, self.m = map(int, input().split())

        arr = list(map(int, input().split()))

        self.no_case = False
        # 진실을 아는 사람이 없다면 모든 파티에서 거짓말을 할 수 있다
        if arr[0] == 0:
            self.no_case = True
            print(self.m)
            return

        # 진실을 아는 사람의 번호
        self.truth = set()
        for i in range(1, len(arr)):
            self.truth.add(arr[i])

        self.parties = []
        for _ in range(self.m):
            arr = list(map(int, input().split()))
            self.parties.append(set(arr[1:]))

        self.impossible = [False for _ in range(self.m)] # 거짓말을 할 수 없는 파티

        """
        1. self.truth에 있는 사람들이 속한 곳에서는 진실만을 말해야 한다
        2. 진실만을 말하는 파티에 참석한 사람들이 참석하는 다른 파티에서도 진실만을 말해야 한다
        3. 그 사람들이 참석하는 다른 파티에서도 진실만을 말해야 한다.
        """
        while True:
            new_truth = self.truth
            for idx in range(self.m):
                if self.impossible[idx]:
                    continue

                # 겹치는 게 있다면
                if self.parties[idx] & self.truth:
                    self.impossible[idx] = True
                    new_truth = new_truth | self.parties[idx]

            if new_truth == self.truth:
                break
            self.truth = new_truth

        count = self.impossible.count(False)
        print(count)

def main():
    instance = Problem()
    if instance.no_case:
        return

if __name__ == "__main__":
    main()