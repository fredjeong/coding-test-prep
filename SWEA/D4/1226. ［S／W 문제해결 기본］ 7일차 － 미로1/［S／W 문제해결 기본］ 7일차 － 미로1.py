from collections import deque

for _ in range(1, 11):
    test_case = int(input())

    board = []
    for _ in range(16):
        board.append(list(map(int, list(input().strip()))))

    # 출발점과 도착점 찾기
    for i in range(16):
        for j in range(16):
            if board[i][j] == 2:
                start_x, start_y = i, j

    # 방문 배열 선언
    visited = [[False for _ in range(16)] for _ in range(16)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = True

    answer = 0

    while q:
        x, y = q.popleft()

        if board[x][y] == 3:
            answer = 1
            break

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 벽이면 고려하지 않는다
            if board[nx][ny] == 1:
                continue

            # 이미 방문한 곳이면 고려하지 않는다
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True

            q.append((nx, ny))

    print(f"#{test_case} {answer}")