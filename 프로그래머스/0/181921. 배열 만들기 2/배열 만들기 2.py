def solution(l, r):
    answer = []
    for i in range(l, r+1):
        temp = ''
        for j in str(i):
            if j == "0" or j == "5":
                temp += j
        if len(temp) == len(str(i)):
            answer.append(i)
    if answer == []:
        answer.append(-1)
    return answer