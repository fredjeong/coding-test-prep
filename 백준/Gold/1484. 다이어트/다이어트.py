import sys
input = sys.stdin.readline

import heapq

g = int(input())

arr = []
heapq.heapify(arr)

for i in range(1, int(g**0.5)+1):
    if g % i == 0:
        y = i # a - b
        if g//i != g/i:
            continue
        x = g//i # a + b

        if (x+y)//2 != (x+y)/2:
            continue

        a = (x + y)//2
        b = (x - y)//2

        if b == 0:
            continue
        heapq.heappush(arr, a)

if not arr:
    print(-1)
else:
    while arr:
        print(heapq.heappop(arr))
