T = int(input())

for test_case in range(1, T+1):
    d, w, k = map(int, input().split())

    board = []
    for _ in range(d):
        board.append(list(map(int, input().split())))

    """
    단면의 모든 세로 방향에 대해서 
    동일한 특성의 셀들이 k개 이상 연속적으로 있는 경우
    성능검사를 통과하게 된다
    """

    min_count = d

    def recursion(x, cnt, rows_a, rows_b):
        global min_count

        # cnt가 현재까지의 최솟값 이상이라면 고려할 필요 없다
        if cnt >= min_count:
            return

        # 테스트를 통과할 수 있는지 확인
        for col in range(w):
            # 각 열에 대하여 검사 통과했는지 여부 검사
            test_pass = False

            test_col = ""

            for i in range(d):
                if i in rows_a:
                    test_col += "0"
                elif i in rows_b:
                    test_col += "1"
                else:
                    test_col += str(board[i][col])

            if "0"*k in test_col or "1"*k in test_col:
                test_pass = True
                continue
            else:
                break

        # 검사를 통과했다면 min_count 최신화
        if test_pass:
            min_count = min(min_count, cnt)

        # 마지막 행까지 다 봤다면 다음 행은 보지 않는다
        if x == d-1:
            return

        recursion(x+1, cnt, rows_a, rows_b)
        recursion(x+1, cnt+1, rows_a | {x+1}, rows_b)
        recursion(x+1, cnt+1, rows_a, rows_b | {x+1})

    recursion(0, 0, set(), set())
    recursion(0, 1, {0}, set())
    recursion(0, 1, set(), {0})
    
    print(f"#{test_case} {min_count}")
