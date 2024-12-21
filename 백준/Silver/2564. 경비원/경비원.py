import sys

input = sys.stdin.readline

width, height = map(int, input().split())
n = int(input())
pos = []
for _ in range(n):
    pos.append(list(map(int, input().split())))
d = list(map(int, input().split()))

total = 0
for i in range(n):
    a, b = sorted([d, pos[i]])
    dir_a, dis_a = a
    dir_b, dis_b = b

    if dir_a == dir_b:
        total += abs(dis_a - dis_b)
        continue

    if dir_a == 1:
        if dir_b == 2:
            total += min(dis_a + dis_b, 2*width - dis_a - dis_b) + height
        elif dir_b == 3:
            total += dis_a + dis_b
        elif dir_b == 4:
            total += width - dis_a + dis_b

    elif dir_a == 2:
        if dir_b == 3:
            total += dis_a + height - dis_b
        elif dir_b == 4:
            total += width - dis_a + height - dis_b

    elif dir_a == 3:
        if dir_b == 4:
            total += min(dis_a + dis_b, 2*height - dis_a - dis_b) + width

print(total)