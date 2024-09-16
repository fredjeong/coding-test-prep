import sys

input = sys.stdin.readline

M = int(input())

S = set()

for _ in range(M):
    line = list(input().split())

    if len(line) == 1:
        oper = line[0]
    elif len(line) == 2:
        oper = line[0]
        x = int(line[1])
    
    if oper == "add":
        if x not in S:
            S.add(x)
    elif oper == "remove":
        if x in S:
            S.remove(x)
    elif oper == "check":
        if x in S:
            print(1)
        else:
            print(0)
    elif oper == "toggle":
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif oper == "all":
        S = set()
        for i in range(1, 21):
            S.add(i)
    elif oper == "empty":
        S = set()
