s = input().strip()
n = int(input())
arr = set()
for _ in range(n):
    arr.add(input().strip())

length = len(s)
dp = [0 for _ in range(length+1)]

dp[0] = 1
for i in range(length):
    if not dp[i]:
        continue
    for word in arr:
        if s[i:i+len(word)] == word:
            dp[i+len(word)] = 1

print(dp[-1])