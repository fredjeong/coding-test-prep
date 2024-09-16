import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dic_num = {}
dic_name = {}
for i in range(1, N+1):
    name = str(input().strip())
    num = i
    dic_num[i] = name
    dic_name[name] = i

for _ in range(M):
    call = input().strip()
    if call.isdigit():
        print(dic_num[int(call)])
    else:
        print(dic_name[call])