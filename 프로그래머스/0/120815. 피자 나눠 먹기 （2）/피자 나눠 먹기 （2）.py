def solution(n):
    if n % 6 == 0:
        answer = n // 6
    elif n % 6 == 1:
        answer = n
    elif n % 6 == 2:
        answer = n // 6 * 3 + 1
    elif n % 6 == 3: 
        answer = n // 3
    elif n % 6 == 4: 
        answer = n // 6 * 3 + 2
    elif n % 6 == 5: 
        answer = n
    return answer
