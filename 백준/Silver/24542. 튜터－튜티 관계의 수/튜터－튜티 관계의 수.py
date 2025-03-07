import sys
input = sys.stdin.readline


from collections import defaultdict, deque

def bfs(node, graph):
    global visited
    q = deque()
    q.append(node)
    visited[node] = True
    cnt = 1

    while q:
        cur_node = q.popleft()
        for next_node in graph[cur_node]:
            if visited[next_node]:
                continue
            visited[next_node] = True
            cnt += 1

            q.append(next_node)

    return cnt


graph = defaultdict(list)
n, m = map(int, input().split())
visited = [False for _ in range(n+1)]
answer = 1
mod = 1000000007

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for node in range(1, n+1):
    if visited[node]:
        continue

    answer *= bfs(node, graph)
    answer %= mod

print(answer)