import sys

input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+1)]

for i in range(1, N + 1):
    dp[i] = float(input())
    dp[i] = max(dp[i], dp[i - 1] * dp[i])

print('%.3f' % max(dp))