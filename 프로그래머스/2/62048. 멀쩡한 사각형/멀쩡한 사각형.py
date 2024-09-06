def solution(w,h):
#    # 원래 만들 수 있었던 정사각형의 개수
#    original = w * h
#    # 기울기는 두 종류가 있다. 이 중에 더 큰 애를 찾아서
#    slope = max(abs(w/h), abs(h/w))
#
#    if slope != int(slope):
#        slope = int(slope+1)
#    else:
#        slope = int(slope)
#    
#    answer = original - slope * min(w, h)
#    return answer

    # 기울기에 따라 사용할 수 없게 된 정사각형의 개수가 어떻게 달라지는지 보자
    # 예시에서 기울기는 -3/2이다. 따라서 int(abs(기울기))=2를 매 칸 쓸 수 없게 된다
    
    # 직각삼각형에서 나올 수 있는 정사각형의 개수를 구해서 2를 곱하면 된다
    # 각 열에 대해 일차함수 함숫값의 int() 이하인 함수값을 리턴한다
    answer = 0
    # 일차함수: y=-h/w * x + h
    #w, h = min(w,h), max(w,h)
    
    if w == h:
        return w*h - w
    elif w == 1 or h == 1:
        return 0
    for x in range(1, w+1):
        answer += int((-h/w) * x + h)
    answer *= 2
    return answer