def solution(my_string, is_prefix):
    answer = 0
    prefix = ''
    if len(my_string) >= len(is_prefix):
        for i in range(len(is_prefix)):
            prefix += my_string[i]
    if prefix == is_prefix:
        answer = 1
    return answer