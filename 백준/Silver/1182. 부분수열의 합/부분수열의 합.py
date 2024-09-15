N, S = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
def dfs(idx, tot):
    global count

    if idx >= N:
        return

    tot += arr[idx]

    if tot == S:
        count += 1
    
    dfs(idx+1, tot)

    dfs(idx+1, tot - arr[idx])

dfs(0, 0)
print(count)