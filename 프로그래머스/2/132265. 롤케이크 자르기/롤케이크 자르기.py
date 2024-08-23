def solution(topping):
    answer = 0

    cake_1 = set()
    cake_2 = {}
    for i in topping:
        if i in cake_2:
            cake_2[i] += 1
        else:
            cake_2[i] = 1
            
    for i in range(len(topping)):
        cake_1.add(topping[i])
        cake_2[topping[i]] -= 1
        if cake_2[topping[i]] == 0:
            del cake_2[topping[i]]
        if len(cake_1) == len(cake_2):
            answer += 1
    return answer

# 시간 초과
#def solution(topping):
#    answer = 0
#    index = 1
#    while index < len(topping):
#        set_1 = set()
#        set_2 = set()
#        
#        cake_1 = topping[:index]    
#        cake_2 = topping[index:]
#        
#        for i in cake_1:
#            set_1.add(i)
#        for j in cake_2:
#            set_2.add(j)
#
#        if len(set_1) == len(set_2):
#            answer += 1
#        
#        index += 1
#    
#    return answer