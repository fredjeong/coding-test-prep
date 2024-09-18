import sys

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    age, name = input().strip().split()
    arr.append([int(age), name, i])

arr = sorted(arr, key=lambda x:[x[0], x[2]])

for elem in arr:
    print(elem[0], elem[1])
