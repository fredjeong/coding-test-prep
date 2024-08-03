def solution(emergency):
    answer = []
    emergency_sorted = sorted(emergency, reverse = True)
    for i in emergency:
        answer.append(emergency_sorted.index(i) + 1)
    return answer