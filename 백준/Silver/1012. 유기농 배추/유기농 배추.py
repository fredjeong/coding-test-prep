from collections import deque

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def cabbage():
    count = 0

    while positions:
        x, y = positions.pop(0)
        count += 1
        queue = deque([(x, y)])

        while queue:
            x, y = queue.popleft()

            for dx, dy in direction:
                nx, ny = x + dx, y + dy

                if 0 <= nx < M and 0 <= ny < N and arr[ny][nx] == 1:
                    arr[ny][nx] = 0
                    if (nx, ny) in positions:
                        positions.remove((nx, ny))
                        queue.append((nx, ny))

    return count


T = int(input())

for tc in range(1, T + 1):
    # M: 가로, N: 세로, K: 배추가 심어져 있는 위치의 개수
    M, N, K = map(int, input().split())
    positions = [tuple(map(int, input().split())) for _ in range(K)]

    arr = [[0] * M for _ in range(N)]
    for X, Y in positions:
        arr[Y][X] = 1

    print(cabbage())