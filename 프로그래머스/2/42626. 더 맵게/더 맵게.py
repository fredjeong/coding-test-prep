import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            break
        else:
            food_1 = heapq.heappop(scoville)
            food_2 = heapq.heappop(scoville)
            new_food = food_1 + (food_2 * 2)
            heapq.heappush(scoville, new_food)
            answer += 1
            
    return answer

## 시간 초과
#def solution(scoville, K):
#    answer = 0
#    
#    scoville = sorted(scoville, reverse=True)
#
#    while min(scoville) < K:
#        if len(scoville) == 1:
#            answer = -1
#            break
#        else:
#            food_1 = scoville.pop()
#            food_2 = scoville.pop()
#            new_food = food_1 + (food_2 * 2)
#            scoville.append(new_food)
#            scoville = sorted(scoville, reverse=True)
#            answer += 1
#            
#    return answer