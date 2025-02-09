from collections import deque

T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    board = []
    for i in range(n):
        board.append(list(map(int, list(input().strip()))))

    result = [[1e9 for _ in range(n)] for _ in range(n)]
    result[0][0] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if result[x][y]+board[nx][ny] < result[nx][ny]:
                result[nx][ny] = result[x][y]+board[nx][ny]
                q.append((nx, ny))

    print(f"#{test_case} {result[n-1][n-1]}")