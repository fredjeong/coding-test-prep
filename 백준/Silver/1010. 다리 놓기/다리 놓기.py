import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    dp = [0 for _ in range(N+1)]
    dp[0] = 1
    dp[1] = M
    for i in range(2, N+1):
        dp[i] = int(dp[i-1] * (M-i+1) / i)
    print(dp[-1])