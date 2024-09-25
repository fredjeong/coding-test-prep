import sys

input = sys.stdin.readline

T = int(input())
dp = [1, 1]
length = len(dp)
for t in range(1, T+1):
    p, q = map(int, input().split())
    if p==1 or p==2:
        print(f"Case #{t}: {1%q}")
        continue
    if p <= length:
        print(f"Case #{t}: {dp[p-1]%q}")
    else:
        while p > length:
            dp.append(dp[-1]+dp[-2])
            length += 1
        print(f"Case #{t}: {dp[p-1]%q}")