def solution(r1, r2):
    '''
    단순하게 생각하면 큰 원에 있는 정수 점들에서 작은 원에 있는 정수 점들을 빼면 된다.
    하지만 그렇게 될 경우 최대 1000000+1000000 나쁘지 않은데?
    '''
    # 사분원으로 나누고 그 안의 함수값들 더해나가면 되나?

    # 1사분면 하나 구하고 * 4 한 다음 겹치는 경우 더해주면 된다
    # 큰 원: x**2 + y**2 = r2**2 -> y = (r2**2 - x**2)**0.5
    answer = 0
    quadrant = 0
    for x in range(1, r1):
        r1_func = (r1**2 - x**2)**0.5 # r1 함숫값
        r2_func = (r2**2 - x**2)**0.5 # r2 함숫값
        
        # r1의 함숫값이 정수가 아닌 경우
        # int(r2의 함숫값) - int(r1의 함숫값)
        if r1_func != int(r1_func):
            quadrant += int(r2_func) - int(r1_func)
        
        # r1의 함숫값이 정수인 경우
        # int(r2의 함숫값) - int(r1의 함숫값) + 1
        else:
            quadrant += int(r2_func) - int(r1_func) + 1

    answer += quadrant * 4
    
    # r1의 함숫값이 0인 지점부터 r2까지
    overlap = 0
    for x in range(r1, r2+1):
        r2_func = (r2**2 - x**2) ** 0.5
        #print(r2_func)
        overlap += (int(r2_func) * 2 + 1)
    answer += overlap * 2
    
#    overlap = 0
#    # 겹치는 경우 생각 (r2-r1 + 1) * 4
#    if r1 + 1 == r2:
#        for j in range(r1+1, r2):
#            r2_func = (r2**2 - x**2)**0.5
#            overlap += int(r2_func) + 1
#    else:
#        for j in range(r1+1, r2+1):
#            r2_func = (r2**2 - x**2)**0.5
#            overlap += int(r2_func) + 1
    
    #answer += overlap * 2
    
    # x=0에서 겹치는 경우
    y_overlap = r2 - r1 + 1
    answer += y_overlap * 2
    
#    print(quadrant)
#    print(overlap)
#    print(y_overlap)
    return answer