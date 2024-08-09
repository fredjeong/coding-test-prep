def solution(my_strings, parts):
    answer = ''
    for i, j in zip(my_strings, parts):
        s = j[0]
        e = j[1]
        answer += i[s]
        for k in range(e - s):
            answer += i[s + k + 1]
    return answer