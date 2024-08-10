def solution(myStr):
    answer = []
    myStr = myStr.replace('b', 'a')
    myStr = myStr.replace('c','a')
    myStr = myStr.split("a")
    for i in myStr:
        if i != '':
            answer.append(i)
    if answer == []:
        answer.append("EMPTY")
    return answer