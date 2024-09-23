import sys

input = sys.stdin.readline

n = int(input())

if n==1:
    print(-1)
elif n==2:
    print(1)
elif n==3:
    print(-1)
elif n==4:
    print(2)
elif n==5:
    print(1)
else:
    dp = [[0, 0] for _ in range(n+1)]

    dp[2] = [1, 0]
    dp[4] = [2, 0]
    dp[5] = [0, 1]

    for i in range(6, n+1):
        if i%2 == 0:
            dp[i][0] = dp[i-2][0] + 1
            dp[i][1] = dp[i-2][1]
            if dp[i][0]==5:
                dp[i][0] -= 5
                dp[i][1] += 2
        else:
            dp[i][0] = dp[i-2][0] + 1
            dp[i][1] = dp[i-2][1]
            if dp[i][0]==5:
                dp[i][0] -= 5
                dp[i][1] += 2
    if dp[-1] == [0, 0]:
        print(-1)
    else:
        print(sum(dp[-1]))