from collections import deque, defaultdict

T = int(input())

for test_case in range(1, T+1):
    n, m, k = map(int, input().split())
    board = [[(0, None) for _ in range(n)] for _ in range(n)]
    q = deque()
    for _ in range(k):
        row, col, num, direction = map(int, input().split())
        q.append((row, col, num, direction-1))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 가장자리로는 이동할 수 없다
    for timestep in range(m):
        dic = defaultdict(list)
        while q:
            x, y, num, direction = q.popleft()

            # 이동 방향에 있는 다음 셀로 이동
            nx = x + dx[direction]
            ny = y + dy[direction]

            # 이동 후 약품에 칠해진 셀에 도착하면
            if nx == 0 or nx == n-1 or ny == 0 or ny == n-1:
                # 군집 내 미생물의 절반이 죽고
                num //= 2

                # 이동 방향이 반대로 바뀜
                if direction == 0:
                    direction = 1
                elif direction == 1:
                    direction = 0
                elif direction == 2:
                    direction = 3
                elif direction == 3:
                    direction = 2

                # 군집에 미생물이 한 마리 있는 경우 군집이 사라짐
                if not num:
                    continue

            dic[(nx, ny)].append((num, direction))

        for coordinates in dic:
            x, y = coordinates
            spores = sorted(dic[coordinates], key=lambda z:-z[0])

            if len(spores) == 1:
                num, direction = spores[0]
                q.append((x, y, num, direction))

            # 이동 후 두 개 이상의 군집이 한 셀에 모이는 경우 군집이 합쳐짐
            else:
                # 미생물 수가 가장 많은 군집의 이동방향이 새 이동방향이 됨
                new_direction = spores[0][1]

                # 합쳐진 군집의 미생물 수는 군집들의 미생물 수의 합
                new_num = sum([i[0] for i in spores])

                q.append((x, y, new_num, new_direction))

    # m시간 후 남아있는 미생물 수의 총합 구하기
    total = sum([i[2] for i in q])

    print(f"#{test_case} {total}")