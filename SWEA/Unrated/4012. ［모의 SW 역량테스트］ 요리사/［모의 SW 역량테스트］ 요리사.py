T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    min_diff = 1e9

    def recursion(idx, num, visited):
        global min_diff
        if num > n//2:
            return

        if idx == n - 1:
            if num == n//2:
                # 맛 차이 계산
                dish_a = 0
                dish_b = 0
                for i in range(n):
                    for j in range(n):
                        if i < j:
                            if i in visited and j in visited:
                                dish_a += board[i][j] + board[j][i]
                            elif i not in visited and j not in visited:
                                dish_b += board[i][j] + board[j][i]
                diff = abs(dish_a - dish_b)
                min_diff = min(min_diff, diff)
            return

        recursion(idx + 1, num, visited)
        recursion(idx + 1, num + 1, visited | {idx})

    recursion(0, 0, set())
    print(f"#{test_case} {min_diff}")