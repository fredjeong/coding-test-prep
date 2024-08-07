def solution(k, score):
    hall = [] # 명예의 전당
    answer = [] # 최하점
    
    for i in range(len(score)):
        # k일까지는 모든 가수가 명예의 전당에 오른다
        if i < k:
            hall.append(score[i])
            answer.append(min(hall))
        else:
            # 기존 명예의 전당 최하점보다 점수가 크면 명예의 전당, 기존 최하점 삭제
            if score[i] > min(hall):
                hall.remove(min(hall))
                hall.append(score[i])
                answer.append(min(hall))
            # 명예의 전당 진입 실패할 시 기존 최하점 다시 입력
            else:
                answer.append(min(hall))

    return answer