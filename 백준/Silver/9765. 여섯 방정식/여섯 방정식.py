import sys

input = sys.stdin.readline

c1, c2, c3, c4, c5, c6 = map(int, input().split())

answer = []
for x1 in range(2, int(c1**0.5+1)):
    if c1/x1 == c1//x1:
        x2 = c1//x1
        if c5/x2 == c5//x2:
            x3 = c5//x2
            answer += [x1, x2, x3]
            break
        elif c5/x1 == c5//x1:
            x3 = c5//x1
            answer += [x2, x1, x3]
            break

for x5 in range(2, int(c6**0.5+1)):
    if c6/x5 == c6//x5:
        x6 = c6//x5
        if c3/x6 == c3//x6:
            x7 = c3//x6
            answer += [x5, x6, x7]
            break
        elif c3/x5 == c3//x5:
            x7 = c3//x5
            answer += [x6, x5, x7]
            break

print(" ".join(map(str, answer)))