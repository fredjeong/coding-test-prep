import sys

input = sys.stdin.readline

# 일곱 난장이의 키의 합은 정확하게 100
# 주어진 수 중 7개를 선택해 그 합이 100인 경우 이들의 키를 오름차순으로 출력

heights = []
for _ in range(9):
    heights.append(int(input()))

heights.sort()

total = sum(heights)

for i in range(9):
    for j in range(9):
        if i<j:
            if total - heights[i] - heights[j] == 100:
                keys = [i, j]

for i in range(9):
    if i in keys:
        continue
    print(heights[i])