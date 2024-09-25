import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    num = int(input())
    if num <= 3:
        print(1)
        continue
    elif num <= 5:
        print(2)
        continue
    dp = [1, 1, 1, 2, 2]
    for i in range(5, num):
        dp.append(dp[i-1] + dp[i-5])
    print(dp[-1])