import sys
input = sys.stdin.readline

from collections import deque

class Problem():
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.start_walk = self.n
        self.start_teleport = self.n

    def bfs(self):
        visited = [False for _ in range(1000001)]
        q = deque()
        q.append(self.n)
        time = 0

        child = []

        while q:
            x = q.popleft()
            if visited[x]:
                continue
            visited[x] = True

            if x == self.k:
                self.min_time = time
                return

            nx_1 = x - 1
            if nx_1 >= 0 and not visited[nx_1]:
                child.append(nx_1)

            if self.n < self.k:
                nx_2 = x + 1
                if nx_2 <= 1000000 and not visited[nx_2]:
                    child.append(nx_2)

                nx_3 = 2*x
                if 0 < nx_3 <= 1000000 and not visited[nx_3]:
                    q.append(nx_3)

            if not q:
                q.extend(child)
                child = []
                time += 1

def main():
    instance = Problem()
    instance.bfs()
    print(instance.min_time)

if __name__ == "__main__":
    main()