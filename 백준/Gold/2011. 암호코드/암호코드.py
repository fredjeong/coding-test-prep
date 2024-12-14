import sys
input = sys.stdin.readline

n = list(map(int, list(input().strip())))
length_n = len(n)

if n[0] == 0:
    print(0)
else:
    dp = [0 for _ in range(length_n + 1)]
    dp[0] = dp[1] = 1

    for i in range(1, length_n):
        # 1자리 허용
        if n[i] > 0:
            dp[i+1] += dp[i]
        # 2자리 허용
        if 10 <= n[i-1]*10 + n[i] <= 26:
            dp[i+1] += dp[i-1]

    print(dp[-1] % 1000000)