from collections import deque

T = int(input())

for test_case in range(1, T+1):
    n, k = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    """
    등산로는 가장 높은 봉우리에서 시작해야 한다
    """
    # 최고 높이 찾기
    max_height = 0
    for i in range(n):
        for j in range(n):
            height = board[i][j]
            max_height = max(max_height, height)

    """
    deque q에 가장 높은 등산로의 좌표를 정리하고, 더 낮은 곳으로 갈 수 있는지 선택
    4방향 탐색을 통해서 낮게 갈 수 있는지 확인
    큐에 들어가야 하는 정보: x, y, 누적 길이, 깊이 깎았는지 여부
    visited가 꼭 있어야 하나? 어차피 자기 자신 미만의 높이로만 가야 하는데?
    """
    # 4방향 탐색
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 가장 긴 등산로의 길이 (정답)
    max_dist = 0

    # 가장 높은 등산로의 좌표 정리 (initialising q)
    q = deque()

    for i in range(n):
        for j in range(n):
            if board[i][j] == max_height:
                q.append((i, j, max_height, 1, {(i, j)}, True))

    while q:
        x, y, current_height, cum_dist, history, chance = q.popleft()

        # 최고 길이 업데이트
        max_dist = max(max_dist, cum_dist)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 격자 밖으로 벗어나는 경우는 고려하지 않는다
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            # 이미 방문한 지점은 고려하지 않는다
            if (nx, ny) in history:
                continue

            new_height = board[nx][ny]
            # 찬스를 쓰는 경우
            if chance:
                # 찬스를 쓰면 최대 k만큼 깎을 수 있다
                for bonus in range(1, k + 1):
                    new_height_with_chance = new_height - bonus

                    # 찬스를 써도 내려갈 수 없다면 고려하지 않는다
                    if new_height_with_chance >= current_height:
                        continue

                    q.append((nx, ny, new_height_with_chance, cum_dist + 1, history | {(nx, ny)}, False))

            # 찬스를 쓰지 않는 경우
            # 현재 높이 이상이라면 고려하지 않는다
            if new_height >= current_height:
                continue

            q.append((nx, ny, new_height, cum_dist+1, history | {(nx, ny)}, chance))

    print(f"#{test_case} {max_dist}")
