import sys
import heapq

input = sys.stdin.readline

N = int(input())

q = []
heapq.heapify(q)

for _ in range(N):
    num = int(input())
    if num==0:
        if q:
            temp = heapq.heappop(q)
            print(temp[0]*temp[1])
        else:
            print(0)
    else:
        if num>0:
            heapq.heappush(q, [num, 1])
        else:
            heapq.heappush(q, [abs(num), -1])