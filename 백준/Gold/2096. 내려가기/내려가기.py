import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

a, b, c =  map(int, input().split())

dp = deque(maxlen=2)

dp.append([[a, a], [b, b], [c, c]])
for i in range(1, n):
    a, b, c = map(int, input().split())
    dp.append([[a + max(dp[-1][0][0], dp[-1][1][0]), 
                a + min(dp[-1][0][1], dp[-1][1][1])],
               [b + max(dp[-1][0][0], dp[-1][1][0], dp[-1][2][0]),
                b + min(dp[-1][0][1], dp[-1][1][1], dp[-1][2][1])], 
               [c + max(dp[-1][1][0], dp[-1][2][0]),
                c + min(dp[-1][1][1], dp[-1][2][1])]])

print(max(dp[-1][0][0], dp[-1][1][0], dp[-1][2][0]), min(dp[-1][0][1], dp[-1][1][1], dp[-1][2][1]))