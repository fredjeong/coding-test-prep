import sys

input = sys.stdin.readline

N = int(input())

if N==0 or N==1:
    print(1)
else:
    dp = [0 for _ in range(N+1)]
    dp[0] = 1
    dp[1] = 1

    for i in range(2, N+1):
        dp[i] = (dp[i-1] + dp[i-2] + 1)%1000000007
    print(dp[-1])