def solution(my_string):
    answer = ''
    for k in my_string:
        if k not in answer:
            answer += k
    return answer