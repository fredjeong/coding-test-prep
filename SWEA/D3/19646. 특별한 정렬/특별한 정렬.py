from collections import deque

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = deque(sorted(map(int, input().split())))

    answer = []
    for i in range(n):
        if i == 10:
            break

        if i % 2 == 0:
            answer.append(arr.pop())
        else:
            answer.append(arr.popleft())

    print(f"#{test_case} {' '.join(map(str, answer))}")