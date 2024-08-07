def solution(name, yearning, photo):
    # 이름-추억 딕셔너리 생성
    dictionary = {}
    for i, j in zip(name, yearning):
        dictionary[i] = j
    
    # 추억 점수 매기기
    answer = []
    for i in photo:
        score = 0
        for j in i:
            if j in dictionary:
                score += dictionary[j]
        answer.append(score)
    return answer