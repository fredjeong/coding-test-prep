import sys

input = sys.stdin.readline

width, height = map(int, input().split())
n = int(input())

xs = [0, height]
ys = [0, width]

for _ in range(n):
    direction, num = map(int, input().split())
    if direction == 0:
        xs.append(num)
    else:
        ys.append(num)

xs.sort()
ys.sort()

max_dis_x = 0
max_dis_y = 0

for i in range(len(xs) - 1):
    max_dis_x = max(max_dis_x, xs[i+1] - xs[i])
for i in range(len(ys) - 1):
    max_dis_y = max(max_dis_y, ys[i+1] - ys[i])

print(max_dis_x * max_dis_y)