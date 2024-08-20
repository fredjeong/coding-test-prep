def solution(clothes):
    answer = 1
    # 의상의 종류: [의상의 이름] 딕셔너리를 만들고
    closet = {}
    for i in clothes:
        if i[1] not in closet:
            closet[i[1]] = 1
        else:
            closet[i[1]] += 1
    # 각 밸류를 곱해준다
    for key in closet:
        answer *= closet[key] + 1
    # 아무것도 안 입는 경우는 뺀다
    answer -= 1
    return answer