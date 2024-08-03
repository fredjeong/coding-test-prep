def solution(n, numlist):
    answer = []
    for k in numlist:
        if k % n == 0:
            answer.append(k)
    return answer