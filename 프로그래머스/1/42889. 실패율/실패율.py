def solution(N, stages):
    answer = []
    
    failure_ratio = {} 
    left_players = len(stages) 
    
    for i in range(1,N+1):
        if left_players == 0:
            failure_ratio[i] = 0
        else:
            failure_ratio[i] = stages.count(i)/left_players
            left_players -= stages.count(i)
        
    answer = sorted(failure_ratio, key=lambda x : failure_ratio[x], reverse=True)

    return answer