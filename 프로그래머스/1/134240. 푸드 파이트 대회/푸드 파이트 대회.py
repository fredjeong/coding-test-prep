def solution(food):
    order = ''
    for i in range(1, len(food)):
        food[i] = food[i] // 2
        for j in range(food[i]):
            order += str(i)
    
    reverse = ''
    for i in order:
        reverse = i + reverse
    
    answer = order + '0' + reverse
    return answer
    