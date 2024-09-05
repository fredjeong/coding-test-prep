def solution(k, d):
    answer = 0
    for x in range(0, d//k+1):
        answer += int((d**2 - (x*k)**2)**0.5)//k + 1
    return answer