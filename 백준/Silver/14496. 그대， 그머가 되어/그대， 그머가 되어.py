from collections import deque

a, b = map(int, input().split())
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x-1].append(y)
    graph[y-1].append(x)

def solution(a, b, N, M, graph):
    visited = [False for _ in range(N)]
    
    def bfs(a, b, N, M, graph):
        count = 0
        if a == b:
            return 0
        
        q = deque()
        q.append(a)
        visited[a-1] = True
        child = []
        while q:
            node = q.popleft()
            if node == b:
                return count

            for elem in graph[node-1]:
                if visited[elem-1] == True:
                    continue
                visited[elem-1] = True
                child.append(elem)

            if len(q) == 0:
                q.extend(child)
                count += 1
                child = []
        
        return -1
    
    return bfs(a, b, N, M, graph)

if __name__ == "__main__":
    result = solution(a, b, N, M, graph)
    print(result)