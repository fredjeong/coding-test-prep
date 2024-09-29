import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

l, r, count = 0, 0, 0
dic = defaultdict(int)
answer = 0
while r < n:
    if dic[arr[r]]==0:
        count += 1
    dic[arr[r]] += 1
    
    while count > 2:
        dic[arr[l]] -= 1
        if dic[arr[l]] == 0:
            count -= 1
        l += 1
    
    answer = max(answer, r-l+1)
    r += 1

print(answer)