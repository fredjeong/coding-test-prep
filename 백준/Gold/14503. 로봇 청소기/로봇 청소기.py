import sys
from collections import deque

input = sys.stdin.readline

# 로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수 구하기

n, m = map(int, input().split())
x_init, y_init, d = map(int, input().split())

# 값이 0이라면 아직 청소되지 않은 빈 칸, 1인 경우 벽 존재
visited = [list(map(int, input().split())) for _ in range(n)]

# 로봇 청소기가 바라보는 방향: 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0

q = deque()
q.append((x_init, y_init))

while q:
    x, y = q.popleft()

    # 현재 칸이 아직 청소되지 않은 경우 현재 칸을 청소한다
    if not visited[x][y]:
        visited[x][y] = 2
        cnt += 1

    do_clean = False

    # 주변 4방향 중 청소되지 않은 빈 칸 있는지 확인
    rotate_cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 청소되지 않은 빈 칸이 하나라도 있다면 반시계 방향으로 90도 회전
        if not visited[nx][ny]:
            d -= 1
            if d < 0:
                d += 4

            # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
            if not visited[x + dx[d]][y + dy[d]]:
                new_x = x + dx[d]
                new_y = y + dy[d]
                q.append((new_x, new_y))
                do_clean = True
            else:
                q.append((x, y))
                do_clean = True
            break

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if not do_clean:
        nx = x - dx[d]
        ny = y - dy[d]

        # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다
        if visited[nx][ny] == 1:
            break

        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다
        q.append((nx, ny))

print(cnt)