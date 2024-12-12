import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())

s = set()
for _ in range(k):
    a, b, c, d = map(int, input().split())
    s.add(((b, a), (d, c)))
    s.add(((d, c), (b, a)))

dp = [[0] * (n + 1) for _ in range(m + 1)]

# 초기값 설정
dp[0][0] = 1

for i in range(m + 1):
    for j in range(n + 1):
        if i > 0:  # 위쪽에서 오는 경로가 막혀있는지 확인
            if ((i, j), (i - 1, j)) not in s:
                dp[i][j] += dp[i - 1][j]
        if j > 0:  # 왼쪽에서 오는 경로가 막혀있는지 확인
            if ((i, j), (i, j - 1)) not in s:
                dp[i][j] += dp[i][j - 1]

print(dp[m][n])