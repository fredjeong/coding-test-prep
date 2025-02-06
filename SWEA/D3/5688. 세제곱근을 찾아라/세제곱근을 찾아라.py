dic = {}
for i in range(1, 10**6+1):
    dic[i**3] = i

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    if n not in dic:
        answer = -1
    else:
        answer = dic[n]
    print(f"#{test_case} {answer}")