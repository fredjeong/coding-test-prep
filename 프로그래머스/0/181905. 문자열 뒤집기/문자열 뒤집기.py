def solution(my_string, s, e):
    temp_start = my_string[:s]
    temp_mid = my_string[s:e+1]
    temp_end = my_string[e+1:]
    
    temp_mid_reversed = ''
    for i in temp_mid:
        temp_mid_reversed = i + temp_mid_reversed
    
    answer = temp_start + temp_mid_reversed + temp_end
    return answer