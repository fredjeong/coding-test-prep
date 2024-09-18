import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())
    n -= 1
    floor = str(n%h+1)
    num = str(n//h+1)
    if len(num) == 1:
        print(floor + "0" + num)
    else:
        print(floor + num)