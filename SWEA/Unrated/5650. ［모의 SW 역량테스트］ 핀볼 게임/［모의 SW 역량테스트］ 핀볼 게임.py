from collections import deque, defaultdict

T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    # 벽 부딪히는 것 = 5번 블록 부딪히는 것으로 처리
    board = []
    board.append([5 for _ in range(n+2)])
    for _ in range(n):
        arr = list(map(int, input().split()))
        board.append([5] + arr + [5])
    board.append([5 for _ in range(n+2)])

    # 0: 상, 1: 우, 2: 하, 3: 좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 웜홀 조사
    worm_hole_dic = defaultdict(set)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] >= 6:
                worm_hole_dic[board[i][j]].add((i, j))

    # score initialisation
    max_score = 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] != 0:
                continue
            for k in range(4):
                x = i
                y = j
                direction = k
                score = 0

                count = 0

                while True:

                    x += dx[direction]
                    y += dy[direction]

                    # 종료 조건 1) 출발 위치로 돌아왔다면 종료
                    if (x, y) == (i, j):
                        max_score = max(max_score, score)
                        break

                    # 종료 조건 2) 블랙홀이라면 종료
                    if board[x][y] == -1:
                        max_score = max(max_score, score)
                        break

                    #################################

                    # 웜홀을 만났을 경우
                    if 6 <= board[x][y] <= 10:
                        # 같은 번호를 가진 웜홀을 찾는다
                        for coordinate in worm_hole_dic[board[x][y]]:
                            # 위치 갱신
                            if coordinate != (x, y):
                                x = coordinate[0]
                                y = coordinate[1]
                                break

                    # 1번 블록을 만났을 경우
                    elif board[x][y] == 1:
                        if direction == 2:
                            direction = 1
                        elif direction == 3:
                            direction = 0
                        else:
                            direction = (direction + 2) % 4

                        score += 1

                    # 2번 블록을 만났을 경우
                    elif board[x][y] == 2:
                        if direction == 0:
                            direction = 1
                        elif direction == 3:
                            direction = 2
                        else:
                            direction = (direction + 2) % 4

                        score += 1

                    # 3번 블록을 만났을 경우
                    elif board[x][y] == 3:
                        if direction == 0:
                            direction = 3
                        elif direction == 1:
                            direction = 2
                        else:
                            direction = (direction + 2) % 4

                        score += 1

                    # 4번 블록을 만났을 경우
                    elif board[x][y] == 4:
                        if direction == 1:
                            direction = 0
                        elif direction == 2:
                            direction = 3
                        else:
                            direction = (direction + 2) % 4

                        score += 1

                    # 5번 블록을 만났을 경우
                    elif board[x][y] == 5:
                        direction = (direction + 2) % 4
                        score += 1

                max_score = max(max_score, score)

    print(f"#{test_case} {max_score}")
