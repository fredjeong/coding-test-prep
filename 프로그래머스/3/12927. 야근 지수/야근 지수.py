import heapq

def solution(n, works):
    for i in range(len(works)):
        works[i] = -works[i]
    heapq.heapify(works)
    
    # 가장 작은 값에 1을 더해준다
    while n > 0:
        smallest = heapq.heappop(works)
        if smallest == 0:
            heapq.heappush(works, smallest)
            break
        smallest += 1
        heapq.heappush(works, smallest)
        n -= 1
    
    return sum(i**2 for i in works)