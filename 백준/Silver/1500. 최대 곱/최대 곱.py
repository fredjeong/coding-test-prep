import sys

input = sys.stdin.readline

S, K = map(int, input().split())

arr = [S//K for _ in range(K)]

for i in range(S%K):
    arr[i] += 1

answer = 1
while arr:
    answer *= arr.pop()

print(answer)