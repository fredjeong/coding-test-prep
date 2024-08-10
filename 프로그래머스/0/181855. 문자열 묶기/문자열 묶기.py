def solution(strArr):
    dic = {}
    for i in strArr:
        if len(i) in dic:
            dic[len(i)] += 1
        else:
            dic[len(i)] = 1
    arr = sorted(dic.items(), key=lambda x:x[1], reverse = True)
    answer = arr[0][1]
    return answer