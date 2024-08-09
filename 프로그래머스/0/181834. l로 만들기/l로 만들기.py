def solution(myString):
    answer = ''
    for i in myString:
        temp = [i, "l"]
        if sorted(temp).index(i) == 0:
            answer += "l"
        else:
            answer += i
    return answer