import sys

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0 for _ in range(i+1)] for i in range(n)]
dp[0] = [1]

for i in range(1, n):
    dp[i][0] = 1
    dp[i][-1] = 1
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[-1][k-1])