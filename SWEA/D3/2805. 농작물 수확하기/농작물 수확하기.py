T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, list(input().strip()))))

    profit = 0
    # 정중앙 1개에서 시작하여 row가 하나씩 증가할수록 양 옆에 한 칸씩 추가
    # 중간을 넘어가면 다시 한 칸씩 감소
    for i in range(n):
        if i == 0:
            start = n//2
            end = start + 1
        elif i <= n//2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1

        row = board[i]
        profit += sum(row[start:end])

    print(f"#{test_case} {profit}")
