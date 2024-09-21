import sys

input = sys.stdin.readline

N, M = map(int, input().split())
seq = list(map(int, input().split()))

result = set()
def dfs(N, M, count, saved, arr):
    if count == M-1:
        for elem in arr:
            new = saved + " " + str(elem)
            new = new.strip()
            result.add(new)
    else:
        for i in range(len(arr)):
            temp = arr[:]
            del temp[i]
            dfs(N, M, count+1, saved + " " + str(arr[i]), temp)

dfs(N, M, 0, "", seq)

result = sorted(result, key=lambda x: list(map(int, x.split())))
for elem in result:
    print(elem)