import sys
import heapq

input = sys.stdin.readline

R, C = map(int, input().split())
arr = [str(input().strip()) for _ in range(R)]

words = []
heapq.heapify(words)

for i in range(R):
    stack = ""
    for j in range(C):
        if arr[i][j] == "#":
            if len(stack) > 1:
                heapq.heappush(words, stack)
            stack = ""
            continue
        if j == C-1:
            if stack == "":
                break
            else:
                stack += arr[i][j]
                heapq.heappush(words, stack)
                stack = ""
                break
        stack += arr[i][j]

for j in range(C):
    stack = ""
    for i in range(R):
        if arr[i][j] == "#":
            if len(stack) > 1:
                heapq.heappush(words, stack)
            stack = ""
            continue
        if i == R-1:
            if stack == "":
                break
            else:
                stack += arr[i][j]
                heapq.heappush(words, stack)
                stack = ""
                break
        stack += arr[i][j]

print(heapq.heappop(words))