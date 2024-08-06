def solution(n):
    answer = ''
    n = str(n)
    n = sorted(n, reverse = True)
    for i in n:
        answer += i
    return int(answer)