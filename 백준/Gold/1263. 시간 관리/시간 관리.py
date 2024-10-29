import sys
input = sys.stdin.readline

arr = [list(map(int,input().split())) for _ in range(int(input()))]
arr.sort(key=lambda x: -x[1])

time = 1e9
for t,s in arr:
    time = min(time, s)
    time -= t

if time >= 0:
    print(time)
else:
    print(-1)