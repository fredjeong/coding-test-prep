import heapq

def solution(operations):
    q = []
    for elem in operations:
        elem = elem.split(" ")
        order = elem[0]
        num = int(elem[1])
        if order == "I": # 숫자 삽입
            heapq.heappush(q, num)
        elif order == "D":
            if len(q) == 0:
                pass
            elif num == 1: # 최댓값 삭제
                q = heapq.nlargest(len(q),q)[1:]
                heapq.heapify(q)
            elif num == -1:
                heapq.heappop(q) # 최솟값 삭제

    if len(q) == 0:
        answer = [0,0]
    else:
        answer = [max(q), min(q)]
    return answer