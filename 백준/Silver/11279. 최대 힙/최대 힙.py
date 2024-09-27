import sys
import heapq

input = sys.stdin.readline

N = int(input())

q = []
heapq.heapify(q)

for _ in range(N):
    num = int(input())
    if num>0:
        heapq.heappush(q, -1*num)
    elif num==0:
        if q:
            temp = heapq.heappop(q)
            print(-1*temp)
        else:
            print(0)