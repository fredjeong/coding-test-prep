import sys
input = sys.stdin.readline

n = int(input())

def solution(n):
    if n%2 == 0 or n%5 == 0:
        return -1
    else:
        target = 1
        answer = 1

        while target % n != 0:
            target = (target % n) * 10 + 1
            answer += 1

        return answer

print(solution(n))