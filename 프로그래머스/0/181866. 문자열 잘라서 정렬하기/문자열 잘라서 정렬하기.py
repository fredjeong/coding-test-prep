def solution(myString):
    answer = []
    myString = myString.split("x")
    for i in myString:
        if i != "":
            answer.append(i)
    answer.sort()
    return answer