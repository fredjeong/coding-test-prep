import sys

input = sys.stdin.readline

while True:
    line = input().strip()
    if line == "":
        break
    else:
        a, b = map(int, line.split())
        print(a+b)