import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = []
for i in range(len(arr)):
    temp = arr[:]
    target = temp[i]
    del temp[i]
    count = 1
    for j in range(len(temp)):
        if temp[j][0] > target[0] and temp[j][1] > target[1]:
            count += 1
    result.append(count)
print(" ".join(map(str, result)))