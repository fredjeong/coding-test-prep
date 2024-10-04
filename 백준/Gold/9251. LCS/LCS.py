import sys

input = sys.stdin.readline

string_1 = input().strip()
string_2 = input().strip()

n = len(string_1)
m = len(string_2)

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        if string_1[i]==string_2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[n][m])