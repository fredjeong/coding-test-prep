def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        # i의 약수의 개수 구하기
        num_divisor = 0
        for j in range(1, i+1):
            if i % j == 0:
                num_divisor += 1
        # i의 약수의 개수가 짝수인지 판별
        if num_divisor % 2 == 0:
            answer += i
        else:
            answer -= i 
    return answer
    