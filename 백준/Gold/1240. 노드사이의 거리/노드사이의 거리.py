import sys
input = sys.stdin.readline

from collections import defaultdict, deque

class Problem():
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.dic = defaultdict(list)
        for _ in range(self.n - 1):
            start, end, dist = map(int, input().split())
            self.dic[start].append((end, dist))
            self.dic[end].append((start, dist))

    def bfs(self, start, end):
        visited = [False for _ in range(self.n+1)]

        q = deque()
        q.append((start, 0))

        while q:
            node, cum_dist = q.popleft()

            if visited[node]:
                continue
            visited[node] = True

            if node == end:
                return cum_dist

            for connected_node, dist in self.dic[node]:
                if visited[connected_node]:
                    continue
                q.append((connected_node, cum_dist + dist))

def main():
    instance = Problem()
    for _ in range(instance.m):
        start, end = map(int, input().split())
        print(instance.bfs(start, end))

if __name__ == "__main__":
    main()