def is_safe(row, col, cols, diagonals, anti_diagonals):
    if col in cols:
        return False
    if (row - col) in diagonals:
        return False
    if (row + col) in anti_diagonals:
        return False
    return True


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())

    count = 0

    def recursion(row, cols, diagonals, anti_diagonals):
        global count

        if row == n:
            count += 1
            return

        for col in range(n):
            if is_safe(row, col, cols, diagonals, anti_diagonals):
                recursion(row + 1, cols | {col}, diagonals | {row - col}, anti_diagonals | {row + col})

    recursion(0, set(), set(), set())

    print(f"#{test_case} {count}")