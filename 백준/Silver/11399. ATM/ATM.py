import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

new_arr = [arr[0]]
for i in range(1, N):
    new_arr.append(new_arr[i-1] + arr[i])

print(sum(new_arr))