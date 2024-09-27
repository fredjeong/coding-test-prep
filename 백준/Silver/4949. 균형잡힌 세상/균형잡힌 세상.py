import sys
from collections import deque

input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    if sentence==".":
        break
    
    q = deque()
    result = "yes"

    for char in sentence:
        if char not in ["(", ")", "[", "]"]:
            continue
        if char=="(" or char=="[":
            q.append(char)
        else:
            if not q:
                result = "no"
                break
            temp = q.pop()
            if (char==")" and temp=="(") or (char=="]" and temp=="["):
                pass
            else:
                result = "no"
                break
    
    if q:
        result = "no"

    print(result)