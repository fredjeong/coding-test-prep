def solution(my_string, m, c):
    answer = ''
    i = 0
    while (c - 1) + (m * i) < len(my_string):
        answer += my_string[(c - 1) + (m * i)]
        i += 1
    return answer