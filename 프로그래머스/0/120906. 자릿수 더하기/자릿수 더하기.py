def solution(n):
    answer = []
    n = str(n)
    for k in n:
        k = int(k)
        answer.append(k)
    answer = sum(answer)
    return answer