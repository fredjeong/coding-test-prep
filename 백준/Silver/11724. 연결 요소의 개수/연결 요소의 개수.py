from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(M)]

def solution(N, M, graph):
    visited = [False for _ in range(N)]
    
    def bfs(N, graph):
        count = 0

        for node in range(1, N+1):
            if visited[node-1] == True:
                continue
            
            visited[node-1] = True
            count += 1
            q = deque()
            q.append(node)

            while q:
                cur = q.popleft()

                for elem in graph:
                    if cur not in elem:
                        continue

                    if elem[0] == cur:
                        new = elem[1]
                        if visited[new-1] == True:
                            continue
                        visited[new-1] = True
                        q.append(new)
                    if elem[1] == cur:
                        new = elem[0]
                        if visited[new-1] == True:
                            continue
                        visited[new-1] = True
                        q.append(new)
        return count

    return bfs(N, graph)

if __name__ == "__main__":
    result = solution(N, M, graph)
    print(result)