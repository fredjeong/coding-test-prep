def solution(array, commands):
    answer = []
    for i in commands:
        start = i[0] - 1
        end = i[1]
        num = i[2] - 1
        new_array = sorted(array[start:end])
        answer.append(new_array[num])
    return answer