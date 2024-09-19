import sys

input = sys.stdin.readline

N = int(input())
x = 1
is_break = False
while x < N:
    temp = sum(map(int, list(str(x))))
    if x + temp == N:
        print(x)
        is_break = True
        break
    x += 1

if is_break == False:
    print(0)