from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    complete = []
    onboard = deque([0 for _ in range(bridge_length)], maxlen=bridge_length)
    length = len(truck_weights)
    truck_weights.reverse() # pop 사용하기 위해서 뒤집어준다
    bridge_sum = sum(onboard)
    
    while len(complete) < length:
        time += 1

        exit = onboard.popleft() # 한 칸씩 앞으로 보낸다
        
        if exit > 0:
            complete.append(exit)
            bridge_sum -= exit
        
        if len(truck_weights) > 0:
            if bridge_sum + truck_weights[-1] <= weight:
                enter = truck_weights.pop()
                onboard.append(enter)
                bridge_sum += enter
                
            else:
                onboard.append(0)
        else:
            onboard.append(0)
        
        if len(complete) == length:
            break
    
    return time