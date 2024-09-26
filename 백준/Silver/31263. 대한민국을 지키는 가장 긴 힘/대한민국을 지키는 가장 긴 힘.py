import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
string = deque(input().strip())

count = 0
stack = ""
result = []
while string:
    stack += string.popleft()
    if not string and stack:
        if int(stack) <= 641:
            count += 1
            break
        else:
            count += 2
            break
    if len(stack)==3:
        if string[0]=="0":
            count += 1
            stack = stack[1:]
        else:
            if int(stack) <= 641:
                count += 1
                stack = ""
            else:
                count += 1
                stack = stack[2]
print(count)