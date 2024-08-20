def solution(cacheSize, cities):    
    # 대소문자를 구분하지 않으므로 모두 소문자로 바꾸어준다
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    
    answer = 0
    arr = []
    
    for i in range(len(cities)):
        if cities[i] in arr:
            answer += 1
            arr.remove(cities[i])
            arr.append(cities[i])
        else:
            answer += 5
            arr.append(cities[i])
        if len(arr) > cacheSize:
            arr.pop(0)

    return answer
    #    
    #    
    #
    #for i in range(len(cities)):
    #    if cities[i] in arr: # cache hit
    #        answer += 1
    #        cities.
    #    else: # cache miss
    #        answer += 5
    #        
    #    
    #    if len(arr) < cacheSize:
    #        arr.append(cities[i])
    #    else:
    #        arr.append(cities[i])
    #        arr.pop(0)
    #
    #return answer