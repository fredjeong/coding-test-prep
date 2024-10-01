import sys

input = sys.stdin.readline

n, m = map(int, input().split())

visited = set()

def dfs(num, count, arr):
    global visited
    if count==m:
        string = " ".join(map(str, arr))
        if string in visited:
            return
        else:
            visited.add(string)
            return
    
    for i in range(num, n+1):
        dfs(i, count + 1, arr + [num])

for i in range(1, n+1):
    dfs(i, 0, [])

visited = sorted(visited)
for elem in visited:
    print(elem)