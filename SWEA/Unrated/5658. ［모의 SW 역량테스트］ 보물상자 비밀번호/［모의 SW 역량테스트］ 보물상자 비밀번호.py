T = int(input())

for test_case in range(1, T+1):
    n, k = map(int, input().split())

    # n//k개 선택

    # 16진수 숫자 0-F가 공백 없이 N개 주어진다
    nums = input().strip()

    s = set()

    for i in range(n):
        if i > n - n//4:
            temp = nums[i:]
            temp += nums[:n//4 - len(temp)]
        else:
            temp = nums[i:i+n//4]

        num = int(temp, 16)
        s.add(num)

    s = sorted(s)

    print(f"#{test_case} {s[-k]}")