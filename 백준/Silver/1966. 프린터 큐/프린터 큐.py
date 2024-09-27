import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    importance_arr = deque(list(map(int, input().split())))
    order_arr = deque([i for i in range(N)])

    count = 0
    while order_arr:
        importance = importance_arr.popleft()
        order = order_arr.popleft()
        if importance_arr:
            if importance < max(importance_arr):
                importance_arr.append(importance)
                order_arr.append(order)
            else:
                count += 1
                if order == M:
                    print(count)
                    break
        else:
            count += 1
            print(count)
            break