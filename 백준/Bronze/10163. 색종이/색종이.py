import sys

input = sys.stdin.readline

n = int(input())
board = [[-1 for _ in range(1001)] for _ in range(1001)]
areas = [0 for _ in range(n)]
for i in range(n):
    x1, y1, width, height = map(int, input().split())
    for j in range(x1, x1+width):
        for k in range(y1, y1+height):
            original = board[j][k]
            if original != -1:
                areas[original] -= 1
            board[j][k] = i
    areas[i] = width * height

for area in areas:
    print(area)