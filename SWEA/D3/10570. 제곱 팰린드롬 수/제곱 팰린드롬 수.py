T = int(input())

for test_case in range(1, T+1):
    a, b = map(int, input().split())
    count = 0

    for num in range(a, b+1):
        s_num = str(num)

        early_stopping = False
        # 주어진 수가 팰린드롬인지 확인
        for i in range(len(s_num)//2):
            if s_num[i] != s_num[len(s_num) - 1 - i]:
                early_stopping = True

        # 하나라도 걸렸으면 다음 숫자로 넘어간다
        if early_stopping:
            continue

        # 제곱수가 팰린드롬인지 확인
        if num ** 0.5 == int(num ** 0.5):
            new_s_num = str(int(num**0.5))
            for i in range(len(new_s_num)//2):
                if new_s_num[i] != new_s_num[len(new_s_num) - 1 - i]:
                    early_stopping = True

            if early_stopping:
                continue

            if not early_stopping:
                count += 1

    print(f"#{test_case} {count}")