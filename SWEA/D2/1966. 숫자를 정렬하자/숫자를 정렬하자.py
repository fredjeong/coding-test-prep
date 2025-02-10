T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(N - 1):
        min_idx = i
        for j in range(i+1, N):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    print(f"#{test_case} {' '.join(map(str, nums))}")