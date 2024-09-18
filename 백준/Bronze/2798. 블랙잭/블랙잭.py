import sys

input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

def find(N, M, arr, num):
    global result
    visited = []
    temp = arr[:]
    for _ in range(len(temp)-1):
        start = temp.pop()
        for i in range(len(temp)):
            new = num + start + temp[i]
            if new > M:
                continue            
            if new in visited:
                continue
            visited.append(new)
            if new > result:
                result = new

global result
result = -1
for _ in range(N-2):
    start = cards.pop()
    find(N, M, cards, start)

print(result)
