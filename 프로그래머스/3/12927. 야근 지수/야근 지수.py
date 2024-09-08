import heapq

def solution(n, works):
    # 야근 피로도 = 야근을 시작하는 시점에서 남은 일의 작업량을 제곱하여 더한 값
    # N시간 동안 야근 피로도를 최소화하도록 일한다
    # 결국 n을 잘 분배해서 work에 빼주고, 이들의 제곱을 최소화하는 것
    
    # works[0] - x1, works[1] - x2, works[2] - x3을 최소화하는 것
    
    # 각 수를 works의 합 - n의 평균에 최대한 가깝게 만들면 된다
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
    
    
#    objective = (sum(works) - n)//len(works) 
#    if objective <= 0:
#        return 0
#    
#    # 두 번째 예시의 경우 평균이 4/3인데, 그러면 1.333이니까 
#    # int(objective)까지 내려보고 남는건 int(objective)+1로 만든다
#    works = sorted(works, reverse=True) # 가장 큰 수부터 처리
#    idx = 0
#    for i in range(len(works)):
#        if (i+1) * int(objective+1) + len(works)-(i+1) * int(objective+1) == n:
#            idx = i
#            break
#    # i번째까지 int(objective) 이후는 int(objective) + 1
#    return (int(objective) ** 2) * (idx+1) + (int(objective+1) ** 2) * (len(works)-(idx+1))
#    
#    # 남은 works의 개수 * int(objective)+1가 n이라면?
#    
#    # 남은 n