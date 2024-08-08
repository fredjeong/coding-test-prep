def solution(my_string, is_suffix):
    gnirts_ym = ''
    is_prefix = ''
    for i in my_string:
        gnirts_ym = i + gnirts_ym
    for j in is_suffix:
        is_prefix = j + is_prefix
    
    prefix = ''
    answer = 0
    if len(my_string) >= len(is_suffix):
        for i in range(len(is_suffix)):
            prefix += gnirts_ym[i]
        if prefix == is_prefix:
            answer = 1
    return answer