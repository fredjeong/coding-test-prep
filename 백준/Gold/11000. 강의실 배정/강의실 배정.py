import sys
import heapq
from collections import deque

input = sys.stdin.readline

n = int(input())

q = []
heapq.heapify(q)
cnt = 0

arr = []
for _ in range(n): # 최대 20만개
    arr.append(list(map(int, input().split())))

arr = deque(sorted(arr))

while arr:
    s, t = arr.popleft()

    # 힙에는 끝나는 시간을 넣는다
    if q:
        prev_t = heapq.heappop(q)
        if s >= prev_t:
            heapq.heappush(q, t)
            # 기존 강의실에서 교체
        else:
            heapq.heappush(q, prev_t)
            heapq.heappush(q, t)
            if len(q) >= cnt:
                cnt += 1
    else:
        heapq.heappush(q, t)
        if len(q) >= cnt:
            cnt += 1

print(cnt)