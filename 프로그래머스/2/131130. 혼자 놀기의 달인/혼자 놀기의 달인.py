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
    
    return answer