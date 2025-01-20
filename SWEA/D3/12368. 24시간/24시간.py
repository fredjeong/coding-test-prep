T = int(input())

for test_case in range(1, T+1):
    a, b = map(int, input().split())
    n = a + b
    if n >= 24:
        n -= 24
    
    print(f"#{test_case} {n}")