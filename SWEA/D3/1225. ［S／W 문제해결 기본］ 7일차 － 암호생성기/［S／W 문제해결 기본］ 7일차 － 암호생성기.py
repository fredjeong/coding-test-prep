from collections import deque

for _ in range(10):
    test_case = int(input())
    arr = deque(map(int, input().split()))

    early_stopping = False
    while not early_stopping:
        for i in range(1, 6):
            num = arr.popleft()
            if num - i <= 0:
                num = 0
                arr.append(num)
                early_stopping = True
                break
            else:
                num -= i
                arr.append(num)

    print(f"#{test_case}", " ".join(map(str, arr)))