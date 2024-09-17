import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = deque(sorted(arr, key=lambda x:(x[1], x[0], x[1]-x[0])))

count = 1
next_available_time = arr.popleft()[1]
while arr:
    start, end = arr.popleft()
    if start < next_available_time:
        continue
    count += 1
    next_available_time = end
    
print(count)