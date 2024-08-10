def solution(myString, pat):
    for i in range(len(myString)):
        if myString[-len(pat):] == pat:
            answer = myString
            break
        else:
            myString = myString[:-1]
    #for i in range(len(myString)):
    #    if i == 0:
    #        if myString[-len(pat):] == pat:
    #            answer = myString
    #            break
    #    else:
    #        temp = myString[:-i]
    #        if temp[-len(pat):] == pat:
    #            answer = temp
    #            break

    return answer