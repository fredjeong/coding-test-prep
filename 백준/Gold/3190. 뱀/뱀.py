from collections import deque

n = int(input())
k = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(k):
    row, col = map(int, input().split())

    row -= 1
    col -= 1

    # 사과의 위치는 2로 표시
    board[row][col] = 2

# 방향 정의 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direction_change_timesteps = set()
direction_dic = {}
direction_count = int(input()) # 뱀의 방향 변환 횟수
for _ in range(direction_count):
    x, c = input().split()
    x = int(x)
    direction_dic[x] = c
    direction_change_timesteps.add(x)

timestep = 0

# 뱀은 처음에 오른쪽을 향한다
direction = 1

# 뱀 머리의 위치: 처음엔 맨 위 맨 좌측에 위치
snake_x = 0
snake_y = 0

# 뱀은 1로 표시
board[snake_x][snake_y] = 1

snake = deque()
snake.append((0, 0))

# 뱀의 길이는 1부터 시작
snake_length = 1

# 뱀은 매 초마다 이동한다
while True:
    timestep += 1

    # 몸 길이를 늘려 머리를 다음 칸에 위치시킨다
    snake_length += 1

    snake_x += dx[direction]
    snake_y += dy[direction]

    # 벽에 부딪히면 게임이 끝난다
    if snake_x < 0 or snake_x >= n or snake_y < 0 or snake_y >= n:
        break

    # 자기 자신과 부딪히면 게임이 끝난다
    elif board[snake_x][snake_y] == 1:
        break

    snake.append((snake_x, snake_y))

    # 이동한 칸에 사과가 있다면
    if board[snake_x][snake_y] == 2:
        # 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다
        board[snake_x][snake_y] = 1

    # 이동한 칸에 사과가 없다면
    else:
        board[snake_x][snake_y] = 1

        # 몸길이를 줄여서
        snake_length -= 1

        # 꼬리가 위치한 칸을 비워준다
        tail_x, tail_y = snake.popleft()
        board[tail_x][tail_y] = 0

    # 방향을 바꾸어야 하는지 확인
    if timestep in direction_change_timesteps:
        if direction_dic[timestep] == "L":
            direction -= 1
            if direction < 0:
                direction += 4
        else:
            direction += 1
            if direction >= 4:
                direction -= 4

print(timestep)
