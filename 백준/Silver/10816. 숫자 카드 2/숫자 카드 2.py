import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
candidates = list(map(int, input().split()))

dic = {}
for i in range(len(arr)):
    if arr[i] in dic:
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1

print(" ".join(map(lambda x: str(dic[x]) if x in dic else "0", candidates)))