import sys

input = sys.stdin.readline

R, C, W = map(int, input().split())

dp = [[0 for j in range(i+1)] for i in range(R+W-1)]

dp[0][0] = 1

for i in range(1, R+W-1):
    for j in range(i+1):
        if j==0 or j==i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

total = 0
for i in range(R-1, R-1+W):
    if i==R-1:
        total += dp[i][C-1]
    else:
        for j in range(C-1, C+i-R+1):
            total += dp[i][j]
print(total)