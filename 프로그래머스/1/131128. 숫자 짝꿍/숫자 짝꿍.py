def solution(X, Y):
    answer = ''
    dic = {}
    temp = ''
    for i in X:
        if i not in dic:
            if i in Y:
                X_count = X.count(i)
                Y_count = Y.count(i)
                dic[i] = min(X_count, Y_count)
    if len(dic) == 0:
        answer = '-1'
    elif len(dic) == 1 and "0" in dic:
        answer = '0'
    #else:
    #    temp = sorted(temp, reverse = True)
    #    for j in temp:
    #        answer += j
    #return answer
    else:
        arr = sorted(dic.items(), reverse = True)
        for i in range(len(arr)):
            answer += arr[i][0]*arr[i][1]
    return answer
    
    
#    answer = ''
#    temp = ''
#    for i in X:
#        if i not in temp:
#            if i in Y:
#                X_count = X.count(i)
#                Y_count = Y.count(i)
#                temp += i * min(X_count, Y_count)
#    if temp == '':
#        answer = '-1'
#    elif int(temp) == 0:
#        answer = '0'
#    else:
#        temp = sorted(temp, reverse = True)
#        for j in temp:
#            answer += j
#    return answer