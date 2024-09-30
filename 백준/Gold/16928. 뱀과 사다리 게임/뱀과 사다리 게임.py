import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

ladder = {}
for _ in range(n):
    start, end = map(int, input().split())
    ladder[start] = end

snake = {}
for _ in range(m):
    start, end = map(int, input().split())
    snake[start] = end

def bfs():
    visited = [False for _ in range(101)]
    q = deque()
    q.append(1)
    visited[1] = True

    child = []
    count = 0

    while q:
        x = q.popleft()
        if x == 100:
            break

        else:
            for i in range(1, 7):
                nx = x + i
                if nx < 1 or nx > 100:
                    continue
                
                if visited[nx] == True:
                    continue
                visited[nx] = True

                if nx in ladder:
                    nx = ladder[nx]
                    if visited[nx] == True:
                        continue
                    visited[nx] = True
                    child.append(nx)
                elif nx in snake:
                    nx = snake[nx]
                    if visited[nx] == True:
                        continue
                    visited[nx] = True
                    child.append(nx)
                else:
                    child.append(nx)
        
        if not q:
            q.extend(child)
            count += 1
            child = []
    
    return count

result = bfs()
print(result)