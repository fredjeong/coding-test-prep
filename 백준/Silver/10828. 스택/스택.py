import sys

input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    line = input().strip().split()
    if len(line) == 1:
        if line[0] == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif line[0] == "size":
            print(len(stack))
        elif line[0] == "empty":
            if stack:
                print(0)
            else:
                print(1)
        elif line[0] == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)
    else:
        if line[0] == "push":
            stack.append(int(line[1]))