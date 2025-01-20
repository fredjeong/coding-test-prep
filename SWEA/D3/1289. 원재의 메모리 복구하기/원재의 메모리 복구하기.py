T = int(input())

for test_case in range(1, T+1):
    s = input().strip()
    check = [False if char == "1" else True for char in s]

    count = 0
    for idx in range(len(check)):
        if not check[idx]:
            count += 1
            for sub_idx in range(idx, len(check)):
                if not check[sub_idx]:
                    check[sub_idx] = True
                else:
                    check[sub_idx] = False
        if False not in check:
            break

    print(f"#{test_case} {count}")