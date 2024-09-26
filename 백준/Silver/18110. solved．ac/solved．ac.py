import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

if n==0:
    print(0)
else:
    rating = 0
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    
    arr = deque(arr)
    
    if n*0.15 - int(n*0.15) >= 0.5:
        temp = int(n*0.15) + 1
    else:
        temp = int(n*0.15)

    for _ in range(temp):
        arr.pop()
        arr.popleft()

    result = sum(arr)/(n-2*temp)
    if result - int(result) >= 0.5:
        result = int(result) + 1
    else:
        result = int(result)

    print(result)