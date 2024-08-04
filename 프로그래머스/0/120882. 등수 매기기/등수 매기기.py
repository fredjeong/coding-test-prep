def solution(score):
    answer = []
    for english, maths in score:
        mean = (english + maths)*0.5
        answer.append(mean)
    answer = [sorted(answer, reverse = True).index(ele) + 1 for ele in answer]
    return answer