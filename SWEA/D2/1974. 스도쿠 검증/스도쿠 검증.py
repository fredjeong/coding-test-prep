T = int(input())

for test_case in range(1, T+1):
    board = []
    for _ in range(9):
        board.append(list(map(int, input().split())))
    
    early_stopping = False
    result = 1

    # 3x3 검증
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            s = set()
            for sub_i in range(i, i+3):
                for sub_j in range(j, j+3):
                    s.add(board[sub_i][sub_j])
            if len(s) != 9:
                result = 0
                early_stopping = True
                break
        if early_stopping:
            break
    
    if result:
        # 가로 검증
        for i in range(9):
            row = board[i]
            if len(set(board[i])) != 9:
                result = 0
                early_stopping = True
                break
        if not early_stopping:
            # 세로 검증
            for i in range(9):
                s = set()
                for j in range(9):
                    s.add(board[j][i])
                if len(s) != 9:
                    result = 0
                    break
    print(f"#{test_case} {result}")