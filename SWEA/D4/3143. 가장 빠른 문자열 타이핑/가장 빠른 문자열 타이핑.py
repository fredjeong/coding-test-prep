T = int(input())

for test_case in range(1, T+1):
    a, b = input().split()

    cnt = a.count(b)
    answer = cnt + len(a) - cnt*len(b)
    print(f"#{test_case} {answer}")