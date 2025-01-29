T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    for num in set(arr):
        if arr.count(num) in [1, 3]:
            answer = num
            break
    print(f"#{test_case} {answer}")