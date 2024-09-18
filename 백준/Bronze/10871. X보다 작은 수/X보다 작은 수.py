import sys

input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))

result = []
for num in arr:
    if num < X:
        result.append(num)

print(" ".join(map(str, result)))