def solution(keymap, targets):
    answer = []
    for target in targets:
        counts = [] 
        for i in target:
            temp = [] # 각 key의 입력횟수 또는 가능/불가능 여부 저장
            for key in keymap:
                if i in key: 
                    index = key.index(i) + 1
                    temp.append(index)
            if temp != []:
                counts.append(min(temp))
            else: # 주어진 keymap들로 목표 문자열을 작성할 수 없다면 answer에 -1을 추가
                answer.append(-1)
                break # target의 i를 입력할 수 없다면 어차피 목표 문자열을 작성하지 못하므로 break
        if len(counts) == len(target):
            answer.append(sum(counts))
    return answer