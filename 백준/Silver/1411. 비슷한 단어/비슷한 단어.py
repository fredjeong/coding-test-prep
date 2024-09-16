import sys

input = sys.stdin.readline

N = int(input())

def solution(input, N):
    if N==0 or N==1:
        return 0

    arr = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    dic = {}
    for _ in range(N):
        line = str(input().strip())
        idx = 0
        for i in range(len(line)):
            if line[i].isupper():
                continue
            line = line.replace(line[i], arr[idx])
            idx += 1
        if line in dic:
            dic[line] += 1
        else:
            dic[line] = 1

    answer = 0
    for value in dic.values():
        if value < 2:
            continue
        else:
            answer += int(value * (value-1) / 2)

    return answer

if __name__ == '__main__':
    result = solution(input, N)
    print(result)