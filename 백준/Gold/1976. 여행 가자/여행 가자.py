import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

arr = []

# 같은 도시를 여러 번 방문할 수 있다
graph = [list(map(int, input().split())) for _ in range(n)]


plans = list(map(lambda x: x-1, list(map(int, input().split()))))
visited_dic = {}
for city in plans:
    visited_dic[city] = False
# 임의의 노드를 하나 꺼내서 보면 됨

answer = "NO"

q = deque()
q.append(plans[0])
visited = [False for _ in range(n)]
visited[plans[0]] = True
while q:
    cur_node = q.popleft()

    if cur_node in visited_dic:
        visited_dic[cur_node] = True
    if False not in visited_dic.values():
        answer = "YES"
        break

    for next_node in range(n):
        if graph[cur_node][next_node] and not visited[next_node]:
            q.append(next_node)
            visited[cur_node] = True

print(answer)