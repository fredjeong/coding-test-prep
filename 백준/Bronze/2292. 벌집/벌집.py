import sys

input = sys.stdin.readline

N = int(input())

if N==1:
    print(1)
else:
    dp = [1]
    ring = 1
    while dp[-1] < N:
        dp.append(dp[-1] + 6*ring)
        ring += 1
    print(len(dp))