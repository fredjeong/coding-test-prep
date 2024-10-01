import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, end):
    q = deque()
    q.append(start)
    visited = [False for _ in range(10001)]
    visited[int(start)] = True
    orders = ["" for _ in range(10001)]
    
    while q:
        x = q.popleft()

        if len(x) != 4:
            x = "0"*(4 - len(x)) + x
        
        if x==end:
            break

        nx_d = int(x)*2 % 10000
        nx_s = int(x) - 1
        if nx_s == -1:
            nx_s = 9999
        nx_l = int(x[1:] + x[0])
        nx_r = int(x[-1] + x[:-1])
        
        arr = [[nx_d, "D"], [nx_s, "S"], [nx_l, "L"], [nx_r, "R"]]

        for i in range(len(arr)):
            if arr[i][0] < 0 or arr[i][0] > 10000:
                continue
            if visited[arr[i][0]]==True:
                continue
            visited[arr[i][0]] = True
            orders[arr[i][0]] += orders[int(x)] + arr[i][1]
            
            arr[i][0] = str(arr[i][0])
            if len(arr[i][0]) != 4:
                arr[i][0] = "0"*(4 - len(arr[i][0])) + arr[i][0]
            q.append(arr[i][0])

    return orders[int(end)]

t = int(input())
for _ in range(t):
    start, end = input().split()
    result = bfs(start, end)
    print(result)