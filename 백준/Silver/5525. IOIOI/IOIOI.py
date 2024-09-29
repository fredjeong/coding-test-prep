import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

target = "IO"*n + "I"

count = 0
for i in range(m-(2*n)):
    if i==m-(2*n+1):
        temp = s[i:]
    else:
        temp = s[i:i+(2*n+1)]
    if temp==target:
        count += 1
print(count)