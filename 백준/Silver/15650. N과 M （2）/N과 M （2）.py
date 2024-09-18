import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = [i for i in range(1, N+1)]

result = []

def dfs(start, saved, count, arr):
    if count == M-1:
        result.append(saved + [start])

    else:
        for i in range(len(arr)):
            dfs(arr[i], saved + [start], count+1, arr[i+1:])

for i in range(N-M+1):
    dfs(lst[i], [], 0, lst[i+1:])

for elem in result:
    print(" ".join(map(str, elem)))