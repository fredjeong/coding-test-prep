from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)        

    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
    total = sum_1 + sum_2
    
    if total % 2 == 1:
        return -1
    
    count = 0
    
    while True:
        if sum_1 == sum_2:
            return count
        
        if len(queue1) == 0 or len(queue2) == 0 or count == (len(queue1) + len(queue2)) * 2:
            return -1
        
        count += 1
        
        if sum_1 > sum_2:
            temp = queue1.popleft()
            queue2.append(temp)
            sum_1 -= temp
            sum_2 += temp
        
        else:
            temp = queue2.popleft()
            queue1.append(temp)
            sum_2 -= temp
            sum_1 += temp