import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

result = 0
for num in arr:
    result += num**2
result %= 10
print(result)