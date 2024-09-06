def solution(w,h):
    answer = 0

    if w == h:
        return w*h - w
    elif w == 1 or h == 1:
        return 0
    
    # 일차함수: y=-h/w * x + h
    for x in range(1, w+1):
        answer += int((-h/w) * x + h)
    
    answer *= 2
    return answer