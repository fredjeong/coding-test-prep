import sys

input = sys.stdin.readline

T = int(input())


for _ in range(T):
    log = input().strip()
    result = 0
    count = 0
    for ox in log:
        if ox == "O":
            count += 1
            result += count
        else:
            count = 0
    print(result)