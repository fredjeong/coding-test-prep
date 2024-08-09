def solution(myString, pat):
    temp = myString.replace("A", "0").replace("B", "A").replace("0", "B")
    if pat in temp:
        answer = 1
    else:
        answer = 0
    return answer