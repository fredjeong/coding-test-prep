T = int(input())

for test_case in range(1, T+1):
    n, k = map(int, input().split())
    arr = sorted(map(int, input().split()))

    min_diff = 1e9
    for i in range(n-k+1):
        min_diff = min(min_diff, arr[i+k-1] - arr[i])

    print(f"#{test_case} {min_diff}")