T = int(input())

for test_case in range(1, T+1):
    n, length = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    # 가로
    horizontal = 0
    for row in board:
        do_continue = False
        # while count stack
        idx = 0

        num = row[0]
        count = 0
        prev_num = row[0]

        nums = []
        counts = []
        while idx < n:
            num = row[idx]
            if num == prev_num:
                count += 1
            else:
                nums.append(prev_num)
                counts.append(count)

                prev_num = num
                count = 1
            idx += 1
            if idx == n:
                nums.append(num)
                counts.append(count)

        if len(nums) != 1:
            for i in range(len(nums)):
                if i == 0:
                    if nums[i] < nums[i+1] - 1:
                        do_continue = True
                        break
                    if nums[i] < nums[i+1]:
                        if counts[i] < length:
                            do_continue = True
                            break
                elif i == len(nums) - 1:
                    if nums[i] < nums[i-1] - 1:
                        do_continue = True
                        break
                    if nums[i] < nums[i-1]:
                        if counts[i] < length:
                            do_continue = True
                            break
                else:
                    if nums[i] < nums[i+1] - 1 or nums[i] < nums[i-1] - 1:
                        do_continue = True
                        break
                    if nums[i] < nums[i+1] and nums[i] < nums[i-1]:
                        if counts[i] < length * 2:
                            do_continue = True
                            break
                    elif nums[i] < nums[i+1] or nums[i] < nums[i-1]:
                        if counts[i] < length:
                            do_continue = True
                            break

        if do_continue:
            continue
        horizontal += 1

    # 세로
    vertical = 0
    for j in range(n):
        col = []
        for row in range(n):
            col.append(board[row][j])

        do_continue = False
        idx = 0

        num = col[0]
        count = 0
        prev_num = col[0]

        nums = []
        counts = []
        while idx < n:
            num = col[idx]
            if num == prev_num:
                count += 1
            else:
                nums.append(prev_num)
                counts.append(count)
                prev_num = num
                count = 1
            idx += 1
            if idx == n:
                nums.append(num)
                counts.append(count)

        if len(nums) != 1:
            for i in range(len(nums)):
                if i == 0:
                    if nums[i] < nums[i+1] - 1:
                        do_continue = True
                        break
                    if nums[i] < nums[i+1]:
                        if counts[i] < length:
                            do_continue = True
                            break
                elif i == len(nums) - 1:
                    if nums[i] < nums[i-1] - 1:
                        do_continue = True
                        break
                    if nums[i] < nums[i-1]:
                        if counts[i] < length:
                            do_continue = True
                            break
                else:
                    if nums[i] < nums[i+1] - 1 or nums[i] < nums[i-1] - 1:
                        do_continue = True
                        break

                    if nums[i] < nums[i+1] and nums[i] < nums[i-1]:
                        if counts[i] < length * 2:
                            do_continue = True
                            break

                    elif nums[i] < nums[i+1] or nums[i] < nums[i-1]:
                        if counts[i] < length:
                            do_continue = True
                            break

        if do_continue:
            continue
        vertical += 1

    answer = horizontal + vertical
    print(f"#{test_case} {answer}")
