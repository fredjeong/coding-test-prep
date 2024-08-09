def solution(my_string):
    answer = []
    index = 0
    while index < len(my_string):
        if index != len(my_string):
            temp = ''
            for i in range(index, len(my_string)):
                temp += my_string[i]
            answer.append(temp)
        else:
            answer.append(my_string[index])
        index += 1
    answer.sort()
    return answer