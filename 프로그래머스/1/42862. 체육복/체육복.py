def solution(n, lost, reserve):
    answer = n - len(lost)
    lost = sorted(lost)
    reserve = sorted(reserve)
    temp = []
    for j in reserve:
        if j in lost:
            answer += 1
            temp.append(j)
    
    for i in range(len(temp)):
        reserve.remove(temp[i])
        lost.remove(temp[i])
            
    for i in lost:
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)
        elif i+1 in reserve:
            answer += 1
            reserve.remove(i+1)
    return answer

#5, [4, 5], [3, 4]