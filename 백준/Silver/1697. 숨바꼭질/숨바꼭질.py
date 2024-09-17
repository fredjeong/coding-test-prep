import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

def solution(N, K):

    def bfs(N, K):
        count = 0
        q = deque()
        q.append(N)
        visited = set()
        child = []
        while q:
            x = q.popleft()
            if x == K:
                return count
            visited.add(x)
            arr = [x+1, x-1, 2*x]
            for nx in arr:
                if nx < 0 or nx > 100000:
                    continue
                if nx in visited:
                    continue
                else:
                    child.append(nx)
            if len(q) == 0:
                q.extend(child)
                count += 1
                child = []

    return bfs(N, K)

if __name__ == '__main__':
    result = solution(N, K)
    print(result)