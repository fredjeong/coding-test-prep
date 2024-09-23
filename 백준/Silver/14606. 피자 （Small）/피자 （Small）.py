import sys

input = sys.stdin.readline

n = int(input())

if n==1:
    print(0)
elif n==2:
    print(1)
else:
    dp = [0 for _ in range(n+1)]
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + i-1
    print(dp[-1])