import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(len(arr))]
minimum = arr[0]

for i in range(1, N):
    num = arr[i]
    if num < minimum:
        minimum = num
    dp[i] = max(dp[i-1], num-minimum)


print(" ".join(map(str, dp)))