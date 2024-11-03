import sys
input = sys.stdin.readline

arr = []
while True:
    num = input().strip()
    if not num:
        break
    arr.append(int(num))
print(sum(arr))