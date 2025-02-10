def get_powers(x, y):
    arr = []
    for bc in board[x][y]:
        arr.append(power_dic[bc])
    arr = sorted(arr, reverse=True)
    return arr

T = int(input())

for test_case in range(1, T+1):
    m, a = map(int, input().split())

    moves_a = list(map(int, input().split()))
    moves_b = list(map(int, input().split()))

    board = [[[] for _ in range(10)] for _ in range(10)]

    power_dic = {}

    for bc in range(a):
        y, x, c, p = map(int, input().split())

        # 좌표 시작점을 0, 0으로 맞춰준다
        x -= 1
        y -= 1

        # print("x", x, "y", y, "c", c, "p", p)
        power_dic[bc] = p
        for i in range(-c, c+1):
            for j in range(-c, c+1):
                if abs(i) + abs(j) > c:
                    continue

                nx = x + i
                ny = y + j

                if nx < 0 or nx >= 10 or ny < 0 or ny >= 10:
                    continue

                board[nx][ny].append(bc)

    total_power = 0

    x_a, y_a = 0, 0
    x_b, y_b = 9, 9

    # 0초에도 충전은 됨
    if board[x_a][y_a]:
        total_power += get_powers(x_a, y_a)[0]
    if board[x_b][y_b]:
        total_power += get_powers(x_b, y_b)[0]

    # 정지, 상, 우, 하, 좌
    dx = [0, -1, 0, 1, 0]
    dy = [0, 0, 1, 0, -1]

    for timestep in range(m):
        direction_a = moves_a[timestep]
        direction_b = moves_b[timestep]

        x_a += dx[direction_a]
        y_a += dy[direction_a]

        x_b += dx[direction_b]
        y_b += dy[direction_b]

        bcs_a = board[x_a][y_a]
        bcs_b = board[x_b][y_b]

        if not bcs_a and not bcs_b:
            continue
        elif bcs_a and not bcs_b:
            total_power += get_powers(x_a, y_a)[0]
        elif bcs_b and not bcs_a:
            total_power += get_powers(x_b, y_b)[0]
        else:
            # 비교해야함
            max_power = 0
            for bc_a in bcs_a:
                for bc_b in bcs_b:
                    if bc_a == bc_b:
                        max_power = max(max_power, power_dic[bc_a])
                    else:
                        p_a = power_dic[bc_a]
                        p_b = power_dic[bc_b]
                        max_power = max(max_power, p_a + p_b)
            total_power += max_power

    print(f"#{test_case} {total_power}")