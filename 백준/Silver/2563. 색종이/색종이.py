import sys

input = sys.stdin.readline

board = [[False for _ in range(100)] for _ in range(100)]

n = int(input())
for _ in range(n):
    x1, y1 = map(int, input().split())# 좌상단 점
    x1 -= 1
    y1 -= 1
    for i in range(x1, x1+10):
        for j in range(y1, y1+10):
            board[i][j] = True

count = 0
for row in board:
    count += row.count(True)

print(count)