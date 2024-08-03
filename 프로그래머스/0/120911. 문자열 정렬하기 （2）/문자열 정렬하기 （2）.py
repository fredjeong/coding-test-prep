def solution(my_string):
    answer = ''
    my_string = my_string.lower()
    my_string = sorted(my_string)
    for i in my_string:
        answer += i
    return answer