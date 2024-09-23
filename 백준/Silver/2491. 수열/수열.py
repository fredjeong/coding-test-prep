import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

if N==1:
    print(1)
elif N==1:
    print(2)
else:
    dp = [0 for _ in range(N)]
    dp[0] = 1
    dp[1] = 2

    if arr[1]>arr[0]:
        sign = "increasing"
        equal = 1
    elif arr[1]<arr[0]:
        sign = "decreasing"
        equal = 1
    else:
        sign = "neutral"
        equal = 2
    stack = 2

    for i in range(2, N):
        if sign=="increasing":
            if arr[i]>arr[i-1]:
                equal = 1
                stack += 1
                dp[i]=max(dp[i-1], stack)
            elif arr[i]<arr[i-1]:
                sign = "decreasing"
                dp[i] = max(dp[i-1], equal+1)
                stack = equal+1
                equal = 1
            else:
                equal += 1
                stack += 1
                dp[i] = max(dp[i-1], stack)
        elif sign=="decreasing":
            if arr[i]<arr[i-1]:
                equal = 1
                stack += 1
                dp[i] = max(dp[i-1], stack)
            elif arr[i]>arr[i-1]:
                sign = "increasing"
                dp[i] = max(dp[i-1], equal+1)
                stack = equal+1
                equal = 1
            else:
                equal += 1
                stack += 1
                dp[i] = max(dp[i-1], stack)
        elif sign=="neutral":
            if arr[i]>arr[i-1]:
                sign = "increasing"
                stack += 1
                equal = 1
                dp[i] = max(dp[i-1], stack)
            elif arr[i]<arr[i-1]:
                sign = "decreasing"
                stack += 1
                equal = 1
                dp[i] = max(dp[i-1], stack)
            else:
                stack += 1
                equal += 1
                dp[i] = max(dp[i-1], stack)

    print(dp[-1])