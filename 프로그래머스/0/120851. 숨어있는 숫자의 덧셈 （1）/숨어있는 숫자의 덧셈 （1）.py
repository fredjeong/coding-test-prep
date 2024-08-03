def solution(my_string):
    answer = 0
    for k in my_string:
        if k.isdigit():
            answer += int(k)
    return answer