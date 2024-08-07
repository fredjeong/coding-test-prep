def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    first_score = 0
    second_score = 0
    third_score = 0
    
    for i in range(len(answers)):
        first_index = i % len(first)
        second_index = i % len(second)
        third_index = i % len(third)
        if answers[i] == first[first_index]:
            first_score += 1
        if answers[i] == second[second_index]:
            second_score += 1
        if answers[i] == third[third_index]:
            third_score += 1
    
    scores = [first_score, second_score, third_score]
    answer = []
    for index, s in enumerate(scores):
        if s == max(scores):
            answer.append(index + 1)

    return answer