import sys

input = sys.stdin.readline

board = []
for _ in range(10):
    board.append(list(map(int, input().split())))

no_zero = True
for board_row in board:
    if 1 in board_row:
        no_zero = False
        break

if no_zero:
    print(0)

else:
    papers = [5, 5, 5, 5, 5]
    history = set()

    min_count = 1e9
    def recursion(x, y, area_size, papers_, board_):
        global min_count, count, history
        if (x, y, area_size, tuple(papers_)) in history:
            return
        history.add((x, y, area_size, tuple(papers_)))

        if 25 - sum(papers_) >= min_count:
            return

        # 보드 복사 후 x, y를 출발점으로, 입력받은 size만큼 지우기
        board = [row[:] for row in board_]
        for sub_x in range(area_size + 1):
            for sub_y in range(area_size + 1):
                board[x + sub_x][y + sub_y] = 0

        # papers 복사 후 area_size 인덱스 값 1 빼주기
        papers = papers_[:]
        papers[area_size] -= 1

        # 종료조건 1: 보드에 1이 없을 것
        no_zero = True
        for board_row in board:
            if 1 in board_row:
                no_zero = False
                break

        if no_zero:
            min_count = min(min_count, 25 - sum(papers))
            return

        # 종료조건 2: 종이를 모두 사용했을 것
        if not sum(papers):
            return

        # 다음 경우 탐색
        flag = False
        for nx in range(x, 10):
            for ny in range(10):
                if nx == x and ny <= y:
                    continue

                if not board[nx][ny]:
                    continue

                # 경우 탐색하기
                for size in range(4, -1, -1):
                    if not papers[size]:
                        continue
                    early_stopping = False
                    for sub_x in range(size+1):
                        for sub_y in range(size+1):
                            if nx + sub_x >= 10 or ny + sub_y >= 10:
                                early_stopping = True
                                break
                            if not board[nx+sub_x][ny+sub_y]:
                                early_stopping = True
                                break
                        if early_stopping:
                            break

                    if early_stopping:
                        continue

                    if not papers[size]:
                        continue

                    recursion(nx, ny, size, papers, board)
                    flag = True

            if flag:
                break


    flag = False
    for i in range(10):
        for j in range(10):
            if not board[i][j]:
                continue

            for size in range(4, -1, -1):
                early_stopping = False
                for sub_x in range(size + 1):
                    for sub_y in range(size + 1):
                        if i + sub_x >= 10 or j + sub_y >= 10:
                            early_stopping = True
                            break

                        if not board[i + sub_x][j + sub_y]:
                            early_stopping = True
                            break

                    if early_stopping:
                        break

                if early_stopping:
                    continue

                flag = True
                recursion(i, j, size, papers, board)

            break

        if flag:
            break

    if min_count == 1e9:
        min_count = -1

    print(min_count)