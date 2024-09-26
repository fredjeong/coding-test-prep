import sys

input = sys.stdin.readline

N = int(input())

if N==0:
    print(0)
elif N in [1, 2, 5, 7]:
    print(1)
elif N in [3, 4, 6]:
    print(2)
else:
    dp = [0 for _ in range(N+1)]
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    dp[4] = 2
    dp[5] = 1
    dp[6] = 2
    dp[7] = 1

    for i in range(8, N+1):
        dp[i] = min(dp[i-1], dp[i-2], dp[i-5], dp[i-7])+1
    print(dp[-1])