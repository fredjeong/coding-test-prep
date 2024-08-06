def solution(s):
    answer = True
    s = s.lower()
    temp = [0] * 2
    for i in s:
        if i == "p":
            temp[0] += 1
        elif i == "y":
            temp[1] += 1
    if temp[0] != temp[1]:
        answer = False
    return answer