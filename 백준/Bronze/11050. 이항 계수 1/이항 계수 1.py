import sys

input = sys.stdin.readline

N, K = map(int, input().split())

numer = 1
denom = 1
for i in range(K):
    numer *= N-i
    denom *= i+1

print(numer // denom)