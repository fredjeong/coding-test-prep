def solution(my_string):
    answer = ""
    keys = ['a', 'e', 'i', 'o', 'u']
    for k in my_string:
        if k not in keys:
            answer = answer + k
    return answer