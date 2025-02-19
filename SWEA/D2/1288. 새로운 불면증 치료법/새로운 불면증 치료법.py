T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    ans = {str(i) for i in range(10)}
    s = set()
    cnt = 0
    while s != ans:
        s |= set(list(str(n * (cnt+1))))
        cnt += 1

    print(f"#{test_case} {n*cnt}")