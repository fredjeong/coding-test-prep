import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
start = 1
end = max(arr)

while start <= end: 
    mid = (start+end) // 2
    
    length = 0 
    for i in arr:
        if i >= mid:
            length += i - mid
    
    if length >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)