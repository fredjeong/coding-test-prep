def solution(survey, choices):
    scores = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for question, choice in zip(survey, choices):
        if 4 - choice > 0:
            scores[question[0]] += 4 - choice
        elif 4 - choice < 0:
            scores[question[1]] += abs(4 - choice)
    
    answer = ''
    if scores["R"] >= scores["T"]:
        answer += "R"
    else:
        answer += "T"
    
    if scores["C"] >= scores["F"]:
        answer += "C"
    else:
        answer += "F"

    if scores["J"] >= scores["M"]:
        answer += "J"
    else:
        answer += "M"

    if scores["A"] >= scores["N"]:
        answer += "A"
    else:
        answer += "N"
        
    return answer