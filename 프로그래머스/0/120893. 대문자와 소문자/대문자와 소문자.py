def solution(my_string):
    answer = ''
    for k in my_string:
        if k == k.upper():
            k = k.lower()
            answer += k
        else:
            k = k.upper()
            answer += k
    return answer