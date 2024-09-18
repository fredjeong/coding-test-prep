import sys

input = sys.stdin.readline

arr = set(int(input())%42 for _ in range(10))
print(len(arr))