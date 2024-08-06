def solution(d, budget):
    d = sorted(d)
    expenditure = 0
    answer = 0
    for i in d:
        if budget - expenditure >= i:
            expenditure += i
            answer += 1
    return answer