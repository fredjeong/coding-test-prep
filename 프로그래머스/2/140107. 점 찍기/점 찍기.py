def solution(k, d):
    '''
    단순히 원점에서 시작해서 점을 찍어나가는 방식으로는 시간 초과가 발생한다. 
    k=1, d=1000000인 경우 1000000*1000000번 연산을 해야 하기 때문
    그보다는 뒤에서부터 지워나가는 것이 낫지 않을까?
    또는, 계단식으로 일괄적으로 더하고, 남은 점들만 계산하는 것도 방법이다
    ㅇㅇㅇㅇㅇ
    ㅇㅇㅇㅇ
    ㅇㅇㅇ
    ㅇㅇ
    ㅇ
    '''
    answer = 0
    # 정삼각형 경계와 그 안에 있는 점
    for x in range(0, d//k+1):
        answer += int((d**2 - (x*k)**2)**0.5)//k + 1
        #for y in range(0, int((d**2 - x**2)**0.5)//k + 1, k):
        #    answer += y
        ##answer += (d - k*i) // k
    
    # 활꼴 경계와 그 안에 있는 점

    
    
#    answer = 0
#    # while문을 이용해서 x값마다 모든 y에 대해 점 찍기
#    x = 0
#    while x <= d:
#        for y in range(0, d+1, k):
#            if (x**2 + y**2)**0.5 <= d:
#                answer += 1
#        x += k
    return answer