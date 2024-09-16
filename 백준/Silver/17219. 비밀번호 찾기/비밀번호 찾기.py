import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dic = {}
for _ in range(N):
    site, pw = input().strip().split()
    dic[site] = pw

for _ in range(M):
    site = input().strip()
    print(dic[site])