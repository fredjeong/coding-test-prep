import sys

input = sys.stdin.readline

T = int(input())

def is_vps(line):
    stack = []
    for i in range(len(line)):
        if i == 0 and line[i] == ")":
            return "NO"

        if line[i] == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                return "NO"
            stack.pop()
    
    if len(stack) != 0:
        return "NO"
    
    return "YES"

for _ in range(T):
    line = input().strip()
    result = is_vps(line)
    print(result)