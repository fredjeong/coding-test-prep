import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
result = [[0 for _ in range(n)] for _ in range(n)]

def find(start, end):
    if graph[start][end] == 1:
        result[start][end] = 1
    visited = [False for _ in range(n)]
    q = deque()
    q.append(start)
    count = False
    while q:
        node = q.popleft()
        if node==end and count ==True:
            result[start][end]=1
            break
        count = True
        for i in range(n):
            if i==node:
                continue
            if graph[node][i]==1:
                if visited[i]==True:
                    continue
                visited[i] = True
                q.append(i)

for i in range(n):
    for j in range(n):
        find(i, j)

for line in result:
    print(" ".join(map(str, line)))