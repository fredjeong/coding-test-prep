import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    visited = [False for _ in range(n)]
    min_q = []
    max_q = []
    for i in range(n):
        order, num = input().split()
        num = int(num)

        if order == 'I':
            heapq.heappush(min_q, (num, i))
            heapq.heappush(max_q, (-num, i))
            visited[i] = True
        
        elif order == 'D':
            if int(num) == -1:
                while min_q and visited[min_q[0][1]] == 0:
                    heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = False
                    heapq.heappop(min_q)
            elif int(num) == 1:
                while max_q and visited[max_q[0][1]] == 0:
                    heapq.heappop(max_q)
                if max_q:
                    visited[max_q[0][1]] = False
                    heapq.heappop(max_q)

    if True not in visited:
        print("EMPTY")
    
    else:
        while max_q and visited[max_q[0][1]] == 0:
            heapq.heappop(max_q)
        while min_q and visited[min_q[0][1]] == 0:
            heapq.heappop(min_q)
        print(-max_q[0][0], min_q[0][0])