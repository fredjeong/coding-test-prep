import sys

input = sys.stdin.readline

N = int(input())

if N==3 or N==5:
    print(1)
elif N==4 or N==7:
    print(-1)
else:
    dp = [[0,0] for _ in range(N+1)]
    dp[3] = [1,0]
    dp[5] = [0,1]
    dp[6] = [2,0]
    for i in range(8, N+1):
        if i%5==0:
            dp[i] = [0, i//5]
            continue
        dp[i][0] = dp[i-3][0] + 1
        dp[i][1] = dp[i-3][1]
        if dp[i][0]==5:
            dp[i][1] += 3
            dp[i][0] = 0
    if dp[-1]==[0,0]:
        print(-1)
    else:
        print(sum(dp[-1]))