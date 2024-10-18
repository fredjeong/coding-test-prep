import sys
input = sys.stdin.readline

from collections import defaultdict, deque

class Problem():
    def __init__(self):
        self.n = int(input())
        self.graphs = defaultdict(list)
        while True:
            arr = list(map(int, input().split()))
            if arr == [-1, -1]:
                break
            x = arr[0]
            y = arr[1]
            self.graphs[x].append(y)
            self.graphs[y].append(x)

        self.scores = [0 for _ in range(self.n+1)]
        self.scores[0] = 1e9

    def run(self):
        # 각 회원에 대해서
        for node in range(1, self.n+1):
            visited = [False for _ in range(self.n+1)]
            visited[0] = True
            q = deque()
            q.append(node)

            score = 0
            child = []
            while q:
                x = q.popleft()
                if visited[x]:
                    continue
                visited[x] = True

                for nx in self.graphs[x]:
                    if visited[nx]:
                        continue
                    if nx in q or nx in child:
                        continue
                    child.append(nx)

                if not q:
                    if False not in visited:
                        self.scores[node] = score
                        break
                    q.extend(child)
                    score += 1
                    child = []

def main():
    instance = Problem()
    instance.run()

    min_score = min(instance.scores)
    # 회장 후보의 점수와 후보의 수 출력
    print(min_score, instance.scores.count(min_score))

    # 회장 후보를 오름차순으로 모두 출력
    arr = [i for i in range(1, instance.n+1) if instance.scores[i]==min_score]
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    main()