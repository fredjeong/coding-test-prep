from collections import deque

# 8방향 탐색
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

T = int(input())

for test_case in range(1, T+1):
    # 지뢰가 있는 칸을 제외하고 다른 모든 칸의 숫자들이 표시되려면 최소 몇 번의 클릭을 해야 하는지 구하기
    n = int(input()) # 최대 300

    # 각 칸마다 주변 8칸의 지뢰 개수 조사해서 좌표들 줄세우기
    board = []
    for _ in range(n):
        board.append(list(input().strip()))

    mine = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = []

    for x in range(n):
        for y in range(n):
            if board[x][y] == "*":
                visited[x][y] = True
                continue
            else:
                cnt = 0
                # 주변 8방향 탐사
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if board[nx][ny] == "*":
                        cnt += 1
                q.append((cnt, x, y, 0))
                mine[x][y] = cnt

    num_click = 0

    q = deque(sorted(q, key=lambda x: x[0]))

    while q:
        cnt, x, y, is_chain = q.popleft()
        # 이미 숫자 조회가 완료되었다면 넘어간다
        if visited[x][y]:
            continue
        visited[x][y] = True

        # 클릭한 칸에서 연쇄 반응으로 조사하게 된 칸이라면 클릭 수에 포함하지 않는다
        if not is_chain:
            num_click += 1

        # 주변에 지뢰가 없는 칸이었다면 연쇄 반응
        if not cnt:
            # 8방향 탐색하여
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if visited[nx][ny]:
                    continue
                q.appendleft((mine[nx][ny], nx, ny, 1))

        # 지뢰가 있는 칸이라면 그대로 종료
    print(f"#{test_case} {num_click}")
