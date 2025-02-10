T = int(input())
for test_case in range(1, T+1):
    n = int(input())

    arr = []
    for _ in range(n):
        arr.append(int(input()))

    cnt = 0

    s = set()
    for i in range(1, len(arr)):
        num = arr[i]
        if num in s:
            continue

        # 공차 구하기
        diff = num - 1

        for i in range(num, arr[-1]+1, diff):
            s.add(i)
        cnt += 1

    print(f"#{test_case} {cnt}")
