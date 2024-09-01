def solution(storey):
    answer = 0
    
    storey = list(str(storey))
    length = len(storey)
    
    for i in reversed(range(1, length)):
        if int(storey[i]) == "10":
            storey[i] = "0"
            storey[i-1] = str(int(storey[i-1]) + 1)
        
        if int(storey[i]) == 5:
            if int(storey[i-1]) >= 5:
                answer += 10 - int(storey[i])
                storey[i-1] = str(int(storey[i-1]) + 1)
            else:
                answer += int(storey[i])
        elif int(storey[i]) > 5: 
            answer += 10 - int(storey[i])
            storey[i-1] = str(int(storey[i-1]) + 1)
        else: 
            answer += int(storey[i])
    
    if storey[0] == "10":
        storey[0] = "0"
        storey.insert(0, "1")
    
    if int(storey[0]) > 5:
        answer += 10 - int(storey[0]) + 1
    else:
        answer += int(storey[0])
        
    return answer