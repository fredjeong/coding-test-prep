import sys

input = sys.stdin.readline

N = 41
fib_0 = [0 for _ in range(N)]
fib_1 = [0 for _ in range(N)]

fib_0[0] = 1
fib_1[1] = 1
for i in range(2, N):
    fib_0[i] = fib_0[i-1] + fib_0[i-2]
    fib_1[i] = fib_1[i-1] + fib_1[i-2]

T = int(input())
for _ in range(T):
    num = int(input())
    print(fib_0[num], fib_1[num])