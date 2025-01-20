T = int(input())

for _ in range(T):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    count = 0

    check = [False for _ in range(n)]
    for idx in range(n):
        ans = idx + 1
        num = arr[0][idx]
        if num == ans:
            check[idx] = True

    for idx in range(n-1, 0, -1):
        if not check[idx]:
            for sub_idx in range(1, idx+1):
                if check[sub_idx]:
                    check[sub_idx] = False
                else:
                    check[sub_idx] = True

            count += 1

        if False not in check:
            break

    print(count)