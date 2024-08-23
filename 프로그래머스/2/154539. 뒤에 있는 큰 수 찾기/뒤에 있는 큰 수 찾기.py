def solution(numbers):
    stack = []
    answer = [-1 for _ in range(len(numbers))]

    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            idx = stack.pop()
            answer[idx] = num
        stack.append(i)

    return answer

# 시간 초과
#def solution(numbers):
#    answer = []
#    numbers.reverse()
#    while len(numbers) > 0:
#        if len(numbers) == 1:
#            answer.append(-1)
#            break
#        else:
#            num = numbers.pop()
#
#            for i in reversed(range(len(numbers))):
#                if numbers[i] > num:
#                    answer.append(numbers[i])
#                    break
#                if i == 0:
#                    answer.append(-1)
#
#    return answer