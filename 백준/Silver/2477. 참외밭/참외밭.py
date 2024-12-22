import sys

input = sys.stdin.readline

k = int(input())

points = [[0, 0]]
for _ in range(5):
    direction, dis = map(int, input().split())
    x, y = points[-1]
    if direction == 1:
        points.append([x+dis, y])
    elif direction == 2:
        points.append([x-dis, y])
    elif direction == 3:
        points.append([x, y-dis])
    else:
        points.append([x, y+dis])

xs = set()
ys = set()

for point in points:
    x, y = point
    xs.add(x)
    ys.add(y)

x1, x2, x3 = sorted(xs)
y1, y2, y3 = sorted(ys)

total = (x3 - x1) * (y3 - y1)

for point in [[x1, y1], [x1, y3], [x3, y1], [x3, y3]]:
    if point not in points:
        missing_point = point
        break

print((total - abs(x2 - missing_point[0]) * abs(y2 - missing_point[1]))*k)