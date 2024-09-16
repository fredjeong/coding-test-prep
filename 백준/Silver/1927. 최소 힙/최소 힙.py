import sys
import heapq

input = sys.stdin.readline

N = int(input())
q = []
heapq.heapify(q)

for _ in range(N):
    num = int(input())
    if num == 0:
        if len(q) != 0:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, num)