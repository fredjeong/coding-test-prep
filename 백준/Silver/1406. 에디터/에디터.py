import sys
from collections import deque

input = sys.stdin.readline

before_cursor = deque(str(input().strip()))
after_cursor = deque()

M = int(input())

for _ in range(M):
    line = list(map(str, input().split()))
    if line == ['L']:
        if before_cursor:
            char = before_cursor.pop()
            after_cursor.appendleft(char)
    elif line == ['D']:
        if after_cursor:
            char = after_cursor.popleft()
            before_cursor.append(char)
    elif line == ['B']:
        if before_cursor:
            before_cursor.pop()

    else:
        new_str = line[1]
        before_cursor.append(new_str)

print("".join(map(str, before_cursor)) + "".join(map(str, after_cursor)))