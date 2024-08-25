def solution(order):
    answer = 0
    sub = []
    idx = 0
    
    for main in range(1, len(order) + 1):
        sub.append(main)
        while len(sub) > 0 and sub[-1] == order[idx]:
            answer += 1
            idx += 1
            sub.pop()

    return answer