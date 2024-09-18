import sys

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

floor = 1
while floor < N:
    for i in range(floor+1):
        if i == 0:
            arr[floor][i] += arr[floor-1][i]
        elif i == floor:
            arr[floor][i] += arr[floor-1][i-1]
        else:
            arr[floor][i] += max(arr[floor-1][i], arr[floor-1][i-1])
    floor += 1

print(max(arr[floor-1]))