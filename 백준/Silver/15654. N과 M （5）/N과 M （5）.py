import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
result = []

def dfs(idx, saved, count, visited):
    check = visited[:]
    save = saved[:]
    if check[idx] == True:
        return
    check[idx] = True
    save.append(lst[idx])

    if False not in check or count == M-1:
        result.append(save)
        return 
    
    for i in range(len(lst)):
        dfs(i, save, count + 1, check)
    
visited = [False for _ in range(len(lst))]
for i in range(len(lst)):
    dfs(i, [], 0, visited)

for elem in result:
    print(" ".join(map(str, elem)))