import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

def bfs(N):
    q = deque()
    q.append(N)
    visited = set()
    count = 0
    child = []
    while q:
        num = q.popleft()
        if num==1:
            return count
        visited.add(num)

        if num%3 == 0 and num//3 not in visited:
            child.append(num//3)
        if num%2 == 0 and num//2 not in visited:
            child.append(num//2)
        child.append(num-1)

        if len(q)==0:
            q.extend(child)
            count += 1
            child = []

print(bfs(N))