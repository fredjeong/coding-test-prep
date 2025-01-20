T = int(input())

for test_case in range(1, T+1):
    s = input().strip()

    a = 1
    b = 1

    for char in s:
        if char == "L":
            b += a
        else:
            a += b

    print(f"#{test_case} {a} {b}")