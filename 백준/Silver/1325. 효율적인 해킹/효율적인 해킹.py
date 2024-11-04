import sys
input = sys.stdin.readline

from collections import deque

class Problem():
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.graph = [[] for _ in range(self.n + 1)]
        self.answer = []

        for _ in range(self.m):
            a, b = map(int, input().split())
            self.graph[b].append(a)

    def bfs(self, computer):
        q = deque()
        q.append(computer)
        visited = [False for _ in range(self.n + 1)]
        visited[computer] = True
        count = 1
        while q:
            x = q.popleft()
            for nx in self.graph[x]:
                if not visited[nx]:
                    q.append(nx)
                    visited[nx] = True
                    count += 1
        return count

    def run(self):
        maximum = 1
        for computer in range(1, self.n + 1):
            count = self.bfs(computer)
            if count > maximum:
                maximum = count
                self.answer = []
                self.answer.append(computer)
            elif count == maximum:
                self.answer.append(computer)

        print(*self.answer)

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()