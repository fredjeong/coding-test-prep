import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(m):
    temp = list(map(int, input().split()))
    temp[0] -= 1
    temp[1] -= 1
    arr.append(temp)

dic = {}
for i in range(n):
    dic[i] = [0 for _ in range(n)]

def bfs(start, end):
    q = deque()
    visited = [False for _ in range(n)]
    q.append(start)
    visited[start] = True
    count = 0
    child = []
    while q:
        target = q.popleft()
        if target == end:
            break
        for graph in arr:
            if target not in graph:
                continue
            if target == graph[0]:
                new = graph[1]
            elif target == graph[1]:
                new = graph[0]
            if visited[new]==True:
                continue

            visited[new]=True
            child.append(new)

        if not q:
            q.extend(child)
            count += 1
            child = []
    return count

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        dic[i][j] = bfs(i, j)

for key in dic.keys():
    dic[key] = sum(dic[key])

result = sorted(list(dic.items()), key=lambda x:x[1])
print(result[0][0]+1)