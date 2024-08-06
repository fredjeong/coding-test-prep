def solution(n):
    watermelon = ["수", "박"]
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += watermelon[0]
        else:
            answer += watermelon[1]
    return answer