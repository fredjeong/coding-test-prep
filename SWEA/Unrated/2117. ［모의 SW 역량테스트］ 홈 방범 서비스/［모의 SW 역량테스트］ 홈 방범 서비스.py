T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())

    house_count = 0
    board = []
    for _ in range(n):
        arr = list(map(int, input().split()))
        house_count += sum(arr)
        board.append(arr)

    limit = house_count * m

    max_count = 0
    k = 1
    while k**2 + (k-1)**2 < limit:
        cost = k**2 + (k-1)**2
        for i in range(n):
            for j in range(n):
                cnt = 0
                for row in range(-k+1, k):
                    for col in range(-k+1, k):
                        if abs(row)+abs(col) > k-1:
                            continue
                        nx = i + row
                        ny = j + col
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        if board[nx][ny]:
                            cnt += 1
                profit = cnt * m - cost
                if profit >= 0:
                    max_count = max(max_count, cnt)
        k += 1

    print(f"#{test_case} {max_count}")