from collections import defaultdict

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    dic = defaultdict(dict)
    for _ in range(3):
        string = input().strip()
        for i in range(n):
            if string[i] in dic[i]:
                dic[i][string[i]] += 1
            else:
                dic[i][string[i]] = 1

    cnt = 0
    for i in range(n):
        cnt += 3 - max(dic[i].values())

    print(f"#{test_case} {cnt}")