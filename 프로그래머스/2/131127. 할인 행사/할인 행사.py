def solution(want, number, discount):
    answer = 0
    dic = {}
    for product, number in zip(want, number):
        dic[product] = number
    
    for i in range(len(discount)-9): 
        temp = discount[i:i+10]
        dic2 = {}
        for i in temp:
            if i in dic2:
                dic2[i] += 1
            else:
                dic2[i] = 1
        if dic == dic2:
            answer += 1

    return answer