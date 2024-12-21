import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 연속적인 k일의 온도의 합이 최대가 되는 값을 출력

sum_val = sum(arr[:k])
maximum = sum_val
for i in range(n-k):
    sum_val -= arr[i]
    sum_val += arr[i+k]
    maximum = max(maximum, sum_val)

print(maximum)