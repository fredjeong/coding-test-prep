def solution(arr, queries):
    answer = []
    for query in queries:
        s = query[0]
        e = query[1]
        k = query[2]
        temp = []
        for i in range(s, e+1):
            if arr[i] > k:
                temp.append(arr[i])
        if temp == []:
            answer.append(-1)
        else:
            answer.append(min(temp))
    return answer