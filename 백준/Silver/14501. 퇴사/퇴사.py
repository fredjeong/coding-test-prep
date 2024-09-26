import sys

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(N+1)]

if arr[N-1][0] == 1:
   dp[N-1] = arr[N-1][1]

for idx in range(N-2, -1, -1):
    if idx + arr[idx][0] > N:
      dp[idx] = dp[idx+1]
      continue
    dp[idx] = max(dp[idx + arr[idx][0]] + arr[idx][1], dp[idx+1])

print(dp[0])