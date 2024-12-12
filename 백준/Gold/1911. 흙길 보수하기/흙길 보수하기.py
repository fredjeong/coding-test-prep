import sys
import heapq

input = sys.stdin.readline

n, l = map(int, input().split())

pools = []

for _ in range(n):
    heapq.heappush(pools, tuple(map(int, input().split())))

pos = 0
count = 0
while pools:
    start, end = heapq.heappop(pools)
    if pos < start:
        pos = start

    plank = (end - pos - 1) // l + 1
    count += plank
    pos += plank * l

print(count)