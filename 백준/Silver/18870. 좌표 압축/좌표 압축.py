import sys
import heapq

input = sys.stdin.readline

N = int(input())
arr = list(map(lambda x: -int(x), input().split()))

S = list(set(arr))
heapq.heapify(S)

dic = {}
while S:
    num = heapq.heappop(S)
    rep = len(S)
    dic[num] = rep

print(" ".join(map(lambda x: str(dic[x]), arr)))