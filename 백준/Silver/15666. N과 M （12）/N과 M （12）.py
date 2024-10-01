import sys

input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))

visited = []

def dfs(idx, count, arr):
    global visited
    if count==m:
        if arr in visited:
            return
        else:
            visited.append(arr)
            return
    for idx in range(n):
        if arr[-1] > seq[idx]:
            continue
        else:
            dfs(idx, count + 1, arr + [seq[idx]])

for idx in range(n):
    dfs(idx, 1, [seq[idx]])

visited.sort()
for elem in visited:
    string = " ".join(map(str, elem))
    print(string)