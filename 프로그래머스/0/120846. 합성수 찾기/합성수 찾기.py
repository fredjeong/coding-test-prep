def solution(n):
    answer = 0
    answers = []
    for i in range(1,n+1):
        stack = 0
        for j in range(1, i+1):
            if i % j == 0:
                stack += 1
        answers.append(stack)
    for k in answers:
        if k >= 3:
            answer += 1
    return answer