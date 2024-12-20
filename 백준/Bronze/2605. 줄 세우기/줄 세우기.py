import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
arr = []

for person, num in enumerate(nums):
    if num > len(arr):
        arr.append(person+1)
    else:
        arr.insert(num, person+1)

print(" ".join(map(str, arr[::-1])))