def solution(a, b, c, d):
    dic = {a: 0, b: 0, c: 0, d: 0}
    arr = [a, b, c, d]
    for i in arr:
        dic[i] += 1
    sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    if len(sorted_dic) == 1:
        answer = 1111 * sorted_dic[0][0]
    elif len(sorted_dic) == 2:
        if sorted_dic[0][1] == 3:
            answer = (10 * sorted_dic[0][0] + sorted_dic[1][0]) ** 2
        else:
            answer = (sorted_dic[0][0] + sorted_dic[1][0]) * abs(sorted_dic[0][0] - sorted_dic[1][0])
    elif len(sorted_dic) == 3:
        answer = sorted_dic[1][0] * sorted_dic[2][0]
    else:
        answer = min(a, b, c, d)
    return answer