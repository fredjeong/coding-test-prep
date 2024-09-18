import sys

input = sys.stdin.readline

N, K = map(int, input().split())

result = []
arr = [i for i in range(1, N)]
idx = 0
visited = [False for _ in range(N)]
count = 1
while False in visited:
    if idx == N:
        idx = 0

    if visited[idx] == False:
        if count%K == 0:
            visited[idx] = True
            result.append(str(idx+1))
        count += 1
    
    idx += 1
    
print("<" + ", ".join(result) + ">")