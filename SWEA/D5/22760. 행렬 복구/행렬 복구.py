from collections import defaultdict

T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    arr = []
    for _ in range(2*n):
        arr.append(list(map(int, input().split())))

    # 2n개의 행을 가진 arr를 적절히 섞으면 A와 A^T로 이루어진 B를 만들 수 있음
    # 모든 원소가 서로 다름이 보장되었으므로 각 행의 첫 숫자 개수를 세고, 겹치는 수를 찾으면 됨
    # 딕셔너리 이용
    # 그 중 하나를 선택하면 됨

    # 2n개 행의 첫 번째 숫자들을 정리
    first_nums = defaultdict(int)
    for row in range(2*n):
        first_num = arr[row][0]

        if first_num in first_nums:
            first_row_idx = row
            transpose_first_row_idx = first_nums[first_num]
        else:
            first_nums[first_num] = row

    first_row = arr[first_row_idx]
    transpose_first_row = arr[transpose_first_row_idx]

    board = [first_row]

    for idx in range(1, n):
        # 첫 번째 숫자가 transpose_first_row의 idx번째 숫자와 일치하는 row 번호를 dic에서 찾아서 붙이면 됨
        target_num = transpose_first_row[idx]
        target_row_idx = first_nums[target_num]
        target_row = arr[target_row_idx]
        board.append(target_row)

    for row in board:
        print(" ".join(map(str, row)))