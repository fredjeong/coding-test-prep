from collections import deque

N = int(input())
graph = []
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph.append([[a,b], c])

def solution(N, graph):

    def bfs(N, graph):
        visited = [False for _ in range(N)]
        dist = [0 for _ in range(N)]
        node = 1
        visited[0] = True
        q = deque()
        q.append(node)
        while q:
            cur = q.popleft()

            for i in range(N-1):
                if graph[i][0][0] == cur:
                    new = graph[i][0][1]
                    score = graph[i][1]
                
                elif graph[i][0][1] == cur:
                    new = graph[i][0][0]
                    score = graph[i][1]
                else:
                    continue

                if visited[new-1] == True:
                    continue
                visited[new-1] = True

                dist[new-1] += dist[cur-1] + score
                q.append(new)
        
        return max(dist)

    return bfs(N, graph)

if __name__ == "__main__":
    result = solution(N, graph)
    print(result)
