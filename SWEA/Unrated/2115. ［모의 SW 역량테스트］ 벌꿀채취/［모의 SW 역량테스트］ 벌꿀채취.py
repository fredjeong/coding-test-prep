T = int(input())

def combination(arr, n):
    result = []
    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i+1:], n - 1):
            result.append([elem] + rest)
    return result


for test_case in range(1, T+1):
    n, m, c = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    max_profit = 0
    # 두 일꾼은 가로로 연속되도록 m개의 벌통을 선택할 수 있다
    for row_1 in range(n):
        for col_1 in range(n-(m-1)):
            for row_2 in range(row_1, n):
                for col_2 in range(n-(m-1)):
                    # 첫 번째 일꾼과 영역이 겹쳐서는 안된다
                    if row_2 == row_1 and {i for i in range(col_1, col_1+m)} & {i for i in range(col_2, col_2+m)}:
                        continue
                    # 일꾼 1의 선택
                    worker_1_ = board[row_1][col_1:col_1 + m]
                    worker_1 = worker_1_[:]

                    # 일꾼 2의 선택
                    worker_2_ = board[row_2][col_2:col_2+m]
                    worker_2 = worker_2_[:]

                    worker_1_final = None
                    if sum(worker_1) > c:
                        max_squared = 0

                        for i in range(len(worker_1)):
                            results = combination(worker_1, i)
                            for result in results:
                                squared = sum([i**2 for i in result])
                                if squared > max_squared and sum(result) <= c:
                                    max_squared = squared
                                    worker_1_final = result

                    if worker_1_final:
                        worker_1 = worker_1_final

                    worker_2_final = None
                    if sum(worker_2) > c:
                        max_squared = 0
                        for i in range(len(worker_2)):
                            results = combination(worker_2, i)
                            for result in results:
                                squared = sum([i ** 2 for i in result])
                                if squared > max_squared and sum(result) <= c:
                                    max_squared = squared
                                    worker_2_final = result
                    if worker_2_final:
                        worker_2 = worker_2_final

                    profit = 0
                    profit += sum([num**2 for num in worker_1]) + sum([num**2 for num in worker_2])

                    max_profit = max(max_profit, profit)

    print(f"#{test_case} {max_profit}")