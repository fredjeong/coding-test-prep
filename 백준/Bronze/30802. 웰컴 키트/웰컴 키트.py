import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
T, P = map(int, input().split())

shirts = 0
for i in range(len(arr)):
    if arr[i] == 0:
        continue
    else:
        shirts += (arr[i]-1) // T + 1

quotient = 0
remainder = 0
if sum(arr) != 0:
    quotient += sum(arr) // P
    remainder = sum(arr) - quotient*P

print(shirts)
print(quotient, remainder)