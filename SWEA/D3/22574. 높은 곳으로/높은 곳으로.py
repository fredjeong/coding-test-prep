T = int(input())

for _ in range(T):
    n, p = map(int, input().split())

    current_floor = 0

    for i in range(1, n+1):
        current_floor += i
        if current_floor == p:
            current_floor -= 1

    print(current_floor)
