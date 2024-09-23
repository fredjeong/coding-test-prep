import sys

input = sys.stdin.readline

N = int(input())

if N==0:
    print(1)
else:
    t = [0 for _ in range(N+1)]
    t[0] = 1
    for i in range(1, N+1):
        for j in range(i):
            t[i] += t[i-1-j]*t[j]
    print(t[-1])