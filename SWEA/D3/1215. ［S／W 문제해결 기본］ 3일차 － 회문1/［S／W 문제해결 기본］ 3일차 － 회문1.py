T = 10
for test_case in range(1, T+1):
    length = int(input())

    board = []
    for _ in range(8):
        board.append(list(input().strip()))
    ans = 0

    # 가로 문자열을 대상으로 조사
    for row in board:
        # 구해야 하는 문자열의 길이가 8보다 크다면 어차피 구할 수 없음
        if length > 8:
            break
        for i in range(8 - length + 1):
            # 문자열 찾기
            s = row[i:i+length]

            # 팰린드롬인지 검사
            early_stopping = False
            for j in range(length//2):
                if s[j] != s[length-1-j]:
                    early_stopping = True
                    break

            # 팰린드롬이라면 카운트 1 추가
            if not early_stopping:
                ans += 1

    # 세로 문자열을 대상으로 조사
    for col_idx in range(8):
        for i in range(8 - length + 1):
            s = ""
            for row_idx in range(i, i + length):
                s += board[row_idx][col_idx]

            early_stopping = False
            for j in range(length//2):
                if s[j] != s[length-1-j]:
                    early_stopping = True
                    break

            if not early_stopping:
                ans += 1

    print(f"#{test_case} {ans}")