def solution(t, p):
    answer = 0
    # p의 길이 정의
    length_p = len(p)
    # t에서 길이 p만큼 잘라가며 p 이하의 수가 나오는지 조사
    # 0 주의
    for i in range(len(t) - int(len(p)) + 1):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
    return answer