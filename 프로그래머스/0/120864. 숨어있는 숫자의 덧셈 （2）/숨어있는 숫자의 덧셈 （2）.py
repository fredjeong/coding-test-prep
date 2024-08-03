def solution(my_string):
    answer = 0
    buffer = ''
    for i in my_string:
        if i.isdigit():
            buffer += i
        else:
            buffer += ','
    buffer = buffer.split(',')
    for j in buffer:
        if j.isdigit():
            j = int(j)
            answer += j
    return answer