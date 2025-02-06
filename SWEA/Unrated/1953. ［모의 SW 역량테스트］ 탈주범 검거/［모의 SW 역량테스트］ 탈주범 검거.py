from collections import deque

T = int(input())

for test_case in range(1, T+1):
    n, m, r, c, time_limit = map(int, input().split())

    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    # 방문 배열
    visited = [[False for _ in range(m)] for _ in range(n)]

    # 탈주범은 (r, c) 위치에서 출발한다
    q = deque()
    q.append((r, c, 1, visited)) # row, col, timestep

    # 방향: 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 결과를 저장할 집합 (좌표 저장)
    s = set()

    while q:
        x, y, t, visited_ = q.popleft()

        # visited 배열 복사
        visited = []
        for row in visited_:
            visited.append(row[:])

        if visited[x][y]:
            continue
        visited[x][y] = True

        s.add((x, y))

        # 시간이 다 되었을 경우 종료
        if t == time_limit:
            continue

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 격자 밖으론 이동 불가
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 보드에서의 값이 0인 경우 이동 불가
            if not board[nx][ny]:
                continue

            # 이미 방문한 지점으로는 이동 불가
            if visited[nx][ny]:
                continue

            do_move = False
            if board[x][y] == 1:
                if k == 0: # 하와 연결
                    if board[nx][ny] in [1, 2, 5, 6]:
                        do_move = True
                elif k == 1: # 상과 연결
                    if board[nx][ny] in [1, 2, 4, 7]:
                        do_move = True
                elif k == 2: # 우와 연결
                    if board[nx][ny] in [1, 3, 4, 5]:
                        do_move = True
                elif k == 3: # 좌와 연결
                    if board[nx][ny] in [1, 3, 6, 7]:
                        do_move = True

            elif board[x][y] == 2:
                if k == 0: # 하와 연결
                    if board[nx][ny] in [1, 2, 5, 6]:
                        do_move = True

                elif k == 1: # 상과 연결
                    if board[nx][ny] in [1, 2, 4, 7]:
                        do_move = True

            elif board[x][y] == 3:
                if k == 2: # 우와 연결
                    if board[nx][ny] in [1, 3, 4, 5]:
                        do_move = True
                elif k == 3: # 좌와 연결
                    if board[nx][ny] in [1, 3, 6, 7]:
                        do_move = True

            elif board[x][y] == 4:
                if k == 0: # 하와 연결
                    if board[nx][ny] in [1, 2, 5, 6]:
                        do_move = True
                elif k == 3: # 좌와 연결
                    if board[nx][ny] in [1, 3, 6, 7]:
                        do_move = True

            elif board[x][y] == 5:
                if k == 1: # 상과 연결
                    if board[nx][ny] in [1, 2, 4, 7]:
                        do_move = True
                elif k == 3: # 좌와 연결
                    if board[nx][ny] in [1, 3, 6, 7]:
                        do_move = True

            elif board[x][y] == 6:
                if k == 1: # 상과 연결
                    if board[nx][ny] in [1, 2, 4, 7]:
                        do_move = True
                elif k == 2: # 우와 연결
                    if board[nx][ny] in [1, 3, 4, 5]:
                        do_move = True

            elif board[x][y] == 7:
                if k == 0: # 하와 연결
                    if board[nx][ny] in [1, 2, 5, 6]:
                        do_move = True
                elif k == 2: # 우와 연결
                    if board[nx][ny] in [1, 3, 4, 5]:
                        do_move = True
            if do_move:
                q.append((nx, ny, t + 1, visited))

    print(f"#{test_case} {len(s)}")