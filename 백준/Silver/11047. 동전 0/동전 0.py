import sys

input = sys.stdin.readline

N, K = map(int, input().split())

arr = []
for _ in range(N):
    num = int(input())
    if num > K:
        continue
    arr.append(num)

count = 0
while K > 0:
    num = arr.pop()
    count += K // num
    K %= num

print(count)