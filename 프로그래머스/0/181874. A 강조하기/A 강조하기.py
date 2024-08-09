def solution(myString):
    answer = ''
    for i in myString:
        if i == 'a' or i == 'A':
            myString = myString.replace(i, i.upper())
        else:
            myString = myString.replace(i, i.lower())
    return myString