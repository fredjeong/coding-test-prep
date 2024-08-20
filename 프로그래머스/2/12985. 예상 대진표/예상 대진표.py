def solution(n,a,b):
    a = a - 1
    b = b - 1
    a_group = a // 2
    b_group = b // 2
    answer = 1
    
    while a_group != b_group:
        answer += 1
        a_group = a // (2**answer)
        b_group = b // (2**answer)
    
    return answer