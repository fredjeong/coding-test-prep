def solution(sides):
    answer = 0
    
    # Case 1) sides의 가장 긴 변이 삼각형의 가장 긴 변인 경우
    for i in range(max(sides) + 1):
        if i + min(sides) > max(sides):
            answer += 1
    
    # Case 2) 나머지 한 변이 가장 긴 변인 경우
    answer += sum(sides) - max(sides) - 1

    return answer