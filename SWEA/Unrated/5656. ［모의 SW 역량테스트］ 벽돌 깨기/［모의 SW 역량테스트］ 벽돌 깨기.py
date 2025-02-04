from collections import deque

T = int(input())

for test_case in range(1, T+1):
    n, w, h = map(int, input().split())
    board_ = []

    for _ in range(h):
        board_.append(list(map(int, input().split())))

    def perm_with_replacement(arr):
        if len(arr) == n:
            results.append(arr)
            return
        for i in range(w):
            perm_with_replacement(arr + [i])


    results = []
    perm_with_replacement([])
    min_score = 1e9
    # 각 케이스에 대해 브루트포스 실시
    for result in results:
        # 보드 복사
        board = []
        for i in range(h):
            board.append(board_[i][:])

        for i in range(n):
            col = result[i]
            for row in range(h):
                if board[row][col]:
                    q = deque()
                    q.append((row, col))
                    break

            while q:
                x, y = q.popleft()
                length = board[x][y]

                board[x][y] = 0

                # length-1 범위에 있는 모든 벽돌이 동시에 제거됨
                for splash in range(-length+1, length):
                    if splash == 0:
                        continue

                    if 0 <= x + splash < h:
                        q.append((x+splash, y))
                    if 0 <= y + splash < w:
                        q.append((x, y+splash))

            # 남은 벽돌들 아래로 끌어내리기
            new_board = [[None for _ in range(w)] for _ in range(h)]
            for col_ in range(w):
                col_list = []
                for row_ in range(h):
                    if board[row_][col_]:
                        col_list.append(board[row_][col_])

                # col_list 패딩
                col_list = [0 for _ in range(h - len(col_list))] + col_list

                for row in range(h):
                    new_board[row][col_] = col_list[row]
            board = new_board

        # 남은 개수 세기
        score = 0
        for i in range(h):
            for j in range(w):
                if board[i][j]:
                    score += 1
        min_score = min(min_score, score)
    print(f"#{test_case} {min_score}")
