def solution(common):
    if common[2]-common[1] == common[1] - common[0]:
        answer = common[-1] + (common[-1] - common[-2])
    elif common[2] / common[1] == common[1] / common[0]:
        answer = common[-1] * (common[-1] / common[-2])
    return answer