import sys

input = sys.stdin.readline

N = int(input())

dic = {}
for _ in range(N):
    num = int(input())
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

for key in sorted(dic.keys()):
    for _ in range(dic[key]):
        print(key)