def solution(my_string, num1, num2):
    answer = ''
    for k in range(len(my_string)):
        if k == num1:
            answer += my_string[num2]
        elif k == num2:
            answer += my_string[num1]
        else:
            answer += my_string[k]
    return answer