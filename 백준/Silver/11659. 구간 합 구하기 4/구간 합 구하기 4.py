import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
sums = [0 for _ in range(N)]
sums[0] = arr[0]

for i in range(1, N):
    sums[i] = sums[i-1] + arr[i]

for _ in range(M):
    start, end = map(int, input().split())
    start -= 1 
    end -= 1
    if start == end:
        print(arr[start])
    else:
        if start == 0:
            print(sums[end])
        else:
            print(sums[end] - sums[start-1])