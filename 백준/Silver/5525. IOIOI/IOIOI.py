import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

cursor, count, result = 0, 0, 0

while cursor < (m-1):
    if s[cursor:cursor + 3] == 'IOI':
        count += 1
        cursor += 2
        if count == n:
            result += 1
            count -= 1
    else:
        cursor += 1
        count = 0

print(result)