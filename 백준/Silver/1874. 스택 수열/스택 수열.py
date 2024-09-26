import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
seq = [int(input()) for _ in range(n)]
q = deque([i for i in range(1, n+1)])

stack = []
is_break = False
result = []

for num in seq:
    # push하는 경우
    if len(stack)==0:
        stack.append(q.popleft())
        result.append("+")
    while stack[-1] < num:
        stack.append(q.popleft())
        result.append("+")
    while True:
        temp = stack.pop()
        if temp == num:
            result.append("-")
            break
        else:
            is_break = True
            break
    if is_break == True:
        print("NO")
        break

if is_break == False:
    for re in result:
        print(re)