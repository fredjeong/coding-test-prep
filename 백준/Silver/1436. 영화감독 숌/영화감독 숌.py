import sys

input = sys.stdin.readline

N = int(input())

num = 1
idx = 666
while num < N:
    idx += 1
    if "666" not in str(idx):
        continue
    num += 1
print(idx)