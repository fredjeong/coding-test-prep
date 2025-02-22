T = int(input())

for test_case in range(1, T+1):
    n, p = map(int, input().split())

    # n개를 p개로 나누되, 곱이 가장 커지는 경우
    # 최대한 비슷하게 분할하면 됨

    answer = 1
    remainder = n % p
    for i in range(p):
        if i < n % p:
            answer *= n//p + 1
        else:
            answer *= n//p

    print(f"#{test_case} {answer}")