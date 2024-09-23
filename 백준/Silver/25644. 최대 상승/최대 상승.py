import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(N)]
min_price = arr[0]

for i in range(1, N):
    dp[i] = max(0, arr[i] - min_price, dp[i-1])
    if arr[i] < min_price:
        min_price = arr[i]
print(dp[-1])