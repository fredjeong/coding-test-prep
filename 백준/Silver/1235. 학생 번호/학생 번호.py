import sys

input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]

idx = -1
while idx <= len(arr[0]):
    s = set()
    for i in range(n):
        s.add(arr[i][idx:])
    if len(s) != n:
        idx -= 1
    else:
        print(abs(idx))
        break