def solution(number):
    temp = 0
    for i in str(number):
        temp += int(i)
    answer = temp % 9
    return answer