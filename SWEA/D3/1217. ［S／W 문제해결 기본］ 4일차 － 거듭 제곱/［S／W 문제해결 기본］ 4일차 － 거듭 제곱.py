def recursion(T, n, m, val, cnt):
    if cnt == m:
        print(f"#{test_case} {val}")
        return
    recursion(T, n, m, val*n, cnt+1)

for test_case in range(1, 11):
    T = int(input())
    n, m = map(int, input().split())
    recursion(T, n, m, 1, 0)