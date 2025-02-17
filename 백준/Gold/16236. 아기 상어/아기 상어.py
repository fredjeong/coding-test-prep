import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

fish_dic = {}
for row in range(n):
    arr = list(map(int, input().split()))
    for col in range(n):
        if arr[col] == 9:
            x = row
            y = col
            continue
        if arr[col]:
            fish_dic[(row, col)] = arr[col]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

timestep = 0
size = 2
cur_cnt = 0

while fish_dic and min(fish_dic.values()) < size:
    q = deque()
    q.append((x, y, 0))

    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[x][y] = True

    target_dist = None
    targets = set()

    while q:
        cur_x, cur_y, dist = q.popleft()
        if target_dist and dist > target_dist:
            continue

        if (cur_x, cur_y) in fish_dic and fish_dic[(cur_x, cur_y)] < size:
            if not target_dist:
                target_dist = dist
                targets.add((cur_x, cur_y))
            else:
                if dist == target_dist:
                    targets.add((cur_x, cur_y))
            continue

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            if (nx, ny) in fish_dic and fish_dic[(nx, ny)] > size:
                continue
            q.append((nx, ny, dist+1))

    if target_dist:
        target_x, target_y = sorted(targets)[0]

        fish_dic.pop((target_x, target_y))

        cur_cnt += 1
        if cur_cnt == size:
            size += 1
            cur_cnt = 0

        timestep += target_dist
        x = target_x
        y = target_y
    else:
        break

print(timestep)