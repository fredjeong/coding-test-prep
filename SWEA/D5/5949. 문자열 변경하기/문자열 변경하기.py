from collections import deque

T = int(input())

for test_case in range(1, T+1):
    # 두 문자열의 길이는 모두 10**5 이하
    s = input().strip()
    t = input().strip()

    # s와 t가 동일하다면 움직일 필요가 없다
    if s == t:
        print(f"#{test_case} {0}")
        continue

    # 문자열의 길이
    n = len(s)

    q_1 = deque()
    q_2 = deque()
    cnt = 0

    for i in range(n):
        if s[i] != t[i]:
            if s[i] == "a":
                q_1.append(i)
            else:
                q_2.append(i)

    while q_1:
        x = q_1.popleft()
        y = q_2.popleft()
        cnt += abs(x - y)

    print(f"#{test_case} {cnt}")