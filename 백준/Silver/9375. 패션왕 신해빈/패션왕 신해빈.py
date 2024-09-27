import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    dic = {}
    for _ in range(n):
        clothing, category = map(str, input().split())
        if category in dic:
            dic[category].append(clothing)
        else:
            dic[category] = [clothing]
    choice = 1
    for key in dic.keys():
        choice *= len(set(dic[key]))+1
    choice -= 1
    print(choice)