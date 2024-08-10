def solution(my_string):
    temp = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    dic = {}
    for alphabet in temp:
        dic[alphabet] = my_string.count(alphabet)
    answer = list(dic.values())
    return answer