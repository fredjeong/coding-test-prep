def solution(s):
    s = s.split(" ")
    temp = []
    for i in s:
        temp.append(int(i))
    maximum = max(temp)
    minimum = min(temp)
    answer = f"{minimum} {maximum}"
    return answer