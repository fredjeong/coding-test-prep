def solution(my_string, n):
    answer = ''
    for k in my_string:
        answer += k * n
    return answer