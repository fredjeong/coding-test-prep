from collections import deque

T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    # 대각선 방향으로 움직이고 사각형 모양을 그리며 출발한 카페로 돌아와야 함
    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]

    max_count = -1

    # 방향은 한 칸씩 바꿀 수 있음
    for row in range(n):
        for col in range(n):
            # 시작점 지정
            q = deque()
            q.append((row, col, 0, set(), [0, 0, 0, 0])) # x, y, direction, dessert set, lengths
            while q:
                x, y, direction, s, lengths = q.popleft()

                if direction == 3 and lengths[0] == lengths[2] and lengths[1] == lengths[3]:
                    max_count = max(max_count, sum(lengths))
                    continue

                if sum(lengths) == (n - 1)*2:
                    continue

                # 방향을 고정하거나 다음 방향으로 넘어가거나
                direction_choices = [direction, direction+1]

                for new_direction in direction_choices:
                    # print(new_direction)
                    if new_direction > 3:
                        continue
                    nx = x + dx[new_direction]
                    ny = y + dy[new_direction]

                    # 격자 밖인 경우 고려하지 않음
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue

                    # 이미 먹어본 디저트인 경우 고려하지 않음
                    if board[nx][ny] in s:
                        continue

                    temp_lengths = lengths[:]
                    temp_lengths[new_direction] += 1

                    q.append((nx, ny, new_direction, s | {board[nx][ny]}, temp_lengths))

    print(f"#{test_case} {max_count}")