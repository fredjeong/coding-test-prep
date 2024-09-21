import sys

input = sys.stdin.readline

N = int(input())

two = 0
five = 0
for i in range(1, N+1):
    while i:
        if i % 2 == 0:
            two += 1
            i //= 2
        if i % 5 == 0:
            five += 1
            i //= 5
        if i % 2 != 0 and i % 5 != 0:
            break
print(min(two, five))