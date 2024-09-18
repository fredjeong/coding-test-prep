import sys
import heapq

input = sys.stdin.readline

N = int(input())

arr = []
heapq.heapify(arr)

for _ in range(N):
    heapq.heappush(arr, int(input().strip()))

for _ in range(N):
    print(heapq.heappop(arr))