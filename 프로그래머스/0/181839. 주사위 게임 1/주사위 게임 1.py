def solution(a, b):
    answer = 0
    if a % 2 == 1 or b % 2 == 1:
        if a % 2 == 0 or b % 2 == 0:
            answer = 2 * (a + b)
        else:
            answer = a ** 2 + b ** 2
    else:
        answer = abs(a - b)        
    return answer