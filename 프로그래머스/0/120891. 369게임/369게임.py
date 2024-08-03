def solution(order):
    answer = 0
    order = str(order)
    for k in order:
        if k == '3' or k == '6' or k == '9':
            answer += 1
    return answer