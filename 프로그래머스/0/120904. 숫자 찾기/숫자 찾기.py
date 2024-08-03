def solution(num, k):
    num = str(num)
    k = str(k)
    for i in num:
        if i == k:
            answer = num.index(i) + 1
            break
        else:
            answer = -1
    return answer