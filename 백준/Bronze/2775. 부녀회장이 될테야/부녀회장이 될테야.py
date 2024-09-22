import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
    dp[0] = [i for i in range(n+1)]
    for i in range(1, k+1):
        for j in range(n+1):
            dp[i][j] = sum(dp[i-1][:j])+dp[i-1][j]
            
    print(dp[-1][-1])