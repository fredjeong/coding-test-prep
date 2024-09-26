import sys

input = sys.stdin.readline

m, n = map(int, input().split())

if n in [0, 1]:
    print(0)
else:
    primes = []
    arr = [False for _ in range(n+1)]
    for i in range(2, int(n**0.5)+1):
        for j in range(i*2, n+1, i):
            arr[j] = True

    for i in range(m, n+1):
        if i < 2:
            continue
        if arr[i]==False:
            print(i)