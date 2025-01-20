T = int(input())

for _ in range(T):
    n = int(input())

    if n % 3 == 1:
        print("impossible")

    elif n % 3 == 2:
        print("BA" + "BBA" * (n // 3))

    else:
        print("BBA" * (n//3))