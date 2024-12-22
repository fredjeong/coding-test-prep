import sys

input = sys.stdin.readline

board = [[False for _ in range(100)] for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())# 좌상단 점, 우하단 점
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = True

count = 0
for row in board:
    count += row.count(True)

print(count)