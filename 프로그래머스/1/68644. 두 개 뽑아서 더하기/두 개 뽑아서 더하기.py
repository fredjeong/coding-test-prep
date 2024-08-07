def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i<j:
                num = numbers[i] + numbers[j]
                if num not in answer:
                    answer.append(num)
    answer.sort()
    return answer