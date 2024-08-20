def solution(elements):
    # 집합을 이용한 풀이
    result = set()
    
    length = len(elements)
    
    # 연속하는 부분 수열을 구하는 것이므로 주어진 배열을 반복해서 놓는다.
    elements = elements * 2
    
    for i in range(length):
        for j in range(length):
            result.add(sum(elements[i:i+j+1]))

    answer = len(result)
    return answer
        