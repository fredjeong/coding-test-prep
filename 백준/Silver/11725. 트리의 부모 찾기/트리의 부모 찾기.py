from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def solution(N, graph):
    node = 1
    q = deque()
    q.append(node)
    dic = {} # 자식:부모
    while q:
        cur = q.popleft()
        
        for next in graph[cur]:
            if next in dic:
                continue
            dic[next] = cur
            q.append(next)

    for i in range(2, N+1):
        print(dic[i])

if __name__ == "__main__":
    solution(N, graph)