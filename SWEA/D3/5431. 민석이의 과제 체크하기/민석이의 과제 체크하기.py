T = int(input())

for test_case in range(1, T+1):
    n, k = map(int, input().split())
    nums = set(map(int, input().split()))

    arr = []
    for i in range(1, 1+n):
        if i not in nums:
            arr.append(i)
    answer = " ".join(map(str, sorted(arr)))
    print(f"#{test_case} {answer}")