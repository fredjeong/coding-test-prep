import sys

input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+1)]
arr = [0 for _ in range(N+1)]
for i in range(1, N+1):
    arr[i] = int(input())
if N==1:
    print(arr[1])
elif N==2:
    print(sum(arr[:3]))
else:
    dp[1] = arr[1]
    dp[2] = arr[1]+arr[2]
    for i in range(3, N+1):
        dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])

    print(dp[-1])