def solution(cards):
    for i in range(len(cards)):
        cards[i] -= 1

    arr = []
    # i번 상자 열었는지 확인용
    num_box = len(cards)
    visited = [False for _ in range(num_box)]
    
    # 이제 그룹을 지을 차례
    stack = []
    idx = 0
    while visited.count(False) >= 0:
        if visited.count(False) == 0:
            if stack != []:
                arr.append(stack)
            break
        if visited[idx] == True:
            #stack.append(idx+1)
            arr.append(stack)
            stack = []
            # 아직 False인 것 중에서 새로 열 박스 지정
            for i in range(num_box):
                if visited[i] == False:
                    idx = i
                    break
            continue
        visited[idx] = True
        stack.append(idx+1)
        # 자기 자신을 여는 경우라면
        if idx == cards[idx]:
            arr.append(stack)
            stack = []
            for i in range(num_box):
                if visited[i] == False:
                    idx = i
                    break
        else:
            idx = cards[idx]
    
    if len(arr) == 1:
        return 0
    
    length = []
    for group in arr:
        length.append(len(group))
    length.sort()
    answer = length[-1]*length[-2]
#    answer = 1
#    for group in arr:
#        answer *= len(group)
    return answer
        
        
#    # i번 박스를 열어본다
#    for i in range(1,num_box+1):
#        # i번 박스가 이미 열려있다면 라운드를 종료한다
#        if visited[cards[i-1]] = True:
#            arr.append(stack)
#            stack = []
#            continue
#        # i번 박스를 연다
#        visited[i-1] = True
#        stack.append(i)
#        # i번 박스에 들어있는  
#        cards[i-1]
#    
#    #while visited.count(False) > 0:
#        
#    answer = 0
#    return answer