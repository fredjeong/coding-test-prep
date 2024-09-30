import sys

input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]
for i in range(1, int(n**0.5)+1):
    dp[i**2] = 1
    
for i in range(1, n+1):
    if dp[i] != 0:
        continue
    for j in range(1, int(i**0.5) + 1):
        if dp[i] == 0:
            dp[i] = dp[j**2] + dp[i-j**2]
        else:
            dp[i] = min(dp[i], dp[j**2] + dp[i-j**2])

print(dp[-1])