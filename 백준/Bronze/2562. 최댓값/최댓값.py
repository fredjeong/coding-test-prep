import sys

input = sys.stdin.readline

N = 9
arr = [int(input()) for _ in range(N)]
print(max(arr))
print(arr.index(max(arr))+1)