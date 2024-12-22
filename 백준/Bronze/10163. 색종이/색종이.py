import sys

input = sys.stdin.readline

n = int(input())

board = [[-1 for _ in range(1001)] for _ in range(1001)]

for i in range(n):
    x, y, width, height = map(int, input().split())
    for j in range(x, x+width):
        for k in range(y, y+height):
            board[j][k] = i

for i in range(n):
    count = 0
    for j in range(1001):
        count += board[j].count(i)
    print(count)