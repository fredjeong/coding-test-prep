def get_primes(lower_bound=0, upper_bound=10**6):
    arr = [True for _ in range(upper_bound + 1)]
    arr[0] = False
    arr[1] = False
    for i in range(2, int(upper_bound**0.5)+1):
        for j in range(i*2, upper_bound+1, i):
            arr[j] = False

    primes = set(i for i in range(lower_bound, upper_bound+1) if arr[i])
    return primes

primes = get_primes(0, 10**6)

T = int(input()) # 테스트 케이스의 개수

for test_case in range(1, T+1):
    d, a, b = map(int, input().split())
    d = str(d)

    count = 0

    # 소수가 D를 포함하면 특별한 소수
    for num in range(a, b+1):
        if num in primes and d in str(num):
            count += 1

    print(f"#{test_case} {count}")