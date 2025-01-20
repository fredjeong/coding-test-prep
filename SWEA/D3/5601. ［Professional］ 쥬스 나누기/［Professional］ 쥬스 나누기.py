T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    answer = " ".join(f"1/{n}" for _ in range(n))
    print(f"#{test_case} {answer}")