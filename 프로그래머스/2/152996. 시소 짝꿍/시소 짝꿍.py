from collections import defaultdict

def solution(weights):
    answer = 0
    weights.sort(reverse=True)
    weights_dic = {}
    for weight in weights:
        if weight in weights_dic:
            weights_dic[weight] += 1
        else:
            weights_dic[weight] = 1

    dic = {}
    for weight in set(weights):
        dic[weight] = 0

    for weight in weights:
        if weight*2/3 == int(weight*2/3) and int(weight*2/3) in dic:
            dic[weight] += weights_dic[int(weight*2/3)]
        if weight*1/2 == int(weight*1/2) and int(weight*1/2) in dic:
            dic[weight] += weights_dic[int(weight*1/2)]
        if weight*3/4 == int(weight*3/4) and int(weight*3/4) in dic:
            dic[weight] += weights_dic[int(weight*3/4)]
    
    for weight in set(weights):
        counter = weights.count(weight)
        for i in range(counter):
            dic[weight] += i
    
    for key in dic:
        answer += dic[key]
    return answer
    
#    for i in range(100, 1001):
#        dic[i] = 0
#        
#    weights.sort()
#    
#    for weight in weights:
#        if weight * 1.5 < 1000 and weight*1.5 == int(weight*1.5):
#            dic[int(weight*1.5)] += 1
#        if weight * 2 < 1000:
#            dic[weight*2] += 1
#    for weight in set(weights):
#        if weights.count(weight) >= 2:
#            dic[weight] += weights.count(weight) - 1
#            
#    for weight in set(weights):
#        if weight in dic:
#            answer += dic[weight]
#    return answer
        

# 시간 초과
#def solution(weights):
#    weights.sort()
#    # 차이가 두배 이상 나면 볼 필요도 없다!
#    dic = {}
#    for i in range(len(weights)):
#        dic[i] = 0
#
#    start = 0
#    # 두 배까지만 잡으면 된다
#    while start < len(weights)-1:
#        end = start + 1
#        while end < len(weights):
#            weight_1 = weights[start]
#            weight_2 = weights[end]
#            
#            if weight_2 > 2 * weight_1:
#                break
#            
#            if weight_1 == weight_2:
#                dic[start] += 1
#            else:
#                small, big = sorted([weight_1, weight_2])
#                if small * 4 == big * 3 or small * 4 == big * 2 or small * 3 == big * 2:
#                    dic[start] += 1
#                
#            end += 1
#        start += 1
#    answer = 0
#    for i in dic:
#        answer += dic[i]
#    return answer