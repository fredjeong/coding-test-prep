import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().strip()
    n = int(input())
    arr = deque(input().strip().strip("[]").split(','))
    if "" in arr:
        arr.pop()

    mode = 1
    do_break = False
    for order in p:
        if order=="R":
            mode += 1
            continue
        if order=="D":
            if arr:
                if mode%2==1:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                do_break = True
                break
    
    if do_break == False:
        if mode%2 == 0:
            arr.reverse()
            print("[" + ",".join(arr) + "]")
        else:
            print("[" + ",".join(arr) + "]")
    else:
        print("error")