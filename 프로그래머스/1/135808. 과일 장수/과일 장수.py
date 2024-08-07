def solution(k, m, score):
    # k: 최고점 
    # m: 한 상자에 들어가는 사과의 개수
    
    # 남는 사과 버리기
    score = sorted(score)
    index = len(score) % m
    score = score[index:]

    # 낮은 애들부터 묶는 것이 좋음
    num_box = len(score) // m
    answer = 0

    for i in range(num_box): # 총 박스의 개수 i = 0 1 2 3
        package = score[m*i:m*i+m] # 0:3, 3:6, 6:9, 9:12

        answer += m * min(package)
    # 가능한 많은 사과를 팔았을 때 얻을 수 있는 최대 이익
    
    # 각 상자에 담긴 사과 중 가장 낮은 점수가 가격의 baseline이 된다.
    return answer