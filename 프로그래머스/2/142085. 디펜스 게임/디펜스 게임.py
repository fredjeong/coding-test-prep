import heapq

def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    
    heap = []
    for i in range(len(enemy)):
        if n >= enemy[i]:
            n -= enemy[i]
            heapq.heappush(heap, -enemy[i])
        else:
            if k > 0:
                if heap and enemy[i] <= -heap[0]:
                    n += (-heapq.heappop(heap) - enemy[i])
                    heapq.heappush(heap, -enemy[i])
                k -= 1
            else:
                answer = i
                break

        answer = i+1
    return answer