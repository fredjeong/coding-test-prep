import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = set(map(int, input().split()))
M = int(input())
candidates = deque(list(map(int, input().split())))

while candidates:
    candidate = candidates.popleft()
    if candidate in arr:
        print(1)
    else:
        print(0)