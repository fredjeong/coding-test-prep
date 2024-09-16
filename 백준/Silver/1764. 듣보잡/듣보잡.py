import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

arr_1 = set()
arr_2 = set()

for _ in range(N):
    name = str(input().strip())
    arr_1.add(name)
for _ in range(M):
    name = str(input().strip())
    arr_2.add(name)

intersection = list(arr_1 & arr_2)
heapq.heapify(intersection)

print(len(intersection))
while intersection:
    print(heapq.heappop(intersection))