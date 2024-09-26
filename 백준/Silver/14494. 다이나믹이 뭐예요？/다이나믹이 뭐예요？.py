import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    dp[i][0] = 1
for j in range(m):
    dp[0][j] = 1

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1])%1000000007

print(dp[-1][-1])