import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    line = list(input().strip().split())
    num = int(line[0])
    string = line[1]
    result = ""
    for i in range(len(string)):
        result += string[i]*num
    print(result)