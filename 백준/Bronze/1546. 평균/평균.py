import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

M = max(arr)

new_arr = []
for score in arr:
    new_arr.append(score/M * 100)

print(sum(new_arr)/N)