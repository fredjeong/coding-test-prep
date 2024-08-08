def solution(s):
    answer = 0
    x_count = 0
    not_x_count = 0
    for i in s:
        if x_count == not_x_count:
            answer += 1
            k = i
        if k == i:
            x_count += 1
        else:
            not_x_count += 1
    return answer